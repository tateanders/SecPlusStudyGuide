"use strict";
// Study app front end. No frameworks, no network beyond the local server.

const main = document.getElementById("main");
const keysBar = document.getElementById("keys");
const S = {
  view: "home", home: null, selected: new Set(), session: null, decks: [],
  q: null, ans: null, active: 0, lowConf: false, shownAt: 0, hint: "", answered: 0,
  fb: null, busy: false,
  past: [], reviewIdx: -1, returnTo: null, reviewStart: 0,  // answered {q, fb} this session, for "Previous"
  exam: null, examResult: null, examGrid: false, timer: null,  // exam mode
};

// ---------- helpers ----------
async function api(path, body) {
  const opts = body === undefined ? {} :
    { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) };
  try {
    const r = await fetch(path, opts);
    return await r.json();
  } catch (e) {
    return { error: "Can't reach the study app. Is `python3 study.py` still running?" };
  }
}
const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const kbd = s => `<kbd>${s}</kbd>`;
const keys = html => { keysBar.innerHTML = html; };
const letter = i => String.fromCharCode(97 + i);
const keyLabel = n => (n < 9 ? String(n + 1) : n === 9 ? "0" : "");
const pct = (n, d) => (d ? (100 * n / d).toFixed(1) : 0);

function bar(c) {
  const total = c.unseen + c.learning + c.solid;
  return `<div class="bar" title="${c.unseen} unseen · ${c.learning} learning · ${c.solid} solid">` +
    `<span class="solid" style="width:${pct(c.solid, total)}%"></span>` +
    `<span class="learning" style="width:${pct(c.learning, total)}%"></span>` +
    `<span class="unseen" style="width:${pct(c.unseen, total)}%"></span></div>`;
}

function showError(msg) {
  main.innerHTML = `<div class="verdict missed">${esc(msg)}</div><button id="go-home">Back to home</button>`;
  document.getElementById("go-home").onclick = showHome;
  S.view = "error";
  keys(`${kbd("Enter")} home`);
}

// ---------- home ----------
async function showHome() {
  if (!leaveExam()) return;
  if (S.session) await endSessionQuietly();
  S.view = "home";
  const h = await api("/api/home");
  if (h.error) return showError(h.error);
  S.home = h;
  S.selected = new Set(h.selected);
  renderHome();
}

function renderHome() {
  const h = S.home;
  let html = `<h1>What are you studying?</h1>
    <p class="lede">Pick your decks. The app handles the mix of reviews, weak spots and new material.</p>`;
  if (!h.decks.length) {
    html += `<p>No question files yet. Put <code>.md</code> files in the <code>questions/</code> folder
      (see <code>FORMAT.md</code>), then refresh this page.</p>`;
  }
  h.decks.forEach((d, i) => {
    const c = d.counts, on = S.selected.has(d.id);
    html += `<label class="deck ${on ? "on" : ""}" data-deck="${esc(d.id)}">
      <span class="num">${keyLabel(i)}</span>
      <input type="checkbox" ${on ? "checked" : ""} tabindex="-1">
      <div class="spacer">
        <div class="name">${esc(d.name)}</div>
        <div class="counts">${c.questions} questions · ${c.unseen} new · ${c.learning} learning · ${c.solid} solid${c.due ? ` · <b>${c.due} due</b>` : ""}
          <span class="muted"> · ${esc(d.file)}</span></div>
      </div>${bar(c)}</label>`;
  });
  if (h.decks.length) {
    html += `<div class="row" style="margin-top:20px"><button class="primary big" id="start" ${S.selected.size ? "" : "disabled"}>Start</button>
      <span class="muted small">Stop whenever you like. Every answer is saved.</span></div>
      <div class="row" style="margin-top:12px"><button class="big" id="exam" ${S.selected.size ? "" : "disabled"}>Exam mode (E)</button>
      <span class="muted small">${h.exam.questions} questions · ${h.exam.minutes} minutes · no feedback until the end</span></div>
      <label class="toggle" id="cram"><input type="checkbox" ${h.cram ? "checked" : ""} tabindex="-1">
      <span><b>Cram mode (C)</b> <span class="muted small">${h.cram
        ? "on: concepts keep coming back this session until solid, no waiting days between reviews"
        : "off: normal spaced review, concepts come back over days"}</span></span></label>`;
  }
  html += issuesHtml(h.issues);
  main.innerHTML = html;
  main.querySelectorAll(".deck").forEach(el => el.addEventListener("click", e => {
    e.preventDefault();
    toggleDeck(el.dataset.deck);
  }));
  const st = document.getElementById("start");
  if (st) st.onclick = startSession;
  const ex = document.getElementById("exam");
  if (ex) ex.onclick = startExam;
  const cr = document.getElementById("cram");
  if (cr) cr.onclick = e => { e.preventDefault(); toggleCram(); };
  keys(`${kbd("Enter")} start · ${kbd("E")} exam · ${kbd("C")} cram · ${kbd("1")}–${kbd("9")} toggle decks · ${kbd("P")} progress`);
}

function issuesHtml(issues) {
  if (!issues.length) return "";
  const errors = issues.filter(i => i.level === "error");
  const warns = issues.filter(i => i.level === "warn");
  const li = i => `<li class="${i.level}">${esc(i.file.split("/").pop())}:${i.line}: ${i.level.toUpperCase()} ${esc(i.message)}</li>`;
  let html = "";
  if (errors.length) {
    const skipped = new Set(errors.map(i => i.qid).filter(Boolean)).size;
    html += `<details class="issues" open><summary>${errors.length} problem(s) in question files` +
      (skipped ? `: ${skipped} question(s) skipped` : "") + `</summary><ul>${errors.map(li).join("")}</ul>
      <p class="small">Fix the file and refresh. <code>python3 study.py validate</code> shows the same list.</p></details>`;
  }
  if (warns.length) {
    html += `<details class="issues" style="border-color:var(--line);background:none"><summary class="muted">${warns.length} writing warning(s): questions still load</summary>
      <ul>${warns.map(li).join("")}</ul></details>`;
  }
  return html;
}

