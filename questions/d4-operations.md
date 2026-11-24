---
deck: Domain 4 – Security Operations
section: "4.0"
exam_weight: 28
topics:
  4.1: Given a scenario, apply common security techniques to computing resources
  4.2: Explain the security implications of proper hardware, software, and data asset management
  4.3: Explain various activities associated with vulnerability management
  4.4: Explain security alerting and monitoring concepts and tools
  4.5: Given a scenario, modify enterprise capabilities to enhance security
  4.6: Given a scenario, implement and maintain identity and access management
  4.7: Explain the importance of automation and orchestration related to secure operations
  4.8: Explain appropriate incident response activities
  4.9: Given a scenario, use data sources to support an investigation
---

## d4-mobile-2
type: match
topic: 4.1
group: mobile-deployment

Match each deployment model to its description.

### Match
- Employees use their own personal phones for work => BYOD (Bring Your Own Device)
- The company buys the phone, and employees may use it personally => COPE (Corporate-Owned, Personally Enabled)
- Employees pick a phone from a list of approved models that the company buys => CYOD (Choose Your Own Device)
- The company buys the phone and allows only business use => Corporate-owned

### Distractors
- MDM (Mobile Device Management): MDM is the management tool used with all of these, not a deployment model.

### Explanation
BYOD is bring your own device, COPE is corporate-owned personally enabled, and CYOD is choose your own device.

## d4-mobile-models-1
type: single
topic: 4.1
group: mobile-deployment

A consulting firm buys the same smartphone model for every employee. The firm owns and manages the phones, but employees are allowed to install personal apps and make personal calls on them. Which deployment model is this?

### Options
- [x] COPE (Corporate-Owned, Personally Enabled)
- [ ] BYOD (Bring Your Own Device)
  why: With BYOD the employee owns the device. Here the firm bought and owns the phones.
- [ ] CYOD (Choose Your Own Device)
  why: With CYOD the employee picks from an approved list. Here everyone gets the same model.
- [ ] Kiosk mode on a single-purpose device
  why: Kiosk mode locks a device to a single app or purpose. These phones allow personal apps.

### Explanation
COPE means corporate-owned, personally enabled: the company owns and controls the device and permits personal use. Company ownership rules out BYOD, and no choice of device rules out CYOD.

## d4-mobile-3
type: single
topic: 4.1
group: mobile-deployment

Field technicians must send customer data from rural job sites. The only nearby Wi-Fi networks are open public hotspots. Which connection should their company tablets use?

### Options
- [x] The tablets' cellular data connection
- [ ] The open hotspot, since tablets have antivirus
  why: Antivirus doesn't encrypt traffic. Anyone on an open hotspot can watch or tamper with it.
- [ ] Bluetooth tethering to a customer's laptop
  why: The customer's laptop isn't trusted, and its connection is unknown.
- [ ] Whichever hotspot has the strongest signal
  why: Signal strength says nothing about security. A rogue access point can have the strongest signal.

### Explanation
SY0-701 lists cellular, Wi-Fi and Bluetooth connection methods for mobile devices. Cellular links are encrypted between the device and the carrier, unlike open Wi-Fi. A VPN (Virtual Private Network) still adds protection for sensitive data. Bluetooth should only pair with trusted devices.

## d4-wifi-1
type: single
topic: 4.1
group: wireless-security

A coffee shop wants its guest Wi-Fi to use a shared password but resist offline dictionary attacks against captured handshakes. What should it use?

### Options
- [x] WPA3-Personal with SAE (Simultaneous Authentication of Equals)
- [ ] WPA2-Personal with a PSK (Pre-Shared Key)
  why: WPA2 (Wi-Fi Protected Access 2) PSK handshakes can be captured and cracked offline.
- [ ] WPA2-Enterprise with RADIUS (Remote Authentication Dial-In User Service)
  why: Enterprise needs individual accounts, not a shared password.
- [ ] WEP (Wired Equivalent Privacy) with a 128-bit key
  why: WEP is broken and should never be used.

### Explanation
WPA3-Personal uses SAE (Simultaneous Authentication of Equals), which replaces WPA2's pre-shared key handshake and blocks offline dictionary attacks.

## d4-wifi-3
type: multi
topic: 4.1
group: wireless-security

A company wants each employee to log in to Wi-Fi with their own domain credentials, and to remove access instantly when someone leaves. Which TWO components are needed?

### Options
- [x] WPA3-Enterprise
- [x] A RADIUS (Remote Authentication Dial-In User Service) server
- [ ] A single shared passphrase
  why: A shared passphrase can't be revoked for one person.
- [ ] MAC (Media Access Control) address filtering
  why: MACs are easy to spoof and aren't tied to the employee's credentials.
- [ ] Disabling the SSID (Service Set Identifier) broadcast
  why: Hidden SSIDs are easy to find and don't authenticate anyone.

### Explanation
Enterprise mode uses 802.1X (port-based Network Access Control standard) with a RADIUS server, so each user authenticates individually. Disabling a user's account removes their access.

## d4-wifi-4
type: single
topic: 4.1
group: wireless-security

Before installing access points in a new warehouse, a company walks the building measuring signal strength and interference, then produces a color-coded map of coverage. What has the company done?

### Options
- [ ] A penetration test
  why: A penetration test tries to break in. This measures coverage.
- [x] A site survey with a heat map
- [ ] A war-driving attack against nearby networks
  why: War driving is searching for wireless networks to attack.
- [ ] A deauthentication test
  why: That would disconnect clients. Nothing is being disconnected.

### Explanation
Site surveys measure coverage and interference, and heat maps visualize signal strength. They help place access points so coverage doesn't leak far outside the building and doesn't leave gaps.

## d4-appsec-1
type: single
topic: 4.1
group: application-security

A developer wants to make sure a session cookie is never sent over plain HTTP (Hypertext Transfer Protocol) and can't be read by JavaScript. What should she set?

### Options
- [x] The Secure and HttpOnly attributes
- [ ] A longer session timeout
  why: Timeout length doesn't control how the cookie is sent or read.
- [ ] Code signing on the web app
  why: Code signing proves who wrote code. It doesn't protect cookies.
- [ ] Input validation on login fields
  why: Input validation stops injection. It doesn't change cookie handling.

### Explanation
The Secure attribute sends the cookie only over HTTPS (Hypertext Transfer Protocol Secure). HttpOnly blocks JavaScript access, which limits cookie theft through XSS (Cross-Site Scripting).

## d4-appsec-3
type: single
topic: 4.1
group: application-security

A company wants employees' computers to run only software that was published by approved developers and hasn't been changed since. What should it require?

### Options
- [x] Code signing
- [ ] Input validation
  why: Input validation protects apps from bad data. It doesn't verify who published the app.
- [ ] Static code analysis
  why: Static analysis finds bugs in source code. It doesn't prove who published the program.
- [ ] Secure cookies
  why: Cookies are web session data.

### Explanation
Code signing uses a digital signature to prove who published software and that it hasn't been modified.

## d4-appsec-4
type: single
topic: 4.1
group: application-security

A security analyst wants to open a suspicious attachment and watch what it does without risking the production network. What should the analyst use?

### Options
- [x] A sandbox
- [ ] A jump server
  why: A jump server is a hardened entry point for admin access. It doesn't isolate untrusted code.
- [ ] A load balancer
  why: Load balancers spread traffic across servers.
- [ ] Code signing
  why: Code signing proves who published software. It doesn't let you safely run unknown files.

### Explanation
A sandbox is an isolated environment where untrusted code can run and be observed without affecting real systems.

## d4-baseline-1
type: single
topic: 4.1
group: secure-baselines

A company builds a standard hardened configuration for its web servers, deploys it to every new server, and checks monthly for servers that have drifted from it. What is the company managing?

### Options
- [x] A secure baseline
- [ ] A business impact analysis
  why: A BIA (Business Impact Analysis) identifies critical processes and the cost of losing them. It isn't a server configuration.
- [ ] A risk register
  why: A risk register tracks identified risks and owners. It doesn't define server settings.
- [ ] A change advisory board
  why: The CAB (Change Advisory Board) approves changes. The standard configuration itself is something else.

