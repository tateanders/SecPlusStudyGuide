# Question file format

This is the spec for writing question files for the study app. Hand this whole file to Claude (or any writer) along with the topic you want covered.

A question file is a markdown (`.md`) file in the `questions/` folder. One file = one deck (for example one exam domain). Files whose names start with `_` (like `_aliases.md`) are not decks.

Check a file before dropping it in:

```
python3 study.py validate path/to/new-file.md
```

---

## 1. File layout

```markdown
---
deck: Domain 2 – Threats, Vulnerabilities, and Mitigations
section: "2.0"
topics:
  2.2: Explain common threat vectors and attack surfaces
  2.4: Given a scenario, analyze indicators of malicious activity
---

## d2-whaling-1
type: single
topic: 2.2
group: whaling

Stem text goes here (any markdown).

### Options
...

### Explanation
...

## d2-whaling-2
...
```

### Front matter (between the `---` lines at the top)

| Key | Required | Meaning |
|---|---|---|
| `deck` | yes | Display name of the deck. |
| `section` | no | Free text, e.g. `"2.0"` or `Week 3`. |
| `topic` | no | Default topic for questions in this file that don't set one. |
| `topics` | no | Map of topic code → readable name, shown in the progress view. Indent each entry two spaces. |
| `exam_weight` | no | This deck's share of an exam-mode exam, as a percentage (e.g. `22`). Decks without it are weighted by how many concepts they have. |

### Each question

1. A heading line `## <id>`. This starts a question.
2. Metadata lines `key: value` directly under the heading (no blank line before them).
3. A blank line, then the **stem**: the question text, any markdown, including tables and code blocks.
4. Sections, each starting with a `### Name` heading.

Metadata keys:

| Key | Required | Meaning |
|---|---|---|
| `type` | yes | `single`, `multi`, `typed`, `order`, `match`, or `pbq`. |
| `topic` | yes* | Objective/topic code, e.g. `2.2`. Plain text, so `ch3` or `week-2` also work. *Can come from the front matter default. PBQ parts inherit it from their parent. |
| `group` | strongly recommended | Variant group: questions that test the same concept share a group. |
| `tags` | no | Comma-separated free tags. |
| `shuffle` | no | `shuffle: no` keeps options in file order (e.g. options that are numbers in sequence). Default is to shuffle every time. |

Sections (which ones apply depends on the type):

| Section | Used by | Content |
|---|---|---|
| `### Options` | single, multi | `- [x] correct option` / `- [ ] wrong option`, each wrong option followed by an indented `why:` line. |
| `### Accept` | typed | One accepted answer per `-` line. |
| `### Wrong answers` | typed | Common wrong answers: `- answer: why it's wrong`. |
| `### Order` | order | Items **in the correct order**, numbered `1.`, `2.`, … Optional indented `why:` per item. |
| `### Match` | match | `- left => right` pairs. |
| `### Distractors` | match | Extra right-hand values that match nothing: `- value: why it's wrong`. |
| `### Exhibit` | any | Log snippet, config, table, network description. Shown in a box under the stem. |
| `### Explanation` | all (required, except on PBQ parts) | Why the correct answer is correct. |

`why:` lines are indented under their list item (two or more spaces). A long `why:` can continue on further indented lines.

---

## 2. IDs: the most important rule

Every question needs an ID in its `## ` heading. **Progress is stored against the ID**, so:

- IDs must be unique across **all** files. If two questions share an ID, the first one (alphabetical by file name) wins and the other is skipped with an error.
- Use lowercase letters, digits, `-` and `.` only. PBQ parts add `/part` (see below).
- Convention: `<deck prefix>-<concept slug>-<n>`, e.g. `d2-whaling-1`, `d2-whaling-2`, `d4-ir-order-1`.
- **Never rename an ID after you've studied it.** A renamed ID is a brand-new question; the old progress is orphaned.
- Reordering questions, moving them to another file, and rewording them is safe: progress follows the ID.
- If you **change the correct answer** of a question (different `[x]`, accepted answers, order or pairs), the app notices and makes that concept due again so you re-check it. To deliberately wipe a question's progress, give it a new ID.
- Deleting a question hides its history. If the same ID comes back later, its history comes back too.

---