function toggleDeck(id) {
  S.selected.has(id) ? S.selected.delete(id) : S.selected.add(id);
  renderHome();
}

async function toggleCram() {
  const r = await api("/api/settings/cram", { on: !S.home.cram });
  if (r.error) return showError(r.error);
  S.home.cram = r.cram;
  renderHome();
}

async function resetProgress() {
  if (!confirm("Erase all answers and progress for every deck? This can't be undone.")) return;
  const r = await api("/api/reset", {});
  if (r.error) return showError(r.error);
  showHome();
}

async function startSession() {
  if (!S.selected.size) return;
  const r = await api("/api/session", { decks: [...S.selected] });
  if (r.error) return showError(r.error);
  S.session = r.session;
  S.decks = [...S.selected];
  S.past = [];
  nextQuestion();
}

async function endSessionQuietly() {
  const sid = S.session;
  S.session = null;
  if (sid) await api(`/api/session/${sid}/end`, {});
}

// ---------- question ----------
async function nextQuestion() {
  const r = await api(`/api/session/${S.session}/next`);
  if (r.expired) return showHome();
  if (r.error) return showError(r.error);
  if (r.done) return endSession();
  S.q = r.question;
  S.answered = r.answered;
  S.ans = newAnswer(S.q);
  S.active = 0;
  S.lowConf = false;
  S.hint = "";
  S.shownAt = Date.now();
  S.view = "question";
  renderQuestion();
  focusTyped();
}

function newAnswer(q) {
  switch (q.type) {
    case "single": return { choice: null };
    case "multi": return { choices: new Set() };
    case "typed": return { text: "" };
    case "order": return { seq: [] };
    case "match": return { answers: {}, row: 0 };
    case "pbq": return { parts: q.parts.map(newAnswer) };
  }
  return {};
}

const typeLabel = q => ({
  single: "Pick one", multi: "Select multiple", typed: "Typed answer", order: "Ordering", match: "Matching", pbq: "Scenario",
}[q.type] || q.type);

const instructions = q => ({
  single: "Pick one.",
  multi: `Select ${q.select}.`,
  typed: "Type your answer.",
  order: "Press the items in the order they should happen. Backspace undoes.",
  match: "Pick a match for each item. ↑/↓ moves between rows, a number picks.",
}[q.type] || "");

function bodyHtml(q, ans, p) {
  let h = `<div class="instr">${instructions(q)}</div>`;
  if (q.type === "single" || q.type === "multi") {
    q.options.forEach((o, n) => {
      const sel = q.type === "single" ? ans.choice === o.idx : ans.choices.has(o.idx);
      h += `<div class="opt ${sel ? "sel" : ""}" data-act="opt" data-p="${p}" data-n="${n}">
        <span class="k">${keyLabel(n)}</span><div class="t">${o.html}</div></div>`;
    });
  } else if (q.type === "typed") {
    h += `<input class="typed" data-p="${p}" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" value="${esc(ans.text)}" placeholder="Your answer">`;
  } else if (q.type === "order") {
    q.items.forEach((it, n) => {
      const used = ans.seq.includes(it.idx);
      h += `<div class="opt ${used ? "used" : ""}" data-act="ord" data-p="${p}" data-n="${n}">
        <span class="k">${keyLabel(n)}</span><div class="t">${it.html}</div></div>`;
    });
    const byIdx = Object.fromEntries(q.items.map(it => [it.idx, it.html]));
    h += `<div class="seq">${ans.seq.length ? `<ol>${ans.seq.map(i => `<li>${byIdx[i]}</li>`).join("")}</ol>` :
      `<span class="muted small">Your order appears here.</span>`}</div>`;
  } else if (q.type === "match") {
    h += `<div class="bank">${q.choices.map((c, n) => `<span><span class="k">${keyLabel(n)}</span>${c.html}</span>`).join("")}</div>`;
    q.rows.forEach((r, n) => {
      const cur = ans.answers[r.idx];
      h += `<div class="match-row ${n === ans.row ? "active" : ""}" data-act="row" data-p="${p}" data-n="${n}">
        <div>${r.html}</div>
        <select data-p="${p}" data-n="${n}"><option value="">—</option>${q.choices.map((c, ci) =>
          `<option value="${ci}" ${cur === c.value ? "selected" : ""}>${keyLabel(ci) ? keyLabel(ci) + ". " : ""}${esc(c.value)}</option>`).join("")}</select></div>`;
    });
  }
  return h;
}

function renderQuestion() {
  const q = S.q;
  let h = `<div class="qmeta"><span class="row"><span class="pill type">${typeLabel(q)}</span>
    <span class="pill">${S.answered} answered this session</span></span><a href="#" id="end">End session (Q)</a></div>`;
  h += `<div class="qcard"><div class="stem">${q.stem}</div>`;
  if (q.exhibit) h += `<div class="exhibit"><div class="label">Exhibit</div>${q.exhibit}</div>`;
  if (q.type === "pbq") {
    q.parts.forEach((part, i) => {
      h += `<div class="part ${i === S.active ? "active" : ""}" data-part="${i}">
        <div class="plabel">Part ${letter(i)}</div><div class="stem">${part.stem}</div>
        ${bodyHtml(part, S.ans.parts[i], i)}</div>`;
    });
  } else {
    h += bodyHtml(q, S.ans, 0);
  }
  h += `</div><div class="answerbar">
    ${S.past.length ? `<button id="prev">← Previous (B)</button>` : ""}
    <span class="spacer"></span>
    <button id="dontknow">Don't know (D)</button>
    <span class="lowconf ${S.lowConf ? "on" : ""}" id="lowconf">${S.lowConf ? "☑" : "☐"} Not sure (L)</span>
    <button class="primary" id="submit">Submit</button></div>
    <div class="hint">${esc(S.hint)}</div>`;
  main.innerHTML = h;
  bindPrev();

  document.getElementById("end").onclick = e => { e.preventDefault(); endSession(); };
  document.getElementById("submit").onclick = () => submit(S.lowConf);
  document.getElementById("dontknow").onclick = () => submit(false, true);
  document.getElementById("lowconf").onclick = () => { S.lowConf = !S.lowConf; renderQuestion(); };
  bindBody(q);
  keys(`${kbd("1")}–${kbd("9")} pick · ${kbd("Enter")} submit · ${kbd("Shift")}+${kbd("Enter")} submit as not sure · ${kbd("L")} not sure · ${kbd("D")} don't know` +
    (hasTyped(q) ? ` · ${kbd("Esc")} leave text box` : "") + (q.type === "pbq" ? ` · ${kbd("Tab")} next part` : "") +
    (S.past.length ? ` · ${kbd("B")} previous` : "") + ` · ${kbd("Q")} end`);
}

