---
deck: Domain 1 – General Security Concepts
section: "1.0"
exam_weight: 12
topics:
  1.1: Compare and contrast various types of security controls
  1.2: Summarize fundamental security concepts
  1.3: Explain the importance of change management processes and the impact to security
  1.4: Explain the importance of using appropriate cryptographic solutions
---

## d1-ctrl-type-1
type: single
topic: 1.1
group: control-types

A legacy manufacturing controller can't receive security patches. The security team puts it on an isolated VLAN (Virtual Local Area Network) and adds extra monitoring on that segment. Which type of control does this BEST describe?

### Options
- [ ] Corrective
  why: Corrective controls fix or restore something after an incident, like restoring from backup. Nothing has gone wrong yet here.
- [x] Compensating
- [ ] Deterrent
  why: Deterrents discourage an attacker, like a warning banner. An isolated VLAN doesn't discourage anyone, it limits exposure.
- [ ] Directive
  why: Directive controls tell people what to do, like a policy. This is a technical workaround.

### Explanation
A compensating control stands in for a primary control that can't be used. The giveaway is "can't receive patches": patching is the normal control, so segmentation and monitoring are the substitute that reduces the same risk.

## d1-control-types-1
type: single
topic: 1.1
group: control-types

A retailer installs a system that reviews door badge logs every night and flags any entry made outside business hours for the security manager to look at the next morning. The system has no ability to stop an entry while it happens. Which type of control is this?

### Options
- [x] Detective
- [ ] Preventive
  why: A preventive control stops the event before it happens, like a locked door. This system only reports entries after the fact.
- [ ] Corrective
  why: A corrective control repairs damage after an incident, like restoring from backup. Flagging log entries doesn't fix anything.
- [ ] Compensating
  why: A compensating control stands in for a required control that can't be implemented. Nothing in the scenario says another control is missing.

### Explanation
Detective controls identify and record events that have already happened. The clues are "reviews logs", "flags", and the statement that it can't stop an entry in progress.

## d1-control-types-3
type: match
topic: 1.1
group: control-types

Match each control to its control type.

### Match
- Sign warning that the area is under video surveillance => Deterrent
- Restoring a server from backup after a ransomware infection => Corrective
- Door lock that only opens for an authorized badge => Preventive
- Acceptable use policy that every employee must sign => Directive
- Weekly review of firewall logs for past intrusions => Detective

### Distractors
- Compensating: A compensating control replaces a required control that can't be used. None of these is standing in for another control.
- Managerial: That's a control category (how it's implemented), not a type by function.

### Explanation
Deterrent discourages, preventive blocks, detective finds out afterward, corrective repairs, and directive tells people what to do. A sign doesn't physically stop anyone, which is why it's deterrent and not preventive.

## d1-ctrl-cat-1
type: single
topic: 1.1
group: control-categories

A security manager updates the company's risk assessment and requires quarterly access reviews. Which control category does this BEST fit?

### Options
- [ ] Operational
  why: Operational controls are carried out by people day to day, like guards or the help desk following a process. This is oversight and planning.
- [ ] Technical
  why: Technical controls are implemented by systems, like firewalls or encryption.
- [x] Managerial
- [ ] Physical
  why: Physical controls protect physical spaces, like locks and fences.

### Explanation
Managerial (administrative) controls focus on security design, planning and oversight: risk assessments, policies, and review requirements. The words "risk assessment" and "requires" point to management-level decisions.

## d1-ctrl-cat-2
type: match
topic: 1.1
group: control-categories

Match each control to its category.

### Match
- Full-disk encryption on laptops => Technical
- Security guard checking badges at the lobby => Operational
- Fencing around the data center parking lot => Physical
- Annual security risk assessment => Managerial

### Distractors
- Corrective: Corrective is a control type (what it does), not a category.
- Preventive: Preventive is a control type, not a category.

### Explanation
CompTIA's four categories describe how a control is implemented: technical (by systems), managerial (oversight and planning), operational (performed by people), physical (protects physical spaces).

## d1-cia-1
type: single
topic: 1.2
group: cia-triad

A hospital's patient portal goes offline for six hours during a DDoS (Distributed Denial of Service) attack. No data is stolen or changed. Which part of the CIA (Confidentiality, Integrity, and Availability) triad was affected?

### Options
- [ ] Confidentiality
  why: Confidentiality is about unauthorized disclosure. No data was exposed.
- [ ] Integrity
  why: Integrity is about unauthorized changes. No data was altered.
- [x] Availability
- [ ] Non-repudiation
  why: Non-repudiation proves who did something. It isn't part of the CIA triad and isn't relevant to an outage.

### Explanation
Availability means systems and data are accessible when needed. A DDoS that takes the portal offline is a direct hit to availability.

## d1-cia-3
type: single
topic: 1.2
group: cia-triad

An attacker on the network changes the destination account number in a wire transfer request while it's in transit. Which security goal was violated?

### Options
- [x] Integrity
- [ ] Availability
  why: The transfer still went through, so the system stayed available.
- [ ] Confidentiality
  why: The attacker may have seen the data, but the harm described is that it was changed.
- [ ] Authentication
  why: Nothing here involves proving identity at login.

### Explanation
Integrity means data isn't altered without authorization. Changing the account number in transit is an integrity violation. Hashing and digital signatures are the usual integrity controls.

## d1-zt-2
type: match
topic: 1.2
group: zero-trust

Match each Zero Trust component to the plane it belongs to.

### Match
- Policy engine => Control plane
- Policy administrator => Control plane
- Policy enforcement point => Data plane
- Subject requesting access => Data plane