### Explanation
A secure baseline is a known-good configuration. The lifecycle is establish, deploy, and maintain, which includes checking for drift and updating the baseline as threats change.

## d4-baseline-2
type: order
topic: 4.1
group: secure-baselines

Put the secure baseline lifecycle in order.

### Order
1. Establish the baseline from a benchmark such as CIS (Center for Internet Security)
   why: You start by defining the hardened configuration.
2. Deploy the baseline to systems
   why: Once defined, it's pushed out, often with automation or Group Policy.
3. Maintain the baseline by monitoring drift and updating it
   why: Systems drift and threats change, so the baseline needs ongoing upkeep.

### Explanation
Establish, deploy, maintain. A baseline that isn't monitored and updated stops reflecting the real state of the systems.

## d4-disposal-1
type: single
topic: 4.2
group: asset-disposal

A company is retiring 200 hard drives that held customer data. It needs proof for auditors that the data was destroyed. What should it get from its disposal vendor?

### Options
- [x] A certificate of destruction
- [ ] A data retention policy
  why: A retention policy says how long to keep data, not proof it was destroyed.
- [ ] An asset inventory report
  why: An inventory lists assets, not their destruction.
- [ ] A non-disclosure agreement
  why: An NDA (Non-Disclosure Agreement) protects confidentiality but doesn't prove destruction.

### Explanation
A certificate of destruction documents which assets were destroyed, when and how. It's the evidence auditors look for.

## d4-disposal-3
type: multi
topic: 4.2
group: asset-disposal

Which TWO methods are destruction rather than sanitization?

### Options
- [x] Shredding the drives
- [x] Incinerating the drives
- [ ] Overwriting with zeros
  why: Overwriting leaves the drive usable, so it's sanitization.
- [ ] Using the SSD's (Solid-State Drive) secure erase command
  why: Secure erase leaves the drive usable, so it's sanitization.
- [ ] Encrypting and deleting the key
  why: Crypto-erase leaves the drive usable.

### Explanation
Destruction makes the media physically unusable (shredding, pulverizing, incinerating). Sanitization removes data so the media can be reused.

## d4-asset-1
type: single
topic: 4.2
group: asset-management

During an incident, the security team finds an unpatched server that nobody can identify. No one knows who is responsible for it or what data it holds. Which asset management practice failed?

### Options
- [ ] Sanitizing the server's drives on a schedule
  why: Sanitization removes data from media at end of life. The server is still in use.
- [x] Assigning an owner and tracking it in an inventory
- [ ] Certificate of destruction
  why: That documents disposal. The server hasn't been disposed of.
- [ ] Setting a data retention period for its files
  why: Retention decides how long data is kept. The problem is that nobody owns the server.

### Explanation
Every asset should be inventoried and have an owner who is accountable for it, along with its classification. Enumeration and inventory tracking find systems that would otherwise be forgotten and left unpatched.

## d4-asset-2
type: single
topic: 4.2
group: asset-management

A company wants to stop teams from buying cloud services and hardware that security has never reviewed. At which point in the asset lifecycle is the control MOST effective?

### Options
- [x] Acquisition and procurement
- [ ] Disposal and decommissioning
  why: By then the unreviewed asset has already been in use.
- [ ] Data retention
  why: Retention covers how long data is kept, not what is bought.
- [ ] Sanitization
  why: Sanitization happens at end of life.

### Explanation
Building security review into acquisition and procurement catches risky assets before they enter the environment. It also makes sure each new asset gets an owner and lands in the inventory.

## d4-asset-3
type: match
topic: 4.2
group: asset-management

Match each asset management activity to the term for it.

### Match
- Labeling a new laptop as holding confidential data so the right controls apply => Classification
- A network scan finds devices that aren't in the asset database => Enumeration
- A list of every device with its location and model => Inventory
- Recording which manager is responsible for a server => Ownership

### Distractors
- Sanitization: Sanitization removes data when an asset is disposed of. None of these activities happens at disposal.

### Explanation
Asset management covers acquisition/procurement, assignment/accounting (ownership and classification), monitoring and tracking (inventory and enumeration), and disposal.

## d4-sastdast-1
type: single
topic: 4.3
group: sast-dast

A team scans its source code for vulnerabilities before compiling it, without running the application. What is this?

### Options
- [x] SAST (Static Application Security Testing)
- [ ] DAST (Dynamic Application Security Testing)
  why: Dynamic analysis tests the running application.
- [ ] Fuzzing
  why: Fuzzing sends random input to a running application.
- [ ] Penetration testing
  why: Pen testing attacks running systems.

### Explanation
Static application security testing reviews source code without running it. It finds problems early but can produce false positives.

## d4-sastdast-3
type: single
topic: 4.3
group: sast-dast

A security tester sends thousands of random, malformed inputs to an application to see if it crashes. What is this technique?

### Options
- [x] Fuzzing
- [ ] Static code analysis
  why: Static analysis reads code. Fuzzing runs the app with bad input.
- [ ] Code signing
  why: Code signing proves who published code.
- [ ] Regression testing
  why: Regression testing checks that old features still work after changes.

### Explanation
Fuzzing is a dynamic technique that sends unexpected input to find crashes and memory bugs.

## d4-vulnresult-3
type: single
topic: 4.3
group: vuln-scan-results

Which scan type gives the MOST accurate results about missing patches on a server?

### Options
- [x] A credentialed scan
- [ ] An unauthenticated external scan
  why: Without credentials the scanner only sees what's exposed on the network.
- [ ] A passive scan of network traffic
  why: Passive scanning sees only what crosses the network.
- [ ] A ping sweep
  why: A ping sweep only finds which hosts are up.

### Explanation
A credentialed scan logs in to the system, so it can check installed software and patch levels directly.

## d4-scan-results-1
type: single
topic: 4.3
group: vuln-scan-results

A vulnerability scanner reports that a web server is missing a critical patch. The administrator checks and confirms the patch was installed last month; the scanner was fooled by an outdated version banner. What is this scanner result called?

### Options
- [x] False positive
- [ ] False negative
  why: A false negative is a real vulnerability the scanner missed. Here the scanner reported something that isn't there.
- [ ] True positive
  why: A true positive is a reported vulnerability that really exists. This one doesn't.
- [ ] Exception
  why: An exception is a documented decision not to fix a real finding. This finding isn't real.

### Explanation
A false positive is an alert for a problem that doesn't exist. The administrator's manual check contradicting the scanner is what confirms it.

## d4-scan-results-3
type: single
topic: 4.3
group: vuln-scan-results

A security manager is reviewing how the vulnerability scanner is tuned. Which result type is the MOST dangerous, because the organization doesn't know it has a problem?

### Options
- [x] False negative
- [ ] False positive
  why: A false positive wastes analyst time, but nothing is actually at risk.
- [ ] True positive
  why: A true positive is real and reported, so it can be fixed.
- [ ] Informational finding
  why: Informational findings are reported and low risk. Nothing is hidden.

### Explanation
A false negative leaves a real vulnerability in place with nobody aware of it. Every other result type either isn't a real risk or is visible to the team.

## d4-cvss-1
type: single
topic: 4.3
group: cvss-cve

A vulnerability has the CVE (Common Vulnerabilities and Exposures) identifier CVE-2026-1234 and a score of 9.8. What does the 9.8 represent?

### Options
- [x] The CVSS (Common Vulnerability Scoring System) severity score
- [ ] The CVE exposure factor used in loss calculations
  why: Exposure factor is a risk calculation term, not a CVE attribute.
- [ ] The number of systems affected worldwide so far
  why: CVSS scores rate severity, not how many systems are affected.
- [ ] The number of days until the vendor's patch is released
  why: CVSS scores don't track patch timing.

### Explanation
CVE gives a vulnerability its unique ID (Identifier). CVSS (Common Vulnerability Scoring System) rates its severity from 0 to 10.

## d4-cvss-2
type: match
topic: 4.3
group: cvss-cve

Match each term to its description.

