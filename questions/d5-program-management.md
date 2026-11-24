---
deck: Domain 5 – Security Program Management and Oversight
section: "5.0"
exam_weight: 20
topics:
  5.1: Summarize elements of effective security governance
  5.2: Explain elements of the risk management process
  5.3: Explain the processes associated with third-party risk assessment and management
  5.4: Summarize elements of effective security compliance
  5.5: Explain types and purposes of audits and assessments
  5.6: Given a scenario, implement security awareness practices
---

## d5-govdoc-1
type: single
topic: 5.1
group: governance-documents

A document states, "All company laptops must use BitLocker full-disk encryption with a 256-bit key." It names a specific, mandatory technology. What type of document is this?

### Options
- [ ] Policy
  why: A policy states high-level goals, like "company data must be protected." It doesn't name specific technologies.
- [x] Standard
- [ ] Procedure
  why: A procedure gives step-by-step instructions for how to do something.
- [ ] Guideline
  why: Guidelines are recommendations, not mandatory.

### Explanation
A standard sets mandatory, specific requirements (which technology, which setting) that support a policy.

## d5-govdoc-2
type: match
topic: 5.1
group: governance-documents

Match each statement to the type of governance document it comes from.

### Match
- "The company will protect customer data from unauthorized access." => Policy
- "Passwords must be at least 14 characters." => Standard
- "Step 1: Open the admin console. Step 2: Select the user. Step 3: Click Reset." => Procedure
- "Consider using a passphrase made of several random words." => Guideline

### Distractors
- Playbook: A playbook is a step-by-step response plan for a specific type of incident. None of these describe incident response.

### Explanation
Policies state intent, standards set mandatory specifics, procedures give steps, and guidelines give optional advice.

## d5-govdoc-4
type: single
topic: 5.1
group: governance-documents

Which document do employees typically sign to confirm they understand what they may and may not do with company computers and networks?

### Options
- [x] Acceptable use policy
- [ ] Business continuity plan
  why: A BCP (Business Continuity Plan) covers keeping operations running during a disruption.
- [ ] Change management policy
  why: Change management governs changes to systems, not employee behavior.
- [ ] Data retention standard
  why: Retention covers how long data is kept.

### Explanation
The AUP (acceptable use policy) defines allowed and prohibited use of company resources. It's usually signed during onboarding.

## d5-govstruct-1
type: single
topic: 5.1
group: governance-structures

A large company has each business unit make its own security decisions, with no central security team setting rules. What governance structure is this?

### Options
- [x] Decentralized
- [ ] Centralized
  why: Centralized governance has one central authority making decisions.
- [ ] Federated identity
  why: Federation is about trusting another organization's authentication.
- [ ] Matrix
  why: Matrix is an org chart term, not one of the SY0-701 governance structures.

### Explanation
Decentralized governance pushes decisions to individual units. It's flexible, but security can be inconsistent across the company.

## d5-govstruct-3
type: multi
topic: 5.1
group: governance-structures

Which TWO are governance structures listed in SY0-701?

### Options
- [x] Boards
- [x] Committees
- [ ] Honeynets
  why: Honeynets are decoy networks.
- [ ] Jump servers
  why: Jump servers are infrastructure.
- [ ] Load balancers
  why: Load balancers are infrastructure.

### Explanation
SY0-701 governance structures include boards, committees, government entities, and centralized or decentralized models.

## d5-dataroles-1
type: single
topic: 5.1
group: data-roles

The VP (Vice President) of Sales decides how the customer database should be classified and who should have access to it. What is her data role?

### Options
- [x] Data owner
- [ ] Data custodian
  why: Custodians carry out the owner's decisions, like running backups and applying permissions.
- [ ] Data processor
  why: A processor handles data on behalf of a controller, usually a third party.
- [ ] Data subject
  why: The data subject is the person the data is about.

### Explanation
The data owner is a senior person accountable for the data. They decide classification and access. Others carry it out.

## d5-data-roles-1
type: single
topic: 5.1
group: data-roles

A retailer collects customer email addresses and decides they'll be used for marketing. It hires an outside email platform that sends the campaigns strictly according to the retailer's instructions. Under privacy regulations such as GDPR (General Data Protection Regulation), what is the email platform's role?

### Options
- [x] Data processor
- [ ] Data controller
  why: The controller decides why and how the data is used. That's the retailer.
- [ ] Data subject
  why: The subjects are the customers the email addresses belong to.
- [ ] Data custodian
  why: A custodian handles day-to-day storage and protection, usually inside the organization. The regulatory term for an outside party acting on instructions is different.

### Explanation
A processor handles personal data on behalf of the controller and only as instructed. "Hires an outside platform" and "strictly according to the retailer's instructions" are the cues.

## d5-data-roles-3
type: match
topic: 5.1
group: data-roles

Match each responsibility to the data role.

### Match
- Decides why and how personal data is processed => Controller
- Runs backups and applies the access permissions that were approved => Custodian
- Handles personal data on another organization's behalf => Processor
- Is the person the personal data is about => Subject
- Is accountable for a data set and sets its classification => Owner

### Distractors
- Auditor: An auditor checks whether the roles are doing their jobs. It isn't a data role.
- Regulator: A regulator enforces the law from outside the organization.

### Explanation
Controller and processor are the privacy-law pair (decides versus acts on instructions). Owner and custodian are the internal pair (accountable versus hands-on).

## d5-govproc-1
type: single
topic: 5.1
group: governance-procedures

The SOC (Security Operations Center) has a document for ransomware incidents that lists exactly who to call, which systems to isolate first, and which evidence to collect, in order. What is this document?

### Options
- [x] A playbook
- [ ] A guideline
  why: Guidelines are optional recommendations. This document gives required steps for a specific situation.
- [ ] A policy
  why: A policy states high-level intent. It doesn't list step-by-step actions for one incident type.