## 3. Question types

### Single choice (`single`)

Exactly one `[x]`. Four options is standard.

```markdown
## d2-whaling-1
type: single
topic: 2.2
group: whaling

The CFO of a mid-sized company receives an email that appears to come from the company's outside legal counsel. It references a real pending acquisition and asks her to wire an escrow deposit before end of day. No one else in the company received the message. Which attack does this BEST describe?

### Options
- [ ] Spear phishing
  why: Spear phishing is any phishing aimed at a specific person or group. Close, but when the target is a senior executive the more precise term is whaling.
- [x] Whaling
- [ ] Vishing
  why: Vishing happens over voice calls. This attack arrived by email.
- [ ] Watering hole attack
  why: A watering hole compromises a website the targets visit. Nothing here involves a website.

### Explanation
Whaling is targeted phishing aimed at high-value executives. The giveaways: a single executive recipient, insider detail (the acquisition) that makes it believable, and an urgent financial request.
```

### Multiple select (`multi`)

Two or more `[x]`, and at least two wrong options. The app shows "Select N" automatically, so don't rely on the stem alone (but saying "Which TWO…" in the stem is fine and exam-like). Graded as an exact set: all correct options and nothing else.

```markdown
## d4-mfa-inherence-1
type: multi
topic: 4.6
group: mfa-factor-types

A hospital is replacing shared workstation passwords. The security team wants the second login factor to be "something you are" so it can't be shared between nurses. Which TWO methods meet that requirement?

### Options
- [x] Fingerprint reader
- [x] Palm vein scan
- [ ] Proximity badge
  why: A badge is something you have. It can be handed to a coworker.
- [ ] Workstation geolocation
  why: Location is "somewhere you are", a separate attribute from inherence (biometrics).
- [ ] Six-digit PIN
  why: A PIN is something you know, and it can be shared verbally.

### Explanation
"Something you are" means inherence factors: biometrics such as fingerprints, palm veins, retina or face. They're tied to the person's body, so they can't be passed around like badges or PINs.
```

### Typed short answer (`typed`)

The learner types the answer. List every form you'd accept. Typed questions can't be bluffed, so every concept should have at least one.

```markdown
## d2-whaling-2
type: typed
topic: 2.2
group: whaling

A phishing campaign built specifically to deceive a company's senior executives, such as the CEO or CFO, is known as what?

### Accept
- whaling
- whaling attack
- whale phishing

### Wrong answers
- spear phishing: Spear phishing targets any specific individual. The executive-specific term is whaling.
- phishing: Too general. The question asks for the term for attacks aimed at executives.

### Explanation
Whaling is the "big fish" form of spear phishing: the targets are executives with authority to move money or approve access.
```

**How typed answers are matched:**

- Case, spaces, hyphens and punctuation are ignored: `Pre-Shared Key` = `preshared key` = `pre shared key`. `SHA-256` = `SHA256`.
- One leading article the learner adds is ignored: `a firewall` matches `firewall`.
- Terms in `questions/_aliases.md` are interchangeable (e.g. `MFA` = `multifactor authentication`). Aliases match whole answers only.
- Dots, slashes and colons are kept when they touch a digit, so IPs, CIDRs and versions stay exact: `10.0.0.1` ≠ `100.0.1`, `802.1X` keeps its dot.

**Tricky cases. Handle these in `### Accept`:**

- **No typo tolerance.** `AES`/`DES`, `SSH`/`SSL`, `SAML`/`SAM` are one letter apart and all different real answers. A misspelling is wrong.
- **No plural stripping** (stripping `s` would turn `HTTPS` into `HTTP`). If `firewalls` is also acceptable, list it.
- **Acronym vs expansion:** list both (`- SAML` and `- Security Assertion Markup Language`) unless the pair is already in `_aliases.md`.
- **Numbers with words:** `636`, `port 636`, `tcp 636` and `tcp/636` are different strings. List the forms you'd accept.
- **Answers that start with "A":** the article rule only strips what the learner adds, so `A record` still requires the `A`. `record` alone won't match.
- **Ask for one specific thing.** "What should the analyst do?" has a dozen right phrasings and can't be typed-matched. "Which protocol…", "What port…", "What is this attack called?" work well.
- Use `### Wrong answers` for the confusions you expect. The learner sees that specific explanation when they type one.