### Match
- A unique ID (Identifier) assigned to a publicly known vulnerability => CVE (Common Vulnerabilities and Exposures)
- A 0–10 score rating how severe a vulnerability is => CVSS (Common Vulnerability Scoring System)
- A standard for automating checks against security benchmarks => SCAP (Security Content Automation Protocol)
- Hardening guidelines published by the Center for Internet Security => CIS (Center for Internet Security) Benchmarks

### Distractors
- NVD (National Vulnerability Database): The National Vulnerability Database stores CVE details. None of the descriptions match it exactly.

### Explanation
CVE identifies, CVSS scores, SCAP automates compliance checks, and CIS Benchmarks give hardening guidance.

## d4-vulnfix-1
type: single
topic: 4.3
group: vuln-remediation

A critical vulnerability exists on a medical device, and the vendor says a patch won't be ready for six months. The device must stay in service. What should the security team do?

### Options
- [x] Document an exception and apply compensating controls
- [ ] Ignore it until the patch arrives
  why: Ignoring a critical vulnerability without documenting or reducing the risk isn't acceptable.
- [ ] Mark it as a false positive
  why: The vulnerability is real.
- [ ] Remove the device from the asset inventory for now
  why: That hides the risk without reducing it.

### Explanation
When a vulnerability can't be fixed, the organization documents an exception (with approval) and adds compensating controls like segmentation and monitoring.

## d4-vulnfix-2
type: order
topic: 4.3
group: vuln-remediation

Put these vulnerability management activities in order.

### Order
1. Identify vulnerabilities with a scan
   why: You start by finding the vulnerabilities.
2. Analyze and prioritize findings using CVSS (Common Vulnerability Scoring System) and business context
   why: Findings are confirmed and ranked before anyone acts.
3. Remediate by patching or applying controls
   why: Fixes are applied in priority order.
4. Rescan to validate the fix
   why: Validation confirms the fix actually worked.
5. Report the results
   why: Reporting closes the cycle and informs the next one.

### Explanation
Identify, analyze, remediate, validate, report. Rescanning after the fix is the step people most often skip.

## d4-vulnfix-3
type: multi
topic: 4.3
group: vuln-remediation

A team patches a critical flaw on 40 web servers. Which TWO steps validate that the remediation worked?

### Options
- [x] Rescanning the servers for the same vulnerability
- [x] Verifying the patched version on a sample of servers
- [ ] Closing the ticket once the patch job reports success
  why: A successful job doesn't prove the flaw is gone. Some servers may have been skipped or need a reboot.
- [ ] Buying cyber insurance for the web servers
  why: Insurance is a response option for risk. It doesn't check whether the fix worked.
- [ ] Granting an exemption for the patched servers
  why: An exemption excuses a system from a requirement. It doesn't validate anything.

### Explanation
SY0-701 validation of remediation includes rescanning, audit and verification. An exception temporarily allows a known risk with compensating controls. An exemption formally excuses a system from the requirement.

## d4-threatfeed-1
type: match
topic: 4.3
group: threat-feeds

Match each vulnerability information source to its description.

### Match
- Free public information such as security blogs and government advisories => Open-source intelligence
- A paid feed curated by a security vendor => Proprietary threat feed
- An industry group where member banks share threat data => Information-sharing organization
- Hidden forums where stolen credentials are sold => Dark web

### Distractors
- Bug bounty: A bug bounty pays outside researchers to report flaws. It isn't a feed of threat information.

### Explanation
SY0-701 lists threat feeds including OSINT (Open-Source Intelligence), proprietary or third-party feeds, information-sharing organizations, and the dark web. Each gives a different view of current threats.

## d4-threatfeed-2
type: single
topic: 4.3
group: threat-feeds

A software company wants outside researchers to report flaws in its products instead of selling them, and it offers cash rewards. What is this program?

### Options
- [ ] A penetration test
  why: A pen test is a contracted engagement with a defined scope and team.
- [x] A bug bounty
- [ ] A proprietary threat feed
  why: A threat feed delivers information about threats. It doesn't pay researchers for findings.
- [ ] A dark web monitoring service
  why: Dark web monitoring watches for stolen data. It doesn't reward researchers.

### Explanation
A bug bounty is a form of responsible disclosure program that pays outside researchers for valid vulnerability reports.

## d4-vulnid-1
type: single
topic: 4.3
group: vuln-identification

A development team's application uses 300 open-source libraries. The team wants an automatic alert whenever a newly published flaw affects one of them. Which identification method fits?

### Options
- [x] Package monitoring
- [ ] Dynamic analysis
  why: Dynamic analysis tests the running application. It doesn't track advisories for the libraries it uses.
- [ ] A penetration test
  why: A penetration test is a point-in-time exercise, not ongoing alerting.
- [ ] A system/process audit
  why: An audit checks whether procedures are followed. It doesn't watch for new library flaws.

### Explanation
Package monitoring tracks third-party libraries and dependencies against vulnerability databases and alerts when a new flaw affects a version in use. It's one of the application security identification methods in SY0-701.

## d4-vulnid-2
type: match
topic: 4.3
group: vuln-identification

Match each activity to the vulnerability identification method.

### Match
- An outside researcher reports a flaw through the company's published security contact page, and no reward is offered => Responsible disclosure program
- Hired testers try to exploit weaknesses to prove their real impact => Penetration testing
- Reviewers check that patching and access review procedures are actually followed => System/process audit
- An automated tool checks hosts against a database of known flaws => Vulnerability scan

### Distractors
- Bug bounty program: A bug bounty pays rewards. The researcher here was offered none.

### Explanation
SY0-701 identification methods include vulnerability scans, application security analysis, threat feeds, penetration testing, responsible disclosure (including bug bounties) and system/process audits.

## d4-vulnctx-1
type: single
topic: 4.3
group: vuln-analysis-context

A scanner rates a flaw 9.8 (critical) under CVSS (Common Vulnerability Scoring System). The affected server sits on an isolated lab network with no sensitive data. How should the team treat the rating when prioritizing?

### Options
- [x] Adjust for environmental variables, lowering its priority
- [ ] Treat it as critical, because base scores can't be changed
  why: CVSS includes environmental metrics so organizations can adjust the base score for their own setting.
- [ ] Ignore it, because isolated systems can't be attacked
  why: Isolation reduces risk but doesn't remove it. The flaw still needs a plan.
- [ ] Raise it, because lab networks have higher exposure
  why: An isolated lab has less exposure, not more.

### Explanation
Base scores describe a flaw in general. Environmental variables, such as exposure, data value and existing controls, adjust that score for the organization's systems.

## d4-vulnctx-2
type: multi
topic: 4.3
group: vuln-analysis-context

Two servers have the same CVE (Common Vulnerabilities and Exposures) entry with the same base score. Which TWO factors should decide which server is patched first?

### Options
- [x] The business impact if each server is breached
- [x] The company's risk tolerance for each system
- [ ] Which server's software vendor is the larger one
  why: Vendor size doesn't change how harmful a breach of each server would be.
- [ ] The order the scanner listed them in its report
  why: Report order is arbitrary. It reflects no risk.
- [ ] Which server has the newer hardware
  why: Hardware age doesn't change the risk from this software flaw.

### Explanation
Vulnerability analysis weighs classification, exposure factor, environmental variables, industry/organizational impact and risk tolerance, not just the base score.

## d4-monitor-1
type: single
topic: 4.4
group: monitoring-tools

An analyst needs one place to collect logs from firewalls, servers and endpoints, correlate events, and generate alerts. Which tool fits?

### Options
- [x] SIEM (Security Information and Event Management)
- [ ] NetFlow collector for traffic records
  why: NetFlow shows traffic metadata only, not logs from all these sources.
- [ ] DLP (Data Loss Prevention)
  why: DLP prevents data from leaving. It doesn't collect and correlate logs.
- [ ] Vulnerability scanner with a reporting dashboard
  why: Scanners find weaknesses. They don't correlate logs.

### Explanation
A SIEM (security information and event management) aggregates logs, correlates events across sources, and alerts on suspicious activity.

## d4-monitor-3
type: single
topic: 4.4
group: monitoring-tools

A SOC (Security Operations Center) gets 2,000 alerts a day from one rule, and nearly all of them turn out to be harmless. What should the team do FIRST?