- [ ] A memorandum of understanding
  why: An MOU (Memorandum of Understanding) is a non-binding agreement between organizations.

### Explanation
A playbook is a step-by-step procedure for a specific scenario, such as a ransomware or phishing incident. Playbooks are often automated in SOAR (Security Orchestration, Automation, and Response) platforms.

## d5-govproc-2
type: single
topic: 5.1
group: governance-procedures

A company's developers keep shipping features with security flaws that are only found after release. Which governance document would MOST directly fix this by requiring security reviews and testing at every phase of development?

### Options
- [ ] An acceptable use policy for developers
  why: An AUP (Acceptable Use Policy) governs how employees use company resources, not how software is built.
- [x] An SDLC (Software Development Life Cycle) policy
- [ ] A business continuity policy for the dev team
  why: Business continuity covers keeping operations running through disruption.
- [ ] A data retention standard
  why: Retention covers how long data is kept.

### Explanation
A software development life cycle policy builds security into requirements, design, coding, testing, and deployment, so flaws are caught before release instead of after.

## d5-govproc-3
type: single
topic: 5.1
group: governance-procedures

A multinational company has to revise its security policies because a country where it operates passed a new data protection law. Which governance consideration drove the change?

### Options
- [ ] Internal performance metrics
  why: Metrics measure how the program performs. The trigger here came from outside the company.
- [x] External regulatory and legal requirements
- [ ] A risk appetite statement from the board
  why: The board's appetite didn't change. A new law did.
- [ ] A change advisory board decision
  why: The CAB (Change Advisory Board) approves technical changes to systems, not policy changes driven by new laws.

### Explanation
SY0-701 lists external considerations for governance: regulatory, legal, industry, and local, regional, national and global requirements. Policies need regular monitoring and revision when these change.

## d5-policy-1
type: match
topic: 5.1
group: policies-standards

Match each requirement to the governance document it belongs in.

### Match
- How the company will restore servers and data at an alternate site after a data center fire => Disaster recovery policy
- How staff report and handle a suspected breach => Incident response policy
- "All laptops must use full-disk encryption with 256-bit keys." => Encryption standard
- "Badges must be worn visibly, and visitors must be escorted at all times." => Physical security standard

### Distractors
- Business continuity policy: Business continuity keeps the whole business running. Restoring servers and data specifically is disaster recovery.

### Explanation
SY0-701 policies include acceptable use, information security, business continuity, disaster recovery, incident response, SDLC (Software Development Life Cycle) and change management. Standards cover password, access control, physical security and encryption.

## d5-policy-2
type: single
topic: 5.1
group: policies-standards

On an employee's last day, IT (Information Technology) disables their accounts, collects their laptop and badge, and moves their files to their manager, using the same documented checklist every time. What type of governance document is the checklist?

### Options
- [x] An offboarding procedure
- [ ] An acceptable use policy
  why: An AUP (Acceptable Use Policy) says how employees may use company resources. It isn't a list of steps for departures.
- [ ] An information security policy
  why: A policy states high-level intent. Step-by-step actions belong in a procedure.
- [ ] A password standard
  why: A password standard sets password rules. It doesn't cover departing employees.

### Explanation
Procedures are step-by-step instructions. SY0-701 lists change management, onboarding/offboarding and playbooks as procedures.

## d5-riskcalc-3
type: match
topic: 5.2
group: risk-calculation

Match each risk term to its definition.

### Match
- The percentage of an asset's value lost in one event => Exposure factor
- The expected cost of one occurrence of a risk => Single loss expectancy
- How many times per year a risk is expected to occur => Annualized rate of occurrence
- The expected yearly cost of a risk => Annualized loss expectancy

### Distractors
- Risk tolerance: Tolerance is how much deviation from the risk appetite is acceptable, not a calculation value.

### Explanation
EF (Exposure Factor) × asset value = SLE (Single Loss Expectancy). SLE × ARO (Annualized Rate of Occurrence) = ALE (Annualized Loss Expectancy).

## d5-pbq-risk
type: pbq
topic: 5.2
group: risk-calculation

A company is reviewing ransomware risk for its file server.

### Exhibit
| Item | Value |
|---|---|
| File server and data value | $500,000 |
| Expected loss per ransomware event | 40% of value |
| Expected frequency | Once every 2 years |
| Cyber insurance premium | $60,000 per year |
| Offline backup solution | $30,000 per year, reduces loss per event to 5% |

### Explanation
SLE (Single Loss Expectancy) = $500,000 × 0.40 = $200,000. ARO (Annualized Rate of Occurrence) = 0.5. ALE (Annualized Loss Expectancy) = $100,000. With backups, SLE drops to $25,000, so ALE drops to $12,500. Paying $30,000 to cut expected yearly losses by $87,500 is worthwhile.

## d5-pbq-risk/a
type: single

What is the annualized loss expectancy without the backup solution?

### Options
- [ ] $200,000
  why: That's the SLE ($500,000 × 40%). It still has to be multiplied by the ARO (Annualized Rate of Occurrence).
- [x] $100,000
- [ ] $400,000
  why: That multiplies by 2 instead of 0.5. Once every 2 years is an ARO of 0.5.
- [ ] $250,000
  why: That's half the asset value. The exposure factor is 40%, not 50%.

## d5-pbq-risk/b
type: single

What is the annualized loss expectancy with the offline backup solution in place?

### Options
- [x] $12,500
- [ ] $25,000
  why: That's the new SLE ($500,000 × 5%). Multiply it by the ARO (Annualized Rate of Occurrence) of 0.5.
- [ ] $50,000
  why: That would be 10% of value per year. The new exposure factor is 5%, and the ARO is 0.5.
- [ ] $87,500
  why: That's how much the backups reduce the ALE (Annualized Loss Expectancy), not the ALE itself.

