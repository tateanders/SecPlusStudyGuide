---
deck: Domain 2 – Threats, Vulnerabilities, and Mitigations
section: "2.0"
exam_weight: 22
topics:
  2.1: Compare and contrast common threat actors and motivations
  2.2: Explain common threat vectors and attack surfaces
  2.3: Explain various types of vulnerabilities
  2.4: Given a scenario, analyze indicators of malicious activity
  2.5: Explain the purpose of mitigation techniques used to secure the enterprise
---

## d2-actor-1
type: single
topic: 2.1
group: threat-actors

A group spends 18 months quietly inside a defense contractor's network, using custom malware and zero-day exploits to steal weapons designs. Which threat actor is MOST likely responsible?

### Options
- [ ] Organized crime
  why: Organized crime is usually after money and moves faster, like ransomware or fraud. Long-term theft of defense designs points elsewhere.
- [x] Nation-state
- [ ] Hacktivist
  why: Hacktivists want attention for a cause, like defacements or leaks. They rarely stay hidden for 18 months.
- [ ] Insider threat
  why: Nothing suggests someone inside the company. The attackers had to break in.

### Explanation
Nation-states have the most resources and sophistication, stay hidden for long periods (an APT (Advanced Persistent Threat), or advanced persistent threat), and are motivated by espionage. Custom malware, zero-days and military targets all point there.

## d2-actor-2
type: match
topic: 2.1
group: threat-actors

Match each scenario to the MOST likely threat actor.

### Match
- A group defaces a city website to protest a new law => Hacktivist
- A teenager runs a downloaded DDoS (Distributed Denial of Service) tool against a game server => Unskilled attacker
- A group encrypts a hospital's systems and demands a Bitcoin ransom => Organized crime
- A fired admin uses a forgotten account to delete production data => Insider threat

### Distractors
- Nation-state: None of these involve a government's resources or espionage goals.

### Explanation
Hacktivists act for a cause, unskilled attackers use tools they didn't write, organized crime is financially motivated, and insiders already have access.

## d2-actor-4
type: multi
topic: 2.1
group: threat-actors

Which TWO attributes BEST distinguish a nation-state actor from an unskilled attacker?

### Options
- [x] Much greater funding and resources
- [x] Higher level of sophistication
- [ ] Located outside the target's country
  why: Nation-state actors can operate from anywhere. Location isn't the distinguishing attribute.
- [ ] Motivated mainly by financial gain
  why: Nation-states are usually motivated by espionage or disruption, not money.
- [ ] Operating as an internal actor
  why: Nation-states are usually external.

### Explanation
SY0-701 compares threat actors by internal or external, resources and funding, and sophistication. Nation-states sit at the top of both resources and sophistication.

## d2-shadow-it-1
type: single
topic: 2.1
group: shadow-it

A marketing team, frustrated by a slow procurement process, signs up for a cloud file-sharing service with a company credit card and uploads customer lists to it. The technology department has no idea the service exists. Which threat actor category BEST describes the marketing team?

### Options
- [x] Shadow IT (Information Technology)
- [ ] Insider threat
  why: An insider threat abuses legitimate access to harm the organization. This team means well; the problem is unapproved technology.
- [ ] Hacktivist
  why: Hacktivists attack to promote a political or social cause. Nobody here is attacking anything.
- [ ] Unskilled attacker using others' tools
  why: An unskilled attacker runs other people's tools against a target. The team is just trying to get work done.

### Explanation
Shadow IT is technology that staff set up without the knowledge or approval of the technology department. The clues are the motive (getting around a slow process) and the fact that nobody responsible for security knows about it.

## d2-shadow-it-3
type: single
topic: 2.1
group: shadow-it

A security analyst is building a threat actor matrix. One row describes an actor that is internal to the organization, isn't trying to cause harm, and mostly wants to get around slow or restrictive technology processes. Which actor belongs in that row?

### Options
- [x] Shadow IT (Information Technology)
- [ ] Insider threat
  why: Also internal, but motivated by revenge, money, or ideology. An insider threat intends harm.
- [ ] Organized crime
  why: External, well funded, and motivated by financial gain.
- [ ] Nation-state advanced persistent threat
  why: External, with the highest resources and sophistication, motivated by espionage or disruption.

### Explanation
Internal plus no malicious intent plus a convenience motive equals shadow IT. Insider threat shares the "internal" attribute, so intent is what separates the two.

## d2-motive-1
type: match
topic: 2.1
group: threat-motivations

Match each attack to the attacker's MOST likely motivation.

### Match
- A former employee leaks the CEO's (Chief Executive Officer) private emails after being fired => Revenge
- A group floods a pipeline company's website on the day of a protest => Philosophical/political beliefs
- Attackers copy a rival company's product designs over several months => Espionage
- Criminals threaten to publish stolen patient photos unless paid => Blackmail

### Distractors
- Ethical: Ethical (white-hat) hackers act to improve security with permission. None of these attackers had permission.
- War: Acts of war are military operations between states. None of these are state military actions.

### Explanation
SY0-701 lists motivations including data exfiltration, espionage, service disruption, blackmail, financial gain, philosophical or political beliefs, ethical, revenge, disruption or chaos, and war. Read what the attacker gains from the outcome.

## d2-motive-2
type: single
topic: 2.1
group: threat-motivations

An attack on a regional power grid's control systems causes outages during a military conflict between two countries. No ransom is demanded and no data is sold. Which motivation BEST fits?

### Options
- [ ] Financial gain
  why: No ransom or sale was involved, so money isn't the goal.
- [x] War
- [ ] Ethical
  why: Ethical hackers work with permission to improve security. Causing outages isn't ethical hacking.
- [ ] Revenge
  why: Revenge is personal, like a fired employee striking back. This is tied to a conflict between countries.

### Explanation
Attacks on critical infrastructure during a conflict between nations are acts of war, usually by nation-state actors. The lack of a financial demand is the key clue.

## d2-bec-1
type: single
topic: 2.2
group: bec

The accounts payable team gets an email from a vendor's real email account, which was hacked, saying the vendor's bank account has changed. The team updates the payment details and sends $90,000 to the attacker. What attack is this?

### Options
- [ ] Typosquatting
  why: Typosquatting uses a look-alike domain. This email came from the vendor's real account.
- [x] Business email compromise
- [ ] Watering hole attack
  why: A watering hole compromises a website the targets visit.
- [ ] Smishing
  why: Smishing uses SMS (Short Message Service) text messages.

### Explanation
Business email compromise uses a real or convincingly spoofed business email account to trick staff into sending money or data. A hijacked vendor account asking to change payment details is the classic form.

## d2-bec-2
type: single
topic: 2.2
group: bec

A finance clerk receives an email that appears to come from the CFO's (Chief Financial Officer) real mailbox. It asks for an urgent wire to close a confidential acquisition and says not to discuss it with anyone. Which control would MOST likely have stopped the loss?

### Options
- [ ] A longer minimum password length for finance staff
  why: The clerk's password wasn't involved. The clerk was tricked into acting.
- [x] Verifying payment requests by calling a known number
- [ ] Encrypting all outbound email with S/MIME (Secure/Multipurpose Internet Mail Extensions)
  why: Encryption hides message contents. It doesn't confirm that the request is legitimate.