// Answer-entry handlers shared by study questions and exam questions.
function bindBody(q) {
  main.querySelectorAll("[data-act]").forEach(el => el.addEventListener("click", e => {
    if (e.target.tagName === "SELECT" || e.target.tagName === "OPTION") return;
    setActive(+el.dataset.p);
    const t = target();
    if (el.dataset.act === "row") { t.ans.row = +el.dataset.n; rerender(); return; }
    pick(+el.dataset.n);
  }));
  main.querySelectorAll("select").forEach(el => el.addEventListener("change", () => {
    setActive(+el.dataset.p);
    const t = target();
    t.ans.row = +el.dataset.n;
    const ci = el.value === "" ? null : +el.value;
    const rowIdx = t.q.rows[t.ans.row].idx;
    if (ci === null) delete t.ans.answers[rowIdx]; else t.ans.answers[rowIdx] = t.q.choices[ci].value;
    rerender();
  }));
  main.querySelectorAll("input.typed").forEach(el => {
    el.addEventListener("input", () => {
      const p = +el.dataset.p;
      (q.type === "pbq" ? S.ans.parts[p] : S.ans).text = el.value;
    });
    el.addEventListener("focus", () => {
      const p = +el.dataset.p;
      if (q.type === "pbq" && S.active !== p) { S.active = p; markActivePart(); }
    });
  });
}

const rerender = () => (S.view === "exam" ? renderExam() : renderQuestion());

function hasTyped(q) { return q.type === "typed" || (q.type === "pbq" && q.parts.some(p => p.type === "typed")); }

function markActivePart() {
  main.querySelectorAll(".part").forEach(el => el.classList.toggle("active", +el.dataset.part === S.active));
}

function setActive(p) {
  if (S.q.type === "pbq" && S.active !== p) S.active = p;
}

function target() {
  if (S.q.type === "pbq") return { q: S.q.parts[S.active], ans: S.ans.parts[S.active] };
  return { q: S.q, ans: S.ans };
}

function focusTyped() {
  const t = target();
  if (t.q.type !== "typed") return;
  const el = main.querySelector(`input.typed[data-p="${S.q.type === "pbq" ? S.active : 0}"]`);
  if (el) { el.focus(); el.setSelectionRange(el.value.length, el.value.length); }
}

function pick(n) {
  const { q, ans } = target();
  if (q.type === "single" && q.options[n]) ans.choice = q.options[n].idx;
  else if (q.type === "multi" && q.options[n]) {
    const i = q.options[n].idx;
    ans.choices.has(i) ? ans.choices.delete(i) : ans.choices.add(i);
  } else if (q.type === "order" && q.items[n]) {
    const i = q.items[n].idx;
    if (!ans.seq.includes(i)) ans.seq.push(i);
  } else if (q.type === "match" && q.choices[n]) {
    ans.answers[q.rows[ans.row].idx] = q.choices[n].value;
    if (ans.row < q.rows.length - 1) ans.row++;
  } else return;
  S.hint = "";
  rerender();
}

function complete(q, ans) {
  switch (q.type) {
    case "single": return ans.choice !== null;
    case "multi": return ans.choices.size > 0;
    case "typed": return ans.text.trim() !== "";
    case "order": return ans.seq.length === q.items.length;
    case "match": return q.rows.every(r => ans.answers[r.idx] !== undefined);
    case "pbq": return q.parts.every((p, i) => complete(p, ans.parts[i]));
  }
  return false;
}

function response(q, ans) {
  switch (q.type) {
    case "single": return { choice: ans.choice };
    case "multi": return { choices: [...ans.choices] };
    case "typed": return { text: ans.text };
    case "order": return { sequence: ans.seq };
    case "match": return { answers: q.rows.map((_, i) => ans.answers[i] ?? null) };
    case "pbq": return { parts: Object.fromEntries(q.parts.map((p, i) => [p.qid, response(p, ans.parts[i])])) };
  }
  return {};
}

async function submit(low, dontKnow = false) {
  if (S.busy || S.view !== "question") return;
  if (!dontKnow && !complete(S.q, S.ans)) {
    S.hint = S.q.type === "pbq" ? "Answer every part first, or press D for Don't know." :
      S.q.type === "order" ? "Place every item first, or press D for Don't know." :
      S.q.type === "match" ? "Match every row first, or press D for Don't know." :
      "Pick an answer first, or press D for Don't know.";
    renderQuestion();
    return;
  }
  S.busy = true;
  const fb = await api(`/api/session/${S.session}/answer`, {
    qid: S.q.qid, low_conf: !!low && !dontKnow, dont_know: dontKnow,
    response: dontKnow ? null : response(S.q, S.ans), ms: Date.now() - S.shownAt,
  });
  S.busy = false;
  if (fb.expired) return showHome();
  if (fb.error) { S.hint = fb.error; renderQuestion(); return; }
  S.fb = fb;
  S.answered = fb.answered;
  S.past.push({ q: S.q, fb });
  S.view = "feedback";
  renderFeedback();
}