## d5-pbq-risk/c
type: single

Buying the cyber insurance policy is which risk response?

### Options
- [x] Transfer
- [ ] Mitigate
  why: The backup solution is mitigation. Insurance shifts the financial impact.
- [ ] Accept
  why: Accepting means doing nothing extra.
- [ ] Avoid
  why: Avoiding would mean getting rid of the file server.

## d5-ale-2
type: single
topic: 5.2
group: risk-calculation

A company's laptops cost $1,500 each. When one is stolen the full value is lost, and the company loses about 12 laptops a year. A vendor offers tracking software for $20,000 per year that would cut thefts to 2 per year. From a purely quantitative standpoint, what should the risk analyst conclude?

### Options
- [x] The software costs more than the loss it prevents
- [ ] The software pays for itself within the first year
  why: It prevents $15,000 of loss a year ($18,000 down to $3,000) but costs $20,000.
- [ ] The annual loss with the software would be $18,000
  why: $18,000 is the loss without it (12 × $1,500). With it the loss is 2 × $1,500 = $3,000.
- [ ] The loss per stolen laptop with the software is $3,000
  why: Each theft still costs $1,500. The $3,000 figure is the yearly total with the software.

### Explanation
ALE (Annualized Loss Expectancy) before = 12 × $1,500 = $18,000. ALE after = 2 × $1,500 = $3,000. The control saves $15,000 a year and costs $20,000, so on numbers alone it isn't justified.

## d5-appetite-1
type: single
topic: 5.2
group: risk-appetite-tolerance

The board states that the company is willing to take on high risk to launch new products quickly. Which term BEST describes this statement?

### Options
- [x] Risk appetite
- [ ] Risk tolerance
  why: Tolerance is how much variation from the appetite is acceptable for a specific risk.
- [ ] Residual risk
  why: Residual risk is what's left after controls.
- [ ] Risk threshold
  why: A threshold is a specific trigger level, not a broad statement of willingness.

### Explanation
Risk appetite is the overall amount of risk an organization is willing to pursue to meet its goals. SY0-701 describes appetites as expansionary, conservative or neutral.

## d5-appetite-3
type: match
topic: 5.2
group: risk-appetite-tolerance

Match each risk appetite to its description.

### Match
- Willing to take on more risk in pursuit of growth => Expansionary
- Prefers to avoid risk even if it means missing opportunities => Conservative
- Balances risk and opportunity without leaning either way => Neutral

### Distractors
- Residual: Residual is the risk left after controls, not an appetite.
- Inherent: Inherent is the risk before controls, not an appetite.

### Explanation
SY0-701 lists three risk appetite types: expansionary, conservative and neutral.

## d5-response-1
type: single
topic: 5.2
group: risk-responses

A company decides to stop offering an online payment feature because the risk is too high and can't be reduced affordably. Which risk response is this?

### Options
- [x] Avoid
- [ ] Accept
  why: Accepting means keeping the feature and living with the risk.
- [ ] Transfer
  why: Transfer shifts the impact to a third party, like an insurer.
- [ ] Mitigate
  why: Mitigation reduces the risk while keeping the activity.

### Explanation
Avoiding a risk means stopping the activity that creates it.

## d5-response-2
type: match
topic: 5.2
group: risk-responses

Match each action to the risk response.

### Match
- Buying cyber insurance => Transfer
- Installing a WAF (Web Application Firewall) in front of a vulnerable app => Mitigate
- Documenting that a low-impact risk will be left as is => Accept
- Shutting down a legacy service instead of securing it => Avoid

### Distractors
- Exemption: An exemption is a formal approval not to meet a requirement. It's a form of acceptance, but "accept" is the response itself.

### Explanation
Transfer shifts impact, mitigate reduces likelihood or impact, accept lives with the risk, and avoid stops the activity.

## d5-response-4
type: multi
topic: 5.2
group: risk-responses

Which TWO are forms of risk acceptance in SY0-701?

### Options
- [x] Exemption
- [x] Exception
- [ ] Insurance
  why: Insurance is transfer.
- [ ] Segmentation
  why: Segmentation is mitigation.
- [ ] Decommissioning the system
  why: Removing the system is avoidance.

### Explanation
SY0-701 lists exemptions and exceptions under acceptance. Both are formal approvals to live with a risk instead of fixing it.

## d5-register-1
type: single
topic: 5.2
group: risk-register

A company keeps a document listing each identified risk, its likelihood, impact, owner and current response. What is this document?

### Options
- [x] Risk register
- [ ] Business impact analysis
  why: A BIA (Business Impact Analysis) identifies critical functions and recovery targets, not a full list of risks.
- [ ] Asset inventory
  why: An inventory lists assets, not risks.
- [ ] Change log
  why: A change log records system changes.

### Explanation
A risk register tracks all known risks with their details and owners. It's a living document.

## d5-register-3
type: single
topic: 5.2
group: risk-register

In a risk register, who is the risk owner?

### Options
- [x] The person accountable for managing that risk
- [ ] The attacker most likely to exploit it
  why: That's a threat actor.
- [ ] The person who first reported the risk
  why: Reporting a risk doesn't make you accountable for it.
- [ ] The auditor who reviews it
  why: Auditors review. They don't own the risk.

### Explanation
Each risk should have an owner who is accountable for monitoring it and making sure the response is carried out.

## d5-register-4
type: single
topic: 5.2
group: risk-register

The risk register entry for phishing includes a metric: "more than 5% of employees click a simulated phish in a quarter." When the metric crosses that line, the risk is escalated. What is this metric?

### Options
- [x] A key risk indicator
- [ ] Single loss expectancy
  why: SLE (Single Loss Expectancy) is the dollar cost of one event. This measures a trend that signals rising risk.
- [ ] Recovery point objective
  why: RPO (Recovery Point Objective) is the maximum acceptable data loss in a recovery.
