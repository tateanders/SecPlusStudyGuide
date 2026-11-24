---
deck: Domain 3 – Security Architecture
section: "3.0"
exam_weight: 18
topics:
  3.1: Compare and contrast security implications of different architecture models
  3.2: Given a scenario, apply security principles to secure enterprise infrastructure
  3.3: Compare and contrast concepts and strategies to protect data
  3.4: Explain the importance of resilience and recovery in security architecture
---

## d3-cloudmodel-1
type: single
topic: 3.1
group: cloud-architecture-models

A team defines its entire network, servers and firewall rules in version-controlled template files and deploys identical environments from them. What is this practice?

### Options
- [x] Infrastructure as code
- [ ] Serverless computing
  why: Serverless runs functions without managing servers. This is about defining infrastructure in files.
- [ ] Software-defined networking
  why: SDN (Software-Defined Networking) separates network control from forwarding. It doesn't cover servers and full environments in templates.
- [ ] Microservices
  why: Microservices is an application design pattern, not a deployment method.

### Explanation
Infrastructure as code defines infrastructure in files. It gives consistent, repeatable deployments and makes configuration drift easier to spot.

## d3-cloudmodel-2
type: match
topic: 3.1
group: cloud-architecture-models

Match each description to the architecture model.

### Match
- Code runs as event-triggered functions, and the provider manages all servers => Serverless
- An application is split into small, independent services that talk over APIs (Application Programming Interfaces) => Microservices
- Network routing decisions are made by a central controller, separate from switches => Software-defined networking
- A system has no network connection to any other network => Air-gapped

### Distractors
- Monolithic: A monolithic application is one large codebase, the opposite of microservices.

### Explanation
Serverless removes server management, microservices split apps into small pieces, SDN (Software-Defined Networking) separates the control plane from the data plane, and air gaps physically isolate systems.

## d3-embedded-1
type: single
topic: 3.1
group: embedded-ics

A water treatment plant's control system runs on 15-year-old controllers that the vendor no longer patches, and the plant can't take them offline. What is the BEST way to protect them?

### Options
- [ ] Install endpoint antivirus on each controller and workstation
  why: Most ICS (Industrial Control System) controllers can't run standard endpoint software.
- [x] Isolate them on a tightly controlled network segment
- [ ] Move the control system to a public cloud
  why: That would add internet exposure to critical systems.
- [ ] Replace them with consumer IoT (Internet of Things) devices
  why: Consumer IoT has its own weak security and isn't built for industrial control.

### Explanation
ICS and SCADA (Supervisory Control and Data Acquisition) systems often can't be patched or rebooted. Segmentation (or an air gap) is the main compensating control.

## d3-embedded-3
type: multi
topic: 3.1
group: embedded-ics

Which TWO considerations make embedded and real-time systems harder to secure than standard servers?

### Options
- [x] Limited ability to install patches
- [x] Limited processing power for security software
- [ ] They can't be placed on a separate network
  why: They can be segmented. Segmentation is the standard control.
- [ ] They run standard Windows builds
  why: Many run custom firmware or an RTOS (Real-Time Operating System).
- [ ] They rarely connect to a network
  why: Many are networked. That's why they need protecting.

### Explanation
SY0-701 lists considerations such as inability to patch, power and compute limits, and long lifespans. Those make embedded devices hard to secure with normal tools.

## d3-embedded-4
type: single
topic: 3.1
group: embedded-ics

A hotel installs internet-connected thermostats in every room. They ship with a shared default password and get firmware updates rarely. What is the BEST way to reduce the risk they add to the hotel network?

### Options
- [ ] Connect them to the same network as the front-desk computers
  why: That puts weak devices next to sensitive systems.
- [x] Put them on a separate network segment and change the passwords
- [ ] Install desktop antivirus software on each thermostat
  why: IoT (Internet of Things) devices usually can't run standard endpoint software.
- [ ] Disable logging on the thermostats to save storage
  why: Losing logs makes problems harder to detect.

### Explanation
IoT devices often have weak defaults and slow patching. Segmentation limits what a compromised device can reach, and changing default credentials removes the easiest way in.

## d3-shared-resp-4
type: single
topic: 3.1
group: shared-responsibility

A company migrates its order database to virtual machines it rents from an IaaS (Infrastructure as a Service) provider. Six months later, attackers exploit an unpatched vulnerability in the guest operating system on those virtual machines. Under the usual cloud responsibility matrix, who was responsible for patching it?

### Options
- [x] The customer
- [ ] The cloud provider
  why: In IaaS the provider secures the facilities, hardware, and hypervisor. The guest operating system belongs to the tenant.
- [ ] The hypervisor vendor
  why: The vendor patches the hypervisor software. It has nothing to do with operating systems installed inside the virtual machines.
- [ ] A third-party auditor
  why: Auditors assess whether controls exist. They don't operate or patch systems.

### Explanation
With IaaS, everything from the guest operating system upward (OS (Operating System), applications, data, access) is the customer's job. The vulnerability was in the guest OS, so the patching gap was the customer's.

## d3-shared-resp-3
type: match
topic: 3.1
group: shared-responsibility

Under a typical cloud responsibility matrix, match each task to the party responsible for it.