### Distractors
- Management plane: Not one of the two Zero Trust planes CompTIA uses. SY0-701 splits Zero Trust into control and data planes.

### Explanation
The control plane makes decisions (policy engine and policy administrator). The data plane is where subjects, systems and the enforcement point handle the actual traffic.

## d1-zt-planes-1
type: single
topic: 1.2
group: zero-trust

In a zero trust architecture, a user requests access to a payroll application. One component evaluates the user's identity, the device's health, and current threat intelligence, then makes the decision to grant or deny. Which component is this?

### Options
- [x] Policy engine
- [ ] Policy administrator
  why: The administrator carries out the decision by telling the enforcement point to open or close the session. It doesn't make the decision.
- [ ] Policy enforcement point
  why: The PEP (Policy Enforcement Point) sits in the data plane and allows or blocks the traffic based on what the control plane tells it.
- [ ] Implicit trust zone
  why: That's the area behind the enforcement point where the resource lives. It isn't a decision-making component.

### Explanation
The policy engine is the control plane component that makes the grant/deny decision. "Evaluates" and "makes the decision" point to it; carrying out the decision belongs to the policy administrator and the PEP.

## d1-zt-planes-3
type: multi
topic: 1.2
group: zero-trust

Which TWO components together make up the policy decision point in the control plane of a zero trust architecture?

### Options
- [x] Policy engine
- [x] Policy administrator
- [ ] Policy enforcement point
  why: The PEP (Policy Enforcement Point) is in the data plane. It enforces decisions; it isn't part of the decision point.
- [ ] Subject/system
  why: That's the user or device requesting access, which lives in the data plane.
- [ ] Implicit trust zone
  why: That's the protected area behind the PEP, not a control plane component.

### Explanation
The policy decision point is the policy engine (decides) plus the policy administrator (issues the session commands). Everything the traffic touches (subject, PEP, trust zone) is data plane.

## d1-deception-1
type: single
topic: 1.2
group: deception-tech

A security team creates a fake AWS (Amazon Web Services) access key and plants it in a code repository. If the key is ever used, an alert fires. What is this called?

### Options
- [ ] Honeypot
  why: A honeypot is an entire fake system that attracts attackers. This is a single piece of fake data.
- [ ] Honeyfile
  why: A honeyfile is a fake file (like "passwords.xlsx"). This is a credential, not a file.
- [x] Honeytoken
- [ ] Honeynet
  why: A honeynet is a network of honeypots.

### Explanation
A honeytoken is fake data, such as a credential, API (Application Programming Interface) key or database record, that has no legitimate use. Any use of it means someone is where they shouldn't be.

## d1-deception-2
type: match
topic: 1.2
group: deception-tech

Match each deception technology to its description.

### Match
- A fake server running vulnerable services to attract attackers => Honeypot
- Several fake servers and workstations on their own subnet => Honeynet
- A document named "Salaries_2026.xlsx" with an access alert => Honeyfile
- A fake customer record in a database that triggers an alert when queried => Honeytoken

### Distractors
- Sinkhole: DNS (Domain Name System) sinkholing redirects malicious traffic to a controlled address. It's a related defense, but it isn't a decoy object.

### Explanation
The four "honey" terms scale from a single piece of data (honeytoken) to a file (honeyfile) to a system (honeypot) to a whole network (honeynet).

## d1-nonrep-1
type: single
topic: 1.2
group: non-repudiation

A purchasing manager approves a $40,000 order in the company's procurement system and later claims he never approved it. The system digitally signs every approval with the approver's private key. Which security concept lets the company prove he made the approval?

### Options
- [x] Non-repudiation
- [ ] Data confidentiality
  why: Confidentiality keeps data secret from unauthorized people. It says nothing about who performed an action.
- [ ] Authorization
  why: Authorization determines what he's allowed to do. It doesn't prove afterward that he did it.
- [ ] Availability
  why: Availability means systems are up when needed. It isn't about proof of an action.

### Explanation
Non-repudiation means someone can't credibly deny an action. The signature made with a private key only he holds, combined with "later claims he never approved it", is the textbook setup.

## d1-nonrep-3
type: single
topic: 1.2
group: non-repudiation

Two companies authenticate the messages they exchange with an HMAC (Hash-based Message Authentication Code) built from a secret key that both of them hold. An auditor says this arrangement can't provide non-repudiation. Why is the auditor correct?

### Options
- [x] Either company could have produced that exact tag
- [ ] An HMAC can't detect changes to a message
  why: It can. Detecting changes (integrity) is exactly what an HMAC provides.
- [ ] The secret key travels inside each message
  why: The key is never sent. Only the resulting tag accompanies the message.
- [ ] Hash functions can be reversed to forge a tag
  why: Cryptographic hashes are one-way. Forging a tag requires the key, not reversing the hash.

### Explanation
Non-repudiation needs something only one party could have created, which means an asymmetric private key. With a shared secret, either side could have generated the tag, so neither can prove the other did.

## d1-aaa-1
type: single
topic: 1.2
group: aaa

A user logs in to the company VPN (Virtual Private Network) with a password and a hardware token. The VPN server then records the session start time, the user's source address, and how much data the session transferred. Which security function does that record serve?

### Options
- [ ] Authentication
  why: Authentication happened at login, when the password and token proved the user's identity. Recording the session afterward is a separate function.
- [ ] Authorization
  why: Authorization decides what the user is allowed to reach once connected. Logging usage doesn't grant or deny anything.