### Options
- [x] Tune the alert rule
- [ ] Disable all alerting
  why: That removes visibility entirely.
- [ ] Hire more analysts to review every alert
  why: That treats the symptom. The rule itself is the problem.
- [ ] Archive the alerts without reviewing them
  why: Real attacks would be lost in the archive.

### Explanation
Alert tuning adjusts thresholds and conditions to cut false positives, which reduces alert fatigue so real attacks get noticed.

## d4-monitor-4
type: match
topic: 4.4
group: monitoring-tools

Match each monitoring need to the BEST tool or method.

### Match
- A switch sends an alert the moment an interface goes down => SNMP (Simple Network Management Protocol) traps
- See which hosts talked to which, how much, and when, without full packet contents => NetFlow
- Check systems for vulnerabilities without installing software on them => Agentless scanning
- Automatically compare system settings against a published benchmark => SCAP (Security Content Automation Protocol)

### Distractors
- Packet capture: Packet captures record full packet contents. None of these needs requires the full packets.

### Explanation
SNMP traps push device alerts, NetFlow summarizes traffic flows, agentless scanning works over the network, and SCAP automates configuration checks against benchmarks.

## d4-monact-1
type: single
topic: 4.4
group: monitoring-activities

A company's firewalls, servers and cloud services each keep their logs in their own place. Analysts waste time signing in to each one during an investigation. Which monitoring activity solves this?

### Options
- [x] Log aggregation
- [ ] Archiving
  why: Archiving moves old logs into long-term storage. It doesn't bring current logs together for searching.
- [ ] Alert tuning
  why: Tuning adjusts alert rules. It doesn't change where logs live.
- [ ] Vulnerability scanning
  why: Scanning looks for flaws. It doesn't collect logs.

### Explanation
Log aggregation collects logs from many sources into one place, usually a SIEM (Security Information and Event Management), so they can be searched and correlated.

## d4-monact-2
type: match
topic: 4.4
group: monitoring-activities

Match each monitoring step to the activity.

### Match
- An EDR (Endpoint Detection and Response) agent moves a suspicious file into an isolated folder where it can't run => Quarantine
- Logs older than 90 days move to cheap storage and are kept for seven years => Archiving
- The on-call analyst gets a page when an admin account signs in at 3 a.m. => Alerting
- A weekly summary of incidents and open findings goes to management => Reporting

### Distractors
- Alert tuning: Tuning changes rules to cut false positives. None of these steps changes a rule.

### Explanation
SY0-701 monitoring activities are log aggregation, alerting, scanning, reporting, archiving, and alert response and remediation/validation (including quarantine and alert tuning).

## d4-email-1
type: single
topic: 4.5
group: email-security

A company wants receiving mail servers to check whether a sending server's IP (Internet Protocol) is authorized to send mail for its domain. Which DNS (Domain Name System) record does this?

### Options
- [x] SPF (Sender Policy Framework)
- [ ] DKIM (DomainKeys Identified Mail)
  why: DKIM signs the message. It doesn't list authorized sending IPs.
- [ ] DMARC (Domain-based Message Authentication, Reporting, and Conformance)
  why: DMARC tells receivers what to do when checks fail.
- [ ] MX (Mail Exchanger)
  why: MX records say where to deliver mail for the domain, not who can send it.

### Explanation
Sender Policy Framework lists the servers allowed to send mail for a domain.

## d4-email-auth-1
type: single
topic: 4.5
group: email-security

A company's customers are receiving forged invoices that appear to come from the company's domain. The company wants receiving mail servers to verify a cryptographic signature in each message header using a public key published in the company's DNS (Domain Name System). Which should it implement?

### Options
- [x] DKIM (DomainKeys Identified Mail)
- [ ] SPF (Sender Policy Framework)
  why: SPF lists the IP (Internet Protocol) addresses allowed to send for the domain. It doesn't sign messages.
- [ ] DMARC (Domain-based Message Authentication, Reporting, and Conformance)
  why: DMARC tells receivers what to do when the other checks fail and where to send reports. It has no signature of its own.
- [ ] S/MIME (Secure/Multipurpose Internet Mail Extensions)
  why: S/MIME signs with individual users' certificates, not a domain key published in DNS.

### Explanation
DKIM adds a digital signature to the message headers, and receivers validate it with the public key in the sender's DNS. "Signature in the header" plus "public key in DNS" identifies it.

## d4-email-auth-3
type: single
topic: 4.5
group: email-security

A company has published SPF (Sender Policy Framework) and DKIM (DomainKeys Identified Mail) records, but spoofed messages that fail both checks are still landing in recipients' inboxes. The company also wants daily reports showing who is sending mail as its domain. Which addition addresses both needs?

### Options
- [x] A DMARC (Domain-based Message Authentication, Reporting, and Conformance) policy set to reject
- [ ] A secure email gateway filtering all inbound mail
  why: A gateway filters what the company receives. It can't control what other organizations accept.
- [ ] An MX (Mail Exchanger) record with a higher priority
  why: MX records route incoming mail. They have no effect on spoofed outbound mail.
- [ ] S/MIME (Secure/Multipurpose Internet Mail Extensions) certificates for all employees
  why: S/MIME signs individual messages, but receivers won't block unsigned mail because of it, and it produces no reports.

### Explanation
DMARC tells receiving servers what to do with mail that fails SPF and DKIM (none, quarantine, or reject) and where to send aggregate reports. Without it, a failure is just information the receiver can ignore.

## d4-ports-1
type: match
topic: 4.5
group: secure-protocol-ports

Match each secure protocol to its default port.

### Match
- HTTPS (Hypertext Transfer Protocol Secure) => 443
- SSH (Secure Shell) => 22
- LDAPS (Lightweight Directory Access Protocol Secure) => 636
- SMTPS (Simple Mail Transfer Protocol Secure) with implicit TLS (Transport Layer Security) => 465

### Distractors
- 389: LDAP's (Lightweight Directory Access Protocol) unencrypted port.
- 25: SMTP's (Simple Mail Transfer Protocol) default port, normally unencrypted.
- 23: Telnet, which is unencrypted.

### Explanation
Secure versions usually have their own ports. Knowing which ports are unencrypted (23, 25, 389) helps you spot insecure services.

## d4-ports-3
type: single
topic: 4.5
group: secure-protocol-ports

A security audit lists the open ports on a server. Which port runs a protocol that sends credentials in cleartext and should be replaced?

### Options
- [x] 21
- [ ] 22
  why: 22 is SSH (Secure Shell), which is encrypted.
- [ ] 443
  why: 443 is HTTPS (Hypertext Transfer Protocol Secure), which is encrypted.
- [ ] 636
  why: 636 is LDAPS (Lightweight Directory Access Protocol Secure), which is LDAP (Lightweight Directory Access Protocol) over TLS (Transport Layer Security).

### Explanation
Port 21 is FTP (File Transfer Protocol), which is unencrypted. It should be replaced with SFTP (over SSH on 22) or FTPS (File Transfer Protocol Secure).

## d4-endpoint-1
type: single
topic: 4.5
group: endpoint-tools

A company wants an alert whenever a system file like /etc/passwd or a Windows registry key is changed. Which tool does this?

### Options
- [x] File integrity monitoring
- [ ] Data loss prevention
  why: DLP (Data Loss Prevention) stops sensitive data from leaving. It doesn't watch system files for changes.
- [ ] Network access control
  why: NAC (Network Access Control) controls which devices can join the network.
- [ ] Web filter
  why: Web filters control browsing.

### Explanation
FIM (File Integrity Monitoring) hashes important files and alerts when they change, which can reveal tampering or malware.

## d4-endpoint-2
type: match
topic: 4.5
group: endpoint-tools

Match each scenario to the BEST tool.

### Match
- Block employees from emailing spreadsheets that contain credit card numbers => Data loss prevention
- Alert when a critical system file's hash changes => File integrity monitoring
- Check a laptop's patch level before it can join the network => Network access control
- Detect and respond to malicious behavior on endpoints and correlate it across email and network => Extended detection and response

### Distractors
- SIEM (Security Information and Event Management): A SIEM correlates logs but doesn't take action on endpoints or block data.