### Match
- Physical security of the data center in any cloud model => Provider
- Guest OS (Operating System) patching on IaaS (Infrastructure as a Service) virtual machines => Customer
- Patching the application code of a SaaS (Software as a Service) product => Provider
- Classifying the data uploaded to a SaaS product => Customer
- Runtime and OS patching underneath a PaaS (Platform as a Service) deployment => Provider
- Managing user accounts and access rights in SaaS => Customer

### Distractors
- Regulator: Regulators set requirements. They don't operate or secure any layer.
- Internet service provider: The ISP (Internet Service Provider) carries traffic to the cloud. It isn't a party to the responsibility matrix.

### Explanation
The provider always owns the physical layer, and the customer always owns its data and who can access it. What moves between the two is the middle (OS, runtime, application), and it shifts toward the provider as you go from IaaS to PaaS to SaaS.

## d3-containers-1
type: single
topic: 3.1
group: virtualization-containers

A development team packages each microservice with only its libraries and dependencies. All packages share the host's operating system kernel and start in under a second. What technology is this?

### Options
- [ ] Virtual machines
  why: Each VM (Virtual Machine) runs its own full guest operating system on a hypervisor. These packages share the host's kernel.
- [x] Containerization
- [ ] Serverless functions
  why: Serverless runs code without the team managing any host. Here the team packages and runs the services itself.
- [ ] Air-gapped hosts
  why: Air-gapping cuts a system off from other networks. It isn't a packaging method.

### Explanation
Containers bundle an application with its dependencies and share the host OS (Operating System) kernel, which makes them light and fast. VMs each carry a full guest OS, which gives stronger isolation at a higher cost.

## d3-containers-2
type: single
topic: 3.1
group: virtualization-containers

From a security standpoint, what is the MAIN isolation difference between containers and virtual machines?

### Options
- [x] Containers share the host kernel, so a kernel flaw can affect all of them
- [ ] Virtual machines can't be patched once they are deployed
  why: VMs (Virtual Machines) are patched like any other operating system.
- [ ] Containers can only run on public cloud platforms, not on-premises hardware
  why: Containers run on-premises and in any cloud.
- [ ] Virtual machines share one guest operating system kernel
  why: Each VM has its own guest operating system and kernel. That's what isolates them.

### Explanation
Because containers share one kernel, a kernel exploit or a container escape can reach other containers on the host. VMs are separated by the hypervisor, and each has its own OS (Operating System).

## d3-arch-consider-1
type: single
topic: 3.1
group: architecture-considerations

A company is choosing between keeping its HR (Human Resources) system on-premises and moving it to a SaaS (Software as a Service) provider. Which consideration is a benefit of the SaaS option?

### Options
- [ ] Full control over when every patch is applied
  why: That's an on-premises benefit. With SaaS the provider decides when to patch.
- [x] Some risk is transferred to the provider by contract
- [ ] No dependency on any third party
  why: SaaS creates a dependency on the provider. On-premises reduces it.
- [ ] Data stays stored inside the company's own building
  why: SaaS data lives in the provider's facilities.

### Explanation
SY0-701 lists considerations such as availability, resilience, cost, responsiveness, scalability, ease of deployment, risk transference, ease of recovery, patch availability, and power and compute limits. Cloud services transfer some risk and operational work to the provider, at the cost of direct control.

## d3-arch-consider-2
type: single
topic: 3.1
group: architecture-considerations

A company runs all authentication through one data center. An outage there locks every office out of every application. Which architecture weakness does this show?

### Options
- [x] A centralized design with a single point of failure
- [ ] Too much decentralization across business units
  why: The problem is that everything depends on one place, which is the opposite of decentralization.
- [ ] Poor physical isolation through an air gap
  why: An air gap would cut the offices off entirely. It doesn't describe the dependency.
- [ ] A lack of infrastructure as code templates for rebuilding the servers
  why: IaC (Infrastructure as Code) helps rebuild environments consistently, but the weakness here is the single dependency.

### Explanation
Centralized architectures are easier to manage and monitor but create single points of failure. Decentralized designs spread the risk at the cost of more complex management.

## d3-netinfra-1
type: single
topic: 3.1
group: network-infra-models

A data center team wants to change routing and segment traffic for hundreds of switches from one central controller in software, instead of logging in to each device. Which architecture concept fits?

### Options
- [x] SDN (Software-Defined Networking)
- [ ] An air-gapped network
  why: An air gap physically isolates systems. It doesn't program switches centrally.
- [ ] SD-WAN (Software-Defined Wide Area Network)
  why: SD-WAN manages links between sites, such as branch offices. This is about switches inside one data center.
- [ ] Physical isolation of each rack
  why: Physical isolation separates hardware. It doesn't give central control over many switches.

### Explanation
SDN separates the control plane (decisions, in a central controller) from the data plane (forwarding, on the switches). It makes logical segmentation quick to change in software.

## d3-netinfra-2
type: match
topic: 3.1
group: network-infra-models

Match each infrastructure design to its description.

### Match
- Systems sit on a network with no physical connection to any other network => Air-gapped
- VLANs (Virtual Local Area Networks) split one physical network into separate groups => Logical segmentation
- One authentication service in the main data center handles sign-ins for every office => Centralized
- Each region runs its own copy of a service and keeps working if the others fail => Decentralized

### Distractors
- Serverless: Serverless means running code without managing servers. None of these designs describes that.