### Ordering (`order`)

Write the items **in the correct order**. The app always shows them shuffled (never already in order). Graded as the exact sequence.

```markdown
## d4-ir-order-1
type: order
topic: 4.8
group: ir-process

A SOC analyst has just confirmed that ransomware is encrypting files on a file server. Put the remaining incident response activities in the correct order.

### Order
1. Analysis
   why: First scope it: which hosts, which strain, how it got in. You can't contain what you haven't scoped.
2. Containment
   why: Isolate affected systems to stop the spread before removing anything.
3. Eradication
   why: Remove the malware and close the entry point once it can no longer spread.
4. Recovery
   why: Restore from clean backups and return systems to service only after eradication.
5. Lessons learned
   why: The post-incident review comes last, once operations are stable.

### Explanation
After detection, the SY0-701 process continues: analysis → containment → eradication → recovery → lessons learned.
```

Use 4–7 items. Items must be distinct.

### Matching (`match`)

Each left-hand item gets one right-hand value. A right-hand value can be the answer for more than one row (SFTP and SSH are both 22 below). Add `### Distractors` (values that match nothing) so the last row can't be solved by elimination.

```markdown
## d4-secure-ports-1
type: match
topic: 4.5
group: secure-protocol-ports

Match each secure protocol to its default port.

### Match
- SSH => 22
- HTTPS => 443
- LDAPS => 636
- SFTP => 22

### Distractors
- 21: FTP's control port. FTP is unencrypted. SFTP runs over SSH on 22.
- 389: LDAP's unencrypted port. LDAPS uses 636.

### Explanation
SFTP is a subsystem of SSH, so it shares port 22. LDAPS and HTTPS have their own TLS ports.
```

### Scenario / PBQ (`pbq`)

A PBQ is a parent question (scenario stem + `### Exhibit` + `### Explanation`) followed by its **parts**. Each part is a normal question whose ID is `<parent id>/<part>` and whose type is `single`, `multi`, `typed`, `order` or `match`. Parts must come right after the parent, in the same file. They inherit the parent's topic and group; their own `### Explanation` is optional.

Everything shows on one page and is answered together. The PBQ only counts as correct if every part is right; the feedback shows each part separately.

````markdown
## d4-pbq-ssh-spray
type: pbq
topic: 2.4
group: auth-log-analysis

You're investigating an alert on `jump01`, an internet-facing Linux jump host. Review the exhibit and answer each part.

### Exhibit
```text
Nov 03 02:14:07 jump01 sshd[4121]: Failed password for admin from 203.0.113.45 port 51122 ssh2
Nov 03 02:14:09 jump01 sshd[4124]: Failed password for jdoe from 203.0.113.45 port 51130 ssh2
Nov 03 02:14:11 jump01 sshd[4127]: Failed password for mlopez from 203.0.113.45 port 51141 ssh2
Nov 03 02:14:13 jump01 sshd[4130]: Failed password for root from 203.0.113.45 port 51152 ssh2
Nov 03 02:14:15 jump01 sshd[4133]: Accepted password for svc_backup from 203.0.113.45 port 51160 ssh2
```

### Explanation
One source IP tried one password against many accounts, then got in on a service account. That's password spraying, and it succeeded against a weak service-account password.

## d4-pbq-ssh-spray/a
type: single

Which attack does the exhibit show?

### Options
- [x] Password spraying
- [ ] Brute force
  why: Brute force hammers one account with many passwords. Here each account gets a single attempt.
- [ ] Credential stuffing
  why: Stuffing replays leaked username/password pairs. Nothing here points to a breach list.
- [ ] Pass-the-hash
  why: Pass-the-hash reuses NTLM hashes on Windows. These are SSH password logins.

## d4-pbq-ssh-spray/b
type: multi

Which TWO controls would have MOST directly prevented this compromise?

### Options
- [x] Require SSH keys and disable password logins
- [x] Allow SSH only from the VPN address range
- [ ] Lower the account lockout threshold to 3 attempts
  why: Spraying deliberately stays at one or two attempts per account, under any lockout threshold.
- [ ] Move SSH from port 22 to port 2222
  why: That's security through obscurity. Scanners find nonstandard ports within minutes.

