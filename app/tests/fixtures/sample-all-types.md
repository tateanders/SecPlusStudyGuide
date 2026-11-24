---
deck: Sample – every question type
section: Sample
topics:
  2.2: Explain common threat vectors and attack surfaces
  2.4: Given a scenario, analyze indicators of malicious activity
  4.5: Given a scenario, modify enterprise capabilities to enhance security
  4.6: Given a scenario, implement and maintain identity and access management
  4.8: Explain appropriate incident response activities
---

# Sample deck

This file exists to check the parser, the app, and FORMAT.md against each other.
Untick it on the home screen once you have real decks.

## s-whaling-1
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

## s-whaling-2
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

## s-mfa-inherence-1
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

## s-mfa-inherence-2
type: single
topic: 4.6
group: mfa-factor-types

A user logs in with a password and then approves a push notification on their company phone. Which factor types does this login combine?

### Options
- [ ] Something you know and something you are
  why: Nothing biometric is involved; approving a push only proves you hold the phone.
- [x] Something you know and something you have
- [ ] Something you have and somewhere you are
  why: The password is a knowledge factor, and location isn't being checked.
- [ ] Something you know, twice
  why: The push approval isn't a secret you know; it proves possession of the enrolled device.

### Explanation
The password is knowledge. The push notification proves possession of the registered phone, which is a "something you have" factor.

## s-ir-order-1
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

## s-ir-order-2
type: single
topic: 4.8
group: ir-process

An analyst has scoped a worm outbreak to three VLANs and identified the strain. Management wants the infected hosts wiped and reimaged immediately. What should happen FIRST?

### Options
- [ ] Reimage the infected hosts
  why: That's eradication. Doing it before containment lets the worm keep spreading to clean hosts.
- [x] Isolate the affected VLANs
- [ ] Restore data from backups
  why: Recovery comes after eradication; restoring now risks reinfection.
- [ ] Hold a lessons-learned meeting
  why: The post-incident review happens after recovery, not mid-incident.

### Explanation
Analysis is done, so containment is next: isolate the affected segments so the worm stops spreading, then eradicate.

## s-secure-ports-1
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

## s-secure-ports-2
type: typed
topic: 4.5
group: secure-protocol-ports

A directory team is moving all LDAP queries to LDAP over TLS. Which TCP port must the firewall allow to the domain controllers for LDAPS?

### Accept
- 636
- port 636
- tcp 636
- tcp/636

### Wrong answers
- 389: 389 is plain LDAP. LDAPS listens on 636.
- 3269: 3269 is the Global Catalog over TLS, not standard LDAPS.

### Explanation
LDAPS uses TCP 636. Plain LDAP (and LDAP with StartTLS) uses 389.

## s-pbq-ssh-spray
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

## s-pbq-ssh-spray/a
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

## s-pbq-ssh-spray/b
type: multi

Which TWO controls would have MOST directly prevented this compromise?

### Options
- [x] Require SSH keys and disable password logins
- [x] Allow SSH only from the VPN address range
- [ ] Lower the account lockout threshold to 3 attempts
  why: Spraying deliberately stays at one or two attempts per account, under any lockout threshold.
- [ ] Move SSH from port 22 to port 2222
  why: That's security through obscurity. Scanners find nonstandard ports within minutes.

## s-pbq-ssh-spray/c
type: typed

Which source IP address should be blocked at the perimeter firewall?

### Accept
- 203.0.113.45

## s-spray-indicators-1
type: single
topic: 2.4
group: auth-log-analysis

Your SIEM shows 400 accounts each with exactly one failed login in a ten-minute window, all from the same IP address. Which attack is MOST likely?

| Accounts targeted | Failures per account | Source IPs |
|---|---|---|
| 400 | 1 | 1 |

### Options
- [ ] Brute force
  why: Brute force would show many failures against a few accounts, not one failure each across hundreds.
- [x] Password spraying
- [ ] Credential stuffing
  why: Stuffing uses a different leaked password per account; you'd expect some successes and varied patterns, not a uniform single try.
- [ ] Dictionary attack
  why: A dictionary attack runs a word list against one account, producing many failures on that account.

### Explanation
Many accounts, one attempt each, one source: that's the signature of password spraying, which tries a common password everywhere while staying under lockout thresholds.