### Explanation
DLP (Data Loss Prevention) stops data leaving, FIM (File Integrity Monitoring) watches files, NAC (Network Access Control) checks devices before they connect, and XDR (Extended Detection and Response) extends EDR (Endpoint Detection and Response) across more data sources.

## d4-endpoint-3
type: single
topic: 4.5
group: endpoint-tools

An employee who normally downloads a few files a day suddenly downloads thousands of documents from the file server at 2 a.m. No signature or rule matched. Which tool is BEST suited to flag this?

### Options
- [x] User behavior analytics
- [ ] File integrity monitoring
  why: FIM (File Integrity Monitoring) watches whether files change. These files were read, not changed.
- [ ] Network access control
  why: NAC (Network Access Control) decides whether a device can join the network. The employee's device is allowed.
- [ ] A signature-based antivirus scan
  why: Nothing malicious was installed. The behavior itself is unusual.

### Explanation
UBA (User Behavior Analytics) builds a baseline of each user's normal behavior and alerts on large deviations, which catches insider threats and stolen accounts that rules miss. UEBA (User and Entity Behavior Analytics) extends the same idea to devices and other entities.

## d4-filter-1
type: single
topic: 4.5
group: web-dns-filtering

A company wants to block employees from reaching known malicious and gambling sites on any device, including guest phones, by refusing to resolve those domains. Which control fits BEST?

### Options
- [x] DNS (Domain Name System) filtering
- [ ] File integrity monitoring
  why: FIM (File Integrity Monitoring) watches system files for changes. It doesn't control browsing.
- [ ] DKIM (DomainKeys Identified Mail)
  why: DKIM signs outgoing email.
- [ ] Port security
  why: Port security limits which devices can use a switch port. It doesn't filter websites.

### Explanation
DNS filtering refuses to resolve blocked domains, so it works for any device that uses the company's resolvers. It can be paired with web filtering for URL- and content-level control.

## d4-filter-2
type: single
topic: 4.5
group: web-dns-filtering

Remote employees' laptops rarely connect through the office, but the company still wants to enforce its web filtering policy on them everywhere. Which approach fits BEST?

### Options
- [ ] A centralized proxy in the headquarters data center
  why: Traffic that doesn't route through headquarters never reaches the proxy.
- [x] An agent-based web filter on each laptop
- [ ] A WAF (Web Application Firewall) in front of the company's website
  why: A WAF protects the company's own web apps from attacks. It doesn't filter employee browsing.
- [ ] Port security on the office switches
  why: Port security only affects devices plugged into office switches.

### Explanation
Agent-based web filters enforce the policy on the device itself, wherever it is. Centralized proxies only see traffic that passes through them. Both can use URL (Uniform Resource Locator) scanning, content categorization, block rules and reputation.

## d4-filter-3
type: match
topic: 4.5
group: web-dns-filtering

Match each web filter feature to what it does.

### Match
- Blocks a site because a vendor's score says it often hosts malware => Reputation
- Checks the full address of each requested page against known bad paths => URL (Uniform Resource Locator) scanning
- Blocks every site labeled gambling or social media => Content categorization
- An admin-written entry that denies one specific domain => Block rules

### Distractors
- Centralized proxy: A centralized proxy is where filtering happens, not a way of deciding what to block.

### Explanation
SY0-701 web filter features include agent-based and centralized proxy filtering, URL scanning, content categorization, block rules and reputation.

## d4-ids-1
type: single
topic: 4.5
group: ids-detection

An IDS (Intrusion Detection System) detects a brand-new attack that has no published signature, because the traffic is very different from the network's normal patterns. Which detection method found it?

### Options
- [ ] Signature-based detection
  why: Signature detection needs a known pattern. This attack has none.
- [x] Anomaly-based detection
- [ ] Port mirroring
  why: Port mirroring feeds traffic to a sensor. It isn't a detection method.
- [ ] Reputation filtering
  why: Reputation filtering blocks known bad sources. A brand-new attack may come from an unknown source.

### Explanation
Anomaly (behavior or trend) detection compares activity to a baseline of normal, so it can catch unknown attacks. The trade-off is more false positives than signature detection.

## d4-ids-2
type: single
topic: 4.5
group: ids-detection

What is the MAIN drawback of relying only on signature-based IDS (Intrusion Detection System) detection?

### Options
- [x] It misses attacks that have no known signature yet
- [ ] It can't run inline with network traffic
  why: Signature-based engines run inline in IPS (Intrusion Prevention System) devices all the time.
- [ ] It can only be deployed on cloud-hosted networks, not on-premises
  why: Signature IDS runs anywhere.
- [ ] It flags most normal traffic as malicious
  why: Signature detection usually has fewer false positives than anomaly detection.

### Explanation
Signatures match known patterns, so they are accurate for known threats but blind to zero-days and new variants until signatures are updated.

## d4-os-security-1
type: single
topic: 4.5
group: os-security

An administrator needs to push the same password policy, screen-lock timeout and USB (Universal Serial Bus) restrictions to 3,000 Windows domain computers. What should the administrator use?

### Options
- [x] Group Policy
- [ ] SELinux (Security-Enhanced Linux) policies
  why: SELinux enforces mandatory access control on Linux systems. It doesn't manage Windows domain computers.
- [ ] A WAF (Web Application Firewall)
  why: A WAF protects web applications.
- [ ] NetFlow
  why: NetFlow collects traffic metadata.

### Explanation
Group Policy centrally applies settings to Windows domain computers and users. It's the main way to enforce operating system security settings at scale in a Windows environment.

## d4-os-security-2
type: single
topic: 4.5
group: os-security

A Linux web server is compromised through its web application, but the attacker can't read files outside the web content folders even though file permissions would have allowed it. What MOST likely stopped the attacker?

### Options
- [ ] Group Policy
  why: Group Policy manages Windows domain computers, not Linux servers.
- [x] SELinux (Security-Enhanced Linux) enforcing mandatory access policies
- [ ] DNS (Domain Name System) filtering on the server's outbound lookups
  why: DNS filtering controls name resolution. It doesn't restrict file access on a server.
- [ ] A host-based firewall blocking inbound ports
  why: A firewall controls network traffic. It doesn't restrict which files a process can read.

### Explanation
SELinux adds mandatory access controls on top of normal permissions, so a compromised process is confined to what its policy allows.

## d4-fwrules-1
type: single
topic: 4.5
group: firewall-rules

A firewall filters TCP (Transmission Control Protocol) traffic using the rules below, checked from top to bottom. An admin on 10.0.9.15 can't open an SSH (Secure Shell) session on port 22 to 10.0.5.20. Why?

### Exhibit
```text
1  ALLOW  tcp/443  any           -> 10.0.5.20
2  DENY   tcp/any  any           -> 10.0.5.0/24
3  ALLOW  tcp/22   10.0.9.0/24   -> 10.0.5.20
```

### Options
- [x] Rule 2 matches first and blocks the traffic
- [ ] Rule 1 allows only web traffic, so it drops SSH
  why: Rule 1 doesn't match port 22, so the firewall moves on to the next rule. It doesn't drop anything.
- [ ] Rule 3 uses the wrong port for SSH
  why: SSH uses port 22, so rule 3 is correct. It just never gets reached.
- [ ] Firewalls apply the most specific rule first
  why: Most firewalls use the first matching rule, from the top down. Specificity doesn't reorder them.

### Explanation
Firewall rules are processed in order, and the first match wins. The fix is to move the specific allow rule above the broad deny. Each rule names a source, destination, port/protocol and action.

## d4-fwrules-2
type: single
topic: 4.5
group: firewall-rules

Internet mail servers must deliver email to the company's mail server over SMTP (Simple Mail Transfer Protocol), which uses TCP (Transmission Control Protocol) port 25. Which firewall rule is the MOST restrictive that still works?

### Options
- [x] Allow TCP 25 from any to the mail server only
- [ ] Allow TCP 25 from any to the whole internal subnet
  why: This opens port 25 on every internal host, not just the mail server.
- [ ] Allow all TCP ports from any to the mail server
  why: This exposes every service on the mail server, not just mail delivery.