### Explanation
Centralized designs are easier to manage but can become a single point of failure. Decentralized designs add resilience at the cost of consistency. Air gaps and logical segmentation are SY0-701 network infrastructure options.

## d3-failmode-3
type: single
topic: 3.2
group: fail-modes

Which situation is the BEST fit for fail-open?

### Options
- [ ] A firewall in front of a database of card numbers
  why: Protecting payment data favors security, so fail-closed.
- [x] Door locks on emergency exits during a fire
- [ ] A web filter for a classified government network
  why: Classified networks favor security, so fail-closed.
- [ ] An IPS (Intrusion Prevention System) in front of the internet-facing payroll server
  why: Payroll data should stay protected if the IPS fails.

### Explanation
Fail-open is chosen when availability or safety matters more than security. Emergency exits must unlock so people can get out.

## d3-fail-mode-1
type: single
topic: 3.2
group: fail-modes

A hospital places an inline IPS (Intrusion Prevention System) between the internet and its patient records network. Management decides that if the IPS loses power or crashes, no traffic should pass until it's restored, even though that means an outage. Which failure mode is the hospital choosing?

### Options
- [x] Fail-closed
- [ ] Fail-open
  why: Fail-open lets traffic keep flowing uninspected when the device fails. Management wants the opposite.
- [ ] Tap/monitor mode
  why: A tap receives a copy of traffic and isn't in the path at all, so its failure wouldn't stop anything.
- [ ] Active/active
  why: That's a high-availability design with two devices sharing load. It isn't a failure mode.

### Explanation
Fail-closed blocks everything when the device fails, trading availability for security. "No traffic should pass" and accepting an outage are the cues.

## d3-fail-mode-3
type: single
topic: 3.2
group: fail-modes

A manufacturer configures its inline IPS (Intrusion Prevention System) to fail-open. What is the main security trade-off of that choice?

### Options
- [x] Traffic flows uninspected during a failure
- [ ] All traffic is blocked until the device recovers
  why: That's the fail-closed behavior, and it's an availability cost, not a security one.
- [ ] The device can no longer be deployed inline
  why: Failure mode only matters for inline devices. It doesn't change where the device can sit.
- [ ] Signature updates stop until the device restarts
  why: Updates have nothing to do with how the device behaves when it fails.

### Explanation
Fail-open keeps the business running but leaves the network unprotected for as long as the device is down. Whether that's acceptable depends on whether availability or confidentiality matters more for that network.

## d3-inline-1
type: single
topic: 3.2
group: inline-vs-tap

A security team wants a sensor that can actively block malicious traffic, not just alert on it. How must the sensor be placed?

### Options
- [x] Inline with the traffic
- [ ] On a network tap
  why: A tap gives a copy of the traffic. The sensor can see it but can't block it.
- [ ] On a SPAN (Switched Port Analyzer) port
  why: A SPAN port also sends a copy. Blocking requires being in the path.
- [ ] In a honeynet
  why: A honeynet is a decoy network, not where production traffic flows.

### Explanation
To block traffic, a device has to sit in the traffic path (inline). An IPS (Intrusion Prevention System) is inline. An IDS (Intrusion Detection System) can work from a copy on a tap or SPAN port.

## d3-inline-3
type: multi
topic: 3.2
group: inline-vs-tap

Which TWO statements about passive (tap or monitor) sensors are true?

### Options
- [x] They don't add latency to the traffic path
- [x] They can't block traffic in real time
- [ ] They must be configured fail-closed
  why: Fail-open and fail-closed apply to inline devices. A passive sensor failing doesn't affect traffic.
- [ ] They replace the need for a firewall
  why: A passive sensor only watches.
- [ ] They decrypt all TLS (Transport Layer Security) traffic automatically
  why: Decryption requires extra setup, like keys or a proxy.

### Explanation
Passive sensors watch a copy of traffic. They can't slow it down, but they also can't stop anything.

## d3-firewall-1
type: single
topic: 3.2
group: firewall-types

A company wants to protect its web application from SQL (Structured Query Language) injection and cross-site scripting by inspecting HTTP (Hypertext Transfer Protocol) requests. Which device is BEST?

### Options
- [x] Web application firewall
- [ ] Layer 4 firewall
  why: A layer 4 firewall filters by IP (Internet Protocol) and port. It can't read HTTP content.
- [ ] Load balancer
  why: Load balancers spread traffic. They don't inspect for attacks by default.
- [ ] Jump server
  why: A jump server is for admin access.

### Explanation
A WAF (Web Application Firewall) inspects HTTP and HTTPS (Hypertext Transfer Protocol Secure) traffic at layer 7 and blocks attacks like SQLi (SQL Injection) and XSS (Cross-Site Scripting).

## d3-firewall-3
type: match
topic: 3.2
group: firewall-types

Match each device to its BEST fit.

### Match
- A small office wants firewall, antivirus, web filtering and VPN (Virtual Private Network) in one appliance => Unified threat management
- An online store needs protection from SQL (Structured Query Language) injection on its checkout page => Web application firewall
- A router filters traffic only by source IP (Internet Protocol) and destination port => Layer 4 firewall
- An enterprise wants to block social media apps no matter which port they use => Next-generation firewall

### Distractors
- Jump server: A jump server is a hardened host for admin access, not a firewall.