- [ ] Residual risk
  why: Residual risk is what's left after controls. This is a measurement used to watch the risk.

### Explanation
A KRI (Key Risk Indicator) is a metric that warns when a risk is rising. The level that triggers action is the risk threshold. Both are tracked in the risk register alongside the risk owner.

## d5-bia-1
type: single
topic: 5.2
group: bia-metrics

During a business impact analysis, the team decides the order system must be back online within 4 hours of an outage. Which metric is this?

### Options
- [x] RTO (Recovery Time Objective)
- [ ] RPO (Recovery Point Objective)
  why: RPO is how much data loss is acceptable, not how long the system can be down.
- [ ] MTBF (Mean Time Between Failures)
  why: MTBF is the average time between failures.
- [ ] MTTR (Mean Time to Repair)
  why: MTTR is the average time it actually takes to repair, not the target.

### Explanation
The recovery time objective is the maximum acceptable downtime before a system must be restored.

## d5-bia-3
type: match
topic: 5.2
group: bia-metrics

Match each metric to its meaning.

### Match
- Maximum acceptable downtime => RTO (Recovery Time Objective)
- Maximum acceptable data loss, measured in time => RPO (Recovery Point Objective)
- Average time to fix a failed component => MTTR (Mean Time to Repair)
- Average time a component runs before it fails => MTBF (Mean Time Between Failures)

### Distractors
- ALE (Annualized Loss Expectancy): ALE is the expected yearly cost of a risk, not a recovery metric.

### Explanation
RTO and RPO are targets set in the BIA (Business Impact Analysis). MTTR and MTBF are measured from how equipment actually performs.

## d5-bia-4
type: single
topic: 5.2
group: bia-metrics

A storage array has a high MTBF (Mean Time Between Failures) but a long MTTR (Mean Time to Repair). What does that mean?

### Options
- [x] It rarely fails, but repairs take a long time
- [ ] It fails often, but it's fixed quickly each time
  why: That's a low MTBF and a short MTTR.
- [ ] It fails often and takes a long time to fix
  why: That would be a low MTBF.
- [ ] It's reliable enough that backups can be skipped
  why: No metric removes the need for backups.

### Explanation
A higher MTBF means more reliable. A longer MTTR means slower to repair.

## d5-qualquant-1
type: single
topic: 5.2
group: qualitative-quantitative

A team rates each risk as low, medium or high for likelihood and impact, and plots them on a heat map. What type of risk analysis is this?

### Options
- [x] Qualitative
- [ ] Quantitative
  why: Quantitative uses numbers and dollar values like SLE (Single Loss Expectancy) and ALE (Annualized Loss Expectancy).
- [ ] Continuous
  why: Continuous describes how often assessments happen, not how risks are measured.
- [ ] Ad hoc
  why: Ad hoc means one-time and unscheduled, not a type of measurement.

### Explanation
Qualitative analysis uses ratings and judgment. It's fast but subjective.

## d5-qualquant-3
type: multi
topic: 5.2
group: qualitative-quantitative

Which TWO statements about risk assessment frequency are correct according to SY0-701?

### Options
- [x] Ad hoc assessments happen in response to a specific event
- [x] Continuous assessments monitor risk on an ongoing basis
- [ ] Recurring assessments happen only after a breach
  why: Recurring assessments happen on a regular schedule.
- [ ] One-time assessments replace the need for any others
  why: Risk changes over time, so a single assessment goes stale.
- [ ] Continuous assessments are only done by auditors
  why: Continuous monitoring is usually done by internal tools and teams.

### Explanation
SY0-701 lists ad hoc, recurring, one-time and continuous assessments.

## d5-qualquant-4
type: single
topic: 5.2
group: qualitative-quantitative

An analyst says a flood has a 2% chance of hitting the data center in any given year. A colleague simply rates flooding as "unlikely." How do the two statements differ?

### Options
- [x] The first is probability; the second is likelihood
- [ ] The first is likelihood; the second is probability
  why: This is reversed. A numeric chance is probability, and a descriptive rating is likelihood.
- [ ] Both are the annualized loss expectancy
  why: Annualized loss expectancy is a dollar amount per year, not a chance of occurring.
- [ ] Both describe the exposure factor
  why: Exposure factor is the percentage of an asset's value lost in one event.

### Explanation
Probability is a measured, numeric chance used in quantitative analysis. Likelihood is a descriptive rating such as low, medium or high, used in qualitative analysis.

## d5-riskproc-1
type: single
topic: 5.2
group: risk-process

A new risk manager interviews department heads, reviews past incidents and scan results, and lists everything that could harm the business. No ratings or values are assigned yet. Which risk management step is this?

### Options
- [x] Risk identification
- [ ] Risk analysis
  why: Analysis rates likelihood and impact. Nothing has been rated yet.
- [ ] Risk reporting
  why: Reporting communicates risks to leadership after they're understood.
- [ ] Setting the risk appetite
  why: Risk appetite is leadership's overall willingness to take risk, not a list of specific risks.

### Explanation
Risk management starts with risk identification, then assessment and analysis, then a response strategy, with ongoing risk reporting.

## d5-riskproc-2
type: single
topic: 5.2
group: risk-process

Every quarter, the CISO (Chief Information Security Officer) gives the board a summary of the top risks, how they've changed, and which ones exceed the company's tolerance. What is this activity?

### Options
- [x] Risk reporting
- [ ] A business impact analysis
  why: A BIA (Business Impact Analysis) works out recovery needs for business functions. It isn't a recurring briefing.
- [ ] Risk identification
  why: Identification finds new risks. This briefing communicates the status of known ones.
- [ ] A risk transfer
  why: Transfer shifts risk to another party, for example through insurance.

### Explanation
Risk reporting keeps leadership informed about the risk posture so it can make decisions, such as funding mitigations or accepting risks.