- [x] Accounting
- [ ] Attestation
  why: Attestation is a formal statement that something is true, like a device proving its configuration. It isn't usage logging.

### Explanation
Accounting tracks what an identity did: when it connected, from where, for how long, and what it used. Authentication proves who you are, authorization decides what you may do, and accounting records what you did.

## d1-aaa-2
type: match
topic: 1.2
group: aaa

Match each event to the function it performs.

### Match
- A server presents a certificate so a client can confirm which machine it is talking to => Authenticating systems
- An employee scans a fingerprint to unlock a workstation => Authenticating people
- A role grants the help desk read-only access to the ticketing database => Authorization
- A RADIUS (Remote Authentication Dial-In User Service) server logs every login and logout with timestamps => Accounting

### Distractors
- Non-repudiation: Non-repudiation is proof that someone can't deny an action, usually from a digital signature. None of these events produce that proof.
- Availability: Availability keeps systems reachable. None of these events is about uptime.

### Explanation
SY0-701 splits authentication into people (passwords, biometrics) and systems (certificates, device identities). Authorization models such as roles decide access, and accounting keeps the record.

## d1-aaa-3
type: single
topic: 1.2
group: aaa

Before an IoT (Internet of Things) sensor can join a factory network, the network checks a certificate that was installed on the sensor at the factory. No person types anything. What is happening?

### Options
- [x] Authenticating a system
- [ ] Authenticating a user
  why: No user is involved. The identity being proven belongs to the device.
- [ ] Accounting for the session
  why: Accounting records what happened after access is granted. This step proves identity first.
- [ ] Authorizing the sensor's access
  why: Authorization decides what an identity may do. This step proves which device it is.

### Explanation
SY0-701 splits authentication into authenticating people and authenticating systems. Devices and services prove their identity with certificates or keys instead of passwords, often as part of port-based network access control.

## d1-gap-analysis-1
type: single
topic: 1.2
group: gap-analysis

A company wants to align with a well-known security framework. A consultant documents which framework controls the company already has, which ones it is missing, and what it would take to close each difference. What is the consultant performing?

### Options
- [x] Gap analysis
- [ ] Penetration test
  why: A penetration test actively exploits weaknesses to prove they're real. It doesn't compare the organization against a framework.
- [ ] Business impact analysis
  why: A BIA (Business Impact Analysis) identifies critical processes and the effect of losing them. It doesn't measure control coverage.
- [ ] Vulnerability scan
  why: A scan looks for technical flaws on systems. It doesn't compare policies and controls against a framework.

### Explanation
A gap analysis compares the current state with a desired state, such as a framework or standard, and lists the differences and the work needed to close them.

## d1-gap-analysis-2
type: single
topic: 1.2
group: gap-analysis

A newly hired security director wants a roadmap for the next two years. Which step should come FIRST to show where the security program falls short?

### Options
- [ ] Buying the controls the board asked about
  why: Purchasing before measuring risks spending on the wrong things. You need to know what's missing first.
- [ ] Running a phishing simulation
  why: That measures one behavior. It doesn't show how the whole program compares with the target.
- [x] Comparing current controls to the target state
- [ ] Writing a new acceptable use policy
  why: A policy may be one of the fixes, but you don't know which fixes are needed until you've measured the shortfall.