### Explanation
UTM (Unified Threat Management) is all-in-one, WAF (Web Application Firewall) protects web apps, layer 4 filters by address and port, and NGFW (Next-Generation Firewall) adds application awareness.

## d3-pbq-fwrules
type: pbq
topic: 3.2
group: firewall-types

A web server at 10.0.5.20 must accept HTTPS (Hypertext Transfer Protocol Secure) from the internet. Admins at 10.0.10.0/24 must reach it over SSH (Secure Shell). Everything else should be blocked. Rules are processed top to bottom, and the first match wins.

### Exhibit
| # | Source | Destination | Port | Action |
|---|---|---|---|---|
| 1 | any | 10.0.5.20 | 443 | Allow |
| 2 | any | 10.0.5.20 | 22 | Allow |
| 3 | 10.0.10.0/24 | 10.0.5.20 | 22 | Allow |
| 4 | any | any | any | Deny |

### Explanation
Rule 2 allows SSH from anywhere, which breaks the requirement. Because rules match top-down, rule 3 never matters. Removing rule 2 fixes it, and rule 4 is the implicit deny that blocks everything else.

## d3-pbq-fwrules/a
type: single

Which rule violates the requirements?

### Options
- [ ] Rule 1
  why: HTTPS (Hypertext Transfer Protocol Secure) from anywhere is required.
- [x] Rule 2
- [ ] Rule 3
  why: This is exactly what the admins need.
- [ ] Rule 4
  why: This is the correct deny-all rule.

## d3-jump-1
type: single
topic: 3.2
group: jump-proxy

Admins must manage servers in a restricted network segment. Security wants all admin sessions to go through one hardened, closely monitored host. What should be deployed?

### Options
- [x] A jump server
- [ ] A forward proxy
  why: A forward proxy handles users' outbound web traffic.
- [ ] A load balancer
  why: Load balancers spread incoming traffic across servers.
- [ ] A honeypot
  why: A honeypot is a decoy for attackers.

### Explanation
A jump server (jump box) is a hardened host that admins connect to first, then reach the restricted systems from. It gives one controlled, logged entry point.

## d3-jump-3
type: single
topic: 3.2
group: jump-proxy

A company wants to filter employees' web browsing and cache frequently visited sites. What should it deploy?

### Options
- [ ] Reverse proxy
  why: A reverse proxy serves inbound requests to the company's own servers.
- [x] Forward proxy
- [ ] Jump server
  why: Jump servers are for admin access to restricted networks.
- [ ] Screened subnet
  why: A screened subnet is a network zone, not a filtering device.

### Explanation
A forward proxy handles employees' outbound requests, so it can filter content, log browsing and cache pages.

## d3-8021x-1
type: single
topic: 3.2
group: port-based-nac

A company wants to stop visitors from plugging laptops into open network jacks in conference rooms and getting network access. Which control is BEST?

### Options
- [x] 802.1X (port-based Network Access Control)
- [ ] WPA3 (Wi-Fi Protected Access 3) on the wireless network
  why: WPA3 secures Wi-Fi. These are wired jacks.
- [ ] An application allow list
  why: Allow lists control which software runs, not who gets on the network.
- [ ] DNS (Domain Name System) filtering
  why: DNS filtering controls which sites can be resolved, after someone is already on the network.

### Explanation
802.1X makes a device authenticate before the switch port allows traffic. Unauthenticated devices get no access or a guest VLAN (Virtual Local Area Network).

## d3-8021x-2
type: order
topic: 3.2
group: port-based-nac

Put the 802.1X (port-based Network Access Control standard) authentication steps in order.

### Order
1. The supplicant connects to the switch port
   why: The supplicant is the device asking for access.
2. The authenticator requests the supplicant's credentials
   why: The switch (authenticator) blocks traffic and asks for credentials first.
3. The authenticator forwards the credentials to the authentication server
   why: The switch doesn't check credentials itself. It passes them along.
4. The authentication server approves or denies access
   why: The RADIUS (Remote Authentication Dial-In User Service) server makes the decision.
5. The authenticator opens the port
   why: Traffic only flows after approval.

### Explanation
802.1X has three roles: supplicant (the device), authenticator (the switch or access point), and authentication server (usually RADIUS).

## d3-vpn-1
type: single
topic: 3.2
group: vpn-ipsec

Two offices connect over the internet with an IPsec (Internet Protocol Security) VPN (Virtual Private Network). The whole original IP (Internet Protocol) packet, including its header, is encrypted and wrapped in a new packet. Which IPsec mode is this?

### Options
- [x] Tunnel mode
- [ ] Transport mode
  why: Transport mode only encrypts the payload. The original header stays visible.
- [ ] Split tunnel
  why: Split tunneling decides which traffic goes through the VPN. It isn't an IPsec mode.
- [ ] AH-only mode
  why: AH (Authentication Header) provides integrity but no encryption.

### Explanation
Tunnel mode encrypts the entire original packet and adds a new header. It's typical for site-to-site VPNs.

## d3-vpn-2
type: match
topic: 3.2
group: vpn-ipsec

Match each IPsec (Internet Protocol Security) component to what it does.