## d4-pbq-ssh-spray/c
type: typed

Which source IP address should be blocked at the perimeter firewall?

### Accept
- 203.0.113.45
````

Exhibits can be code blocks (logs, configs), markdown tables (firewall rules, asset lists), or plain text (network descriptions). Inside a code block, `##` lines are safe: they're not treated as headings.

### Aliases file (`questions/_aliases.md`, optional)

```markdown
- MFA = multifactor authentication
- PSK = pre-shared key
```

One line per set of equivalent terms. If any term on a line is an accepted answer, all of them are.

---

## 4. Writing good questions

The learner using this app is good at bluffing multiple choice. Every rule below exists to make bluffing fail.

### Wrong options must be plausible

- Use real terms from the **same objective**, ideally the ones people actually confuse (spear phishing vs whaling, IDS vs IPS, hashing vs encryption, RPO vs RTO).
- Every wrong option should be *right in some other situation*. Never use joke options or obviously absurd ones.
- Each wrong option gets a one-line `why:` that explains why it's wrong **here**, ideally naming what would make it right ("Vishing is over voice calls; this arrived by email").

### The stem must not contain or hint at the answer

The stem (and any format instruction in it) must never contain the answer, part of the answer, or a sample answer that happens to be the answer. This matters most for `typed` questions, where the whole point is recall.

| Don't write | Why it fails | Write instead |
|---|---|---|
| "Which key does Alice encrypt with? (Answer like "Bob's public key".)" | The "example" is the answer. | "Which key does Alice encrypt with? Name whose key and which kind." |
| "What type of attack is this? (Give the attack name, not the XSS subtype.)" | Naming what to leave out names the answer. | "What type of attack is attempted in the last log line? Give the general attack name." |
| "Is this an IDS or an IPS?" | A typed question becomes a 50/50 pick. | "What type of device is this sensor?" |
| "…and is often saved in a .pcap file?" (answer: packet capture / pcap) | A synonym or file name of the answer is in the stem. | Describe what it contains, not what it's called. |

Rules:

- **Format instructions describe the shape, never the content.** "Name whose key and which kind", "Give the protocol name", "Answer with a port number". Never quote an example answer, and never say "not X" or "don't give X" where X is (part of) an answer.
- **No accepted answer in the stem.** No term from `### Accept`, its acronym, its expansion or its file extension appears anywhere in the stem.
- **No either/or in typed stems.** "Is this passive or active?" belongs in a `single` question, not a `typed` one.
- **Choice questions:** don't repeat the correct option's words in the stem unless a wrong option's words appear there too.
- The validator warns when an accepted answer, or the correct option's text, appears in the stem.

### No giveaways

- **Length: the correct option may be at most 10 characters longer than the longest wrong option.** It can be the longest, just not obviously. Count characters (spaces included) before you finalize each question. If the correct option leads by more than 10, trim it or add a qualifier or clause to a distractor. For `multi`, compare the longest correct option to the longest wrong option.
- **Vary which option is longest.** Across a file, the correct option must be the longest in no more than 40% of `single`/`multi` questions. In most questions a wrong option should be the longest.
- The validator warns on both: "the correct option is N characters longer than the longest wrong option (max 10)" and "the correct option is the longest in N% of choice questions".
- **No "all of the above" / "none of the above" / "both A and B".**
- **Grammar must fit every option.** If the stem ends in "an", every option starts with a vowel sound. Singular/plural must agree for all options.
- **Absolutes:** don't put "always"/"never" only in wrong options.

### Abbreviations

- **Spell out every abbreviation the first time it appears in each question**, directly after it in parentheses: "HMAC (Hash-based Message Authentication Code)". Questions are shown one at a time, so do this per question, not once per file. Plurals and possessives go on the abbreviation: "VLANs (Virtual Local Area Networks)", "SSD's (Solid-State Drive) secure erase".
- **The expansion must not give away the answer.** If expanding an abbreviation in the stem would spell out the correct option, reword the stem so it doesn't use that abbreviation.
- **Expansions count toward option length.** If an abbreviation's first use is in the correct option, the expansion can push it past the 10-character limit. Lengthen the distractors or reword the option.
- Product names (BitLocker, NetFlow), exam codes (SY0-701) and literal values in logs or code blocks are not abbreviations.
- **Word echo:** don't repeat a distinctive word from the stem in the correct option only.
- **Position:** don't worry about it. The app shuffles options every time.
- Avoid one option that is the "most technical-sounding" or the only one with a qualifier.