### Explanation
Comparing the current state to a target (a framework, a regulation, or the organization's own goals) is a gap analysis. Its output is the list of shortfalls that becomes the roadmap.

## d1-physical-1
type: single
topic: 1.2
group: physical-security

A data center has a problem with tailgating: unauthorized visitors follow employees through the badge door. Management wants an entry that only lets one person through at a time, with a second door that won't open until the first one closes. What should be installed?

### Options
- [ ] Bollards
  why: Bollards are short posts that stop vehicles from ramming a building. They don't control people walking in.
- [x] Access control vestibule
- [ ] Video surveillance
  why: Cameras record tailgating so it can be investigated, but they don't physically stop it.
- [ ] Fencing
  why: Fencing secures a perimeter. It doesn't control who follows whom through a single door.

### Explanation
An access control vestibule (formerly called a mantrap) uses two interlocking doors so only one person passes at a time. It's the standard physical control against tailgating and piggybacking.

## d1-physical-2
type: match
topic: 1.2
group: physical-security

Match each physical security need to the BEST control.

### Match
- Stop a vehicle from being driven into the front lobby => Bollards
- Detect body heat moving through a dark warehouse => Infrared sensor
- Detect someone stepping on a mat in front of a vault => Pressure sensor
- Discourage loitering in a parking lot at night => Lighting

### Distractors
- Access badge: Badges control who opens a door. None of these needs is about door access.
- Ultrasonic sensor: Ultrasonic sensors detect motion with sound waves. Heat and weight are better matches for the needs listed.

### Explanation
Bollards are anti-vehicle barriers. Infrared sensors detect heat signatures, pressure sensors detect weight, microwave and ultrasonic sensors detect motion, and lighting is a deterrent that also helps cameras.

## d1-physical-3
type: single
topic: 1.2
group: physical-security

A remote substation has no staff on site. The security team wants a physical control that can make decisions, respond to an unexpected situation, and question a visitor. Which control provides this?

### Options
- [ ] Video surveillance
  why: Cameras record and can alert, but they can't make judgment calls or talk to an intruder on their own.
- [ ] Microwave motion sensor
  why: A sensor detects motion. It can't evaluate the situation or respond.
- [x] Security guard
- [ ] Access badge reader
  why: A badge reader allows or denies a door. It can't respond to anything outside that.

### Explanation
Guards bring human judgment: they can assess unusual situations, verify identities, and respond. That's why SY0-701 lists guards separately from the passive physical controls.

## d1-ztprinciple-1
type: single
topic: 1.2
group: zero-trust-principles

A user normally signs in from Denver on a managed company laptop. One morning the same account signs in from an unknown personal device in another country, and the zero trust system demands extra verification before granting anything. Which Zero Trust control plane concept is this?

### Options
- [x] Adaptive identity
- [ ] Threat scope reduction
  why: Threat scope reduction limits what an attacker can reach, for example with least privilege and segmentation. It doesn't change how a login is checked.
- [ ] Implicit trust zone
  why: An implicit trust zone is the data plane area behind the enforcement point. It doesn't judge sign-ins.
- [ ] Policy enforcement point
  why: The PEP (Policy Enforcement Point) only carries out decisions in the data plane. It doesn't weigh the context of a request.

### Explanation
Adaptive identity uses context such as location, device health and normal behavior to decide how much verification a request needs. SY0-701 lists it as a control plane concept with threat scope reduction and policy-driven access control.

## d1-ztprinciple-2
type: match
topic: 1.2
group: zero-trust-principles

Match each zero trust practice to the control plane concept it represents.

### Match
- Central rules weigh the user's role, device posture and data sensitivity before allowing a request => Policy-driven access control
- Each user can reach only the few applications their job needs, so a stolen account gets very little => Threat scope reduction
- A sign-in from a new device in an unusual location triggers extra verification => Adaptive identity

### Distractors
- Implicit trust zone: This is the data plane area behind the enforcement point. Zero trust tries to shrink it, and none of these practices describe it.

### Explanation
The SY0-701 Zero Trust control plane covers adaptive identity, threat scope reduction and policy-driven access control, carried out by the policy engine and policy administrator.

## d1-change-1
type: single
topic: 1.3
group: change-management

A team is about to upgrade the firmware on the core switches. The change board asks how the team will return the switches to their previous state if the upgrade fails. What is the board asking for?

### Options
- [ ] Impact analysis
  why: Impact analysis estimates what the change could affect. It doesn't describe how to undo it.
- [x] Backout plan
- [ ] Test results
  why: Test results show whether the change worked in a test environment, not how to reverse it.
- [ ] Maintenance window
  why: The maintenance window is when the change happens, not how to undo it.

### Explanation
A backout (rollback) plan describes how to undo a change and return to the last known good state if something goes wrong.

## d1-change-2
type: order
topic: 1.3
group: change-management

Put these change management steps in the order they normally happen.

### Order
1. Submit the change request
   why: The process starts with a documented request.
2. Perform an impact analysis
   why: The impact must be understood before anyone approves the change.
3. Obtain approval from the change advisory board
   why: Approval comes after the risks are known.
4. Implement during the maintenance window
   why: Changes go in during scheduled downtime to limit disruption.
5. Document the change and update diagrams
   why: Documentation and diagram updates close out the change.

### Explanation
Request, analyze, approve, implement, document. Approval depends on the impact analysis, and documentation happens after the change is in place.

## d1-change-3
type: multi
topic: 1.3
group: change-management

A change to a web server's TLS (Transport Layer Security) settings requires the application service to restart. Which TWO technical concerns should the change plan address?

### Options
- [x] Scheduling downtime for the restart
- [x] Identifying dependent applications that may break
- [ ] Selecting a risk transfer strategy for the web server
  why: Risk transfer (like insurance) is a risk management decision, not a change implementation concern.
- [ ] Classifying the server's data
  why: Data classification matters for protection, but it isn't affected by a TLS settings change.
- [ ] Assigning a data custodian
  why: Custodian is a data governance role, unrelated to this change.

### Explanation
SY0-701 lists technical implications of change management, including downtime, service and application restarts, dependencies, legacy applications, and allow or deny lists.

## d1-change-biz-1
type: single
topic: 1.3
group: change-business-process

Before a change to the payroll system is approved, the change manager meets with HR (Human Resources), finance and the help desk to learn how the change will affect their work. What part of the change management process is this?

### Options
- [x] Identifying and consulting stakeholders
- [ ] Writing the backout plan
  why: A backout plan explains how to undo the change. It doesn't gather input from affected teams.
- [ ] Scheduling a maintenance window
  why: The maintenance window sets when the change happens, not who it affects.
- [ ] Assigning a risk owner in the risk register
  why: Risk owners belong to risk management. This step is about the people the change affects.

### Explanation
Stakeholders are the people and teams affected by a change. Change management consults them so the impact analysis and approval reflect how the business really uses the system.

## d1-change-biz-2
type: match
topic: 1.3
group: change-business-process

Match each change management element to its description.

### Match
- The one person accountable for the change and its outcome => Ownership
- The teams affected by the change, who must be informed or consulted => Stakeholders
- Approved step-by-step instructions that staff follow to make routine changes the same way every time => Standard operating procedure
- The CAB (Change Advisory Board) reviews the request and signs off before work begins => Approval process

### Distractors
- Impact analysis: Impact analysis estimates what a change could affect. None of these descriptions is that estimate.

### Explanation
SY0-701 lists the business processes behind change management: approval process, ownership, stakeholders, impact analysis, test results, backout plan, maintenance window and standard operating procedure.

## d1-change-doc-1
type: single
topic: 1.3
group: change-documentation

An administrator edits a router's configuration file, and the edit breaks routing. The team needs to see exactly which lines changed and restore the earlier copy. Which change management practice makes this possible?

### Options
- [x] Version control
- [ ] A maintenance window
  why: A maintenance window sets when changes happen. It doesn't keep earlier copies of the file.
- [ ] Stakeholder approval
  why: Approval decides whether a change happens. It doesn't keep a record of each edit.
- [ ] An application allow list
  why: Allow lists control what software may run, not the history of a configuration file.

### Explanation
Version control keeps every revision of code, scripts and configuration files, showing who changed what and when, and allowing a quick return to a known good version.

## d1-change-doc-2
type: single
topic: 1.3
group: change-documentation

During an approved change to replace a web server's certificate, an engineer notices an outdated plugin and updates it too, since the server is already down. Why does change management discourage this?

### Options
- [x] Work outside the approved scope is a restricted activity
- [ ] The plugin update must wait for the next risk assessment
  why: Risk assessments don't approve individual changes. The issue is that this work was never in the approved change.
- [ ] Plugins can only be updated by the data custodian
  why: Custodians manage data, not software updates.
- [ ] Certificates and plugins can't change in one window
  why: One window can hold several changes, as long as each one was requested and approved.

### Explanation
An approval covers only the work described in the change request. Extra work during the window is a restricted activity: it skipped impact analysis and testing, and it makes troubleshooting harder. After the change, update diagrams and policies/procedures so documentation matches reality.

## d1-crypto-symasym-1
type: single
topic: 1.4
group: symmetric-asymmetric

A company needs to encrypt 4 TB (terabytes) of backup data quickly each night. Which approach is MOST appropriate?

### Options
- [x] AES-256 (Advanced Encryption Standard, 256-bit key) symmetric encryption
- [ ] RSA-4096 (Rivest-Shamir-Adleman, 4096-bit key) asymmetric encryption
  why: Asymmetric encryption is far too slow for bulk data. It's used for key exchange and signatures.
- [ ] SHA-256 (Secure Hash Algorithm, 256-bit) hashing
  why: Hashing is one-way. You couldn't get the backups back.
- [ ] Elliptic curve digital signatures
  why: Signatures prove origin and integrity. They don't encrypt data.

### Explanation
Symmetric algorithms like AES (Advanced Encryption Standard) are fast and built for large amounts of data. Asymmetric algorithms are slower and are used to exchange the symmetric key or sign data.

## d1-keyuse-3
type: single
topic: 1.4
group: symmetric-asymmetric

A developer wants to send a file to a colleague so that only the colleague can read it. Using asymmetric encryption alone, which key encrypts the file?

### Options
- [x] The colleague's public key
- [ ] The colleague's private key
  why: The developer doesn't have it. The colleague uses it to decrypt.
- [ ] The developer's public key
  why: Then only the developer's private key could decrypt, so the colleague couldn't read the file.
- [ ] The developer's private key
  why: Anyone with the developer's public key could decrypt that. It gives proof of origin, not secrecy.

### Explanation
For confidentiality you encrypt with the recipient's public key, because only the recipient's private key can reverse it. "Only the colleague can read it" is the confidentiality cue.

## d1-crypto-symasym-3
type: single
topic: 1.4
group: key-exchange

During a TLS (Transport Layer Security) handshake, a client and server agree on a shared session key without ever sending that key across the network. Which technique makes this possible?

### Options
- [ ] Key stretching
  why: Key stretching strengthens weak passwords. It isn't used to exchange keys.
- [x] Diffie-Hellman key exchange
- [ ] Out-of-band key exchange
  why: Out-of-band means sending the key through a separate channel, like a phone call. Here it never gets sent at all.
- [ ] Key escrow
  why: Key escrow stores a copy of a key with a trusted third party.

### Explanation
Diffie-Hellman lets two parties derive the same secret over an untrusted network without transmitting it. That shared secret is then used for fast symmetric encryption.

## d1-key-exchange-2
type: single
topic: 1.4
group: key-exchange

Two offices need to start using a new symmetric key for an encrypted link. The security policy says the key must never travel over the same network the link protects. How should the key be delivered?

### Options
- [ ] Email it to the other office's administrator
  why: Email travels over the same network the policy is trying to protect against.
- [x] Deliver it through a separate, out-of-band channel
- [ ] Hash it before sending it over the link
  why: A hash can't be turned back into the key, so the other side couldn't use it.
- [ ] Put the key in the link's first packet
  why: That sends the key in-band, over the exact network the policy forbids.

### Explanation
Out-of-band key exchange sends the key through a different channel, such as a courier or a phone call. In-band exchange uses the same channel, which is why it's protected with techniques like Diffie-Hellman.

## d1-hash-1
type: single
topic: 1.4
group: hashing-salting

Two users chose the same password, but their stored password hashes look completely different. What causes this?

### Options
- [ ] Key stretching
  why: Key stretching slows down hashing. On its own it would still produce identical hashes for identical passwords.
- [x] Salting
- [ ] Encryption
  why: Passwords should be hashed, not encrypted. Encryption with the same key would also give identical output.
- [ ] Tokenization
  why: Tokenization replaces data with a random token. It isn't used for password storage.

### Explanation
A salt is a random value added to each password before hashing, so identical passwords produce different hashes. That defeats precomputed rainbow tables.

## d1-hash-3
type: multi
topic: 1.4
group: hashing-salting

A security analyst downloads an installer disk image and compares its SHA-256 (Secure Hash Algorithm, 256-bit) value with the one on the vendor's site. They match. Which TWO statements are true?

### Options
- [x] The file wasn't altered after the vendor hashed it
- [x] The same input always produces the same hash output
- [ ] The file is now encrypted
  why: Hashing doesn't encrypt anything. The file contents are unchanged and readable.
- [ ] The hash can be reversed to rebuild the original file
  why: Hashes are one-way functions. You can't recover the input.
- [ ] The match proves the vendor's website wasn't hacked
  why: If an attacker changed both the file and the posted hash, they'd still match. Only a digital signature proves origin.

### Explanation
Hashing provides integrity. Identical input gives identical output, so a match means the file is unchanged. It doesn't encrypt anything and can't be reversed.

## d1-hash-4
type: single
topic: 1.4
group: hashing-salting

A password database is protected with salted hashes, but the security team worries that a fast graphics card could still try billions of guesses per second. Which technique slows each guess down?

### Options
- [ ] Tokenization
  why: Tokenization replaces data with a random value from a vault. It isn't used for password storage.
- [ ] Steganography
  why: Steganography hides data inside other data. It doesn't slow down guessing.
- [x] Key stretching
- [ ] Data masking
  why: Masking hides part of a value from view. It doesn't make password hashes harder to crack.

### Explanation
Key stretching (for example PBKDF2 (Password-Based Key Derivation Function 2) or bcrypt) runs the hash many thousands of times, so each guess is expensive. Salting stops precomputed tables, and stretching slows brute force.

## d1-sig-3
type: order
topic: 1.4
group: digital-signatures

Put the steps for creating and checking a digital signature in order.

### Order
1. The sender hashes the message
   why: Signatures are made from the hash, not the full message.
2. The sender encrypts the hash with their private key
   why: Encrypting the hash with the private key creates the signature.
3. The recipient decrypts the signature with the sender's public key
   why: This recovers the hash the sender made.
4. The recipient hashes the received message
   why: The recipient makes their own hash of what arrived.
5. The recipient compares the two hashes
   why: A match proves integrity and origin.

### Explanation
Sign: hash, then encrypt the hash with the private key. Verify: decrypt the signature with the public key, hash the message yourself, and compare.

## d1-keyuse-1
type: single
topic: 1.4
group: digital-signatures

Dana needs to send a contract to Marcus so that Marcus can verify it really came from Dana and wasn't modified. Confidentiality is not required. Which key does Dana use to create the digital signature?

### Options
- [x] Dana's private key
- [ ] Dana's public key
  why: Her public key is what Marcus uses to verify. Anyone can have it, so it can't prove the contract came from her.
- [ ] Marcus's public key
  why: That key would encrypt the contract so only Marcus can read it. That's confidentiality, which isn't needed here.
- [ ] Marcus's private key
  why: Only Marcus has it. Dana can never use it.

### Explanation
Signatures are created with the signer's private key and verified with the signer's public key. The requirement is proof of origin and integrity, not secrecy, so the recipient's keys aren't involved.

## d1-cert-1
type: single
topic: 1.4
group: certificate-types

An organization needs one certificate that secures example.com, shop.example.net and mail.example.org. Which certificate type should it use?

### Options
- [ ] Wildcard certificate for one parent domain
  why: A wildcard covers subdomains of one domain (*.example.com). These are three different domains.
- [x] SAN (Subject Alternative Name) certificate
- [ ] Self-signed certificate
  why: Self-signed certificates aren't trusted by browsers and don't solve the multiple-domain problem.
- [ ] Root certificate
  why: A root certificate belongs to a CA (Certificate Authority) and signs other certificates. It doesn't secure a website.

### Explanation
A SAN (Subject Alternative Name) certificate lists multiple different names in one certificate.

## d1-cert-3
type: single
topic: 1.4
group: certificate-types

An administrator generates a key pair and sends a file containing the public key and the server's details to a certificate authority. What is this file?

### Options
- [ ] Certificate revocation list
  why: A CRL (Certificate Revocation List) lists revoked certificates. It's published by the CA (Certificate Authority), not sent to it.
- [ ] Root of trust
  why: Root of trust is the foundation the trust chain starts from, not a file you submit.
- [x] Certificate signing request
- [ ] OCSP (Online Certificate Status Protocol) response
  why: OCSP responses tell clients whether a certificate is revoked.

### Explanation
A CSR (Certificate Signing Request) contains the public key and identifying details. The CA validates it, signs it and returns a certificate. The private key never leaves the server.

## d1-pbq-cert-errors
type: pbq
topic: 1.4
group: certificate-types

A user reports a browser warning when visiting the company's internal HR (Human Resources) portal. Review the certificate details and answer each part.

### Exhibit
```text
Subject:         CN=hr.corp.example.com
Issuer:          CN=hr.corp.example.com
Valid from:      2025-02-01
Valid to:        2027-02-01
Subject Alt Name: DNS:hr.corp.example.com
Key:             RSA 2048
```

### Explanation
The subject and issuer are the same, so the certificate is self-signed. Browsers only trust certificates chained to a trusted CA (Certificate Authority). The fix is a certificate from the company's internal CA (with the CA's root deployed to devices) or a public CA.

