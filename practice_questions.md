# Azure Buddy: Original Practice Questions (UNOFFICIAL)

All 60 questions below were written from scratch for this project. They are NOT real exam questions and are not copied from any exam site. They follow the public AZ-900 skills outline "as of July 20, 2026" and the Microsoft Learn / Azure docs facts collected in `updated_scope_2026.md`.

- **Split**: Area 1 = 16 (27%), Area 2 = 23 (38%), Area 3 = 21 (35%).
- **Label**: "Unofficial AZ-900 study aid. Not affiliated with or endorsed by Microsoft. Questions are original."

---

## Check-Question Mode Block (System Prompt Integration)

```markdown
# CHECK-QUESTION MODE
When the learner says "quiz me" (optionally with a topic), ask ONE multiple-choice question at a time from the bank, or write a new original one in the same style. Never reproduce or imitate real exam questions. Do not reveal the answer until the learner replies. Then say whether they were right, explain why in 2-3 sentences, name the wrong options' trap, and tag the skill area and outline bullet. After 5 questions, summarise weak areas. Always remind them the questions are unofficial practice.
```

---

## AREA 1: CLOUD CONCEPTS

**Q1.** Your clinic moves its booking system to the cloud. Whichever service model you use, which item always remains YOUR responsibility?
- A. The physical datacenter
- B. Your data
- C. The hypervisor
- D. The physical network cabling
**Answer: B.** Data, identities and configuration stay with the customer in every model. Physical hosts, network and datacenter belong to Microsoft in cloud models.
Tag: 1.1 Shared responsibility model

**Q2.** A school wants to use a ready-made email and calendar service and manage nothing but its users and data. Which service type fits?
- A. IaaS
- B. PaaS
- C. SaaS
- D. On-premises
**Answer: C.** SaaS is a finished application, for example Microsoft 365.
Tag: 1.3 IaaS, PaaS, SaaS

**Q3.** You run a Windows Server VM in Azure. Who patches the operating system inside that VM?
- A. Microsoft
- B. You
- C. The hardware vendor
- D. Nobody, Azure patches it automatically in all cases
**Answer: B.** A VM is IaaS. You manage the OS, installed software and configuration.
Tag: 1.3 IaaS

**Q4.** A developer hosts a web app on Azure App Service. Which is TRUE about the operating system?
- A. The customer patches it
- B. Microsoft manages it
- C. It is shared 50/50
- D. There is no operating system
**Answer: B.** In PaaS, Microsoft manages the OS and runtime. You manage the app, its settings, data and access.
Tag: 1.1 Shared responsibility / 1.3 PaaS

**Q5.** A Nakuru logistics firm keeps customer records on its own servers but runs its public tracking website on Azure. Which cloud model is this?
- A. Public cloud only
- B. Private cloud only
- C. Hybrid cloud
- D. Multi-region
**Answer: C.** Hybrid combines on-premises or private resources with public cloud.
Tag: 1.1 Cloud models

**Q6.** A startup pays only for the compute it uses each hour, with no upfront hardware purchase. Which concept is this?
- A. Consumption-based model
- B. Reserved capacity
- C. Perpetual licensing
- D. Sovereign cloud
**Answer: A.** Consumption-based means pay for what you use.
Tag: 1.1 Consumption-based model

**Q7.** Which statement best describes serverless computing?
- A. There are no servers anywhere
- B. You write code and the platform runs it on demand, so you do not manage the servers
- C. You must buy servers in advance
- D. It can only run on-premises
**Answer: B.** Servers still exist, but Azure manages them. Azure Functions is an example.
Tag: 1.1 Serverless

**Q8.** A mobile-money app sees huge traffic every payday. Azure automatically adds instances then removes them later. Which benefit is this?
- A. Scalability
- B. Data sovereignty
- C. Governance
- D. Hybrid connectivity
**Answer: A.** Scalability (and elasticity) means matching resources to demand.
Tag: 1.2 High availability and scalability

**Q9.** Which benefit describes a system recovering from a failure and continuing to work?
- A. Predictability
- B. Reliability
- C. Manageability
- D. Governance
**Answer: B.** Reliability is resilience and recovery. Predictability is about stable performance and cost.
Tag: 1.2 Reliability and predictability

**Q10.** Which tool helps make COST predictable by estimating the price of services before you deploy?
- A. Azure Policy
- B. Pricing calculator
- C. Resource locks
- D. Azure Arc
**Answer: B.** The pricing calculator is free and works without signing in.
Tag: 1.2 Predictability / 3.1 Cost