- [ ] Blocking USB (Universal Serial Bus) drives on finance workstations
  why: Nothing was delivered by removable media.

### Explanation
BEC (Business Email Compromise) relies on a trusted mailbox and urgency. Out-of-band verification of payment changes and wire requests, using a phone number already on file, breaks the attack no matter how real the email looks.

## d2-bec-3
type: single
topic: 2.2
group: social-engineering

A caller claims to be from the company's IT (Information Technology) help desk. He mentions the employee's manager by name and says he's fixing a payroll issue that will delay her paycheck unless she reads him the code from her authenticator app. What social engineering technique is the caller MAINLY using?

### Options
- [x] Pretexting
- [ ] Watering hole
  why: A watering hole compromises a website. This is a phone call.
- [ ] Typosquatting
  why: Typosquatting relies on mistyped URLs (Uniform Resource Locators).
- [ ] Brand impersonation
  why: Brand impersonation copies a well-known company's branding, usually online. Here the caller builds a made-up story.

### Explanation
Pretexting is creating a believable story (a pretext) to get someone to act. The manager's name and the payroll issue are the pretext. The call itself is also vishing.

## d2-socialeng-1
type: single
topic: 2.2
group: social-engineering

During an election, fake news articles that look like a respected newspaper's site spread on social media. They're designed to mislead voters, and the people sharing them know the stories are false. What is this?

### Options
- [ ] Misinformation
  why: Misinformation is false information shared by people who believe it's true. Here the people spreading it know it's false.
- [x] Disinformation
- [ ] Watering hole attack
  why: A watering hole compromises a real site to deliver malware. These are fake articles meant to mislead.
- [ ] Typosquatting
  why: Typosquatting depends on people mistyping a web address. These stories spread through shares.

### Explanation
Disinformation is false information spread deliberately to deceive. Misinformation is false information spread by people who think it's true. SY0-701 groups both as human vectors.

## d2-socialeng-2
type: match
topic: 2.2
group: social-engineering

Match each scenario to the social engineering technique.

### Match
- A visitor in a delivery uniform says a package needs a signature inside the server room => Impersonation
- A website copies a well-known bank's logo and colors to collect logins => Brand impersonation
- A caller invents a story about an audit to get an employee to reveal a process => Pretexting
- A false rumor that the company is being sold spreads among staff who believe it => Misinformation

### Distractors
- Whaling: Whaling targets senior executives. None of these focus on an executive.

### Explanation
Impersonation pretends to be a specific person or role. Brand impersonation copies a company's identity. Pretexting builds a believable story. Misinformation is false content spread by people who believe it.

## d2-msgphish-1
type: match
topic: 2.2
group: message-phishing

Match each attack to its delivery method.

### Match
- A fake "package delivery failed" link arrives as a text message => Smishing
- A caller pretends to be the bank's fraud department => Vishing
- A fake login link is sent to all employees by email => Phishing
- A fake support account messages a user on Microsoft Teams => Instant messaging attack

### Distractors
- Whaling: Whaling targets executives. None of these focus on an executive.

### Explanation
Smishing uses SMS (Short Message Service), vishing uses voice, phishing uses email, and SY0-701 lists instant messaging as its own message-based threat vector.

## d2-msgphish-3
type: single
topic: 2.2
group: message-phishing

Employees receive a text message that says "Your payroll account is locked. Verify at payroII-portal.co." Which combination of techniques does this use?

### Options
- [ ] Vishing and watering hole
  why: Nothing here is a voice call or a compromised website the employees normally visit.
- [x] Smishing and typosquatting
- [ ] Whaling and pharming
  why: This targets all employees, not executives. Pharming redirects traffic from a real domain.
- [ ] Spear phishing and BEC (Business Email Compromise)
  why: BEC uses compromised email accounts. This is a text message.

### Explanation
The message is SMS (smishing), and "payroII" uses capital I's instead of lowercase l's (typosquatting).

## d2-watering-1
type: single
topic: 2.2
group: watering-hole

Attackers compromise a regional engineering association's website that a target company's engineers visit often, and use it to deliver malware to them. What attack is this?

### Options
- [ ] Typosquatting
  why: Typosquatting relies on a user mistyping a URL (Uniform Resource Locator). The engineers went to the real site.
- [x] Watering hole
- [ ] Spear phishing
  why: Spear phishing sends a targeted message. Here the attacker waits on a website.
- [ ] Supply chain attack
  why: A supply chain attack compromises a vendor's product or service the company uses. A website the engineers visit isn't a supplier.

### Explanation
A watering hole attack compromises a site the targets already trust and visit. The attacker waits for them to come.

## d2-watering-3
type: multi
topic: 2.2
group: watering-hole

Which TWO controls would BEST reduce the risk of a watering hole attack?

### Options
- [x] Keep browsers and plugins fully patched
- [x] Use reputation-based web filtering on all browsing
- [ ] Add SPF (Sender Policy Framework) and DKIM (DomainKeys Identified Mail) records to the company's domain
  why: SPF and DKIM protect email. A watering hole is delivered through a website.
- [ ] Require longer passwords
  why: Watering hole malware usually exploits the browser. Passwords don't stop that.
- [ ] Register look-alike domains
  why: That defends against typosquatting, not a compromised real site.

### Explanation
Watering holes usually exploit browser vulnerabilities on trusted sites. Patching removes the vulnerabilities, and reputation-based web filtering can block the malicious content.

## d2-supply-1
type: single
topic: 2.2
group: supply-chain

Attackers break into a software vendor's build server and insert a backdoor into a signed update. Thousands of the vendor's customers install it. What type of attack is this?

### Options
- [x] Supply chain attack
- [ ] Watering hole
  why: A watering hole compromises a website the targets visit. This compromised a product they use.
- [ ] Zero-day exploit
  why: No unknown vulnerability in the customers' systems was exploited. They installed the backdoor themselves.
- [ ] Insider threat
  why: The attackers were external to the vendor.

### Explanation
A supply chain attack compromises a supplier (software, hardware, or a service provider) to reach its customers.

## d2-supply-2
type: multi
topic: 2.2
group: supply-chain

Which TWO of these are supply chain attack surfaces listed in SY0-701?

### Options
- [x] Managed service providers
- [x] Hardware and software vendors
- [ ] Open service ports
  why: Open ports are an attack surface, but they're network-based, not supply chain.
- [ ] Removable media
  why: Removable media is a separate threat vector.
- [ ] Default credentials
  why: Default credentials are a separate vector, not part of the supply chain category.

### Explanation
SY0-701 lists MSPs (managed service providers), vendors, and suppliers as supply chain attack surfaces.

## d2-typosquat-1
type: single
topic: 2.2
group: typosquatting

Several employees report that the payroll site asked them to log in twice this morning. The help desk finds that each of them typed the address by hand, and their browser history shows `paybridgeportal.com` instead of the real `paybridge-portal.com`. The fake site looks identical to the real one. Which technique did the attacker rely on?

### Options
- [x] Typosquatting
- [ ] Watering hole
  why: A watering hole compromises a legitimate site the victims already visit. The real payroll site was untouched.