### Prefer scenarios

- Write a short situation that requires a decision: "A company… Which control BEST…", "What should the analyst do FIRST?", "Which is the MOST likely cause?". That's what the real exam does.
- Plain definition recall is fine for `typed` variants ("What is this attack called?").
- Use exhibits (logs, configs, tables) where the topic allows. Make the learner *read evidence*.

### Explanations

- `### Explanation` says why the correct answer is right **and what in the stem points to it**. Two to four sentences.
- Every wrong option has its `why:`. For `typed`, list the likely confusions in `### Wrong answers`. For `match`, give each distractor a reason.

### Variants (critical)

- Every concept should have **at least 3 variants** in the same `group`, written with **different wording and different scenarios**, not the same question with options reshuffled.
- **Mix types within a group:** at least one `typed` or `multi` variant per concept. When the learner misses a concept, the app brings it back later as a different variant and prefers typed/multi, because those can't be bluffed.
- Variants must not give each other away. The scenario in one variant shouldn't contain the answer to another.
- A concept only becomes "solid" after the learner gets **two different variants** right, confidently, on **two different days**. (In cram mode the two-days part is off; two variants are still required.) A group with one question can't use this.

### Tagging

- `topic` = the objective code (for Security+ SY0-701: `1.1` … `5.6`). Add the objective names in the front matter `topics:` map so the progress view can show them.
- `group` = a short slug for the concept (`whaling`, `ir-process`, `secure-protocol-ports`). Groups are global across files, so make them specific.
- One file per domain/section keeps things tidy, e.g. `questions/d2-threats.md`.

---

## 5. Prompt to give Claude

Copy this, fill in the brackets, and attach this FORMAT.md:

> Using the attached FORMAT.md exactly, write a question file for **[exam / course]**, objective **[2.2 – Explain common threat vectors and attack surfaces]**.
>
> - Cover these concepts: **[list, or "every concept in the objective"]**.
> - For each concept, write 3–4 variants in one `group`, with different scenarios and wording. At least one variant per concept must be `typed` and one `single` or `multi`. Use `order`, `match` and `pbq` where the content naturally fits (processes → order, ports/protocols/definitions → match, log or config analysis → pbq).
> - IDs: prefix `[d2]-`, then a concept slug and a number. Check that no ID repeats. Don't reuse these existing IDs: **[paste the output of `grep -h '^## ' questions/*.md`, or say "none"]**.
> - Follow every rule in section 4: plausible distractors from the same objective, a `why:` on every wrong option, no length/grammar/"all of the above" giveaways, scenario-based stems.
> - **Never put the answer in the stem.** No example answer ("answer like …"), no "not X" that names the answer, no accepted answer or its acronym/expansion, and no "X or Y?" in typed questions. Format instructions describe the shape only ("name whose key and which kind").
> - **Abbreviations:** spell out each abbreviation in parentheses right after its first use in every question, for example "HMAC (Hash-based Message Authentication Code)", without letting the expansion reveal the answer.
> - **Length:** the correct option may be at most 10 characters longer than the longest wrong option, and the correct option is the longest in at most 40% of the choice questions.
> - For `typed` questions, list every reasonable accepted form (acronym and expansion, with/without "port", plurals if acceptable) and the common wrong answers.
> - Start the file with front matter: `deck`, `section`, and a `topics:` map with the official objective names.
> - Before you output, go through every question and check: (1) no accepted answer or correct-option wording appears in the stem; (2) count characters: the correct option leads the longest wrong option by 10 or fewer; (3) every wrong option has a `why:`; (4) no ID repeats; (5) every abbreviation is spelled out in parentheses at its first use in each question. Fix anything that fails.
> - Output only the file contents in one code block.

Then save it to `questions/`, run `python3 study.py validate questions/<file>.md`, and fix **everything** it reports, warnings included (or paste the output back to Claude). A file written to this spec should validate with zero warnings.