**Q11.** Moving from buying servers to renting cloud resources mostly shifts spending from:
- A. Operational to capital expenditure
- B. Capital to operational expenditure
- C. Neither
- D. Taxes to subscriptions
**Answer: B.** CapEx (upfront purchases) shifts toward OpEx (ongoing pay-as-you-go). Note: CapEx/OpEx is a teaching aid and not an outline bullet.
Tag: 1.1 Compare cloud pricing models

**Q12.** Which model is used exclusively by a single organization?
- A. Public cloud
- B. Private cloud
- C. Community marketplace
- D. Hybrid-only
**Answer: B.** Private cloud serves one organization.
Tag: 1.1 Cloud models

**Q13.** Which service type gives you the MOST control over the operating system?
- A. SaaS
- B. PaaS
- C. IaaS
- D. Serverless
**Answer: C.** IaaS leaves the OS to you.
Tag: 1.3 IaaS, PaaS, SaaS

**Q14.** Using the Azure portal, CLI and templates to deploy and manage resources consistently is an example of which benefit?
- A. Manageability
- B. Latency
- C. Data residency
- D. Elasticity
**Answer: A.** Manageability covers managing resources through tools and automation.
Tag: 1.2 Manageability

**Q15.** In a SaaS solution, which of these is still the customer's responsibility?
- A. The datacenter building
- B. The physical servers
- C. Their user identities and data
- D. The application code written by Microsoft
**Answer: C.** Identities, data and configuration stay with the customer.
Tag: 1.1 Shared responsibility model

**Q16.** A company wants to deploy code without managing VMs or operating systems. Which service type is BEST?
- A. IaaS
- B. PaaS
- C. Colocation
- D. Private datacenter
**Answer: B.** PaaS removes VM and OS management.
Tag: 1.3 PaaS

---

## AREA 2: AZURE ARCHITECTURE AND SERVICES

**Q17.** What is an Azure region?
- A. A single rack of servers
- B. One or more datacenters connected by a low-latency network in a geographic area
- C. A billing account
- D. A type of subscription
**Answer: B.**
Tag: 2.1 Regions

**Q18.** Which statement about availability zones is TRUE?
- A. They are unconnected data lakes
- B. They are physically separate locations within a region with independent power, cooling and networking
- C. They exist only in sovereign clouds
- D. They are always paired with another region
**Answer: B.** Regions that support zones have at least three.
Tag: 2.1 Availability zones

**Q19.** Which is TRUE about region pairs?
- A. You can pick any two regions as a pair
- B. Microsoft defines the pairs; you cannot choose them
- C. Every region has a pair
- D. Pairs share one datacenter
**Answer: B.** Many newer regions are not paired.
Tag: 2.1 Region pairs

**Q20.** Which is the correct order from the broadest scope to the narrowest?
- A. Resource group > subscription > management group > resource
- B. Management group > subscription > resource group > resource
- C. Subscription > management group > resource > resource group
- D. Resource > resource group > subscription > management group
**Answer: B.**
Tag: 2.1 Hierarchy

**Q21.** You delete a resource group. What happens to the resources in it?
- A. Nothing
- B. They move to another group
- C. They are deleted
- D. They are archived
**Answer: C.**
Tag: 2.1 Resource groups

**Q22.** An organization wants to apply one policy across 40 subscriptions. What should it use?
- A. Resource group
- B. Management group
- C. Availability set
- D. Tag
**Answer: B.** Management groups sit above subscriptions and pass down access and policy.
Tag: 2.1 Management groups

**Q23.** You need a group of identical load-balanced VMs that scale out and in automatically. Which service?
- A. Availability set
- B. Virtual Machine Scale Sets
- C. Azure Files
- D. Azure Arc
**Answer: B.**
Tag: 2.2 VM options

**Q24.** Which feature spreads VMs across fault domains and update domains inside a datacenter to limit downtime from hardware failure and planned maintenance?
- A. Availability set
- B. Resource lock
- C. Private Link
- D. Subnet
**Answer: A.**
Tag: 2.2 VM options

**Q25.** Which service is best for small, event-driven code where you pay per execution and do not manage servers?
- A. Azure Functions
- B. A VM
- C. ExpressRoute
- D. Azure Files
**Answer: A.**
Tag: 2.2 Compare compute types

**Q26.** Azure Virtual Desktop offers which capability that is exclusive to it?
- A. Windows 11 Enterprise multi-session
- B. Hosting only Linux desktops
- C. Storing blobs
- D. Running DNS
**Answer: A.** Multiple users can share one VM.
Tag: 2.2 Azure Virtual Desktop

**Q27.** Which connection does NOT travel over the public internet?
- A. Site-to-site VPN
- B. Point-to-site VPN
- C. ExpressRoute
- D. HTTPS to a public website
**Answer: C.** ExpressRoute is a private connection through a connectivity provider.
Tag: 2.2 ExpressRoute