- [ ] DNS (Domain Name System) poisoning
  why: Poisoning sends users to the wrong server even when they type the correct name. Here the browser history shows a different domain name.
- [ ] Pretexting
  why: Pretexting is an invented story told to a person. Nobody contacted these employees.

### Explanation
Typosquatting registers a domain that's a small mistake away from the real one and waits for people to mistype it. The hand-typed address and the missing hyphen in the history are the evidence.

## d2-typosquat-3
type: multi
topic: 2.2
group: typosquatting

A bank wants to reduce the risk of customers landing on look-alike sites whose addresses differ from the bank's real one by a single character. Which TWO actions MOST directly address this?

### Options
- [x] Register common misspellings of the bank's domain
- [x] Monitor new domain registrations for similar names
- [ ] Enable DNSSEC (Domain Name System Security Extensions) on the bank's real domain
  why: DNSSEC protects answers for the real domain. A look-alike is a different, validly registered domain.
- [ ] Require longer passwords for online banking accounts
  why: A fake site captures whatever the customer types, no matter how long it is.
- [ ] Shorten the validity period of the bank's TLS (Transport Layer Security) certificate
  why: The fake site gets its own valid certificate for its own name, so the bank's certificate lifetime doesn't matter.

### Explanation
The attack lives in domains the bank doesn't own, so the direct answers are to own the likely misspellings and to watch for new ones so they can be taken down. Controls on the bank's own domain don't touch a look-alike.

## d2-vector-1
type: match
topic: 2.2
group: threat-vectors

Match each scenario to its threat vector.

### Match
- USB (Universal Serial Bus) sticks labeled "Payroll 2026" are left in the company parking lot => Removable device
- A new router still accepts admin/admin from the factory => Default credentials
- An old Windows server no longer gets security updates => Unsupported systems
- An attacker pairs with a laptop's headset connection from across the café => Bluetooth

### Distractors
- Open service ports: Open ports expose listening services. None of these scenarios relies on a listening network service.
- Watering hole: A watering hole compromises a website the targets visit. None of these use a website.

### Explanation
SY0-701 lists vectors such as message-based, image-based, file-based, voice call, removable device, vulnerable software, unsupported systems, unsecure networks (wireless, wired, Bluetooth), open service ports, default credentials, and supply chain.

## d2-vector-2
type: single
topic: 2.2
group: threat-vectors

A security team compares two ways to find vulnerable software on laptops. One installs software on every laptop. The other scans laptops over the network without installing anything. What is the main trade-off?

### Options
- [x] The installed agent adds software to every laptop
- [ ] The network scan can only detect zero-day exploits
  why: Neither approach detects only zero-days. Both look for known vulnerabilities.
- [ ] The installed agent can't see installed software
  why: An agent on the device sees installed software best. That's its main advantage.
- [ ] The network scan needs the laptops to be powered off
  why: A network scan needs the device on and reachable.

### Explanation
Client-based (agent) scanning gives deep visibility but adds software that must be managed and could itself be vulnerable. Agentless scanning adds nothing to the endpoint but only sees what's reachable over the network.

## d2-vector-3
type: single
topic: 2.2
group: threat-vectors

An attacker sends an employee a résumé file. Opening it runs a hidden macro that downloads malware. Which threat vector is this?

### Options
- [ ] Image-based
  why: Image-based vectors hide malicious content in pictures. This is a document with a macro.
- [ ] Voice call
  why: No phone call was involved.
- [x] File-based
- [ ] Open service port
  why: Nothing connected to a listening service. The user opened a file.

### Explanation
File-based vectors deliver malicious content inside documents, archives, or executables. Macros in office documents are a common example.

## d2-memory-1
type: single
topic: 2.3
group: memory-vulns

An attacker sends a 5,000-character username to a program that only allocated 64 bytes for it. The extra data overwrites the program's return address. What is this vulnerability?

### Options
- [x] Buffer overflow
- [ ] Race condition
  why: Race conditions are about timing, not input size.
- [ ] Cross-site scripting
  why: XSS (Cross-Site Scripting) injects scripts into web pages viewed by other users.
- [ ] Directory traversal
  why: Directory traversal uses ../ sequences to reach files outside the web root.

### Explanation
A buffer overflow writes past the end of a memory buffer. Overwriting the return address can let the attacker run their own code.

## d2-memory-3
type: multi
topic: 2.3
group: memory-vulns

Which TWO controls MOST directly reduce the risk of buffer overflow attacks?

### Options
- [x] Bounds checking and input validation in the code
- [x] ASLR (address space layout randomization)
- [ ] Salting stored passwords before they are hashed
  why: Salting protects password hashes. It has nothing to do with memory.
- [ ] Certificate pinning
  why: Pinning protects TLS (Transport Layer Security) connections from fake certificates.
- [ ] Account lockout policies
  why: Lockouts stop password guessing, not memory corruption.

### Explanation
Bounds checking stops oversized input at the source. ASLR randomizes memory addresses, so an attacker can't reliably predict where to jump.

## d2-webvuln-1
type: single
topic: 2.3
group: web-injection

A login form passes the username straight into a database query. An attacker enters `' OR 1=1 --` and logs in as the first user in the table. What attack is this?

### Options
- [ ] Cross-site scripting through the login form
  why: XSS (Cross-Site Scripting) injects scripts that run in other users' browsers. This manipulates a database query.
- [x] SQL (Structured Query Language) injection
- [ ] Directory traversal
  why: Directory traversal reads files outside the web root.
- [ ] Buffer overflow
  why: The input isn't oversized. It changes the query's logic.

### Explanation
SQL injection inserts SQL syntax into input that gets built into a query. `' OR 1=1` makes the condition always true.

## d2-webvuln-3
type: single
topic: 2.3
group: web-injection

A forum lets users post comments. An attacker posts a comment containing a script that steals the session cookie of everyone who views it. What attack is this?

### Options
- [ ] SQL (Structured Query Language) injection
  why: Nothing here targets the database. The script runs in other users' browsers.
- [ ] Cross-site request forgery
  why: CSRF (Cross-Site Request Forgery) tricks a user's browser into sending an unwanted request. Here the attacker's script runs in the page.
- [x] Stored cross-site scripting
- [ ] Session replay
  why: Replay is what the attacker might do next with the stolen cookie. The attack described is the script injection.

### Explanation
Stored (persistent) XSS (Cross-Site Scripting) saves a malicious script on the site, and it runs in the browser of everyone who views the page. Output encoding and input validation prevent it.

## d2-mobile-1
type: single
topic: 2.3
group: mobile-vulns

An employee installs a game on a company Android phone from a third-party website instead of the Google Play Store. What is this called?

### Options
- [x] Sideloading
- [ ] Jailbreaking
  why: Jailbreaking removes iOS restrictions. Installing an app from outside the store is sideloading.
- [ ] Rooting
  why: Rooting gains admin access to Android. The employee just installed an app.
- [ ] Carrier unlocking
  why: Carrier unlocking lets a phone use another cell provider.

### Explanation
Sideloading installs apps from outside the official app store, skipping the store's security review.