### Match
- Encrypts the payload and provides integrity => Encapsulating Security Payload
- Provides integrity and authentication but no encryption => Authentication Header
- Negotiates keys and security associations => Internet Key Exchange
- Encrypts the entire original packet including the header => Tunnel mode

### Distractors
- Transport mode: Transport mode encrypts only the payload, leaving the original header.
- TLS (Transport Layer Security): TLS is a different protocol used by TLS-based VPNs (Virtual Private Networks), not part of IPsec.

### Explanation
ESP (Encapsulating Security Payload) encrypts, AH (Authentication Header) only authenticates, IKE (Internet Key Exchange) handles keys, and tunnel mode wraps the whole packet.

## d3-sase-1
type: single
topic: 3.2
group: sase-sdwan

A company with remote workers and 50 branch offices wants firewall, secure web gateway, Zero Trust access and SD-WAN (Software-Defined Wide Area Network) delivered together as a cloud service. What is this model called?

### Options
- [x] Secure access service edge
- [ ] Unified threat management
  why: UTM (Unified Threat Management) is an on-premises appliance, not a cloud-delivered framework.
- [ ] Screened subnet
  why: A screened subnet is a network zone.
- [ ] Software-defined networking
  why: SDN (Software-Defined Networking) is a networking approach. It doesn't bundle security services.

### Explanation
SASE (secure access service edge) combines SD-WAN networking and security services delivered from the cloud, close to wherever users are.

## d3-sase-3
type: single
topic: 3.2
group: sase-sdwan

What is the MAIN security advantage of SASE (Secure Access Service Edge) over sending all branch traffic back to headquarters for inspection?

### Options
- [x] Traffic is inspected in the cloud close to users
- [ ] It removes the need for user authentication entirely
  why: SASE includes Zero Trust access, which requires authentication.
- [ ] It encrypts all data at rest on employee endpoints
  why: SASE handles network traffic, not endpoint storage.
- [ ] It replaces endpoint detection and response tools
  why: EDR (Endpoint Detection and Response) protects the endpoint itself. SASE doesn't replace it.

### Explanation
SASE applies consistent security at cloud points of presence, so remote users and branches get protection without routing everything through headquarters.

## d3-zones-1
type: single
topic: 3.2
group: security-zones

A company hosts a public web server and an internal database. It wants the web server reachable from the internet while keeping internet traffic away from the internal network. Where should the web server go?

### Options
- [x] In a screened subnet between two firewall layers
- [ ] On the internal network next to the database it queries
  why: A compromised web server would then sit directly inside the trusted zone.
- [ ] On the guest wireless network
  why: The guest network isn't designed for hosting public services, and it may still be reachable from inside.
- [ ] Behind a jump server
  why: A jump server controls admin access. It doesn't host public services.

### Explanation
A screened subnet (formerly a DMZ (Demilitarized Zone)) holds public-facing systems. Firewall rules let the internet reach those systems but stop that traffic from going deeper into the trusted network.

## d3-zones-2
type: single
topic: 3.2
group: security-zones

An architect reviews a network and finds that every server, from the public web server to the payroll database, sits in one flat network with no internal firewalls. What is the MAIN risk?

### Options
- [ ] Higher latency between the servers
  why: A flat network is usually faster. The issue is security.
- [x] One compromised server can reach all the others
- [ ] Load balancing will no longer work
  why: Load balancing doesn't depend on zones.
- [ ] Certificates won't validate between servers on a single subnet
  why: Certificate validation has nothing to do with network layout.

### Explanation
Security zones group systems by trust level and put controls between them. Without zones, the attack surface is the whole network and an attacker can move laterally without crossing any control.

## d3-placement-1
type: single
topic: 3.2
group: infrastructure-placement

A security architect reviews a new branch office design. They remove an unused remote desktop gateway, close two open ports and turn off a guest Wi-Fi network nobody uses. What is the architect mainly doing?

### Options
- [x] Reducing the attack surface
- [ ] Adding a compensating control
  why: Compensating controls replace a control that can't be used. Nothing was replaced here, only removed.
- [ ] Changing the failure mode to fail-closed
  why: Failure modes describe what a device does when it breaks, not which services exist.
- [ ] Moving devices into a screened subnet
  why: Nothing was moved to a new zone. Unneeded entry points were removed.

### Explanation
The attack surface is every point where an attacker could get in. Removing unused services, ports and networks shrinks it. Device placement, security zones and connectivity are related infrastructure considerations in SY0-701.

## d3-placement-2
type: single
topic: 3.2
group: infrastructure-placement

Remote employees need to reach internal file servers from home. The company wants every session encrypted and wants the traffic to pass through its own security controls. Which option fits BEST?

### Options
- [x] A remote access VPN (Virtual Private Network)
- [ ] Opening the file servers' ports to the internet
  why: This exposes the servers directly to attackers and skips the company's controls.
- [ ] A site-to-site tunnel between two offices
  why: Site-to-site tunnels connect whole office networks, not individual users at home.
- [ ] A public file-sharing link for each team
  why: Public links bypass the company's controls and can be forwarded to anyone.

### Explanation
A remote access VPN gives each user an encrypted tunnel, using TLS (Transport Layer Security) or IPsec (Internet Protocol Security), into the company network, where its security controls apply. Selecting effective controls means matching the control to the access need.

## d3-datastate-1
type: match
topic: 3.3
group: data-states

Match each example to its data state.