## d1-pbq-cert-errors/a
type: single

Why does the browser show a warning?

### Options
- [x] The certificate is self-signed
- [ ] The certificate has expired
  why: It's valid until 2027.
- [ ] The key length is too short
  why: RSA (Rivest-Shamir-Adleman) 2048 is still acceptable.
- [ ] The hostname doesn't match the SAN (Subject Alternative Name)
  why: The SAN matches hr.corp.example.com.

## d1-pbq-cert-errors/b
type: single

What is the BEST long-term fix?

### Options
- [ ] Tell users to click through the warning each visit
  why: That teaches users to ignore real attacks, like an on-path attacker's fake certificate.
- [x] Use a certificate from the internal CA (Certificate Authority)
- [ ] Replace it with a self-signed wildcard certificate for the domain
  why: A wildcard self-signed certificate would still be untrusted.
- [ ] Disable certificate checks in the browser policy
  why: That removes the protection entirely.

## d1-revoke-1
type: single
topic: 1.4
group: cert-revocation

A browser needs to check, in real time, whether a single website certificate has been revoked, without downloading a large list. What does it use?

### Options
- [x] OCSP (Online Certificate Status Protocol)
- [ ] CRL (Certificate Revocation List)
  why: A CRL is the full list of revoked certificates. Downloading it is exactly what the browser wants to avoid.