- [ ] Allow TCP 25 and 3389 from any to the mail server
  why: Port 3389 is remote desktop, which mail delivery doesn't need.

### Explanation
Good firewall rules and access lists allow only the needed port/protocol to the needed destination, and everything else is denied by default. Public-facing servers like this belong in a screened subnet.

## d4-acm-2
type: match
topic: 4.6
group: access-control-models

Match each scenario to the access control model.

### Match
- A file's owner decides who else can open it => Discretionary
- Nurses get access to patient charts because of their job title => Role-based
- Access is allowed only if the user is in HR (Human Resources), on a managed device, during business hours => Attribute-based
- A firewall blocks all traffic to a server after 6 p.m. for everyone => Rule-based

### Distractors
- Mandatory: MAC (Mandatory Access Control) uses clearance and classification labels. None of these use labels.

### Explanation
DAC (Discretionary Access Control) is owner-decided, RBAC (Role-Based Access Control) is job role, ABAC (Attribute-Based Access Control) combines many attributes, and rule-based applies the same rules to everyone.

## d4-access-models-1
type: single
topic: 4.6
group: access-control-models

A defense contractor labels every document Confidential, Secret, or Top Secret, and every user has a clearance level. The operating system enforces access based on those labels, and not even a document's author can grant access to a user with a lower clearance. Which access control model is this?

### Options
- [x] Mandatory access control
- [ ] Discretionary access control
  why: In DAC (Discretionary Access Control) the owner decides who gets access. Here the author can't override the system.
- [ ] Role-based access control
  why: RBAC (Role-Based Access Control) grants permissions by job role. This scenario uses labels and clearances.
- [ ] Attribute-based access control
  why: ABAC (Attribute-Based Access Control) evaluates many attributes through policies. A fixed label hierarchy that nobody can override is a different model.

### Explanation
Mandatory access control is enforced by the system using labels and clearances, and users can't change it. "Not even the author can grant access" is the key phrase.

## d4-sso-1
type: single
topic: 4.6
group: federation-sso

A company wants employees to sign in once with their corporate identity and access Salesforce and other third-party web apps without new passwords. The apps receive signed XML (Extensible Markup Language) assertions. Which protocol is in use?

### Options
- [x] SAML (Security Assertion Markup Language)
- [ ] OAuth (Open Authorization)
  why: OAuth handles authorization (granting an app access to resources), not XML-based sign-in assertions.
- [ ] LDAP (Lightweight Directory Access Protocol)
  why: LDAP is a directory protocol, usually used inside the network.
- [ ] Kerberos
  why: Kerberos uses tickets inside a Windows domain, not XML assertions to web apps.

### Explanation
SAML (Security Assertion Markup Language) passes XML assertions from an identity provider to a service provider for web-based single sign-on and federation.

## d4-sso-3
type: single
topic: 4.6
group: federation-sso

Two companies merge and want users from each to access the other's applications with their existing accounts. What concept does this describe?

### Options
- [x] Federation
- [ ] Provisioning
  why: Provisioning creates accounts. Federation lets existing accounts be trusted.
- [ ] Attestation
  why: Attestation reviews and confirms existing access.
- [ ] Identity proofing
  why: Identity proofing verifies who someone is when an account is created.

### Explanation
Federation is a trust relationship between organizations, so one side accepts the other's authentication.

## d4-mfa-1
type: single
topic: 4.6
group: mfa-factor-types

A login requires a password and a six-digit code from an authenticator app on the user's phone. Which factors are being used?

### Options
- [x] Something you know and something you have
- [ ] Something you know and something you are
  why: The phone app is a possession factor, not a biometric.
- [ ] Something you have and somewhere you are
  why: Nothing checks location.
- [ ] Two things you know
  why: The code comes from a device you possess.

### Explanation
The password is knowledge, and the authenticator app proves possession of the phone. Two different factor types make it true MFA (Multifactor Authentication).

## d4-mfa-2
type: match
topic: 4.6
group: mfa-factor-types

Match each authentication method to its factor type.

### Match
- A PIN (Personal Identification Number) => Something you know
- A hardware security key => Something you have
- A retina scan => Something you are
- Login allowed only from the office's IP (Internet Protocol) range => Somewhere you are

### Distractors
- Something you do: Behavioral factors, like typing patterns, aren't in this list.

### Explanation
Knowledge, possession, inherence (biometrics) and location are the factor types CompTIA expects you to recognize.

## d4-mfa-3
type: multi
topic: 4.6
group: mfa-factor-types

Which TWO combinations are true multifactor authentication?

### Options
- [x] Password and fingerprint
- [x] Smart card and PIN (Personal Identification Number)
- [ ] Password and security question
  why: Both are something you know, so it's one factor used twice.
- [ ] PIN (Personal Identification Number) and password
  why: Both are something you know.
- [ ] Security question and passphrase
  why: Both are something you know.

### Explanation
MFA (Multifactor Authentication) needs at least two different factor types. Two knowledge factors don't count.

## d4-pam-1
type: single
topic: 4.6
group: privileged-access

Admins no longer have permanent admin rights. They request elevated access for a specific task, and it expires automatically after two hours. What is this?

### Options
- [x] Just-in-time permissions
- [ ] Password vaulting
  why: Vaulting stores privileged credentials securely, but it doesn't grant time-limited elevation by itself.
- [ ] Role-based access control
  why: RBAC (Role-Based Access Control) assigns standing permissions by role.
- [ ] Federation
  why: Federation is trust between organizations.

### Explanation
Just-in-time access grants privileges only when needed and removes them automatically, which shrinks the window for misuse.

## d4-pam-3
type: single
topic: 4.6
group: privileged-access

A PAM (Privileged Access Management) tool generates a new admin credential for each session and destroys it when the session ends. What is this type of credential called?

### Options
- [x] Ephemeral credentials
- [ ] Shared credentials
  why: Shared credentials are used by many people and are a risk.
- [ ] Service accounts
  why: Service accounts are for applications, not one-time sessions.
- [ ] Federated credentials
  why: Federated credentials come from another organization's identity provider.

### Explanation
Ephemeral credentials exist only for one session, so a stolen credential is useless afterward.

## d4-password-1
type: single
topic: 4.6
group: password-concepts

Employees keep reusing one password across many sites because they can't remember dozens of unique ones. Which solution BEST addresses this?

### Options
- [ ] Forcing password changes every 30 days
  why: Frequent forced changes lead to predictable patterns and don't stop reuse.
- [x] A password manager that generates and stores unique passwords
- [ ] Lowering the minimum password length so they're easier to remember
  why: Shorter passwords are weaker and don't stop reuse.
- [ ] Allowing passwords to be written on sticky notes
  why: That exposes passwords to anyone nearby.

### Explanation
A password manager generates long, unique passwords for every site and stores them securely, so users only need to remember one strong master password.

## d4-password-2
type: single
topic: 4.6
group: password-concepts

A company replaces passwords with FIDO2 (Fast Identity Online 2) security keys and device biometrics, so users never type a shared secret when they log in. What is this approach called?

### Options
- [ ] Single sign-on across all company apps
  why: SSO (Single Sign-On) lets one login reach many apps. It can still use passwords.
- [ ] Federation
  why: Federation is trust between organizations' identity systems.
- [x] Passwordless authentication
- [ ] Password vaulting
  why: Vaulting stores privileged passwords. Passwords still exist.

### Explanation
Passwordless authentication removes the password, often using public-key credentials on a security key or device that are unlocked with a biometric or PIN (Personal Identification Number). There's no password to phish or reuse.

## d4-password-3
type: single
topic: 4.6
group: password-concepts

A password policy blocks reuse of the last 10 passwords. Users change their password 10 times in one afternoon to get back to their favorite. Which setting stops this?

### Options
- [x] A minimum password age
- [ ] A shorter expiration period
  why: Shorter expiration forces more frequent changes. It doesn't stop rapid cycling.
- [ ] Higher complexity requirements
  why: Complexity rules affect what a password looks like, not how fast it can be changed back.
- [ ] A longer minimum length
  why: Length makes passwords harder to guess but doesn't block cycling.