## d5-agree-a-4
type: single
topic: 5.3
group: agreements-service

A company plans to hire the same penetration testing firm for several projects over three years. It wants to negotiate legal and payment terms once instead of for every project. What should it sign FIRST?

### Options
- [x] Master service agreement
- [ ] Statement of work
  why: An SOW (Statement of Work) covers one project. The umbrella terms go in the MSA (Master Service Agreement).
- [ ] Memorandum of understanding
  why: An MOU (Memorandum of Understanding) is non-binding and isn't used for a paid vendor relationship like this.
- [ ] Service-level agreement
  why: An SLA (Service-Level Agreement) sets performance targets. It isn't the overall legal framework.

### Explanation
An MSA sets the shared terms for an ongoing relationship. Each project then gets a shorter SOW.

## d5-agreements-1
type: single
topic: 5.3
group: agreements-service

A company signs a contract with a cloud hosting provider. One document in the contract states that the hosting will be up 99.95% of each month and specifies the credits the provider owes if it falls short. Which agreement type is that document?

### Options
- [x] Service-level agreement
- [ ] Memorandum of understanding
  why: An MOU (Memorandum of Understanding) states intent and is usually not binding. It wouldn't carry uptime targets or penalties.
- [ ] Non-disclosure agreement
  why: An NDA (Non-Disclosure Agreement) protects confidential information. It says nothing about performance.
- [ ] Master service agreement
  why: An MSA (Master Service Agreement) sets the general legal terms for the whole relationship. Measurable targets like uptime live in a separate document.

### Explanation
A service-level agreement defines measurable performance (uptime, response time) and what happens when the provider misses it. A percentage target with credits attached is the signature.

## d5-agreements-3
type: match
topic: 5.3
group: agreements-service

Match each description to the agreement type.

### Match
- Sets measurable performance targets such as uptime, with penalties => SLA (Service-Level Agreement)
- Protects confidential information shared between the parties => NDA (Non-Disclosure Agreement)
- Defines the tasks, deliverables, and timeline for one project => SOW (Statement of Work)
- Sets the overall legal terms that later project documents fall under => MSA (Master Service Agreement)
- Governs how two companies split profits and duties in a joint venture => BPA (Business Partners Agreement)

### Distractors
- MOU (Memorandum of Understanding): A memorandum of understanding is a non-binding statement of intent. None of these descriptions fits it.
- AUP (Acceptable Use Policy): An acceptable use policy is an internal policy for users, not an agreement with a vendor or partner.

### Explanation
The MSA is the umbrella, and each SOW under it describes one piece of work. The SLA measures performance, the NDA covers secrecy, and the BPA covers a shared business.

## d5-agree-b-1
type: single
topic: 5.3
group: agreements-partner

Two universities agree in writing to "work together on cybersecurity research" but the document creates no legal obligations. Which document is this?

### Options
- [x] MOU (Memorandum of Understanding)
- [ ] MOA (Memorandum of Agreement)
  why: An MOA is more formal and spells out specific responsibilities each side agrees to.
- [ ] MSA (Master Service Agreement)
  why: An MSA is a binding contract for services.
- [ ] SLA (Service-Level Agreement)
  why: An SLA sets performance metrics.

### Explanation
A memorandum of understanding states shared intent and goals. It's usually not legally binding.

## d5-agree-b-4
type: single
topic: 5.3
group: agreements-partner

How does an MOA (Memorandum of Agreement) differ from an MOU (Memorandum of Understanding)?

### Options
- [x] An MOA spells out specific duties for each party
- [ ] An MOA is non-binding, while an MOU is a legally binding contract
  why: It's roughly the other way around. The MOU is the less formal one.
- [ ] An MOA sets uptime and performance guarantees
  why: Performance guarantees belong in an SLA (Service-Level Agreement).
- [ ] An MOA is only used between a company and its employees
  why: MOAs are between organizations.

### Explanation
Both describe cooperation, but an MOA is more formal and specific about who does what. An MOU mainly states shared intent.

## d5-vendor-5
type: single
topic: 5.3
group: agreements-partner

Before a hired firm starts a penetration test, both sides sign a document that sets the in-scope systems, allowed techniques, testing hours, and who to call if something breaks. What is this document?

### Options
- [ ] A service-level agreement
  why: An SLA (Service-Level Agreement) sets performance targets such as uptime.
- [ ] A memorandum of understanding
  why: An MOU (Memorandum of Understanding) is a non-binding statement of shared goals.
- [x] Rules of engagement
- [ ] A business partners agreement
  why: A BPA (Business Partners Agreement) covers how partners share profits and duties.

### Explanation
Rules of engagement define exactly what testers may do, when, and how to escalate. They protect both the client and the testers and keep testing within its legal authorization.

## d5-vendor-1
type: single
topic: 5.3
group: vendor-assessment

A company wants the contractual ability to inspect a cloud vendor's security controls itself, or send an auditor to do it. What should be in the contract?

### Options
- [x] A right-to-audit clause
- [ ] A non-disclosure agreement
  why: An NDA (Non-Disclosure Agreement) protects confidentiality. It doesn't grant audit rights.
- [ ] A memorandum of understanding
  why: An MOU (Memorandum of Understanding) is non-binding.
- [ ] A rules of engagement document
  why: Rules of engagement define how testing is done, not the contractual right to audit.

### Explanation
A right-to-audit clause gives the customer the legal right to examine the vendor's controls.

## d5-vendor-3
type: multi
topic: 5.3
group: vendor-assessment

Before signing with a new payroll vendor, which TWO activities are part of vendor due diligence?

### Options
- [x] Sending a security questionnaire
- [x] Reviewing its SOC 2 (System and Organization Controls 2) audit report
- [ ] Running an unannounced penetration test on the vendor's systems
  why: Testing a vendor's systems without permission is unauthorized and illegal.