- [ ] CSR (Certificate Signing Request)
  why: A CSR requests a certificate. It doesn't check status.
- [ ] Key escrow
  why: Key escrow stores keys with a third party. It has nothing to do with revocation.

### Explanation
The Online Certificate Status Protocol asks the CA (Certificate Authority) about one certificate and returns good, revoked or unknown.

## d1-revoke-3
type: single
topic: 1.4
group: cert-revocation

A web server's private key was stolen. What should the administrator do FIRST about the server's certificate?

### Options
- [ ] Generate a new CSR (Certificate Signing Request) using the same key pair
  why: The old key is compromised. Reusing it defeats the purpose.
- [ ] Wait for the certificate to expire
  why: The attacker could impersonate the site until then.
- [x] Ask the CA (Certificate Authority) to revoke the certificate
- [ ] Switch the certificate to a wildcard
  why: The certificate type doesn't matter. The key is compromised.

### Explanation
A compromised private key means the certificate can no longer be trusted. Revoking it adds it to the CRL (Certificate Revocation List) and OCSP (Online Certificate Status Protocol) responses. Then a new key pair and certificate are issued.

## d1-crypto-hw-1
type: single
topic: 1.4
group: crypto-hardware

A laptop uses a chip on the motherboard to store its disk encryption keys and to confirm the boot process hasn't been tampered with. What is this chip?