### Explanation
SY0-701 password best practices are length, complexity, reuse, expiration and age. A minimum age makes users keep a new password for a set time, so the reuse history can't be cycled through.

## d4-lifecycle-1
type: single
topic: 4.6
group: account-lifecycle

An employee was fired three weeks ago, but their VPN (Virtual Private Network) account still works and was just used to log in. Which process failed?

### Options
- [x] Deprovisioning
- [ ] Identity proofing
  why: Identity proofing verifies who someone is when an account is created.
- [ ] Federation
  why: Federation is trust between organizations.
- [ ] Single sign-on
  why: SSO (Single Sign-On) is how users log in once for many apps. It doesn't remove accounts.

### Explanation
Deprovisioning removes or disables accounts and access when someone leaves or changes roles. It should be tied directly to the HR (Human Resources) termination process.

## d4-lifecycle-2
type: single
topic: 4.6
group: account-lifecycle

Every quarter, managers review a list of what their team members can access and confirm whether each permission is still needed. What is this process?

### Options
- [ ] Provisioning
  why: Provisioning creates accounts and grants initial access.
- [x] Attestation
- [ ] Identity proofing
  why: Identity proofing verifies a person's identity at account creation.
- [ ] Just-in-time access
  why: JIT (Just-in-Time) grants temporary elevated access on request.

### Explanation
Attestation (access recertification) has managers confirm that access is still appropriate. It catches privilege creep, where users collect permissions as they change roles.

## d4-idproof-1
type: single
topic: 4.6
group: identity-proofing

Before a new remote hire gets an account, HR (Human Resources) checks their government-issued photo identification on a video call against their background check records. What is this step called?

### Options
- [x] Identity proofing
- [ ] Attestation
  why: Attestation is a formal confirmation that access or controls are correct. It isn't verifying a new person.
- [ ] Multifactor enrollment
  why: Enrolling sign-in factors comes after the account exists.
- [ ] Provisioning
  why: Provisioning creates the account. It happens after the person's identity is confirmed.

### Explanation
Identity proofing verifies that a person is who they claim to be before an identity is issued. Provisioning follows, and access is then reviewed periodically.

## d4-idproof-2
type: match
topic: 4.6
group: identity-proofing

Match each identity concept to its description.

### Match
- Two companies' systems exchange identity information using a common standard such as SAML (Security Assertion Markup Language) => Interoperability
- Each quarter, a manager formally confirms that every team member's access is still needed => Attestation
- Users from a partner organization sign in with their own company's credentials => Federation
- A new account and its permissions are created when an employee joins => Provisioning

### Distractors
- Identity proofing: Identity proofing checks who a person is before an account exists. None of these descriptions is that check.

### Explanation
Interoperability lets identity systems from different vendors and organizations work together, which federation depends on. Attestation is a periodic sign-off that access is still correct.

## d4-auto-1
type: multi
topic: 4.7
group: automation-orchestration

A SOC (Security Operations Center) automates account provisioning and response to common alerts. Which TWO are benefits SY0-701 lists for automation?

### Options
- [x] Consistent enforcement of security baselines
- [x] Faster reaction time
- [ ] Removing every single point of failure
  why: Automation can create a new single point of failure.
- [ ] Lower complexity in every case
  why: Automation often adds complexity. That's one of its listed risks.
- [ ] Eliminating technical debt
  why: Poorly maintained automation can add technical debt.

### Explanation
SY0-701 benefits include efficiency, enforcing baselines, standard configurations, scaling securely, retaining employees, faster reaction time, and workforce multiplication.

## d4-auto-3
type: single
topic: 4.7
group: automation-orchestration

All of a company's incident response playbooks run through one SOAR (Security Orchestration, Automation, and Response) platform with no backup. What automation risk does this create?

### Options
- [x] Single point of failure
- [ ] Technical debt
  why: Technical debt comes from shortcuts, not from relying on one system.
- [ ] Guard rails
  why: Guard rails are a benefit: automated limits that prevent unsafe changes.
- [ ] Workforce multiplier
  why: That's a benefit of automation.

### Explanation
If the one platform fails, all automated responses stop. SY0-701 lists single point of failure as an automation consideration.

## d4-auto-4
type: single
topic: 4.7
group: automation-orchestration

When the SIEM (Security Information and Event Management) raises a phishing alert, a script automatically opens a ticket, pulls the email's headers, and assigns it to the on-call analyst if the sender is on a threat list. Which automation use case does this show?

### Options
- [x] Ticket creation and escalation
- [ ] User provisioning
  why: User provisioning creates accounts and access.
- [ ] Continuous integration testing
  why: CI (Continuous Integration) testing runs automated tests on code changes.
- [ ] Resource provisioning
  why: Resource provisioning builds servers or cloud resources.

### Explanation
SY0-701 automation use cases include user and resource provisioning, guard rails, security groups, ticket creation, escalation, enabling and disabling services, CI testing, and integrations through APIs (Application Programming Interfaces).

## d4-autocons-1
type: multi
topic: 4.7
group: automation-considerations

A security team built dozens of quick automation scripts that only one engineer understands. That engineer is leaving, and nobody can safely change the scripts. Which TWO automation considerations does this show?

### Options
- [x] Ongoing supportability
- [x] Technical debt
- [ ] Workforce multiplier
  why: That's a benefit of automation, not a problem.
- [ ] Enforcing baselines
  why: That's a benefit of automation, not a problem.
- [ ] Guard rails
  why: Guard rails are an automation use case that blocks unsafe actions.

### Explanation
SY0-701 lists complexity, cost, single point of failure, technical debt and ongoing supportability as automation considerations. Benefits include efficiency, enforcing baselines, secure scaling, employee retention, reaction time and workforce multiplier.

## d4-autocons-2
type: single
topic: 4.7
group: automation-considerations

A company runs every account change, firewall update and alert response through one orchestration server. When that server fails, none of these tasks run. Which automation consideration does this show?

### Options
- [x] Single point of failure
- [ ] Employee retention
  why: Retention is a benefit: automation removes tedious work that drives staff away.
- [ ] Scaling in a secure manner
  why: That's a benefit of automation, not a risk.
- [ ] Technical debt
  why: Technical debt is built-up shortcuts. The issue here is dependence on one system.

### Explanation
Centralizing automation on one system creates a single point of failure. Redundancy and manual fallback procedures reduce the risk.

## d4-irp-1
type: single
topic: 4.8
group: ir-process

An analyst has just removed malware from all affected systems and closed the vulnerability it used. Which phase comes NEXT?

### Options
- [x] Recovery
- [ ] Containment
  why: Containment comes before eradication.
- [ ] Lessons learned
  why: Lessons learned comes after recovery.
- [ ] Analysis
  why: Analysis comes before containment.

### Explanation
Removing the malware and closing the entry point is eradication. Recovery (restoring systems to normal operation) comes next.

## d4-irp-2
type: order
topic: 4.8
group: ir-process

Put the SY0-701 incident response phases in order.

### Order
1. Preparation
   why: Plans, tools and training come before any incident.
2. Detection
   why: You can't respond until you know something happened.
3. Analysis
   why: Scope and understand the incident before acting.
4. Containment
   why: Stop the spread.
5. Eradication
   why: Remove the threat.
6. Recovery
   why: Return to normal operations.
7. Lessons learned
   why: Review and improve after things are stable.

### Explanation
Preparation, detection, analysis, containment, eradication, recovery, lessons learned.

## d4-forensic-1
type: single
topic: 4.8
group: digital-forensics

During an investigation, every person who handles a seized laptop signs a log noting the date, time and reason. What is this called?

### Options
- [x] Chain of custody
- [ ] Legal hold
  why: A legal hold requires preserving data. It isn't the handling log.
- [ ] E-discovery
  why: E-discovery is collecting electronic data for legal proceedings.
- [ ] Root cause analysis
  why: RCA (Root Cause Analysis) figures out why an incident happened.

### Explanation
Chain of custody documents everyone who handled evidence, so it can be shown in court that nothing was tampered with.

## d4-forensic-4
type: single
topic: 4.8
group: digital-forensics