## d2-mobile-3
type: single
topic: 2.3
group: mobile-vulns

Which control BEST prevents employees from running jailbroken phones on the corporate network?

### Options
- [ ] Full-disk encryption on every phone
  why: Encryption protects data at rest. It doesn't detect jailbreaks.
- [x] MDM (Mobile Device Management) with device compliance checks
- [ ] WPA3 (Wi-Fi Protected Access 3) on the corporate Wi-Fi
  why: WPA3 protects the wireless connection, not the device's integrity.
- [ ] A screen lock and PIN (Personal Identification Number) policy
  why: Screen locks don't detect jailbreaking.

### Explanation
Mobile device management can check whether a device is jailbroken or rooted and deny it access until it's compliant.

## d2-toctou-1
type: single
topic: 2.3
group: race-condition

A banking app reads an account's balance, then a few milliseconds later deducts the withdrawal. An attacker submits two withdrawals at the same instant. Both pass the balance check before either deduction is recorded, and the account goes negative. Which vulnerability is this?

### Options
- [x] Race condition
- [ ] Buffer overflow
  why: A buffer overflow writes more data than a memory buffer can hold. Nothing here involves oversized input.
- [ ] Memory injection
  why: Memory injection places malicious code into a running process. The attacker only sent two normal requests.
- [ ] Privilege escalation
  why: That's gaining rights you shouldn't have. The attacker stayed a normal customer and exploited timing.

### Explanation
A race condition happens when the outcome depends on the timing of two operations that should have been handled as one. The gap between reading the balance and recording the deduction is the window.

## d2-toctou-3
type: single
topic: 2.3
group: race-condition

A code review finds that a file-processing service validates a file's permissions and then opens the file in a separate step, leaving a gap in which an attacker could swap the file. Which change BEST removes the vulnerability?

### Options
- [x] Combine the test and the open into one atomic step
- [ ] Run the permission validation twice before opening the file
  why: The gap still exists after the second validation. The attacker just swaps the file a little later.
- [ ] Encrypt the file at rest with a strong algorithm
  why: Encryption protects the contents from being read. It doesn't close the timing window.
- [ ] Add input validation to the file upload form
  why: The upload was fine. The problem is what happens between validating and opening.

### Explanation
The fix for a time-of-check to time-of-use flaw is to remove the window: make validation and use a single atomic operation (or lock the resource in between). Anything that leaves two separate steps leaves the race.

## d2-virt-1
type: single
topic: 2.3
group: virtualization-vulns

An attacker with access to one virtual machine exploits a flaw in the hypervisor and gains control of the host and every other VM (Virtual Machine) on it. What is this vulnerability?

### Options
- [x] VM escape
- [ ] Resource reuse
  why: Resource reuse is when memory or storage left over from one VM is handed to another without being cleared. Nothing was left behind here.
- [ ] Sideloading
  why: Sideloading installs mobile apps from outside the official store.
- [ ] Privilege escalation inside the guest
  why: Gaining admin inside one VM stays inside that VM. Breaking out to the host is a more specific attack.

### Explanation
VM escape breaks out of a guest into the hypervisor, which exposes every other guest on that host. Patching hypervisors and limiting what guests can access are the main defenses.

## d2-virt-2
type: single
topic: 2.3
group: virtualization-vulns

A cloud customer finds fragments of another tenant's data in a newly created virtual disk. What vulnerability does this show?

### Options
- [ ] VM (Virtual Machine) escape
  why: VM escape is breaking out of a guest into the hypervisor. No one broke out of anything here.
- [x] Resource reuse
- [ ] Race condition
  why: A race condition is a timing flaw between two operations. This is leftover data.
- [ ] Buffer overflow
  why: A buffer overflow writes past allocated memory. This is old data that was never wiped.

### Explanation
Resource reuse happens when memory or storage from one virtual machine is reassigned to another without being cleared, which leaks data between tenants.

## d2-hwvuln-1
type: single
topic: 2.3
group: hardware-vulns

A factory runs machinery controllers whose vendor stopped releasing firmware updates three years ago. A new vulnerability is published for them. What is the core problem?

### Options
- [ ] The controllers are vulnerable to SQL (Structured Query Language) injection
  why: Nothing here involves a database. The problem is that no patch is coming.
- [x] The devices are end-of-life and can't be patched
- [ ] The controllers are vulnerable to VM (Virtual Machine) escape
  why: These are physical devices, not virtual machines.
- [ ] The devices use a weak Wi-Fi encryption standard
  why: Nothing indicates a wireless weakness. The issue is lack of vendor support.

### Explanation
End-of-life and legacy hardware no longer gets firmware fixes, so new vulnerabilities stay open for good. The usual answer is compensating controls such as segmentation until the hardware is replaced.

## d2-hwvuln-2
type: single
topic: 2.3
group: hardware-vulns

Attackers modify the firmware on a network card so their code survives operating system reinstalls and disk replacement. Why is this especially dangerous?

### Options
- [ ] Firmware attacks only work on legacy operating systems
  why: Firmware sits below the operating system, so the OS version doesn't matter.
- [x] The code runs below the OS (Operating System) and survives reinstalls
- [ ] Antivirus inside the OS scans firmware on every boot
  why: Most antivirus runs inside the OS and can't inspect device firmware.
- [ ] The attack requires the user to open a malicious file each boot
  why: Once the firmware is modified, it runs automatically with no user action.

### Explanation
Firmware runs before and beneath the operating system. Reinstalling the OS or replacing the disk doesn't touch it, so firmware compromises persist and are hard to detect. Secure boot and signed firmware help prevent them.

## d2-vulntype-1
type: single
topic: 2.3
group: vulnerability-types

Attackers exploit a flaw in a widely used web server that the vendor doesn't know about yet. No patch or signature exists. What is this?

### Options
- [x] A zero-day vulnerability
- [ ] A misconfiguration
  why: A misconfiguration is a setting someone got wrong. Here the software itself has an unknown flaw.
- [ ] A malicious update
  why: A malicious update is a compromised patch pushed through the update process. Nothing was installed here.
- [ ] Resource reuse
  why: Resource reuse leaks leftover data between virtual machines.

### Explanation
A zero-day is a vulnerability unknown to the vendor, so there's no patch and often no signature. Behavior-based detection, segmentation and least privilege limit the damage.

## d2-vulntype-2
type: match
topic: 2.3
group: vulnerability-types

Match each finding to the type of vulnerability.

### Match
- A storage bucket holding customer files allows public read access => Misconfiguration
- A legacy app still encrypts data with DES (Data Encryption Standard) => Cryptographic
- An attacker exploits a flaw in the Windows kernel to get SYSTEM rights => Operating system-based
- A compromised vendor pushes a backdoor through its normal update channel => Malicious update

### Distractors
- Zero-day: A zero-day is unknown to the vendor. Each of these flaws is a known type of weakness.

### Explanation
Misconfigurations are wrong settings, cryptographic vulnerabilities come from weak or broken algorithms, OS-based vulnerabilities live in the operating system, and malicious updates abuse the trusted update path.

## d2-cloudvuln-1
type: single
topic: 2.3
group: cloud-vulns