**Q28.** A remote worker needs an encrypted tunnel from a single laptop to an Azure virtual network. Which?
- A. Point-to-site VPN
- B. Site-to-site VPN
- C. ExpressRoute Direct
- D. Virtual network peering
**Answer: A.**
Tag: 2.2 VPN Gateway

**Q29.** You want private access from your virtual network to one specific Azure service instance, such as one storage account. Which feature?
- A. Azure Private Link
- B. Public IP address
- C. Resource lock
- D. Tag
**Answer: A.**
Tag: 2.2 Private and public endpoints

**Q30.** Rarely accessed data must be stored at the lowest storage cost and you accept hours of retrieval time. Which blob tier?
- A. Hot
- B. Cool
- C. Archive
- D. Premium
**Answer: C.** Archive is offline and must be rehydrated.
Tag: 2.3 Storage tiers

**Q31.** Which redundancy keeps copies across three or more availability zones in the primary region?
- A. LRS
- B. ZRS
- C. RA-GRS
- D. None of these
**Answer: B.**
Tag: 2.3 Redundancy

**Q32.** Which option lets you READ from the secondary region at any time?
- A. LRS
- B. ZRS
- C. GRS
- D. RA-GRS
**Answer: D.** Plain GRS secondaries are not readable unless failover happens.
Tag: 2.3 Redundancy

**Q33.** You must move many terabytes of data to Azure and the network is too slow. Which?
- A. Azure Data Box
- B. Azure Advisor
- C. Azure Policy
- D. Cloud Shell
**Answer: A.** Data Box is an offline physical transfer device.
Tag: 2.3 Migration options

**Q34.** Which service stores unstructured data such as images and backups as objects?
- A. Queue Storage
- B. Blob Storage
- C. Table Storage
- D. Azure Files
**Answer: B.**
Tag: 2.3 Compare storage services

**Q35.** Requiring a password plus a code from an authenticator app is an example of:
- A. Single sign-on
- B. Multifactor authentication
- C. Passwordless only
- D. Conditional deletion
**Answer: B.**
Tag: 2.4 Authentication methods

**Q36.** A policy states: if the sign-in is from an unknown country, require MFA. Which feature?
- A. Azure Policy
- B. Microsoft Entra Conditional Access
- C. Resource locks
- D. Azure Advisor
**Answer: B.**
Tag: 2.4 Conditional Access

**Q37.** You give a technician permission to restart VMs in one resource group only. Which feature?
- A. Azure RBAC
- B. Azure Policy
- C. Tags
- D. Azure Arc
**Answer: A.** Assign a role at the resource group scope.
Tag: 2.4 Azure RBAC

**Q38.** Which set matches the Zero Trust principles?
- A. Trust the network, trust users, trust devices
- B. Verify explicitly, use least-privilege access, assume breach
- C. Block everything
- D. Encrypt only data in transit
**Answer: B.**
Tag: 2.4 Zero Trust

**Q39.** An old application needs domain join and LDAP but you do not want to manage domain controllers. Which service?
- A. Microsoft Entra Domain Services
- B. Azure Cosmos DB
- C. Azure Monitor
- D. Azure Migrate
**Answer: A.**
Tag: 2.4 Directory services

**Q40.** Which service gives a secure score and recommendations for your cloud security posture across Azure and other clouds?
- A. Microsoft Defender for Cloud
- B. Azure Advisor only
- C. Service Health
- D. Azure DNS
**Answer: A.**
Tag: 2.4 Defender for Cloud

---

## AREA 3: AZURE MANAGEMENT AND GOVERNANCE

**Q41.** Which free tool estimates the cost of Azure services before you deploy?
- A. Pricing calculator
- B. Azure Monitor
- C. Resource Health
- D. Bicep
**Answer: A.**
Tag: 3.1 Pricing calculator

**Q42.** You tag a resource group with Environment=Prod. What happens to the resources inside by default?
- A. They automatically inherit it
- B. They do not inherit it
- C. They are deleted
- D. They are locked
**Answer: B.** Use Azure Policy to apply or enforce tags.
Tag: 3.1 Tags

**Q43.** Which Cost Management feature notifies you when spending nears a limit you set?
- A. Budget alerts
- B. Resource locks
- C. Availability zones
- D. Blueprints
**Answer: A.**
Tag: 3.1 Cost Management

**Q44.** Committing to a one-year or three-year term for specific resources to get a discount is called:
- A. Reservations
- B. Spot VMs
- C. Tagging
- D. Peering
**Answer: A.** Savings plans are another commitment option.
Tag: 3.1 Cost optimization