// ---------- feedback ----------
function verdictHtml(fb) {
  if (fb.verdict === "correct") return `<div class="verdict correct"><span class="vicon">✓</span><div>Correct</div></div>`;
  if (fb.verdict === "shaky") return `<div class="verdict shaky"><span class="vicon">~</span><div>Correct, but you weren't sure
    <div class="sub">Counts as shaky: this concept comes back sooner than a confident answer would.</div></div></div>`;
  let title = fb.dont_know ? "Don't know" : "Missed";
  if (fb.type === "pbq" && !fb.dont_know) {
    const right = fb.parts.filter(p => p.correct).length;
    title += `: ${right} of ${fb.parts.length} parts right`;
  }
  return `<div class="verdict missed"><span class="vicon">${fb.dont_know ? "?" : "✗"}</span><div>${title}
    <div class="sub">This question comes back within the next ${fb.requeue_max || 10} questions.</div></div></div>`;
}

function fbBodyHtml(q, fb) {
  let h = "";
  if (q.type === "single" || q.type === "multi") {
    const byIdx = Object.fromEntries(fb.options.map(o => [o.idx, o]));
    for (const shown of q.options) {
      const o = byIdx[shown.idx];
      const cls = o.correct ? "correct" : o.chosen ? "wrongpick" : "";
      const mark = o.correct ? `<span class="mark ok">✓</span>` : o.chosen ? `<span class="mark no">✗</span>` : "";
      const tag = o.chosen ? ` <span class="muted small">(your pick)</span>` : "";
      h += `<div class="fbopt ${cls}">${mark}${o.html}${tag}${!o.correct && o.why ? `<div class="why">${o.why}</div>` : ""}</div>`;
    }
  } else if (q.type === "typed") {
    h += `<p>You typed: ${fb.dont_know ? `<span class="muted">nothing (Don't know)</span>` : `<code>${esc(fb.your_text)}</code>`}
      ${fb.correct ? `<span class="mark ok">✓</span>` : `<span class="mark no">✗</span>`}</p>
      <p>Accepted: ${fb.accepted.map(a => `<code>${esc(a)}</code>`).join(" · ")}</p>`;
  } else if (q.type === "order") {
    h += `<div class="cols"><div><h3>Your order</h3>${fb.your_order.length ? `<ol>${fb.your_order.map(o =>
      `<li><span class="mark ${o.ok ? "ok" : "no"}">${o.ok ? "✓" : "✗"}</span>${o.html}</li>`).join("")}</ol>` : `<p class="muted">Don't know</p>`}</div>
      <div><h3>Correct order</h3><ol>${fb.correct_order.map(o =>
      `<li>${o.html}${o.why ? `<div class="why muted small">${o.why}</div>` : ""}</li>`).join("")}</ol></div></div>`;
  } else if (q.type === "match") {
    h += `<table><thead><tr><th>Item</th><th>Your answer</th><th>Correct</th><th></th></tr></thead><tbody>${fb.rows.map(r =>
      `<tr><td>${r.left}</td><td>${r.yours ? `<span class="mark ${r.ok ? "ok" : "no"}">${r.ok ? "✓" : "✗"}</span>${r.yours}` : `<span class="muted">—</span>`}</td>
       <td>${r.right}</td><td class="small muted">${r.why}</td></tr>`).join("")}</tbody></table>`;
  }
  return h;
}

function feedbackHtml(q, fb) {
  let h = verdictHtml(fb);
  if (fb.yours.length) {
    h += `<div class="yours"><h3>Why your answer was wrong</h3>${fb.yours.map(y =>
      `<div class="item"><b>${y.html}</b>${y.why}</div>`).join("")}</div>`;
  }
  h += `<div class="qcard"><div class="stem">${q.stem}</div>`;
  if (q.exhibit) h += `<div class="exhibit"><div class="label">Exhibit</div>${q.exhibit}</div>`;
  if (q.type === "pbq") {
    fb.parts.forEach((pf, i) => {
      h += `<div class="part"><div class="plabel">Part ${letter(i)}
        <span class="mark ${pf.correct ? "ok" : "no"}">${pf.correct ? "✓" : "✗"}</span></div>
        <div class="stem">${q.parts[i].stem}</div>${fbBodyHtml(q.parts[i], pf)}
        ${pf.explanation ? `<div class="small">${pf.explanation}</div>` : ""}</div>`;
    });
  } else {
    h += fbBodyHtml(q, fb);
  }
  h += `</div>`;
  if (fb.explanation) h += `<div class="explain"><h3>Explanation</h3>${fb.explanation}</div>`;
  return h;
}

function renderFeedback() {
  const fb = S.fb, hasPrev = S.past.length > 1;
  main.innerHTML = feedbackHtml(S.q, fb) + `<div class="answerbar">
    <a href="#" id="end" class="muted small">End session (Q)</a><span class="spacer"></span>
    ${hasPrev ? `<button id="prev">← Previous (B)</button>` : ""}<button class="primary" id="next">Next</button></div>
    <div class="status">This concept is now <b>${fb.status}</b> (box ${fb.box}). ${S.answered} answered this session.</div>`;
  window.scrollTo(0, 0);
  document.getElementById("next").onclick = nextQuestion;
  document.getElementById("end").onclick = e => { e.preventDefault(); endSession(); };
  bindPrev();
  keys(`${kbd("Enter")} next` + (hasPrev ? ` · ${kbd("B")} previous` : "") + ` · ${kbd("Q")} end session`);
}

// ---------- review earlier answers (read only) ----------
function bindPrev() {
  const b = document.getElementById("prev");
  if (b) b.onclick = goBack;
}

// The newest entry the review can show: from a feedback screen, that screen's own entry is skipped.
const reviewLast = () => S.past.length - (S.returnTo === "feedback" ? 2 : 1);

function goBack() {
  if (S.view === "review") {
    if (S.reviewIdx > 0) { S.reviewIdx--; renderReview(); }
    return;
  }
  if (S.view !== "question" && S.view !== "feedback") return;
  S.returnTo = S.view;
  if (reviewLast() < 0) return;
  S.reviewIdx = reviewLast();
  S.reviewStart = Date.now();
  S.view = "review";
  renderReview();
}

function goForward() {
  if (S.reviewIdx < reviewLast()) { S.reviewIdx++; renderReview(); return; }
  S.view = S.returnTo;
  if (S.view === "question") {
    S.shownAt += Date.now() - S.reviewStart;  // reviewing doesn't count as time spent on this question
    renderQuestion();
    focusTyped();
  } else {
    renderFeedback();
  }
}

function renderReview() {
  const { q, fb } = S.past[S.reviewIdx];
  const back = S.reviewIdx === reviewLast() ? (S.returnTo === "question" ? "Back to current question" : "Back") : "Later";
  main.innerHTML = `<div class="notice">Reviewing an earlier question (${S.reviewIdx + 1} of ${S.past.length} this session).
    Your answer is already recorded.</div>` + feedbackHtml(q, fb) + `<div class="answerbar">
    ${S.reviewIdx > 0 ? `<button id="prev">← Earlier (B)</button>` : ""}<span class="spacer"></span>
    <button class="primary" id="fwd">${back} →</button></div>`;
  window.scrollTo(0, 0);
  bindPrev();
  document.getElementById("fwd").onclick = goForward;
  keys((S.reviewIdx > 0 ? `${kbd("B")}/${kbd("←")} earlier · ` : "") +
    `${kbd("Enter")}/${kbd("→")} ${back.toLowerCase()} · ${kbd("Q")} end session`);
}

// ---------- summary ----------
async function endSession() {
  const sid = S.session;
  S.session = null;
  const r = sid ? await api(`/api/session/${sid}/end`, {}) : { answered: 0 };
  S.view = "summary";
  let h = `<h1>Session over</h1>`;
  if (!r.answered) {
    h += `<p class="muted">No questions answered.</p>`;
  } else {
    h += `<div class="stats"><div class="stat"><b>${r.answered}</b>answered</div>
      <div class="stat good"><b>${r.correct}</b>correct</div><div class="stat shaky"><b>${r.shaky}</b>not sure</div>
      <div class="stat bad"><b>${r.missed}</b>missed</div></div>`;
    if (r.missed_topics && r.missed_topics.length) {
      h += `<h2>Topics you missed</h2><table><tbody>${r.missed_topics.map(t =>
        `<tr><td>${esc(t.topic)}</td><td>${esc(t.name)}</td><td class="muted">${esc(t.deck)}</td><td>${t.misses}×</td></tr>`).join("")}</tbody></table>`;
    }
    h += `<p class="muted small">Everything is saved. Missed concepts come back first next time.</p>`;
  }
  h += `<div class="row"><button class="primary" id="again">Keep going</button><button id="home">Home</button><button id="prog">Progress</button></div>`;
  main.innerHTML = h;
  document.getElementById("again").onclick = keepGoing;
  document.getElementById("home").onclick = showHome;
  document.getElementById("prog").onclick = showProgress;
  keys(`${kbd("Enter")} keep going · ${kbd("H")} home · ${kbd("P")} progress`);
}

async function keepGoing() {
  S.selected = new Set(S.decks);
  await startSession();
}

// ---------- progress ----------
async function showProgress() {
  if (!leaveExam()) return;
  if (S.session) await endSessionQuietly();
  S.view = "progress";
  const p = await api("/api/progress");
  if (p.error) return showError(p.error);
  let h = `<h1>Progress</h1>
    <p class="muted small"><b>Unseen</b>: never answered. <b>Learning</b>: missed recently, answered unsure, or not yet confirmed
    on two different versions on two different days. <b>Solid</b>: box ${p.solid_box}+ (next review a week or more away).</p>
    <div class="legend"><span><i style="background:var(--solid)"></i>solid</span><span><i style="background:var(--learning)"></i>learning</span>
    <span><i style="background:var(--unseen)"></i>unseen</span></div>`;
  if (!p.decks.length) h += `<p>No decks loaded.</p>`;
  for (const d of p.decks) {
    const c = d.counts;
    h += `<div class="card"><h2 style="margin-top:0">${esc(d.name)}</h2>
      <div class="row small muted"><span>${c.concepts} concepts · ${c.questions} questions</span><span class="spacer"></span>
      <span>${c.unseen} unseen · ${c.learning} learning · ${c.solid} solid · ${c.due} due</span></div>
      <div style="margin:8px 0 14px">${bar(c)}</div>
      ${chart(d.timeline, c.concepts)}
      <h3>Topics</h3><p class="muted small">Sorted by miss rate over the last 30 days. "Not sure" = correct answers you flagged as unsure.</p>
      <table class="topics"><thead><tr><th>Topic</th><th></th><th>Status</th><th class="num">Answers (30d)</th>
      <th class="num">Missed</th><th class="num">Not sure</th></tr></thead><tbody>${d.topics.map(t => `<tr>
        <td>${esc(t.topic)}</td><td>${esc(t.name)}</td><td>${bar(t)}</td><td class="num">${t.attempts}</td>
        <td class="num">${t.miss_rate === null ? "—" : Math.round(100 * t.miss_rate) + "%"}</td>
        <td class="num">${t.shaky_rate === null ? "—" : Math.round(100 * t.shaky_rate) + "%"}</td></tr>`).join("")}</tbody></table></div>`;
  }
  h += `<div class="card"><h3 style="margin-top:0">Start over</h3>
    <div class="row"><span class="muted small spacer">Erases every answer and puts all decks back to unseen. Your question files aren't touched.</span>
    <button class="danger" id="reset">Reset all progress</button></div></div>`;
  main.innerHTML = h;
  document.getElementById("reset").onclick = resetProgress;
  keys(`${kbd("H")} home · ${kbd("Enter")} home`);
}

function chart(timeline, total) {
  if (!timeline || timeline.length < 2) {
    return `<p class="muted small">A chart of solid concepts over time appears after you've studied on two different days.</p>`;
  }
  const W = 760, H = 150, L = 34, B = 22, T = 8, R = 8;
  const max = Math.max(1, total);
  const x = i => L + (W - L - R) * i / (timeline.length - 1);
  const y = v => T + (H - T - B) * (1 - v / max);
  const line = key => timeline.map((s, i) => `${x(i).toFixed(1)},${y(s[key]).toFixed(1)}`).join(" ");
  return `<svg class="chart" viewBox="0 0 ${W} ${H}" width="100%" role="img" aria-label="Solid and learning concepts over time">
    <line class="axis" x1="${L}" y1="${y(0)}" x2="${W - R}" y2="${y(0)}"/>
    <line class="axis" x1="${L}" y1="${y(max)}" x2="${W - R}" y2="${y(max)}" stroke-dasharray="3 3"/>
    <text x="${L - 6}" y="${y(max) + 4}" text-anchor="end">${max}</text>
    <text x="${L - 6}" y="${y(0) + 4}" text-anchor="end">0</text>
    <text x="${L}" y="${H - 4}">${timeline[0].day}</text>
    <text x="${W - R}" y="${H - 4}" text-anchor="end">${timeline[timeline.length - 1].day}</text>
    <polyline fill="none" stroke="var(--learning)" stroke-width="2" points="${line("learning")}"/>
    <polyline fill="none" stroke="var(--solid)" stroke-width="2.5" points="${line("solid")}"/></svg>`;
}

// ---------- exam ----------
function leaveExam() {
  if (!S.exam) return true;
  if (!confirm("Leave the exam? Your answers so far will be lost.")) return false;
  stopExam();
  return true;
}

function stopExam() {
  clearInterval(S.timer);
  S.timer = null;
  S.exam = null;
  window.onbeforeunload = null;
}

async function startExam() {
  if (!S.selected.size) return;
  if (S.session) await endSessionQuietly();
  const r = await api("/api/exam", { decks: [...S.selected] });
  if (r.error) return showError(r.error);
  if (!r.questions.length) return showError("The selected decks have no questions.");
  S.exam = {
    id: r.exam, qs: r.questions, answers: r.questions.map(newAnswer), flagged: new Set(),
    idx: 0, endsAt: Date.now() + r.seconds_left * 1000, ms: {}, shownAt: Date.now(),
  };
  S.examGrid = false;
  S.view = "exam";
  window.onbeforeunload = () => "Your exam answers will be lost.";
  S.timer = setInterval(tickExam, 1000);
  openExamQuestion(0);
}

function examLeft() { return Math.max(0, Math.round((S.exam.endsAt - Date.now()) / 1000)); }
const clock = sec => `${Math.floor(sec / 3600) ? Math.floor(sec / 3600) + ":" : ""}${String(Math.floor(sec / 60) % 60).padStart(2, "0")}:${String(sec % 60).padStart(2, "0")}`;

function tickExam() {
  if (!S.exam) return;
  const left = examLeft();
  const el = document.getElementById("timer");
  if (el) { el.textContent = clock(left); el.classList.toggle("low", left < 300); }
  if (left <= 0) finishExam(true);
}

function noteTime() {
  const e = S.exam, qid = e.qs[e.idx].qid;
  e.ms[qid] = (e.ms[qid] || 0) + (Date.now() - e.shownAt);
  e.shownAt = Date.now();
}

function openExamQuestion(i) {
  const e = S.exam;
  if (S.view === "exam" && !S.examGrid) noteTime();
  e.idx = Math.max(0, Math.min(e.qs.length - 1, i));
  e.shownAt = Date.now();
  S.q = e.qs[e.idx];
  S.ans = e.answers[e.idx];
  S.active = 0;
  S.examGrid = false;
  renderExam();
  focusTyped();
}

const examAnswered = i => complete(S.exam.qs[i], S.exam.answers[i]);

function renderExam() {
  if (S.examGrid) return renderExamGrid();
  const e = S.exam, q = S.q, left = examLeft(), flagged = e.flagged.has(q.qid);
  let h = `<div class="qmeta"><span class="row"><span class="pill type">Question ${e.idx + 1} of ${e.qs.length}</span>
    <span class="pill">${typeLabel(q)}</span>${flagged ? `<span class="pill flag">⚑ Flagged</span>` : ""}</span>
    <span id="timer" class="timer ${left < 300 ? "low" : ""}">${clock(left)}</span></div>`;
  h += `<div class="qcard"><div class="stem">${q.stem}</div>`;
  if (q.exhibit) h += `<div class="exhibit"><div class="label">Exhibit</div>${q.exhibit}</div>`;
  if (q.type === "pbq") {
    q.parts.forEach((part, i) => {
      h += `<div class="part ${i === S.active ? "active" : ""}" data-part="${i}">
        <div class="plabel">Part ${letter(i)}</div><div class="stem">${part.stem}</div>
        ${bodyHtml(part, S.ans.parts[i], i)}</div>`;
    });
  } else {
    h += bodyHtml(q, S.ans, 0);
  }
  h += `</div><div class="answerbar">
    <button id="eprev" ${e.idx ? "" : "disabled"}>← Previous</button>
    <button id="eflag">${flagged ? "Unflag" : "⚑ Flag"} (F)</button>
    <span class="spacer"></span>
    <button id="egrid">Review all (R)</button>
    ${e.idx < e.qs.length - 1 ? `<button class="primary" id="enext">Next →</button>` :
      `<button class="primary" id="egrid2">Review &amp; finish</button>`}</div>`;
  main.innerHTML = h;
  bindBody(q);
  document.getElementById("eprev").onclick = () => openExamQuestion(e.idx - 1);
  document.getElementById("eflag").onclick = toggleFlag;
  document.getElementById("egrid").onclick = showExamGrid;
  const nx = document.getElementById("enext");
  if (nx) nx.onclick = () => openExamQuestion(e.idx + 1);
  const g2 = document.getElementById("egrid2");
  if (g2) g2.onclick = showExamGrid;
  keys(`${kbd("1")}–${kbd("9")} pick · ${kbd("→")}/${kbd("N")}/${kbd("Enter")} next · ${kbd("←")}/${kbd("B")} previous · ${kbd("F")} flag · ${kbd("R")} review all` +
    (q.type === "pbq" ? ` · ${kbd("Tab")} next part` : ""));
}

function toggleFlag() {
  const f = S.exam.flagged, id = S.q.qid;
  f.has(id) ? f.delete(id) : f.add(id);
  renderExam();
}

function showExamGrid() {
  if (!S.examGrid) noteTime();
  S.examGrid = true;
  renderExamGrid();
}

function renderExamGrid() {
  const e = S.exam;
  const unanswered = e.qs.filter((_, i) => !examAnswered(i)).length;
  let h = `<div class="qmeta"><h1 style="margin:0">Review</h1><span id="timer" class="timer ${examLeft() < 300 ? "low" : ""}">${clock(examLeft())}</span></div>
    <p class="muted small">${e.qs.length - unanswered} answered · ${unanswered} unanswered · ${e.flagged.size} flagged. Click a number to go back to it.</p>
    <div class="grid">${e.qs.map((q, i) => `<button class="tile ${examAnswered(i) ? "done" : ""} ${e.flagged.has(q.qid) ? "flagged" : ""}" data-i="${i}">
      ${i + 1}${e.flagged.has(q.qid) ? "<i>⚑</i>" : ""}</button>`).join("")}</div>
    <div class="legend exam small"><span><i class="done"></i>answered</span><span><i></i>unanswered</span><span>⚑ flagged</span></div>
    <div class="answerbar"><button id="eback">← Back to question ${e.idx + 1}</button><span class="spacer"></span>
    <button class="primary" id="efinish">Finish exam</button></div>`;
  main.innerHTML = h;
  main.querySelectorAll(".tile").forEach(el => el.onclick = () => openExamQuestion(+el.dataset.i));
  document.getElementById("eback").onclick = () => openExamQuestion(e.idx);
  document.getElementById("efinish").onclick = () => finishExam(false);
  keys(`${kbd("Enter")} finish · ${kbd("Esc")}/${kbd("R")} back to the question`);
}

async function finishExam(timeUp) {
  const e = S.exam;
  if (!e || S.busy) return;
  if (!timeUp) {
    const unanswered = e.qs.filter((_, i) => !examAnswered(i)).length;
    const msg = `Finish the exam?` + (unanswered ? `\n${unanswered} question(s) are unanswered and will count as wrong.` : "") +
      (e.flagged.size ? `\n${e.flagged.size} question(s) are flagged.` : "");
    if (!confirm(msg)) return;
  }
  if (!S.examGrid) noteTime();
  const responses = {};
  e.qs.forEach((q, i) => { if (examAnswered(i)) responses[q.qid] = response(q, e.answers[i]); });
  S.busy = true;
  const r = await api(`/api/exam/${e.id}/finish`, { responses, flagged: [...e.flagged], ms: e.ms });
  S.busy = false;
  const qs = e.qs;
  stopExam();
  if (r.error) return showError(r.error);
  S.examResult = { r, qs, timeUp };
  renderExamResult();
}

function renderExamResult() {
  const { r, qs, timeUp } = S.examResult;
  S.view = "examResult";
  let h = `<h1>Exam results</h1>` + (timeUp ? `<div class="notice">Time ran out. Your answers were submitted automatically.</div>` : "");
  h += `<div class="stats"><div class="stat"><b>${r.percent}%</b>score</div>
    <div class="stat good"><b>${r.correct}</b>correct</div><div class="stat bad"><b>${r.total - r.correct}</b>wrong</div>
    <div class="stat"><b>${r.unanswered}</b>unanswered</div><div class="stat"><b>${r.minutes}</b>minutes</div></div>`;
  h += `<h2>By domain</h2><table><tbody>${r.by_deck.map(d => `<tr><td>${esc(d.name)}</td>
    <td class="num">${d.correct} / ${d.total}</td><td class="num">${d.total ? Math.round(100 * d.correct / d.total) : 0}%</td></tr>`).join("")}</tbody></table>`;
  if (r.missed_topics.length) {
    h += `<h2>Topics you missed</h2><table><tbody>${r.missed_topics.map(t =>
      `<tr><td>${esc(t.topic)}</td><td>${esc(t.name)}</td><td class="muted">${esc(t.deck)}</td><td>${t.misses}×</td></tr>`).join("")}</tbody></table>`;
  }
  h += `<h2>Every question</h2><p class="muted small">Click one to see the answer and explanation. Missed questions now come up in your normal study sessions.</p>
    <div class="grid">${r.items.map((it, i) => `<button class="tile ${it.fb.correct ? "right" : "wrong"}" data-i="${i}">
      ${i + 1}${it.flagged ? "<i>⚑</i>" : ""}</button>`).join("")}</div>
    <div class="row" style="margin-top:20px"><button class="primary" id="home">Home</button><button id="prog">Progress</button></div>`;
  main.innerHTML = h;
  window.scrollTo(0, 0);
  main.querySelectorAll(".tile").forEach(el => el.onclick = () => showExamItem(+el.dataset.i));
  document.getElementById("home").onclick = showHome;
  document.getElementById("prog").onclick = showProgress;
  keys(`${kbd("H")} home · ${kbd("P")} progress`);
}

function showExamItem(i) {
  const { r, qs } = S.examResult;
  S.view = "examItem";
  S.examItem = i;
  main.innerHTML = `<div class="notice">Exam question ${i + 1} of ${qs.length}${r.items[i].flagged ? " · you flagged this one" : ""}</div>` +
    feedbackHtml(qs[i], r.items[i].fb) + `<div class="answerbar">
    <button id="iprev" ${i ? "" : "disabled"}>← Previous</button><span class="spacer"></span>
    <button id="iback">Back to results</button><button class="primary" id="inext" ${i < qs.length - 1 ? "" : "disabled"}>Next →</button></div>`;
  window.scrollTo(0, 0);
  document.getElementById("iprev").onclick = () => showExamItem(i - 1);
  document.getElementById("inext").onclick = () => showExamItem(i + 1);
  document.getElementById("iback").onclick = renderExamResult;
  keys(`${kbd("←")} previous · ${kbd("→")} next · ${kbd("Esc")} back to results`);
}

// ---------- keyboard ----------
document.addEventListener("keydown", e => {
  if (e.metaKey || e.ctrlKey || e.altKey) return;
  const tag = e.target.tagName;
  const inText = tag === "INPUT" && e.target.type !== "checkbox";
  const inSelect = tag === "SELECT";
  const key = e.key;

  if (S.view === "home") {
    if (key === "Enter") { e.preventDefault(); startSession(); }
    else if (key === "e" || key === "E") startExam();
    else if (/^[0-9]$/.test(key)) {
      const n = key === "0" ? 9 : +key - 1;
      const d = S.home && S.home.decks[n];
      if (d) toggleDeck(d.id);
    } else if (key === "p" || key === "P") showProgress();
    else if ((key === "c" || key === "C") && S.home && S.home.decks.length) toggleCram();
    return;
  }
  const backKey = key === "b" || key === "B" || key === "ArrowLeft";
  if (S.view === "feedback") {
    if (key === "Enter" && !e.repeat) { e.preventDefault(); nextQuestion(); }
    else if (backKey) { e.preventDefault(); goBack(); }
    else if (key === "q" || key === "Q") endSession();
    return;
  }
  if (S.view === "review") {
    if (backKey) { e.preventDefault(); goBack(); }
    else if ((key === "Enter" || key === "ArrowRight" || key === "Escape") && !e.repeat) { e.preventDefault(); goForward(); }
    else if (key === "q" || key === "Q") endSession();
    return;
  }
  if (S.view === "summary") {
    if (key === "Enter") { e.preventDefault(); keepGoing(); }
    else if (key === "h" || key === "H") showHome();
    else if (key === "p" || key === "P") showProgress();
    return;
  }
  if (S.view === "progress" || S.view === "error") {
    if (key === "Enter" || key === "h" || key === "H" || key === "Escape") showHome();
    return;
  }
  if (S.view === "examResult") {
    if (key === "h" || key === "H") showHome();
    else if (key === "p" || key === "P") showProgress();
    return;
  }
  if (S.view === "examItem") {
    const n = S.examResult.qs.length;
    if (key === "ArrowLeft" && S.examItem > 0) showExamItem(S.examItem - 1);
    else if (key === "ArrowRight" && S.examItem < n - 1) showExamItem(S.examItem + 1);
    else if (key === "Escape" || key === "Enter") renderExamResult();
    return;
  }
  if (S.view === "exam") return examKey(e, key, inText, inSelect);
  if (S.view !== "question") return;

  if (key === "Enter") {
    e.preventDefault();
    if (!e.repeat) submit(e.shiftKey || S.lowConf);
    return;
  }
  if (key === "Escape") { if (inText || inSelect) e.target.blur(); return; }
  if (key === "Tab" && S.q.type === "pbq") {
    e.preventDefault();
    const n = S.q.parts.length;
    S.active = (S.active + (e.shiftKey ? n - 1 : 1)) % n;
    if (document.activeElement) document.activeElement.blur();
    renderQuestion();
    focusTyped();
    return;
  }
  if (inText || inSelect) return;

  if (backKey) { e.preventDefault(); goBack(); }
  else if (key === "l" || key === "L") { S.lowConf = !S.lowConf; renderQuestion(); }
  else if (key === "d" || key === "D") submit(false, true);
  else if (key === "q" || key === "Q") endSession();
  else if (/^[0-9]$/.test(key)) { e.preventDefault(); pick(key === "0" ? 9 : +key - 1); }
  else if (key === "Backspace") {
    const { q, ans } = target();
    if (q.type === "order" && ans.seq.length) { e.preventDefault(); ans.seq.pop(); renderQuestion(); }
  } else if (key === "ArrowDown" || key === "ArrowUp") {
    const { q, ans } = target();
    if (q.type === "match") {
      e.preventDefault();
      ans.row = Math.max(0, Math.min(q.rows.length - 1, ans.row + (key === "ArrowDown" ? 1 : -1)));
      renderQuestion();
    }
  }
});

function examKey(e, key, inText, inSelect) {
  if (S.examGrid) {
    if (key === "Enter" && !e.repeat) { e.preventDefault(); finishExam(false); }
    else if (key === "Escape" || key === "r" || key === "R") openExamQuestion(S.exam.idx);
    return;
  }
  if (key === "Escape") { if (inText || inSelect) e.target.blur(); return; }
  if (key === "Tab" && S.q.type === "pbq") {
    e.preventDefault();
    const n = S.q.parts.length;
    S.active = (S.active + (e.shiftKey ? n - 1 : 1)) % n;
    if (document.activeElement) document.activeElement.blur();
    renderExam();
    focusTyped();
    return;
  }
  if (key === "Enter" && !e.repeat) {
    e.preventDefault();
    if (S.exam.idx < S.exam.qs.length - 1) openExamQuestion(S.exam.idx + 1); else showExamGrid();
    return;
  }
  if (inText || inSelect) return;
  const last = S.exam.idx === S.exam.qs.length - 1;
  if (key === "ArrowRight" || key === "n" || key === "N") { e.preventDefault(); last ? showExamGrid() : openExamQuestion(S.exam.idx + 1); }
  else if (key === "ArrowLeft" || key === "b" || key === "B") { e.preventDefault(); openExamQuestion(S.exam.idx - 1); }
  else if (key === "f" || key === "F") toggleFlag();
  else if (key === "r" || key === "R") showExamGrid();
  else if (/^[0-9]$/.test(key)) { e.preventDefault(); pick(key === "0" ? 9 : +key - 1); }
  else if (key === "Backspace") {
    const { q, ans } = target();
    if (q.type === "order" && ans.seq.length) { e.preventDefault(); ans.seq.pop(); renderExam(); }
  } else if (key === "ArrowDown" || key === "ArrowUp") {
    const { q, ans } = target();
    if (q.type === "match") {
      e.preventDefault();
      ans.row = Math.max(0, Math.min(q.rows.length - 1, ans.row + (key === "ArrowDown" ? 1 : -1)));
      renderExam();
    }
  }
}

document.getElementById("nav-home").onclick = e => { e.preventDefault(); showHome(); };
document.getElementById("nav-progress").onclick = e => { e.preventDefault(); showProgress(); };

showHome();