### Options
- [ ] Hardware security module
  why: An HSM (Hardware Security Module) is a dedicated appliance or card for managing many keys in data centers, not a chip built into a laptop.
- [x] Trusted Platform Module
- [ ] Key management system
  why: A KMS (Key Management Service) is software or a service that manages keys at scale, like a cloud KMS.
- [ ] Secure enclave
  why: A secure enclave is a protected area of a processor for running sensitive code. The boot measurement and BitLocker key storage point to the TPM (Trusted Platform Module).

### Explanation
A TPM is a chip on the motherboard that stores keys and supports secure and measured boot. BitLocker uses it.

## d1-crypto-hw-2
type: match
topic: 1.4
group: crypto-hardware

Match each scenario to the BEST technology.

### Match
- A bank needs FIPS-validated hardware to protect thousands of signing keys in its data center => Hardware security module
- A cloud team needs a managed service to create, rotate and audit encryption keys => Key management system
- A laptop needs to tie its disk encryption to its own motherboard => Trusted Platform Module
- A phone needs an isolated area of its processor to handle biometric data => Secure enclave

### Distractors
- Key escrow: Key escrow stores a copy of keys with a third party for recovery. None of these scenarios are about recovery.

### Explanation
HSMs (Hardware Security Modules) are high-assurance appliances for many keys. KMS (Key Management Service) manages keys as a service. TPMs (Trusted Platform Modules) are per-device chips. Secure enclaves isolate sensitive processing inside a CPU (Central Processing Unit).

## d1-obfuscation-2
type: match
topic: 1.4
group: data-obfuscation

Match each technique to its example.

### Match
- A receipt shows only the last four digits of a card number => Data masking
- Attackers hide stolen data inside the pixels of an image file => Steganography
- Card numbers are replaced with random values mapped in a vault => Tokenization
- Source code is rewritten so it still runs but is hard to read => Obfuscation

### Distractors
- Encryption: Encryption makes data unreadable without a key. None of these use a key.

### Explanation
Masking hides part of the data. Steganography hides data inside other data. Tokenization substitutes a token. Obfuscation makes something hard to understand.

## d1-token-1
type: single
topic: 1.4
group: data-obfuscation

A retailer wants repeat purchases to be easy, but it doesn't want real card numbers anywhere in its own databases. A payment provider keeps the real numbers in a vault and gives the retailer random substitute values that have no mathematical relationship to the originals. Which technique is this?

### Options
- [x] Tokenization
- [ ] Data masking
  why: Masking hides part of a value when it's displayed (for example `****1234`). The real value is still stored.
- [ ] Hashing
  why: A hash is mathematically derived from the input and can't be mapped back to the card number for a later charge.
- [ ] Symmetric encryption
  why: Ciphertext is mathematically related to the original and reversible with the key. Here the substitute is random and resolved by a vault lookup.

### Explanation
Tokenization swaps sensitive data for a random stand-in and keeps the mapping in a separate vault. "No mathematical relationship" and "vault" are the phrases that separate it from encryption and hashing.

## d1-token-3
type: single
topic: 1.4
group: data-obfuscation

A call center's screens show customer card numbers as `XXXX-XXXX-XXXX-4821` so agents can confirm the last four digits. The full number remains stored in the database. Which technique is being applied on the screen?

### Options
- [x] Data masking
- [ ] Tokenization
  why: Tokenization would replace the stored number with a substitute. Here the full number is still in the database.
- [ ] Encryption
  why: Encryption would make the whole value unreadable without a key. The agent can read the last four digits directly.