A company stores customer exports in a cloud object storage bucket. A researcher finds that anyone on the internet can list and download the files without signing in. What type of vulnerability is this?

### Options
- [x] A cloud-specific misconfiguration
- [ ] A zero-day in the provider's storage service
  why: A zero-day is an unknown flaw with no patch. This is a setting the customer chose.
- [ ] A VM (Virtual Machine) escape
  why: VM escape breaks out of a virtual machine into the host. Nothing here involves a hypervisor.
- [ ] A race condition in the upload process
  why: A race condition depends on timing between steps. The files are simply open to everyone.

### Explanation
Under the shared responsibility model, the customer configures access to its own cloud resources. Public storage buckets, overly broad IAM (Identity and Access Management) roles and exposed management interfaces are common cloud-specific vulnerabilities.

## d2-cloudvuln-2
type: multi
topic: 2.3
group: cloud-vulns

A company moves its applications to a public cloud. Which TWO risks come specifically from the cloud model?

### Options
- [x] Cloud management consoles open to the internet
- [x] Overly broad permissions on cloud resources
- [ ] A buffer overflow in the company's own code
  why: Code flaws exist wherever the code runs, in the cloud or on-premises.
- [ ] Employees clicking on phishing links in email
  why: Phishing targets people regardless of where systems are hosted.
- [ ] Unpatched firmware on the office printers
  why: Printers sit in the office. This risk has nothing to do with the cloud.

### Explanation
Cloud-specific vulnerabilities come from how cloud services are reached and configured: internet-facing management consoles and APIs (Application Programming Interfaces), broad identity permissions, public storage and weak tenant isolation.

## d2-malware-1
type: match
topic: 2.4
group: malware-types

Match each malware behavior to its type.

### Match
- Spreads across the network on its own, without user action => Worm
- Looks like a free PDF (Portable Document Format) converter but installs a backdoor => Trojan
- Hides deep in the OS (Operating System) and conceals other malicious files from the user => Rootkit
- Deletes payroll data on a set date if an admin is removed from HR (Human Resources) records => Logic bomb

### Distractors
- Virus: A virus needs a host file and user action to spread.
- Keylogger: A keylogger records keystrokes. None of these describe that.

### Explanation
Worms self-propagate, trojans pretend to be legitimate, rootkits hide at a low level, and logic bombs wait for a condition.

## d2-malware-3
type: single
topic: 2.4
group: malware-types

Antivirus can't see a piece of malware, and the system's own tools report no unusual processes. A scan from a bootable USB (Universal Serial Bus) drive finds modified kernel files. What type of malware is MOST likely present?

### Options
- [ ] Worm
  why: Worms focus on spreading. They don't typically hide from the OS (Operating System) itself.
- [ ] Spyware
  why: Spyware collects information. Hiding from the OS's own tools points to something deeper.
- [x] Rootkit
- [ ] Ransomware
  why: Ransomware announces itself by encrypting files and demanding payment.

### Explanation
Rootkits modify the OS or kernel so the system's own tools can't see them. Scanning from outside the infected OS, like a bootable drive, is how you find them.

## d2-malware-4
type: match
topic: 2.4
group: malware-types

Match each description to the malware type.

### Match
- Encrypts files and demands payment for the key => Ransomware
- Records every keystroke and sends it to the attacker => Keylogger
- Attaches itself to a program and spreads when that program is run => Virus
- Comes preinstalled on a new laptop, using resources and adding attack surface => Bloatware

### Distractors
- Worm: A worm spreads by itself across networks without needing a host program or user action.
- Rootkit: A rootkit hides deep in the OS (Operating System) to conceal itself. None of these describe hiding.

### Explanation
Ransomware extorts, keyloggers capture input, viruses need a host and user action, and bloatware is unwanted preinstalled software. Spyware more broadly collects information about the user.

## d2-pwattack-1
type: single
topic: 2.4
group: password-attacks

A SIEM (Security Information and Event Management) shows one IP (Internet Protocol) trying the password "Winter2026!" once against 800 different accounts within an hour. What attack is this?

### Options
- [ ] Brute force
  why: Brute force tries many passwords against one account.
- [x] Password spraying
- [ ] Credential stuffing
  why: Credential stuffing uses leaked username and password pairs. Here one password is tried everywhere.
- [ ] Pass-the-hash
  why: Pass-the-hash reuses NTLM (New Technology LAN (Local Area Network) Manager) hashes, not plain passwords.

### Explanation
Password spraying tries a few common passwords across many accounts, staying under the lockout threshold for each account.

## d2-pwattack-3
type: single
topic: 2.4
group: password-attacks

Why does an account lockout policy of 5 failed attempts do little to stop password spraying?

### Options
- [ ] Spraying uses stolen hashes instead of passwords
  why: Spraying uses plain password guesses. That describes pass-the-hash.
- [x] Spraying tries only one or two passwords per account
- [ ] Spraying only works against service accounts with no MFA (Multifactor Authentication)
  why: Spraying targets any accounts it can enumerate.
- [ ] Spraying bypasses the login page entirely
  why: Spraying goes through the normal login page.

### Explanation
Spraying deliberately stays under the lockout threshold for each account. The defenses are MFA, banned-password lists, and monitoring for many failures across many accounts.

## d2-onpath-1
type: single
topic: 2.4
group: on-path-downgrade

An attacker on a coffee shop's Wi-Fi uses ARP (Address Resolution Protocol) poisoning so victims' traffic passes through the attacker's laptop before reaching the router. What attack is this?

### Options
- [x] On-path attack
- [ ] Replay attack
  why: Replay resends captured traffic later. Here the attacker sits in the live traffic flow.
- [ ] DNS (Domain Name System) poisoning
  why: DNS poisoning changes name resolution. ARP poisoning targets local MAC (Media Access Control) addresses.
- [ ] Evil twin
  why: An evil twin is a fake access point. Here the attacker is on the real network.

### Explanation
An on-path attack (formerly man-in-the-middle) puts the attacker between two parties so they can read or change traffic. ARP poisoning is a common way to do it.

## d2-onpath-3
type: single
topic: 2.4
group: on-path-downgrade

An attacker captures a valid authentication token from a user's session and resends it later to log in as that user. What attack is this?

### Options
- [ ] Downgrade attack
  why: Nothing forces a weaker protocol.
- [x] Replay attack
- [ ] Password spraying
  why: No passwords are guessed.
- [ ] Birthday attack
  why: Birthday attacks look for hash collisions.

### Explanation
A replay attack resends valid captured data. Timestamps, nonces and short token lifetimes defend against it.

## d2-ddos-1
type: single
topic: 2.4
group: ddos-types

An attacker sends small DNS (Domain Name System) queries with the victim's IP (Internet Protocol) as the spoofed source to thousands of open resolvers. Each resolver sends a much larger response to the victim. What attack is this?

### Options
- [x] Amplified DDoS (Distributed Denial of Service)
- [ ] DNS poisoning of the open resolvers
  why: DNS poisoning corrupts DNS records. Here the attacker floods the victim with responses.
- [ ] On-path attack against the victim
  why: The attacker isn't sitting in the traffic flow.