- [ ] Giving the vendor domain admin access to evaluate it
  why: That's a huge risk and not part of evaluation.
- [ ] Skipping the review because the vendor is well known
  why: Reputation doesn't replace due diligence.

### Explanation
Vendor assessments use questionnaires, independent assessments, evidence of internal audits, and supply chain analysis.

## d5-vendor-4
type: single
topic: 5.3
group: vendor-assessment

A company is choosing between two security vendors. During selection, it learns that the procurement manager's spouse owns one of them. What vendor selection issue is this?

### Options
- [x] Conflict of interest
- [ ] Right-to-audit clause
  why: A right-to-audit clause lets the customer inspect a vendor's controls. It doesn't address personal ties.
- [ ] Supply chain analysis
  why: Supply chain analysis looks at a vendor's own suppliers and dependencies.
- [ ] Rules of engagement
  why: Rules of engagement define how a test or engagement is carried out.

### Explanation
Vendor selection includes due diligence and checking for conflicts of interest. A personal relationship with a vendor can bias the decision, so it should be disclosed and the person removed from the selection.

## d5-vendmon-1
type: single
topic: 5.3
group: vendor-monitoring

A company signed a cloud payroll vendor two years ago after a full security review. Nobody has checked the vendor's security since. Which third-party risk activity is missing?

### Options
- [x] Ongoing vendor monitoring
- [ ] Vendor selection due diligence
  why: Due diligence happens before signing, and it was done.
- [ ] A conflict of interest check
  why: Conflict of interest checks are part of vendor selection, not ongoing oversight.
- [ ] Rules of engagement
  why: Rules of engagement define how a test or engagement is carried out.

### Explanation
Vendor risk changes over time, so vendors need ongoing monitoring: periodic questionnaires, reviews of audit reports and security ratings, and watching for breaches.

## d5-vendmon-2
type: single
topic: 5.3
group: vendor-monitoring

Six months into a contract, a company's monitoring service reports that its file-transfer vendor appeared in a breach report and its security rating dropped. What should the company do NEXT?

### Options
- [x] Reassess the vendor and ask for evidence of fixes
- [ ] Wait for the annual review in the contract
  why: A breach is a trigger for action now. Waiting leaves the company's data exposed.
- [ ] Ask the vendor to sign a new NDA (Non-Disclosure Agreement)
  why: An NDA protects confidential information. It does nothing about the vendor's security weakness.
- [ ] Cancel all vendor agreements company-wide
  why: This overreacts and disrupts the business. Start by reassessing the affected vendor.

### Explanation
Vendor monitoring catches changes in a vendor's risk. A breach or rating drop should trigger reassessment, requests for evidence and, if needed, contract action.

## d5-diligence-1
type: single
topic: 5.4
group: due-diligence-care

Before acquiring another company, a firm investigates its security practices, past breaches and compliance status. Which concept is this?

### Options
- [x] Due diligence
- [ ] Due care
  why: Due care is taking reasonable actions to protect, on an ongoing basis. Investigating before a decision is due diligence.
- [ ] Attestation
  why: Attestation is a formal statement that controls are in place.
- [ ] Legal hold
  why: A legal hold preserves data for litigation.

### Explanation
Due diligence is the research and investigation done to understand risks before acting.

## d5-diligence-3
type: single
topic: 5.4
group: due-diligence-care

A company did a thorough risk assessment and found its web servers were unpatched, but never patched them. A breach followed. What did the company fail to show?

### Options
- [x] Due care
- [ ] Due diligence
  why: The risk assessment was due diligence, and it was done. The failure was not acting on it.
- [ ] Data sovereignty
  why: Sovereignty is about which laws apply to data.
- [ ] Risk transfer
  why: Transfer shifts impact to a third party.

### Explanation
They investigated (due diligence) but didn't take reasonable action (due care). Courts and regulators look for both.

## d5-compliance-1
type: multi
topic: 5.4
group: compliance-consequences

A company is found violating PCI DSS. Which TWO are consequences of non-compliance listed in SY0-701?

### Options
- [x] Fines
- [x] Loss of license
- [ ] Automatic data sovereignty
  why: Sovereignty is a legal concept, not a penalty.
- [ ] A free security audit
  why: Audits after violations are usually at the company's expense.
- [ ] Mandatory risk acceptance
  why: Regulators don't force acceptance. They require fixes.

### Explanation
SY0-701 consequences of non-compliance include fines, sanctions, reputational damage, loss of license, and contractual impacts.

## d5-compliance-3
type: single
topic: 5.4
group: compliance-consequences

A company is required to report security incidents to its state regulator within 72 hours. What type of compliance reporting is this?

### Options
- [x] External
- [ ] Internal
  why: Internal reporting goes to the company's own leadership or board.
- [ ] Ad hoc
  why: Ad hoc describes when an assessment happens, not who receives a report.
- [ ] Qualitative
  why: Qualitative describes how risk is measured.

### Explanation
External compliance reporting goes to regulators, customers or other outside parties. Internal reporting goes to the company's own leaders.

## d5-privacy-1
type: single
topic: 5.4
group: privacy-rights

A former customer of a European online store asks the company to permanently delete all of her personal data. Which GDPR (General Data Protection Regulation) right is she using?

### Options
- [x] Right to be forgotten
- [ ] Right to audit
  why: Right to audit is a contract clause between companies.
- [ ] Data sovereignty
  why: Sovereignty is about which country's laws apply.
- [ ] Legal hold
  why: A legal hold requires keeping data, not deleting it.

### Explanation
The right to be forgotten (right to erasure) lets individuals ask for their personal data to be deleted, with some exceptions.

## d5-privacy-3
type: multi
topic: 5.4
group: privacy-rights

A company is building a privacy program. Which TWO items should it maintain?