A company is sued, and its lawyers instruct IT (Information Technology) to stop the normal deletion of emails and files related to the case. What is this instruction?

### Options
- [ ] Chain of custody
  why: Chain of custody documents who handled evidence. It doesn't stop deletion.
- [x] Legal hold
- [ ] Data sanitization
  why: Sanitization removes data, which is the opposite of what's required.
- [ ] Root cause analysis
  why: RCA (Root Cause Analysis) determines why an incident happened.

### Explanation
A legal hold suspends normal retention and deletion so that relevant data is preserved for litigation. E-discovery is the later process of collecting and producing that data.

## d4-forensic-5
type: single
topic: 4.8
group: digital-forensics

After an analyst creates a drive image, they store the original drive in a sealed evidence bag in a locked room and work only on verified copies, so the evidence stays unchanged. Which digital forensics activity is this?

### Options
- [x] Preservation
- [ ] E-discovery
  why: E-discovery is finding and producing electronic information for a legal case.
- [ ] Legal hold
  why: A legal hold stops normal deletion of relevant data. It doesn't describe handling seized evidence.
- [ ] Root cause analysis
  why: Root cause analysis finds why an incident happened. It isn't about protecting evidence.

### Explanation
SY0-701 digital forensics covers legal hold, chain of custody, acquisition, reporting, preservation and e-discovery. Preservation keeps evidence in its original state so it holds up in court.

## d4-hunt-1
type: single
topic: 4.8
group: hunting-rca

No alerts have fired, but an analyst searches the environment for signs of a technique a new threat group is known to use. What is this activity?

### Options
- [x] Threat hunting
- [ ] Root cause analysis
  why: RCA (Root Cause Analysis) looks back at an incident that already happened.
- [ ] Vulnerability scanning
  why: Scanning finds weaknesses, not attacker activity.
- [ ] Tabletop exercise
  why: A tabletop is a discussion-based drill.

### Explanation
Threat hunting is proactive: analysts look for attackers who may already be inside without waiting for an alert.

## d4-hunt-3
type: single
topic: 4.8
group: hunting-rca

What is the MAIN difference between threat hunting and incident response?

### Options
- [x] Hunting doesn't wait for an alert, but response does
- [ ] Hunting relies only on automated tools, not analysts
  why: Hunting is mostly analyst-driven.
- [ ] Response is handled mainly by outside companies
  why: Most organizations handle incident response internally.
- [ ] Hunting only reviews incidents that already ended
  why: That describes root cause analysis.

### Explanation
Threat hunting is proactive and assumes compromise. Incident response reacts to a detected event.

## d4-hunt-4
type: single
topic: 4.8
group: hunting-rca

After a ransomware incident is fully recovered, the team investigates why the attacker's phishing email led to domain-wide encryption, so the underlying weakness can be fixed. What is this activity?

### Options
- [ ] Threat hunting across the domain
  why: Threat hunting looks for attackers who may be present now. This looks back at a finished incident.
- [x] Root cause analysis
- [ ] Containment
  why: Containment limits the spread during an incident. The incident is already over.
- [ ] E-discovery
  why: E-discovery collects electronic data for legal proceedings.

### Explanation
Root cause analysis identifies the underlying reason an incident succeeded, so the fix addresses the cause rather than the symptom. It feeds lessons learned.

## d4-volatility-1
type: order
topic: 4.8
group: order-of-volatility

A forensic analyst arrives at a running server suspected of compromise. Put the evidence sources in the order they should be collected.

### Order
1. CPU (Central Processing Unit) registers and cache
   why: These change in nanoseconds, so they go first.
2. RAM (Random Access Memory) contents such as running processes and network connections
   why: Memory is lost the moment power is removed.
3. Swap space and temporary files
   why: These are on disk but get overwritten constantly while the system runs.
4. Files on the hard drive
   why: Disk data survives a power loss, so it can wait.
5. Archived backups and offsite logs
   why: These are the most stable and can be collected last.

### Explanation
Evidence is collected from the shortest-lived to the longest-lived so nothing disappears while you're collecting something more durable.

## d4-volatility-3
type: single
topic: 4.8
group: order-of-volatility

An analyst responding to an active intrusion on a workstation plans to pull the power cord immediately and then image the drive. Which evidence would this plan destroy?

### Options
- [x] The list of running processes in memory
- [ ] Documents saved in the user's home folder
  why: Saved files are on disk and survive a power loss.
- [ ] Deleted files in unallocated space on the drive
  why: Those stay on the disk until they're overwritten, so the image would still capture them.
- [ ] Firewall logs already sent to the SIEM (Security Information and Event Management)
  why: Those are stored on another system and aren't affected.

### Explanation
Cutting power wipes RAM (Random Access Memory), which holds running processes, network connections, and often decryption keys or fileless malware. That's why memory is captured before the system is shut down.

## d4-pbq-logs
type: pbq
topic: 4.9
group: investigation-data

An EDR (Endpoint Detection and Response) alert fires on workstation WS-114. Review the data and answer each part.

### Exhibit
```text
[EDR]  09:41:02 WS-114 user=kpatel  WINWORD.EXE spawned powershell.exe -enc JABjAGwAaQBlAG4AdAA...
[EDR]  09:41:05 WS-114 powershell.exe connected to 203.0.113.77:443
[FW]   09:41:05 ALLOW  10.1.4.114 -> 203.0.113.77:443  bytes_out=1,204
[FW]   09:52:40 ALLOW  10.1.4.114 -> 203.0.113.77:443  bytes_out=847,330,112
[DNS]  09:40:58 WS-114 query: invoice-update.top -> 203.0.113.77
```

### Explanation
Word launched encoded PowerShell (a malicious macro), which contacted a suspicious domain. Eleven minutes later, about 847 MB (megabytes) left the network to the same IP (Internet Protocol), which points to data exfiltration. The EDR log shows the process behavior, and the firewall log shows the data volume.

## d4-pbq-logs/a
type: single

Which data source BEST shows how the attack started on the workstation?

### Options
- [x] The EDR (Endpoint Detection and Response) log
- [ ] The firewall log for outbound traffic
  why: The firewall shows connections, not which process started them.
- [ ] The DNS (Domain Name System) log
  why: DNS shows the lookup but not what launched it.
- [ ] A vulnerability scan of the workstation
  why: A scan shows weaknesses, not what happened.

## d4-pbq-logs/b
type: single

What do the firewall entries MOST likely show?

### Options
- [x] Data exfiltration
- [ ] A DDoS (Distributed Denial of Service) attack
  why: The traffic is outbound from one host to one IP (Internet Protocol), not a flood against a target.
- [ ] A port scan
  why: There's one connection to one port.
- [ ] Normal software updates
  why: Updates are downloads. These are large uploads to an unknown domain.

## d4-logs-2
type: match
topic: 4.9
group: investigation-data

Match each investigation question to the BEST data source.

### Match
- Which process on a laptop launched a suspicious script? => Endpoint logs
- Was traffic from an external IP (Internet Protocol) allowed or blocked? => Firewall logs
- What exact data was inside a suspicious network session? => Packet capture
- Who changed a file and when, according to the file's own properties? => Metadata

### Distractors
- Vulnerability scan: Scans show weaknesses, not what happened in an event.

### Explanation
Each source answers different questions. Investigations usually combine several.

## d4-logs-3
type: match
topic: 4.9
group: investigation-data

Match each investigation question to the BEST data source.

### Match
- Did the web app record a user's failed attempts to open its admin page? => Application logs
- Which Windows account signed in to the server at 2 a.m.? => Operating system security logs
- Which hosts had unpatched critical flaws as of last week? => Vulnerability scans
- A scheduled summary of failed sign-ins across all systems arrives each morning => Automated reports
- Was a known exploit signature seen crossing the network boundary? => IDS (Intrusion Detection System) logs

### Distractors
- Packet captures: Captures show full traffic content. None of these questions needs to see what was inside the traffic.

### Explanation
SY0-701 log data includes firewall, application, endpoint, OS (Operating System)-specific security, IPS (Intrusion Prevention System)/IDS and network logs, plus metadata. Other data sources are vulnerability scans, automated reports, dashboards and packet captures.