**Q45.** Which benefit lets you apply existing Windows Server or SQL Server licences to Azure to reduce cost?
- A. Azure Hybrid Benefit
- B. Azure Arc
- C. Conditional Access
- D. Region pairing
**Answer: A.**
Tag: 3.1 Reduce cost

**Q46.** Which Microsoft Purview area is about helping govern, protect and manage data wherever it lives?
- A. It is a DNS service
- B. It is a data governance, security and compliance solution set
- C. It is a VM size
- D. It is a billing report
**Answer: B.**
Tag: 3.2 Purview

**Q47.** Which service evaluates resources against rules such as "only allow these regions" and flags or blocks non-compliance?
- A. Azure Policy
- B. Azure RBAC
- C. Azure Advisor
- D. Azure CLI
**Answer: A.**
Tag: 3.2 Azure Policy

**Q48.** What is the main difference between Azure Policy and RBAC?
- A. Policy controls what users can do; RBAC checks resource compliance
- B. Policy checks resource state against rules; RBAC controls what actions a user may perform
- C. They are identical
- D. RBAC applies only to storage
**Answer: B.**
Tag: 3.2 Azure Policy vs RBAC

**Q49.** Which lock level lets users read and modify a resource but not delete it?
- A. ReadOnly
- B. CanNotDelete
- C. Archive
- D. Immutable
**Answer: B.**
Tag: 3.2 Resource locks

**Q50.** You apply a CanNotDelete lock to a resource group. What happens to resources in it?
- A. They inherit the lock
- B. They are unaffected
- C. They are deleted
- D. The lock is removed
**Answer: A.** Locks are inherited by child resources, including ones added later.
Tag: 3.2 Resource locks

**Q51.** A ReadOnly lock is on a storage account. Which statement is TRUE?
- A. It controls control plane operations, not data inside the account via the data plane
- B. It encrypts the data
- C. It deletes the account
- D. It blocks all reads
**Answer: A.** Locks apply to control plane operations only.
Tag: 3.2 Resource locks

**Q52.** Which tool is a browser-based terminal with Bash or PowerShell that signs you in automatically?
- A. Azure Cloud Shell
- B. Storage Explorer
- C. Azure Migrate
- D. Data Box
**Answer: A.**
Tag: 3.3 Cloud Shell

**Q53.** Which statement about Azure CLI and Azure PowerShell is TRUE?
- A. Only one can manage Azure
- B. Both call Azure Resource Manager to manage resources
- C. They only work in the portal
- D. They cannot create resource groups
**Answer: B.**
Tag: 3.3 CLI and PowerShell

**Q54.** Which service lets you manage on-premises servers and other clouds as if they were in Azure?
- A. Azure Arc
- B. Azure DNS
- C. Azure Files
- D. Azure Cloud Shell
**Answer: A.**
Tag: 3.3 Azure Arc

**Q55.** What does "declarative" mean for an ARM template?
- A. You list each step command in order
- B. You describe the desired end state and ARM works out how to deploy it
- C. You write C# code
- D. It cannot be repeated
**Answer: B.**
Tag: 3.3 ARM and ARM templates

**Q56.** Bicep is best described as:
- A. A VM size
- B. A declarative language for deploying Azure resources that compiles to ARM templates
- C. A monitoring dashboard
- D. A pricing tier
**Answer: B.**
Tag: 3.3 Infrastructure as code

**Q57.** Which tool gives personalized recommendations across reliability, security, performance, cost and operational excellence?
- A. Azure Advisor
- B. Azure Policy
- C. Azure Arc
- D. Azure Files
**Answer: A.**
Tag: 3.4 Azure Advisor

**Q58.** Which service tells you about the health of ONE specific virtual machine?
- A. Azure status
- B. Service Health
- C. Resource Health
- D. Pricing calculator
**Answer: C.** Azure status is global; Service Health is personalized to your services and regions.
Tag: 3.4 Service Health

**Q59.** Which language is used to query data in Log Analytics workspaces?
- A. SQL only
- B. Kusto Query Language (KQL)
- C. Python
- D. Bash
**Answer: B.**
Tag: 3.4 Azure Monitor / Log Analytics

**Q60.** Which Azure Monitor capability gives application performance monitoring for live web apps?
- A. Application Insights
- B. Azure DNS
- C. Azure Policy
- D. Data Box
**Answer: A.**
Tag: 3.4 Application Insights

---

## Builder Notes
- Answer positions are mixed but check them again if you shuffle.
- Q11 (CapEx/OpEx) is a teaching aid, not an outline bullet.
- Q44 and Q45: discount percentages deliberately left out because they change.
- Add a few of your own Kenyan-context questions in the same style, for example scenarios with SACCOs, matatu apps, M-Pesa-style traffic spikes, or Nakuru clinics.