- [ ] Segmentation
  why: Segmentation separates data sets from each other. It doesn't change how one value is displayed.

### Explanation
Masking hides part of a value from the viewer while the underlying data stays intact. The visible last four digits and the unchanged stored number are the giveaways.

## d1-key-escrow-1
type: single
topic: 1.4
group: key-escrow

A company encrypts employee laptops. Legal wants to be sure that if an employee leaves or loses their password, the company can still decrypt the drive. Copies of the encryption keys are held by a trusted third party and released only under defined conditions. What is this arrangement?

### Options
- [x] Key escrow
- [ ] Key stretching
  why: Key stretching makes a weak password harder to brute-force. It doesn't help anyone recover a key.
- [ ] Key exchange
  why: Key exchange is how two parties agree on a key to use. It isn't about recovery.
- [ ] Certificate revocation
  why: Revocation marks a certificate as no longer trusted. It doesn't recover encrypted data.

### Explanation
Key escrow keeps a copy of encryption keys with a trusted party so that data can be recovered when the normal key holder is unavailable.

## d1-key-escrow-2
type: single
topic: 1.4
group: key-escrow

Which is the MAIN risk an organization accepts when it uses key escrow?

### Options
- [ ] Encryption becomes noticeably slower
  why: Escrow doesn't change how encryption runs. It only stores extra copies of keys.
- [x] Whoever holds the escrowed keys can decrypt the data
- [ ] Certificates can no longer be revoked
  why: Escrow has no effect on certificate revocation.
- [ ] Users must change their passwords far more often than before
  why: Escrow doesn't affect password policy.

### Explanation
Escrow trades secrecy for recoverability. The escrow agent becomes a high-value target, and anyone who gets the escrowed keys can decrypt the data, so the agent must be strongly trusted and protected.

## d1-enc-level-1
type: single
topic: 1.4
group: encryption-levels

A database holds customer records. Only the column with Social Security numbers needs encryption, and the application must keep fast access to every other column. Which level of encryption fits BEST?

### Options
- [ ] Full-disk encryption
  why: FDE (Full-Disk Encryption) protects the whole drive if it's stolen, but every column is readable while the server runs.
- [ ] Volume encryption
  why: Volume encryption protects a whole logical volume. It doesn't single out one sensitive field.
- [x] Record-level encryption
- [ ] Transport-layer encryption
  why: Transport encryption protects data in transit. The records would still sit unencrypted in the database.

### Explanation
Record- or field-level encryption protects only the specific sensitive values inside a database. Disk and volume encryption protect data at rest from physical theft, and transport encryption protects data on the wire.

## d1-enc-level-2
type: match
topic: 1.4
group: encryption-levels

Match each requirement to the encryption level that meets it.

### Match
- A stolen laptop must reveal nothing, including the operating system => Full-disk
- One spreadsheet emailed to an auditor must stay protected wherever it goes => File
- A web browser's session with a banking site must be protected on the wire => Transport
- Only the salary column in the HR (Human Resources) database must be protected => Database field

### Distractors
- Partition: Partition encryption protects one partition. None of the requirements is limited to a single partition.

### Explanation
Full-disk covers everything on the drive. File encryption travels with the file. Transport encryption (such as TLS (Transport Layer Security)) covers data in transit. Database or record encryption targets specific fields.

## d1-enc-level-3
type: single
topic: 1.4
group: encryption-levels

A user copies a contract from a BitLocker-encrypted laptop to an unencrypted USB (Universal Serial Bus) drive. The copy opens on any computer. Which encryption level would have kept the contract protected after it was copied?

### Options
- [x] File-level encryption
- [ ] Full-disk encryption
  why: Full-disk encryption protects data only while it sits on that disk. Files are decrypted as they're read and copied.
- [ ] Volume encryption
  why: Volume encryption protects one volume the same way. A copied file leaves the protection behind.
- [ ] Encrypting the laptop's data partition
  why: Partition encryption also protects only the data on that partition.

### Explanation
Full-disk, partition and volume encryption protect storage, so data is safe if the device is stolen but not once it's copied elsewhere. File-level encryption travels with the file. Database and record-level encryption protect data inside a database.

## d1-blockchain-1
type: single
topic: 1.4
group: blockchain

Several shipping companies want a shared record of container handoffs. No single company should control it, and nobody should be able to quietly change a past entry. Which technology fits BEST?

### Options
- [ ] A central database run by the largest member
  why: One company would control the records and could change them.
- [x] A blockchain-based open public ledger
- [ ] A shared spreadsheet with version history
  why: Whoever administers the file can still edit or delete history.
- [ ] A certificate revocation list
  why: A CRL (Certificate Revocation List) lists revoked certificates. It isn't a general record of transactions.

### Explanation
A blockchain is a distributed ledger. Each block includes the hash of the previous one, and every participant holds a copy, so changing an old entry breaks the chain and is obvious to everyone.

## d1-blockchain-2
type: single
topic: 1.4
group: blockchain

Why does altering an old block in a blockchain get detected?

### Options
- [ ] Each block is encrypted with the miner's private key
  why: Blocks aren't kept secret. The ledger is meant to be readable.
- [ ] A certificate authority signs every block
  why: Blockchains don't depend on a central CA (Certificate Authority). Trust comes from the distributed copies.
- [x] Each block contains the hash of the block before it
- [ ] Blocks are stored only on one trusted server
  why: The opposite is true. Copies are distributed across many participants.

### Explanation
Each block includes the previous block's hash. Changing an old block changes its hash, which no longer matches the reference in the next block, and other participants' copies show the mismatch.