### Options
- [x] A data inventory of what personal data it holds and where
- [x] Retention rules for each type of personal data
- [ ] A list of employees' personal passwords
  why: Storing users' passwords is a security risk, not a privacy control.
- [ ] Public copies of all customer records
  why: That would violate privacy.
- [ ] A policy to keep all customer data forever, just in case
  why: Keeping data forever increases risk and often violates privacy law.

### Explanation
SY0-701 privacy elements include data inventory and retention, plus knowing the roles of data subjects, controllers and processors.

## d5-compmon-1
type: single
topic: 5.4
group: compliance-monitoring

Each year, every employee must sign electronically to confirm they've read the updated data handling policy. Which compliance monitoring element is this?

### Options
- [x] Acknowledgement
- [ ] Due care
  why: Due care is the ongoing effort to protect assets. The signature is a specific record of awareness.
- [ ] Attestation by an external auditor
  why: Attestation is a formal statement by leadership or an auditor that controls meet a requirement.
- [ ] Automation
  why: Automation uses tools to check compliance. This is a person confirming they've read a policy.

### Explanation
Compliance monitoring in SY0-701 includes due diligence/care, attestation and acknowledgement, internal and external monitoring, and automation. Acknowledgement records that people know the rules.

## d5-compmon-2
type: single
topic: 5.4
group: compliance-monitoring

A company with thousands of cloud resources uses a tool that checks each resource against PCI DSS (Payment Card Industry Data Security Standard) controls every hour and flags drift. Which compliance monitoring element is this?

### Options
- [x] Automation
- [ ] Acknowledgement
  why: Acknowledgement is people confirming they know a policy.
- [ ] External examination
  why: An examination is performed by an outside party, such as a regulator.
- [ ] Due diligence
  why: Due diligence is investigating before a decision, such as before choosing a vendor.

### Explanation
Automated compliance monitoring checks configurations continuously against required controls, so drift is caught quickly instead of at the next audit.

## d5-pentest-2
type: match
topic: 5.5
group: pentest-environments

Match each penetration test setup to its type.

### Match
- The tester starts with only the company's name => Unknown environment
- The tester gets a list of IP (Internet Protocol) ranges but no credentials => Partially known environment
- The tester gets full documentation and credentials => Known environment
- Attackers and defenders work together and share findings in real time => Integrated

### Distractors
- Passive: Passive describes reconnaissance, not a test environment or team setup.

### Explanation
Unknown, partially known and known describe how much the tester knows. Offensive, defensive and integrated describe team roles (red, blue and purple).

## d5-pentest-env-1
type: single
topic: 5.5
group: pentest-environments

A company hires a penetration testing firm and gives the testers only the company's name. The testers receive no network diagrams, credentials, or IP (Internet Protocol) ranges and must discover everything themselves, as an outside attacker would. Which type of test environment is this?

### Options
- [x] Unknown environment
- [ ] Known environment
  why: In a known environment the testers get full documentation and access up front.
- [ ] Partially known environment
  why: That gives the testers some information, such as user credentials or address ranges. Here they get nothing.
- [ ] Passive reconnaissance
  why: That's a technique for gathering information without touching the target. It isn't an environment type.

### Explanation
An unknown environment test (formerly "black box") starts with no inside information. It's the most realistic view of an outside attacker and the slowest to run.

## d5-pentest-env-3
type: single
topic: 5.5
group: pentest-environments

A penetration tester is given a standard employee account and a list of in-scope subnets, but no architecture documentation and no administrative access. Which type of test environment does this represent?

### Options
- [x] Partially known environment
- [ ] Known environment
  why: That would include full documentation and privileged access.
- [ ] Unknown environment
  why: That would give the tester no account and no subnet list.
- [ ] Integrated testing
  why: Integrated testing combines offensive and defensive teams. It describes who takes part, not how much the testers are told.

### Explanation
A partially known environment (formerly "gray box") gives some inside information but not everything. A normal user account plus scope details simulates an attacker who already has a foothold.

## d5-recon-1
type: single
topic: 5.5
group: reconnaissance

A tester collects employee names from LinkedIn and email formats from public documents, without touching the target's systems. What is this?

### Options
- [x] Passive reconnaissance
- [ ] Active reconnaissance
  why: Active recon interacts with the target's systems, like scanning.
- [ ] Vulnerability scanning
  why: Scanning sends traffic to the target.
- [ ] Footprinting by port scan
  why: Port scans touch the target's systems.

### Explanation
Passive reconnaissance gathers information without direct contact, usually from OSINT (open-source intelligence).

## d5-recon-3
type: multi
topic: 5.5
group: reconnaissance

Which TWO are examples of passive reconnaissance?

### Options
- [x] Searching public DNS (Domain Name System) and WHOIS records
- [x] Reading the company's job postings for its tech stack
- [ ] Running a vulnerability scan against the web server
  why: Scanning sends traffic to the target.
- [ ] Banner grabbing on open ports
  why: Banner grabbing connects to the target's services.
- [ ] Ping sweeping the network range
  why: Ping sweeps send packets to the target.

### Explanation
Passive recon uses information already available, like public records, job postings and social media, without contacting the target's systems.

## d5-audit-1
type: single
topic: 5.5
group: audit-types

A government agency inspects a bank's systems to confirm it follows federal banking regulations. What type of assessment is this?

### Options
- [x] Regulatory examination
- [ ] Internal self-assessment
  why: Self-assessments are done by the organization itself.
- [ ] Penetration test
  why: Pen tests simulate attacks. They don't check regulatory compliance.
- [ ] Tabletop exercise
  why: A tabletop is a discussion-based drill.

### Explanation
External assessments include regulatory examinations, independent third-party audits, and assessments.

## d5-audit-3
type: single
topic: 5.5
group: audit-types

A customer won't sign a contract until the vendor provides a report from an independent firm that reviewed its security controls. What type of assessment does the customer want?