- [ ] Domain hijacking of the victim's domain
  why: Domain hijacking takes over a domain registration.

### Explanation
An amplified (and reflected) DDoS uses small requests that trigger large responses from third-party servers, all sent to the spoofed victim.

## d2-ddos-3
type: multi
topic: 2.4
group: ddos-types

Which TWO are indicators of a DDoS (Distributed Denial of Service) attack rather than a normal traffic spike?

### Options
- [x] Massive traffic from thousands of addresses that aren't customers
- [x] A flood of unrequested DNS (Domain Name System) responses
- [ ] Logins from a single user in two countries an hour apart
  why: That's impossible travel, an indicator of compromised credentials.
- [ ] Gaps in the server's logs
  why: Missing logs suggest log tampering.
- [ ] A user account locked after many failed logins
  why: That suggests password guessing.

### Explanation
DDoS indicators include huge volume from many unrelated sources and unsolicited or repetitive traffic patterns.

## d2-ioc-1
type: single
topic: 2.4
group: indicators-of-compromise

A user's account logs in from Salt Lake City at 9:00 a.m. and from Singapore at 9:30 a.m. What indicator is this?

### Options
- [x] Impossible travel
- [ ] Resource consumption
  why: Resource consumption is unusual CPU (Central Processing Unit), memory or bandwidth use.
- [ ] Concurrent session usage
  why: Close, but the specific indicator for distance and time that can't physically be covered is impossible travel.
- [ ] Blocked content
  why: Blocked content means a filter stopped something.

### Explanation
Impossible travel means logins from locations too far apart for the time between them. It usually means stolen credentials.

## d2-ioc-3
type: multi
topic: 2.4
group: indicators-of-compromise

Which TWO are indicators of malicious activity listed in SY0-701?

### Options
- [x] Account lockout
- [x] Out-of-cycle logging
- [ ] Certificate pinning
  why: Pinning is a defensive control.
- [ ] Code signing
  why: Code signing is a defensive control.
- [ ] Data masking
  why: Data masking is a defensive control.

### Explanation
SY0-701 indicators include account lockout, concurrent session use, blocked content, impossible travel, resource consumption and inaccessibility, out-of-cycle logging, and missing logs.

## d2-ioc-4
type: match
topic: 2.4
group: indicators-of-compromise

Match each observation to the indicator of malicious activity.

### Match
- Users can't open their files, which now have a strange new extension => Resource inaccessibility
- The company's customer database is offered for sale on a leak site => Published/documented
- A server's CPU (Central Processing Unit) sits at 100% all night with no scheduled jobs => Resource consumption
- One account is signed in on two workstations in different buildings at the same time => Concurrent session usage

### Distractors
- Impossible travel: Impossible travel is sign-ins from places too far apart to travel between in the time given. Two nearby buildings at once is concurrent use.

### Explanation
SY0-701 indicators include account lockout, concurrent session usage, blocked content, impossible travel, resource consumption, resource inaccessibility, out-of-cycle logging, published/documented and missing logs.

## d2-dirtrav-1
type: single
topic: 2.4
group: directory-traversal

A web server's access log contains the entry in the exhibit. Which attack was attempted?

### Exhibit
```text
198.51.100.23 - - [12/Mar/2026:04:11:52 +0000] "GET /download?file=../../../../etc/passwd HTTP/1.1" 200 1843
```

### Options
- [x] Directory traversal
- [ ] SQL (Structured Query Language) injection
  why: SQL injection would show database syntax such as `' OR 1=1 --` or `UNION SELECT` in the parameter.
- [ ] Cross-site scripting
  why: XSS (Cross-Site Scripting) would show script content such as `<script>` tags in the request.
- [ ] Command injection
  why: Command injection would show shell characters such as `;` or `|` followed by a command.

### Explanation
Repeated `../` sequences climb out of the web root to reach a file the app was never meant to serve. The 200 status and a non-trivial response size suggest it worked.

## d2-dirtrav-pbq
type: pbq
topic: 2.4
group: directory-traversal

You're reviewing the access log of an internal reporting web app after a data-loss alert. Review the exhibit and answer each part.

### Exhibit
```text
203.0.113.77 - - [14/Sep/2026:01:02:11 +0000] "GET /reports/view?doc=q3.pdf HTTP/1.1" 200 48211
203.0.113.77 - - [14/Sep/2026:01:02:19 +0000] "GET /reports/view?doc=../q3.pdf HTTP/1.1" 404 512
203.0.113.77 - - [14/Sep/2026:01:02:26 +0000] "GET /reports/view?doc=../../../etc/hosts HTTP/1.1" 403 498
203.0.113.77 - - [14/Sep/2026:01:02:34 +0000] "GET /reports/view?doc=..%2F..%2F..%2Fetc%2Fshadow HTTP/1.1" 200 1377
192.0.2.14 - - [14/Sep/2026:01:02:40 +0000] "GET /reports/view?doc=q2.pdf HTTP/1.1" 200 39120
```

### Explanation
One client probed the `doc` parameter, got blocked when it used plain `../`, then succeeded by encoding the slashes. The filter only matched the literal string, and the web service account was able to read a sensitive system file.

## d2-dirtrav-pbq/a
type: single

The third request was blocked but the fourth succeeded. What is the MOST likely reason?

### Options
- [x] Encoded slashes slipped past the filter
- [ ] The attacker switched to a different source address
  why: Both requests come from 203.0.113.77.
- [ ] A stolen session cookie was replayed on the fourth try
  why: Nothing in the log shows a change in authentication between the two requests.
- [ ] The server stopped validating after repeated errors
  why: The fifth request from another client is handled normally, and nothing suggests validation was switched off.

## d2-dirtrav-pbq/d
type: multi

Which TWO changes would BEST prevent this attack from succeeding again?

### Options
- [x] Resolve the full path, then confirm it's inside the reports folder
- [x] Accept a document ID (Identifier) and look up the file name server-side
- [ ] Block 203.0.113.77 at the perimeter firewall
  why: That stops one source. The flaw is still there for the next one.
- [ ] Strip every "../" from the parameter in a single pass before using it
  why: That's the kind of filter that just failed. Encoding or nesting (`....//`) gets around it.
- [ ] Rate-limit requests to the reports endpoint
  why: The attack took four requests. Rate limiting wouldn't notice it.

## d2-physattack-1
type: single
topic: 2.4
group: physical-attacks

An attacker stands near employees in a coffee line with a concealed reader, then later opens the office door with a copy of an employee's badge. What attack is this?

### Options
- [x] RFID (Radio-Frequency Identification) cloning
- [ ] Tailgating behind an employee at the door
  why: Tailgating is following someone through a door. Here the attacker opened the door with a copied badge.
- [ ] Bluesnarfing the employee's phone
  why: Bluesnarfing steals data over Bluetooth. Badges use radio frequency identification.
- [ ] Brute forcing the door's keypad
  why: Brute force tries many combinations. The attacker copied a valid credential.

### Explanation
RFID cloning reads a proximity badge from a short distance and writes its data to a blank card. Badges with encryption and mutual authentication, plus a second factor such as a PIN (Personal Identification Number), defend against it.