### Match
- A customer database stored on an encrypted SAN (Storage Area Network) => Data at rest
- A file being uploaded to cloud storage over HTTPS (Hypertext Transfer Protocol Secure) => Data in transit
- A spreadsheet open in memory while a user edits it => Data in use
- Backup tapes in an offsite vault => Data at rest

### Distractors
- Data in motion: That's another name for data in transit, but CompTIA's term is "in transit". No row maps to it.

### Explanation
At rest is stored, in transit is moving across a network, and in use is being processed in memory.

## d3-datastate-2
type: single
topic: 3.3
group: data-states

Which data state is the HARDEST to protect with encryption?

### Options
- [ ] Data at rest
  why: Disk, file and database encryption protect stored data well.
- [ ] Data in transit
  why: TLS (Transport Layer Security) and IPsec (Internet Protocol Security) protect data moving across networks.
- [x] Data in use
- [ ] Archived data
  why: Archived data is at rest and easy to encrypt.

### Explanation
Data in use has to be decrypted in memory for the CPU (Central Processing Unit) to work on it. Secure enclaves and other confidential computing are the main protections.

## d3-dataclass-1
type: single
topic: 3.3
group: data-classification

A company's merger plans would cause serious harm if leaked before the announcement. Which classification is MOST appropriate?

### Options
- [ ] Public
  why: Public data causes no harm if disclosed.
- [x] Confidential
- [ ] Private
  why: Private usually refers to personal information about individuals.
- [ ] Critical
  why: Critical describes data needed for the business to keep operating, not data that's harmful to disclose.

### Explanation
Confidential data would cause serious harm to the organization if disclosed. Merger plans, trade secrets and strategy documents fit that label.

## d3-dataclass-3
type: multi
topic: 3.3
group: data-classification

A company is setting up data classification. Which TWO are benefits of classifying data?

### Options
- [x] Matching protections to each data type's sensitivity
- [x] Knowing which data falls under legal requirements
- [ ] Removing the need to encrypt data at rest and in transit
  why: Classification decides where encryption is needed. It doesn't replace it.
- [ ] Guaranteeing that no data is ever leaked
  why: No control guarantees that.
- [ ] Letting all employees access all data
  why: Classification usually restricts access.

### Explanation
Classification tells you how sensitive data is, so protection and legal handling can match it instead of treating everything the same.

## d3-sovereignty-1
type: single
topic: 3.3
group: data-sovereignty

A European company learns that its cloud provider stores customer data in a US (United States) region. Under GDPR (General Data Protection Regulation), the data must follow EU (European Union) rules. Which concept is the company dealing with?

### Options
- [x] Data sovereignty
- [ ] Data masking
  why: Masking hides parts of data.
- [ ] Data classification
  why: Classification labels sensitivity. The issue is which country's laws apply.
- [ ] Data retention
  why: Retention is how long data is kept.

### Explanation
Data sovereignty means data is subject to the laws of the country where it's collected or stored.

## d3-sovereignty-3
type: single
topic: 3.3
group: data-sovereignty

Which control MOST directly helps a company meet data sovereignty requirements in the cloud?

### Options
- [ ] Enabling MFA (Multifactor Authentication) on all cloud admin accounts
  why: MFA protects access, not where data is stored.
- [x] Limiting storage and backups to approved regions
- [ ] Encrypting all stored data with AES-256 (Advanced Encryption Standard, 256-bit key) keys
  why: Encryption protects data but doesn't change which country it sits in.
- [ ] Tokenizing all customer records in the cloud
  why: Tokenization doesn't control storage location.

### Explanation
Sovereignty is about location, so the direct control is limiting which regions store and replicate data, including backups.

## d3-datatype-1
type: match
topic: 3.3
group: data-types

Match each item to the data type it represents.

### Match
- Patient health records covered by a specific law => Regulated
- A secret recipe that gives a food company its edge => Trade secret
- Contracts and records under a litigation hold => Legal information
- Quarterly revenue reports before public release => Financial information

### Distractors
- Public: Public data can be released without harm. None of these can.

### Explanation
SY0-701 lists data types including regulated, trade secret, intellectual property, legal information, financial information, and human- and non-human-readable data. The type affects which laws and controls apply.

## d3-datatype-2
type: single
topic: 3.3
group: data-types

A data loss prevention tool easily catches credit card numbers in emails, but it misses the same numbers inside an encoded binary file sent by an application. Which distinction explains this?

### Options
- [x] Human-readable versus non-human-readable data
- [ ] Regulated data versus trade secret data in the messages
  why: Both kinds can be either readable or encoded. The issue is the format the tool sees.
- [ ] Data at rest versus data in transit
  why: Both examples are data in transit.
- [ ] Public versus confidential classification
  why: The card numbers have the same classification in both cases.

### Explanation
Non-human-readable data, such as binary, encoded or compressed formats, is harder for people and simple tools to inspect. Protection must account for both forms.

## d3-protect-1
type: match
topic: 3.3
group: data-protection-methods

Match each requirement to the method that meets it.

### Match
- Customer data must never be accessed from outside the EU (European Union) => Geographic restrictions
- Only the finance group can open the budget folder => Permission restrictions
- Store a value so its integrity can be checked but it can't be read back => Hashing
- Keep the cardholder data environment separate from the corporate network => Segmentation