### Options
- [x] Independent third-party audit
- [ ] Internal self-assessment
  why: The customer wants someone independent, not the vendor grading itself.
- [ ] Passive reconnaissance
  why: Recon is information gathering for testing.
- [ ] Vulnerability scan by the vendor
  why: A self-run scan isn't independent.

### Explanation
Independent third-party audits, like SOC 2 (System and Organization Controls 2) reports, give customers assurance from someone with no stake in the result.

## d5-audit-4
type: single
topic: 5.5
group: audit-types

After an audit, the CEO (Chief Executive Officer) signs a formal statement to regulators confirming that the company's financial reporting controls are in place and working. What is this statement?

### Options
- [ ] A rules of engagement document
  why: Rules of engagement define how testing is done.
- [x] An attestation
- [ ] A risk register
  why: A risk register lists risks and owners.
- [ ] A legal hold
  why: A legal hold preserves data for litigation.

### Explanation
Attestation is a formal declaration, often by leadership or an auditor, that controls meet a requirement. Internal audits (including audit committees and self-assessments) and external audits support it.

## d5-aware-1
type: single
topic: 5.6
group: security-awareness

An employee disables the antivirus on her laptop because it slows down her video editing software. Which type of anomalous behavior is this?

### Options
- [x] Risky
- [ ] Unexpected
  why: Unexpected behavior is unusual for the user, like logging in at 3 a.m. from another country.
- [ ] Unintentional
  why: She did it on purpose.
- [ ] Malicious
  why: She isn't trying to harm the company. She's taking a shortcut.

### Explanation
SY0-701 lists three types of anomalous behavior: risky (deliberately unsafe), unexpected (out of the ordinary), and unintentional (honest mistakes).

## d5-aware-2
type: match
topic: 5.6
group: security-awareness

Match each employee action to the anomalous behavior type.

### Match
- An accountant accidentally emails a payroll file to the wrong person => Unintentional
- A developer who never travels logs in from overseas at 3 a.m. => Unexpected
- A manager shares his password with an intern to save time => Risky

### Distractors
- Compliant: Compliant behavior follows policy. None of these do.
- Expected: Expected behavior isn't anomalous.

### Explanation
Unintentional is an honest mistake, unexpected is unusual for that person, and risky is a deliberate unsafe choice.

## d5-aware-4
type: multi
topic: 5.6
group: security-awareness

A company is evaluating its security awareness program. Which TWO measures BEST show the program is working?

### Options
- [x] Phishing simulation click rates go down over time
- [x] Phishing report rates go up over time
- [ ] The number of training slides increases
  why: More content doesn't mean better behavior.
- [ ] All employees finish training in under five minutes
  why: Fast completion can mean people are skipping through.
- [ ] The security team sends more email reminders
  why: That measures effort, not results.

### Explanation
SY0-701 includes reporting and monitoring for awareness programs. Fewer clicks and more reports show real behavior change.

## d5-training-1
type: single
topic: 5.6
group: awareness-training

An employee gets an email that looks like it's from the CEO (Chief Executive Officer) asking for gift cards. The employee suspects phishing. According to a good awareness program, what should the employee do?

### Options
- [ ] Reply to ask whether the request is real
  why: Replying confirms the address is active and goes straight to the attacker.
- [ ] Delete the email and say nothing
  why: Deleting it protects one person, but the security team never learns about the campaign.
- [x] Report it with the phishing report button
- [ ] Forward it to coworkers as a warning
  why: Forwarding spreads the malicious message further.

### Explanation
Awareness programs teach people to recognize phishing and report it. Reports let the security team find and remove the same message from other inboxes.

## d5-training-2
type: match
topic: 5.6
group: awareness-training

Match each training scenario to the awareness topic it covers.

### Match
- Staff learn to spot a coworker copying large amounts of data before resigning => Insider threat
- Staff are told not to plug in USB (Universal Serial Bus) drives or charging cables they find => Removable media and cables
- Remote staff learn to lock screens and avoid public Wi-Fi without a VPN (Virtual Private Network) => Hybrid/remote work environments
- Staff are warned not to post project details or badge photos on social media => Operational security

### Distractors
- Password management: Password training covers creating and storing credentials. None of these scenarios is about passwords.

### Explanation
SY0-701 user guidance includes policy and handbooks, situational awareness, insider threat, password management, removable media and cables, social engineering, operational security, and hybrid or remote work.

## d5-awareprog-1
type: single
topic: 5.6
group: awareness-program

A company launches an awareness program. In the first month it measures how many staff click a simulated phish, then repeats the simulation every quarter to compare. What does SY0-701 call these two kinds of measurement?

### Options
- [x] Initial and recurring reporting and monitoring
- [ ] Development and execution
  why: Those are building and delivering the program, not measuring it.
- [ ] Risky and unexpected behavior
  why: These are types of anomalous behavior, not ways of measuring the program.
- [ ] Qualitative and quantitative analysis
  why: These are risk analysis methods, not awareness program measurement.

### Explanation
Awareness programs need an initial baseline measurement and recurring reporting and monitoring to show whether behavior improves.

## d5-awareprog-2
type: order
topic: 5.6
group: awareness-program

Put these steps for building a security awareness program in order.

### Order
1. Assess the company's risks and current staff awareness
   why: The program has to be based on the actual risks and where staff are today.
2. Develop training content and phishing campaigns for those risks
   why: Content is built after the needs are known.
3. Execute the training and simulations with staff
   why: Delivery comes once the content exists.
4. Measure results with recurring reporting and monitoring
   why: Results can only be measured after people have been trained.
5. Revise the program based on the results
   why: The findings feed the next round of the program.

### Explanation
SY0-701 lists development, execution, and initial and recurring reporting and monitoring for awareness programs. The cycle repeats as threats and results change.