## d2-physattack-2
type: single
topic: 2.4
group: physical-attacks

An intruder disables a server room's cooling by tampering with the HVAC (Heating, Ventilation, and Air Conditioning) unit outside the building. Servers overheat and shut down. Which category of attack is this?

### Options
- [ ] Brute force
  why: Physical brute force means forcing through a door or lock. The attacker went after the climate system.
- [ ] RFID (Radio-Frequency Identification) cloning
  why: No badge was copied.
- [x] Environmental
- [ ] Denial of service through an amplified DDoS (Distributed Denial of Service)
  why: A DDoS uses network traffic. This attack was physical.

### Explanation
Environmental attacks target the conditions systems need, such as power, cooling and fire suppression. Protecting and monitoring HVAC and power equipment is part of physical security.

## d2-wireless-1
type: single
topic: 2.4
group: wireless-attacks

A user connects to "Airport_Free_WiFi". It has the same name as the real network, but it's broadcast by an attacker's laptop that captures everything the user sends. What attack is this?

### Options
- [x] Evil twin
- [ ] Deauthentication attack
  why: Deauthentication kicks clients off a network. It's often used alongside this attack, but it isn't the fake access point itself.
- [ ] ARP (Address Resolution Protocol) poisoning
  why: ARP poisoning works on a wired or wireless LAN (Local Area Network) the attacker has already joined. Here the attacker built the network.
- [ ] Bluejacking
  why: Bluejacking sends unsolicited messages over Bluetooth.

### Explanation
An evil twin is a rogue access point that imitates a legitimate SSID (Service Set Identifier). Users who connect send their traffic through the attacker. Enterprise authentication and VPNs (Virtual Private Networks) reduce the risk.

## d2-wireless-2
type: single
topic: 2.4
group: wireless-attacks

A wireless intrusion system logs a flood of forged management frames that keep disconnecting clients from the corporate access point. Shortly after, the clients reconnect to a different access point. What did the attacker MOST likely do first?

### Options
- [ ] An amplified DDoS (Distributed Denial of Service) on the internet link
  why: That would flood the internet connection, not disconnect clients from the access point.
- [x] A deauthentication attack
- [ ] A downgrade attack against TLS (Transport Layer Security)
  why: A downgrade attack forces weaker encryption on a connection. These frames are wireless management frames.
- [ ] RFID (Radio-Frequency Identification) cloning
  why: RFID cloning copies access badges.

### Explanation
Deauthentication frames force clients off an access point so the attacker can capture handshakes or push them onto an evil twin. WPA3 (Wi-Fi Protected Access 3) and protected management frames reduce this risk.

## d2-dns-attack-1
type: single
topic: 2.4
group: dns-attacks

Users type the bank's correct address, but they land on a fake site. Investigation shows the company's DNS (Domain Name System) resolver cached a forged record that points the bank's name to the attacker's IP (Internet Protocol). What attack is this?

### Options
- [ ] Typosquatting
  why: Typosquatting needs users to mistype the name. These users typed it correctly.
- [x] DNS poisoning
- [ ] Domain hijacking
  why: Domain hijacking takes over the domain's registration. Here only a cached record on one resolver was forged.
- [ ] Amplified DDoS (Distributed Denial of Service)
  why: An amplified DDoS floods a victim with traffic. It doesn't redirect users.

### Explanation
DNS poisoning inserts false records into a resolver's cache so correct names resolve to the wrong address. DNSSEC (Domain Name System Security Extensions) lets resolvers verify that answers really came from the domain's owner.

## d2-dns-attack-2
type: single
topic: 2.4
group: dns-attacks

An attacker phishes a company's domain registrar login and changes the domain's name servers to ones the attacker controls. All of the company's web and email traffic is now redirected. What is this?

### Options
- [x] Domain hijacking
- [ ] DNS (Domain Name System) cache poisoning
  why: Poisoning forges cached answers on a resolver. Here the official registration itself was changed.
- [ ] Typosquatting
  why: Typosquatting uses a different, look-alike domain. This is the company's real domain.
- [ ] On-path attack
  why: The attacker isn't intercepting live traffic between two parties. They changed the domain's settings.

### Explanation
Domain hijacking takes control of a domain's registration, so the attacker controls where all of its traffic goes. Registrar MFA (Multifactor Authentication) and registry locks are the main defenses.

## d2-forgery-1
type: single
topic: 2.4
group: request-forgery

A user is logged in to their bank in one tab. In another tab they open a malicious page that silently submits a funds transfer form to the bank. The browser includes the user's session cookie, and the transfer goes through. What attack is this?

### Options
- [ ] Server-side request forgery
  why: SSRF (Server-Side Request Forgery) tricks the server into making requests. Here the victim's browser made the request.
- [x] Cross-site request forgery
- [ ] Stored cross-site scripting
  why: XSS (Cross-Site Scripting) injects a script into the bank's own pages. The malicious form was on a different site.
- [ ] Replay attack
  why: Replay resends captured traffic. Nothing was captured; the browser made a new request.

### Explanation
CSRF (Cross-Site Request Forgery) abuses the trust a site has in the user's browser. Anti-CSRF tokens and SameSite cookies stop the forged request from being accepted.

## d2-forgery-2
type: single
topic: 2.4
group: request-forgery

A web app fetches images from any URL (Uniform Resource Locator) a user submits. An attacker submits an internal address, and the server returns data from the cloud provider's internal metadata service. What attack is this?

### Options
- [x] Server-side request forgery
- [ ] Cross-site request forgery
  why: CSRF (Cross-Site Request Forgery) makes the victim's browser send a request. Here the server itself made the request.
- [ ] Directory traversal
  why: Directory traversal reads files through ../ paths. This reached an internal network address.
- [ ] DNS (Domain Name System) poisoning
  why: Nothing changed name resolution. The attacker supplied the address directly.

### Explanation
SSRF (Server-Side Request Forgery) tricks a server into making requests on the attacker's behalf, often to internal services the attacker can't reach directly. Allow lists of permitted destinations are the main fix.

## d2-privesc-1
type: single
topic: 2.4
group: privilege-escalation

An attacker logs in with a stolen help desk account, exploits an unpatched service running as SYSTEM, and creates a new domain administrator account. What did the attacker achieve with the exploit?

### Options
- [x] Privilege escalation
- [ ] Lateral movement
  why: Lateral movement is moving to other systems with similar access. The attacker gained higher rights.
- [ ] Credential replay
  why: Replay reuses captured credentials. The exploit itself gave the attacker new rights.
- [ ] Directory traversal
  why: Directory traversal reads files outside the web root. Nothing here involves web paths.

### Explanation
Privilege escalation turns limited access into higher rights, such as admin or SYSTEM. Patching, least privilege, and running services with minimal rights reduce it.

## d2-privesc-2
type: single
topic: 2.4
group: privilege-escalation

Which control MOST directly limits the damage if an attacker exploits a vulnerable web application to run commands on the server?

### Options
- [ ] A longer key on the site's TLS (Transport Layer Security) certificate
  why: Certificate strength protects traffic in transit. It does nothing once commands run on the server.
- [x] Running the application under a low-privilege account
- [ ] A stricter password policy for website users
  why: User passwords don't limit what an exploited server process can do.