### Distractors
- Obfuscation: Obfuscation makes data or code harder to understand. None of the requirements is about readability.

### Explanation
SY0-701 lists methods to secure data including geographic restrictions, encryption, hashing, masking, tokenization, obfuscation, segmentation and permission restrictions. Pick the one whose effect matches the requirement.

## d3-protect-2
type: single
topic: 3.3
group: data-protection-methods

A cloud storage service blocks any login attempt that comes from an IP (Internet Protocol) address outside the company's home country, even if the credentials are correct. Which data protection method is this?

### Options
- [ ] Tokenization of the stored files
  why: Tokenization replaces data with a substitute value. It doesn't look at where requests come from.
- [x] Geographic restriction
- [ ] Data masking
  why: Masking hides part of a value on screen.
- [ ] Hashing
  why: Hashing is a one-way transformation of data.

### Explanation
Geographic restrictions (geofencing or geolocation-based access) limit where data can be accessed from. They often support data sovereignty requirements.

## d3-sites-2
type: match
topic: 3.4
group: recovery-sites

Match each recovery site to its description.

### Match
- Fully equipped with near-current data, ready within minutes => Hot site
- Has hardware and network but needs data restored and setup => Warm site
- Has power, cooling and space only => Cold site
- Recovery runs in a provider's infrastructure, with no company-owned facility => Cloud-based recovery

### Distractors
- Screened subnet: A screened subnet is a network zone for public-facing servers, not a recovery site.

### Explanation
Speed and cost go together: hot is fastest and most expensive, cold is slowest and cheapest. Cloud recovery can be set up to behave like any of them.

## d3-sites-4
type: single
topic: 3.4
group: recovery-sites

A regional bank's recovery plan requires operations to resume within minutes of losing its primary data center. Budget isn't a constraint. The alternate location must already have running hardware, current data, and network connectivity. Which type of site meets the requirement?

### Options
- [x] Hot site
- [ ] Warm site
  why: A warm site has hardware and connectivity, but data has to be restored first. Recovery takes hours to days.
- [ ] Cold site
  why: A cold site is empty space with power and cooling. Recovery takes days to weeks.
- [ ] Geographic dispersion
  why: That describes how far apart sites are, not how ready the alternate site is.

### Explanation
A hot site mirrors production and can take over almost immediately. "Within minutes", "current data", and "budget isn't a constraint" all point to it, since it's also the most expensive option.

## d3-sites-3
type: order
topic: 3.4
group: recovery-sites

Put these recovery options in order from the SHORTEST expected recovery time to the LONGEST.

### Order
1. Active/active sites that already share production load
   why: Nothing has to fail over. The surviving site is already serving users.
2. Hot site
   why: Fully equipped with current data. It takes over in minutes to hours.
3. Warm site
   why: Hardware and connectivity exist, but data must be restored first.
4. Cold site
   why: Empty space. Equipment has to be delivered and built before any restore.

### Explanation
Recovery time tracks how much is already in place: live traffic, then live data, then hardware only, then just a building. Cost runs in the opposite direction.

## d3-backup-1
type: single
topic: 3.4
group: backups-replication

A database must be recoverable to any point in time, not just the last nightly backup. What technique records every change so they can be replayed?

### Options
- [x] Journaling
- [ ] Snapshots
  why: Snapshots capture a point in time, not every change in between.
- [ ] Full backups
  why: Full backups are point-in-time copies.
- [ ] Load balancing
  why: Load balancing isn't a backup technique.

### Explanation
Journaling logs every change, so the system can be restored to any moment by replaying the journal.

## d3-backup-3
type: multi
topic: 3.4
group: backups-replication

Which TWO practices protect backups from ransomware?

### Options
- [x] Keeping an offline or immutable copy
- [x] Storing a copy offsite
- [ ] Replicating backups in real time to the primary server
  why: Real-time replication can copy ransomware encryption to the backup.
- [ ] Using the same admin account for backups and production
  why: A compromised admin account could then delete backups too.
- [ ] Skipping backup restore tests to save time
  why: Untested backups often fail when you need them.

### Explanation
Offline or immutable copies can't be encrypted by ransomware, and offsite copies survive a site-wide event.

## d3-test-1
type: match
topic: 3.4
group: resilience-testing

Match each test to its description.

### Match
- Team members walk through a disaster scenario in a meeting room => Tabletop exercise
- Production is deliberately switched to the backup system => Failover test
- The backup system runs real workload alongside production to compare results => Parallel processing
- A realistic, staged attack scenario is run without touching production => Simulation

### Distractors
- Penetration test: A pen test looks for vulnerabilities, not recovery readiness.

### Explanation
Tabletop is discussion only, failover actually switches, parallel processing runs both systems at once, and simulation acts out a scenario.

## d3-test-3
type: single
topic: 3.4
group: resilience-testing

Which test gives the MOST confidence that recovery will work, but carries the MOST risk to operations?

### Options
- [ ] Tabletop exercise
  why: Tabletops have no risk but don't test real systems.
- [ ] Simulation
  why: Simulations don't switch production.
- [x] Failover test
- [ ] Checklist review
  why: A checklist review just checks the documents.

### Explanation
A failover test actually moves production to the backup systems. If something goes wrong, the business feels it.

## d3-lb-1
type: single
topic: 3.4
group: lb-clustering

A website spreads incoming requests across six identical web servers so no single server is overloaded. What is this?

### Options
- [x] Load balancing
- [ ] Clustering
  why: Clustering groups servers to act as one system, usually for failover of a single service.
- [ ] Replication
  why: Replication copies data. It doesn't spread requests.
- [ ] Geographic dispersion
  why: Dispersion spreads sites across regions. Nothing here mentions location.

### Explanation
Load balancing distributes requests across servers for performance and availability.

## d3-lb-3
type: multi
topic: 3.4
group: lb-clustering

Which TWO strategies improve resilience against a regional power outage?

### Options
- [x] Geographic dispersion of data centers
- [x] Multi-region or multi-cloud deployment
- [ ] A larger single server
  why: One bigger server in the same region fails the same way.
- [ ] Load balancing within one data center
  why: Every server in that data center loses power together.
- [ ] More frequent snapshots stored locally
  why: Local snapshots go down with the site.

### Explanation
Spreading systems across regions or providers means one regional event can't take everything down.

## d3-power-1
type: single
topic: 3.4
group: power-resilience

A data center's utility power fails. The servers must stay running for the few seconds until the diesel generator starts and takes the load. What provides power during that gap?

### Options
- [x] A UPS (Uninterruptible Power Supply)
- [ ] A second generator
  why: A second generator would also need time to start.
- [ ] A power distribution unit in each rack
  why: A PDU (Power Distribution Unit) distributes power to the racks. It doesn't store power.
- [ ] Load balancing
  why: Load balancing spreads requests across servers. It doesn't supply electricity.

### Explanation
An uninterruptible power supply uses batteries to bridge short outages and the time it takes a generator to start. Generators handle long outages.

## d3-power-2
type: single
topic: 3.4
group: power-resilience

A hospital needs its systems to keep running through a utility outage that could last two days. Which control addresses that requirement?

### Options
- [ ] A UPS (Uninterruptible Power Supply) on every server rack
  why: UPS batteries last minutes, not days.
- [x] An onsite generator with a fuel supply
- [ ] A cold site in another city with space and power
  why: A cold site takes days to bring up, and the goal is to keep running here.
- [ ] Nightly backups to tape
  why: Backups protect data. They don't keep systems powered.

### Explanation
Generators provide long-term power as long as they have fuel. UPS units bridge the short gap until the generator takes over.

## d3-capacity-1
type: single
topic: 3.4
group: capacity-planning

A company expects its online orders to triple during the holiday season. The security team checks that it will have enough analysts to monitor alerts, enough licenses for its security tools, and enough bandwidth at the data center. What is the team doing?

### Options
- [x] Capacity planning
- [ ] A tabletop exercise
  why: A tabletop walks through an incident scenario. This is about having enough resources.
- [ ] A business impact analysis
  why: A BIA (Business Impact Analysis) identifies critical processes and what losing them would cost.
- [ ] Platform diversity
  why: Platform diversity uses different vendors or technologies so one flaw can't hit everything.

### Explanation
Capacity planning makes sure people, technology and infrastructure can handle expected demand, including the people needed to run security operations.

## d3-capacity-2
type: single
topic: 3.4
group: capacity-planning

A company runs its web tier on two different operating systems from different vendors, so a single vulnerability can't take down every server at once. What resilience concept is this?

### Options
- [ ] Capacity planning
  why: Capacity planning is about having enough resources, not using different ones.
- [ ] Clustering
  why: Clustering groups servers to act as one system. It doesn't require different platforms.
- [x] Platform diversity
- [ ] Journaling
  why: Journaling records data changes so they can be replayed.

### Explanation
Platform diversity avoids a single shared weakness. A flaw in one platform leaves the other running.

## d3-continuity-1
type: single
topic: 3.4
group: continuity-diversity

A company runs every server on the same operating system from one vendor. A single flaw in that system could take everything down at once. Which resilience practice addresses this?

### Options
- [x] Platform diversity
- [ ] Capacity planning
  why: Capacity planning makes sure there are enough people and resources. It doesn't remove the shared flaw.
- [ ] Journaling
  why: Journaling records changes for recovery. It doesn't stop one flaw from hitting every server.
- [ ] Adding more servers of the same type
  why: Identical servers share the same flaw, so they would all fail together.

### Explanation
Platform diversity uses different operating systems, vendors or providers so that one flaw or outage can't hit everything. Multi-cloud applies the same idea to cloud providers.

## d3-continuity-2
type: single
topic: 3.4
group: continuity-diversity

A company's plan describes how payroll and customer support will keep running, by hand if needed, during a long disruption while IT (Information Technology) restores systems. What is this planning called?

### Options
- [x] Continuity of operations
- [ ] Capacity planning
  why: Capacity planning sizes people, technology and infrastructure for demand. It isn't a plan for running through a disruption.
- [ ] Multi-cloud deployment
  why: Multi-cloud spreads workloads across providers. It doesn't keep manual business processes going.
- [ ] A tabletop exercise for the IT team
  why: A tabletop exercise tests a plan by discussion. It isn't the plan itself.

### Explanation
Continuity of operations keeps essential business functions running during and after a disruption. It covers people and processes, not only technology. Multi-cloud and platform diversity support it by removing single points of failure.