- [ ] A CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) on the login page
  why: A CAPTCHA slows bots. It doesn't limit the rights of the server process.

### Explanation
Commands run with the rights of the exploited process. A low-privilege service account forces the attacker to find a separate privilege escalation before doing serious damage.

## d2-cryptoattack-1
type: single
topic: 2.4
group: crypto-attacks

An on-path attacker interferes with a TLS (Transport Layer Security) handshake so that the client and server agree on an old, weak protocol version the attacker can break. What attack is this?

### Options
- [x] Downgrade attack
- [ ] Birthday attack
  why: A birthday attack looks for two inputs with the same hash. It doesn't change the negotiated protocol.
- [ ] Replay attack
  why: Replay resends captured traffic. Here the attacker changed what was negotiated.
- [ ] Password spraying
  why: No passwords are being guessed.

### Explanation
A downgrade attack forces a connection onto a weaker protocol or cipher. Disabling old versions on the server removes the weak option entirely.

## d2-cryptoattack-2
type: single
topic: 2.4
group: crypto-attacks

An attacker generates millions of document variants until two of them, one harmless and one fraudulent, produce the same hash. The harmless one gets signed, and the signature now also fits the fraudulent one. What attack is this?

### Options
- [ ] Downgrade attack
  why: No protocol version was forced lower.
- [ ] Pass-the-hash
  why: Pass-the-hash reuses a stolen password hash to log in.
- [x] Birthday (collision) attack
- [ ] Rainbow table attack
  why: Rainbow tables reverse password hashes with precomputed values. This finds two inputs with the same hash.

### Explanation
A birthday attack exploits the math that makes collisions far more likely than intuition suggests. Longer hash outputs, such as SHA-256 (Secure Hash Algorithm, 256-bit) instead of MD5 (Message Digest 5), make collisions impractical.

## d2-mitigate-1
type: single
topic: 2.5
group: mitigation-techniques

A company wants to make sure that only approved software can run on its kiosks. Which mitigation is MOST effective?

### Options
- [ ] Antivirus with signature updates
  why: Antivirus blocks known bad software. Anything new and unknown still runs.
- [x] Application allow list
- [ ] Host-based firewall
  why: A firewall controls network traffic, not which programs can run.
- [ ] Full-disk encryption
  why: Encryption protects data at rest.

### Explanation
An application allow list blocks everything that isn't explicitly approved, which is much stronger than trying to block known bad software.

## d2-mitigate-2
type: match
topic: 2.5
group: mitigation-techniques

Match each action to the mitigation technique.

### Match
- Moving IoT (Internet of Things) cameras onto their own VLAN (Virtual Local Area Network) => Segmentation
- Disconnecting an infected laptop from the network => Isolation
- Giving a help desk tech only the password reset permission => Least privilege
- Removing unused services and changing default passwords on a new server => Hardening

### Distractors
- Encryption: None of these protect data by making it unreadable.

### Explanation
Segmentation separates systems, isolation cuts off a compromised system, least privilege grants only the access needed, and hardening reduces a system's attack surface.

## d2-mitigate-3
type: single
topic: 2.5
group: mitigation-techniques

A company retires an old file server. Which step is part of proper decommissioning as a mitigation technique?

### Options
- [ ] Leaving it powered on in case it's needed again later
  why: A forgotten server stops getting patches and becomes an easy target.
- [x] Removing its accounts, firewall rules and name-server records
- [ ] Moving it to the guest wireless network
  why: That keeps an unmaintained server online and exposes it further.
- [ ] Disabling its antivirus to save resources
  why: That makes an unmaintained system even weaker.

### Explanation
Decommissioning removes a system completely: data is sanitized, and its accounts, firewall rules and DNS (Domain Name System) entries are cleaned up so nothing points to a forgotten, unpatched host.

## d2-hardening-1
type: multi
topic: 2.5
group: hardening

An administrator is hardening a new Windows server before it goes into production. Which TWO steps reduce its attack surface?

### Options
- [x] Disable ports and protocols the server doesn't need
- [x] Remove unnecessary software installed by default
- [ ] Turn off the host-based firewall to simplify troubleshooting
  why: Disabling the firewall increases exposure, which is the opposite of hardening.
- [ ] Keep the default administrator password for vendor support
  why: Default passwords are publicly known. Changing them is a basic hardening step.
- [ ] Give all users local administrator rights
  why: That violates least privilege and makes any compromise worse.

### Explanation
Hardening removes or locks down anything that isn't needed. SY0-701 lists encryption, endpoint protection, host-based firewalls, HIPS (Host-based Intrusion Prevention System), disabling ports and protocols, changing default passwords, and removing unnecessary software.

## d2-hardening-2
type: single
topic: 2.5
group: hardening

A laptop needs a control that watches for suspicious behavior on the device itself and blocks it in real time, such as a process trying to inject code into another process. Which hardening control fits BEST?

### Options
- [ ] Network-based IDS (Intrusion Detection System)
  why: A NIDS (Network-based Intrusion Detection System) watches network traffic and only alerts. It can't see or stop activity inside the laptop.
- [x] Host-based IPS (Intrusion Prevention System)
- [ ] Full-disk encryption
  why: FDE (Full-Disk Encryption) protects data if the laptop is stolen. It doesn't watch running processes.
- [ ] Web application firewall
  why: A WAF (Web Application Firewall) protects web applications from HTTP (Hypertext Transfer Protocol) attacks. It doesn't run on laptops.

### Explanation
A host-based intrusion prevention system runs on the endpoint, inspects local activity, and blocks malicious behavior. "On the device" plus "blocks" points to HIPS (Host-based Intrusion Prevention System) rather than a network sensor or a detect-only tool.

## d2-config-1
type: single
topic: 2.5
group: config-enforcement

Servers built from a company's secure baseline slowly drift as admins change settings by hand. Which mitigation technique automatically detects and resets settings that no longer match the baseline?

### Options
- [x] Configuration enforcement
- [ ] Decommissioning
  why: Decommissioning retires systems. These servers are still in service.
- [ ] Application allow listing
  why: Allow lists control which programs run, not system settings.
- [ ] Network segmentation
  why: Segmentation limits which systems can talk to each other. It doesn't fix settings.

### Explanation
Configuration enforcement uses tools such as Group Policy or configuration management to keep systems at their approved baseline and correct drift automatically.

## d2-config-2
type: single
topic: 2.5
group: config-enforcement

A file share holds payroll reports. Every employee can currently read it, but only three people in payroll need to. Which mitigation fixes this MOST directly?

### Options
- [x] Tightening the share's access control permissions
- [ ] Encrypting the share with the server's full-disk key
  why: Full-disk encryption protects a stolen drive. Signed-in users still read the files normally.
- [ ] Moving the share behind a host-based firewall rule
  why: A firewall controls network connections, not which users can open which files.
- [ ] Turning on monitoring alerts for every file opened
  why: Monitoring records access after it happens. It doesn't prevent it.

### Explanation
Access control in SY0-701 objective 2.5 means ACLs (Access Control Lists) and permissions: give each role only the access it needs, following least privilege.
