"""
Original AZ-900 Practice Questions Bank (60 Questions).
Covering:
- Area 1: Cloud Concepts (25-30%) - 16 Questions
- Area 2: Azure Architecture and Services (35-40%) - 23 Questions
- Area 3: Azure Management and Governance (30-35%) - 21 Questions
"""

from typing import List, Dict, Any

QUESTIONS: List[Dict[str, Any]] = [
    # AREA 1: CLOUD CONCEPTS
    {
        "id": 1,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Shared responsibility model",
        "q": "Your clinic moves its booking system to the cloud. Whichever service model you use, which item always remains YOUR responsibility?",
        "options": {
            "A": "The physical datacenter",
            "B": "Your data",
            "C": "The hypervisor",
            "D": "The physical network cabling"
        },
        "ans": "B",
        "why": "Data, identities, accounts, and configuration settings stay with the customer in every cloud model (IaaS, PaaS, SaaS). Physical hosts, networks, and datacenters always belong to Microsoft.",
        "traps": {
            "A": "The physical building/datacenter is always Microsoft's responsibility in the cloud.",
            "C": "The hypervisor (virtual machine monitor) is managed by Microsoft in all cloud models.",
            "D": "Physical network cabling inside the datacenter is handled entirely by Microsoft."
        }
    },
    {
        "id": 2,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.3 IaaS, PaaS, SaaS",
        "q": "A school wants to use a ready-made email and calendar service and manage nothing but its users and data. Which service type fits?",
        "options": {
            "A": "IaaS",
            "B": "PaaS",
            "C": "SaaS",
            "D": "On-premises"
        },
        "ans": "C",
        "why": "SaaS (Software as a Service) gives you a complete, ready-to-use application (such as Microsoft 365 or Google Workspace) where you only manage your users and data.",
        "traps": {
            "A": "IaaS requires you to manage operating systems, VM patching, and application installation.",
            "B": "PaaS is for developing and deploying custom code without managing servers, not ready-made software.",
            "D": "On-premises requires managing the entire physical and software stack yourself."
        }
    },
    {
        "id": 3,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.3 IaaS",
        "q": "You run a Windows Server VM in Azure. Who patches the operating system inside that VM?",
        "options": {
            "A": "Microsoft",
            "B": "You",
            "C": "The hardware vendor",
            "D": "Nobody, Azure patches it automatically in all cases"
        },
        "ans": "B",
        "why": "An Azure Virtual Machine is IaaS. You control the OS, configuration, and software, so you are responsible for patching it.",
        "traps": {
            "A": "Microsoft manages the physical host and hypervisor, but not the guest OS inside your IaaS VM.",
            "C": "The hardware vendor has no role inside Azure cloud infrastructure.",
            "D": "Azure does not automatically patch IaaS VMs unless you configure specific update management services."
        }
    },
    {
        "id": 4,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Shared responsibility / 1.3 PaaS",
        "q": "A developer hosts a web app on Azure App Service. Which is TRUE about the operating system?",
        "options": {
            "A": "The customer patches it",
            "B": "Microsoft manages it",
            "C": "It is shared 50/50",
            "D": "There is no operating system"
        },
        "ans": "B",
        "why": "In PaaS (like Azure App Service), Microsoft manages the underlying OS, hardware, and web server runtime. You only manage your application code and configuration.",
        "traps": {
            "A": "In PaaS, customers do not manage or patch the operating system.",
            "C": "OS maintenance is strictly Microsoft's responsibility in PaaS.",
            "D": "An OS exists, but it is abstracted away and managed by the cloud provider."
        }
    },
    {
        "id": 5,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Cloud models",
        "q": "A Nakuru logistics firm keeps customer records on its own servers but runs its public tracking website on Azure. Which cloud model is this?",
        "options": {
            "A": "Public cloud only",
            "B": "Private cloud only",
            "C": "Hybrid cloud",
            "D": "Multi-region"
        },
        "ans": "C",
        "why": "Hybrid cloud connects on-premises private infrastructure with public cloud services, allowing data and apps to be shared between them.",
        "traps": {
            "A": "It is not public cloud only because sensitive customer records are held on-premises.",
            "B": "It is not private cloud only because the public web app runs on Azure.",
            "D": "Multi-region refers to geographic distribution inside a cloud provider, not an on-prem + cloud mix."
        }
    },
    {
        "id": 6,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Consumption-based model",
        "q": "A startup pays only for the compute it uses each hour, with no upfront hardware purchase. Which concept is this?",
        "options": {
            "A": "Consumption-based model",
            "B": "Reserved capacity",
            "C": "Perpetual licensing",
            "D": "Sovereign cloud"
        },
        "ans": "A",
        "why": "A consumption-based model means paying only for the exact resources (compute, storage, bandwidth) you consume, similar to buying electricity tokens or airtime bundles.",
        "traps": {
            "B": "Reserved capacity commits you to 1- or 3-year upfront or scheduled commitments.",
            "C": "Perpetual licensing involves traditional upfront permanent software purchases.",
            "D": "Sovereign cloud is a dedicated cloud region for government or strict compliance needs."
        }
    },
    {
        "id": 7,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Serverless",
        "q": "Which statement best describes serverless computing?",
        "options": {
            "A": "There are no servers anywhere",
            "B": "You write code and the platform runs it on demand, so you do not manage the servers",
            "C": "You must buy servers in advance",
            "D": "It can only run on-premises"
        },
        "ans": "B",
        "why": "Serverless code (like Azure Functions) runs in response to events; Azure provisions and scales the underlying compute automatically, so you never manage servers.",
        "traps": {
            "A": "Servers definitely exist; they are simply abstracted away and managed by Microsoft.",
            "C": "Buying servers in advance is the opposite of serverless.",
            "D": "Serverless is primarily a cloud computing paradigm."
        }
    },
    {
        "id": 8,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.2 High availability and scalability",
        "q": "A mobile-money app sees huge traffic every payday. Azure automatically adds instances then removes them later. Which benefit is this?",
        "options": {
            "A": "Scalability",
            "B": "Data sovereignty",
            "C": "Governance",
            "D": "Hybrid connectivity"
        },
        "ans": "A",
        "why": "Scalability (and elasticity) refers to allocating resources dynamically to match surging demand and de-allocating them when traffic subsides.",
        "traps": {
            "B": "Data sovereignty is about keeping data within specific national legal boundaries.",
            "C": "Governance involves policies, resource locks, and compliance enforcement.",
            "D": "Hybrid connectivity connects on-premises networks to Azure."
        }
    },
    {
        "id": 9,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.2 Reliability and predictability",
        "q": "Which benefit describes a system recovering from a failure and continuing to work?",
        "options": {
            "A": "Predictability",
            "B": "Reliability",
            "C": "Manageability",
            "D": "Governance"
        },
        "ans": "B",
        "why": "Reliability is the ability of a system to recover from failures and continue functioning resiliently. Predictability relates to steady performance and transparent costs.",
        "traps": {
            "A": "Predictability focuses on expected performance and consistent costs.",
            "C": "Manageability focuses on administration via portal, CLI, and automated templates.",
            "D": "Governance focuses on enforcing standards and compliance."
        }
    },
    {
        "id": 10,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.2 Predictability / 3.1 Cost",
        "q": "Which tool helps make COST predictable by estimating the price of services before you deploy?",
        "options": {
            "A": "Azure Policy",
            "B": "Pricing calculator",
            "C": "Resource locks",
            "D": "Azure Arc"
        },
        "ans": "B",
        "why": "The Azure Pricing Calculator is a free web tool that allows anyone to estimate expected monthly service costs without signing in.",
        "traps": {
            "A": "Azure Policy enforces resource configuration rules, not cost estimation.",
            "C": "Resource locks prevent accidental deletion or modification.",
            "D": "Azure Arc extends Azure management to hybrid and multicloud environments."
        }
    },
    {
        "id": 11,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Compare cloud pricing models",
        "q": "Moving from buying servers to renting cloud resources mostly shifts spending from:",
        "options": {
            "A": "Operational to capital expenditure",
            "B": "Capital to operational expenditure",
            "C": "Neither",
            "D": "Taxes to subscriptions"
        },
        "ans": "B",
        "why": "CapEx (Capital Expenditure) means large upfront purchases of hardware. OpEx (Operational Expenditure) means ongoing pay-as-you-go operating expenses.",
        "traps": {
            "A": "This is the reverse; on-premises is CapEx, cloud shifts towards OpEx.",
            "C": "There is a distinct financial shift between CapEx and OpEx.",
            "D": "Taxes and subscriptions is not the cloud economic accounting model."
        }
    },
    {
        "id": 12,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Cloud models",
        "q": "Which model is used exclusively by a single organization?",
        "options": {
            "A": "Public cloud",
            "B": "Private cloud",
            "C": "Community marketplace",
            "D": "Hybrid-only"
        },
        "ans": "B",
        "why": "A private cloud provides computing resources used exclusively by one enterprise or organization, physically located at the company's datacenter or hosted by a third party.",
        "traps": {
            "A": "Public clouds are owned and operated by third-party providers and shared multitenant.",
            "C": "A marketplace is a public catalog of commercial software and offerings.",
            "D": "Hybrid combines both public and private infrastructures."
        }
    },
    {
        "id": 13,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.3 IaaS, PaaS, SaaS",
        "q": "Which service type gives you the MOST control over the operating system?",
        "options": {
            "A": "SaaS",
            "B": "PaaS",
            "C": "IaaS",
            "D": "Serverless"
        },
        "ans": "C",
        "why": "IaaS (Infrastructure as a Service) gives you virtual machines where you select, configure, update, and manage the guest operating system directly.",
        "traps": {
            "A": "SaaS provides ready-to-use software with zero access to the underlying OS.",
            "B": "PaaS abstracts the OS away completely so you focus only on app code.",
            "D": "Serverless abstracts both the OS and server management away completely."
        }
    },
    {
        "id": 14,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.2 Manageability",
        "q": "Using the Azure portal, CLI and templates to deploy and manage resources consistently is an example of which benefit?",
        "options": {
            "A": "Manageability",
            "B": "Latency",
            "C": "Data residency",
            "D": "Elasticity"
        },
        "ans": "A",
        "why": "Manageability refers to the ability to manage, scale, and automate cloud resources consistently via web portals, command-line interfaces, and templates.",
        "traps": {
            "B": "Latency is network round-trip response time.",
            "C": "Data residency is about storing data inside designated geographic borders.",
            "D": "Elasticity is the automatic scaling out/in of resources based on workload."
        }
    },
    {
        "id": 15,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.1 Shared responsibility model",
        "q": "In a SaaS solution, which of these is still the customer's responsibility?",
        "options": {
            "A": "The datacenter building",
            "B": "The physical servers",
            "C": "Their user identities and data",
            "D": "The application code written by Microsoft"
        },
        "ans": "C",
        "why": "In every cloud service model (IaaS, PaaS, and SaaS), customer data, account identities, and device access settings ALWAYS remain the customer's responsibility.",
        "traps": {
            "A": "The physical datacenter is 100% Microsoft's responsibility in SaaS.",
            "B": "Physical server hardware is managed by Microsoft.",
            "D": "In SaaS, the application code is provided and maintained by the SaaS provider."
        }
    },
    {
        "id": 16,
        "area": "Area 1: Cloud Concepts",
        "tag": "1.3 PaaS",
        "q": "A company wants to deploy code without managing VMs or operating systems. Which service type is BEST?",
        "options": {
            "A": "IaaS",
            "B": "PaaS",
            "C": "Colocation",
            "D": "Private datacenter"
        },
        "ans": "B",
        "why": "PaaS (Platform as a Service) is specifically engineered for developers to deploy apps without worrying about provisioning VMs, OS patching, or server management.",
        "traps": {
            "A": "IaaS forces you to configure, maintain, and patch virtual machines.",
            "C": "Colocation involves renting physical rack space for your own servers.",
            "D": "A private datacenter requires complete hardware and facility ownership."
        }
    },

    # AREA 2: AZURE ARCHITECTURE AND SERVICES
    {
        "id": 17,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.1 Regions",
        "q": "What is an Azure region?",
        "options": {
            "A": "A single rack of servers",
            "B": "One or more datacenters connected by a low-latency network in a geographic area",
            "C": "A billing account",
            "D": "A type of subscription"
        },
        "ans": "B",
        "why": "An Azure region is a geographical perimeter containing one or more datacenters networked together with dedicated low-latency connectivity.",
        "traps": {
            "A": "A rack of servers is just one piece of hardware inside a datacenter.",
            "C": "A billing account is a financial construct, not a physical location.",
            "D": "A subscription is a management and billing boundary for resources."
        }
    },
    {
        "id": 18,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.1 Availability zones",
        "q": "Which statement about availability zones is TRUE?",
        "options": {
            "A": "They are unconnected data lakes",
            "B": "They are physically separate locations within a region with independent power, cooling and networking",
            "C": "They exist only in sovereign clouds",
            "D": "They are always paired with another region"
        },
        "ans": "B",
        "why": "Availability Zones are physically distinct datacenters within an Azure region, each equipped with independent power, cooling, and network links. Regions that support zones have at least three.",
        "traps": {
            "A": "They are datacenters, not data lakes.",
            "C": "Availability Zones exist across global commercial Azure regions.",
            "D": "Region pairs are different geographical regions hundreds of miles apart, not zones."
        }
    },
    {
        "id": 19,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.1 Region pairs",
        "q": "Which is TRUE about region pairs?",
        "options": {
            "A": "You can pick any two regions as a pair",
            "B": "Microsoft defines the pairs; you cannot choose them",
            "C": "Every region has a pair",
            "D": "Pairs share one datacenter"
        },
        "ans": "B",
        "why": "Microsoft permanently pairs specific regions within the same geography (at least 300 miles apart) for disaster recovery; users cannot define their own pairs, and newer regions often rely on zones instead.",
        "traps": {
            "A": "Customers cannot customize or choose region pairings.",
            "C": "Many newer Azure regions are unpaired and rely on Availability Zones.",
            "D": "Pairs are separated by hundreds of miles; they never share a datacenter."
        }
    },
    {
        "id": 20,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.1 Hierarchy",
        "q": "Which is the correct order from the broadest scope to the narrowest?",
        "options": {
            "A": "Resource group > subscription > management group > resource",
            "B": "Management group > subscription > resource group > resource",
            "C": "Subscription > management group > resource > resource group",
            "D": "Resource > resource group > subscription > management group"
        },
        "ans": "B",
        "why": "The Azure Resource Manager hierarchy flows top-down: Management Groups > Subscriptions > Resource Groups > Individual Resources.",
        "traps": {
            "A": "Management groups sit above subscriptions, not below resource groups.",
            "C": "Management groups are broader than subscriptions.",
            "D": "This is ordered from narrowest to broadest."
        }
    },
    {
        "id": 21,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.1 Resource groups",
        "q": "You delete a resource group. What happens to the resources in it?",
        "options": {
            "A": "Nothing",
            "B": "They move to another group",
            "C": "They are deleted",
            "D": "They are archived"
        },
        "ans": "C",
        "why": "A resource group is a lifecycle container. Deleting a resource group automatically deletes all resources contained inside it.",
        "traps": {
            "A": "Resources do not remain intact when their parent resource group is deleted.",
            "B": "Resources are never automatically migrated to another resource group upon deletion.",
            "D": "Azure does not archive resources on deletion; they are permanently deprovisioned."
        }
    },
    {
        "id": 22,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.1 Management groups",
        "q": "An organization wants to apply one policy across 40 subscriptions. What should it use?",
        "options": {
            "A": "Resource group",
            "B": "Management group",
            "C": "Availability set",
            "D": "Tag"
        },
        "ans": "B",
        "why": "Management groups allow you to manage access, policy, and compliance across multiple subscriptions simultaneously through inheritance.",
        "traps": {
            "A": "A resource group exists inside a single subscription; it cannot span across subscriptions.",
            "C": "An availability set is a VM resilience feature inside a datacenter.",
            "D": "A tag is metadata and cannot enforce compliance policies across subscriptions."
        }
    },
    {
        "id": 23,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 VM options",
        "q": "You need a group of identical load-balanced VMs that scale out and in automatically. Which service?",
        "options": {
            "A": "Availability set",
            "B": "Virtual Machine Scale Sets",
            "C": "Azure Files",
            "D": "Azure Arc"
        },
        "ans": "B",
        "why": "Virtual Machine Scale Sets (VMSS) let you deploy and manage a group of identical, load-balanced VMs that automatically increase or decrease instance count based on demand or schedule.",
        "traps": {
            "A": "Availability sets improve fault domain resilience, but do not provide autoscale.",
            "C": "Azure Files is a cloud SMB/NFS file share service.",
            "D": "Azure Arc connects on-premises and multicloud infrastructure to ARM."
        }
    },
    {
        "id": 24,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 VM options",
        "q": "Which feature spreads VMs across fault domains and update domains inside a datacenter to limit downtime from hardware failure and planned maintenance?",
        "options": {
            "A": "Availability set",
            "B": "Resource lock",
            "C": "Private Link",
            "D": "Subnet"
        },
        "ans": "A",
        "why": "An Availability Set distributes VMs across multiple fault domains (power/switch failure points) and update domains (planned host reboots) within a datacenter.",
        "traps": {
            "B": "Resource locks prevent deletion or modification of resources.",
            "C": "Private Link provides private IP connectivity to PaaS services.",
            "D": "A subnet is an IP range partition inside an Azure Virtual Network."
        }
    },
    {
        "id": 25,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 Compare compute types",
        "q": "Which service is best for small, event-driven code where you pay per execution and do not manage servers?",
        "options": {
            "A": "Azure Functions",
            "B": "A VM",
            "C": "ExpressRoute",
            "D": "Azure Files"
        },
        "ans": "A",
        "why": "Azure Functions is Azure's serverless compute service, triggering code on demand (events/HTTP/queues) and billing only for execution duration.",
        "traps": {
            "B": "A VM requires continuous server and OS management and continuous runtime cost.",
            "C": "ExpressRoute is a dedicated private network connection provider.",
            "D": "Azure Files is a storage service."
        }
    },
    {
        "id": 26,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 Azure Virtual Desktop",
        "q": "Azure Virtual Desktop offers which capability that is exclusive to it?",
        "options": {
            "A": "Windows 11 Enterprise multi-session",
            "B": "Hosting only Linux desktops",
            "C": "Storing blobs",
            "D": "Running DNS"
        },
        "ans": "A",
        "why": "Windows 11 and Windows 10 Enterprise multi-session is exclusive to Azure Virtual Desktop, allowing multiple concurrent users to share a single VM session host to significantly cut costs.",
        "traps": {
            "B": "AVD supports Windows and Linux workloads, but multi-session is Windows-specific.",
            "C": "Blob Storage stores blobs, not AVD.",
            "D": "Azure DNS manages domain name resolution."
        }
    },
    {
        "id": 27,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 ExpressRoute",
        "q": "Which connection does NOT travel over the public internet?",
        "options": {
            "A": "Site-to-site VPN",
            "B": "Point-to-site VPN",
            "C": "ExpressRoute",
            "D": "HTTPS to a public website"
        },
        "ans": "C",
        "why": "ExpressRoute establishes a dedicated, private Layer 3 connection from your on-premises datacenter to Azure through a connectivity provider, completely bypassing the public internet.",
        "traps": {
            "A": "Site-to-site VPN sends encrypted traffic over the public internet.",
            "B": "Point-to-site VPN sends encrypted traffic over the public internet.",
            "D": "Public websites communicate over the public internet."
        }
    },
    {
        "id": 28,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 VPN Gateway",
        "q": "A remote worker needs an encrypted tunnel from a single laptop to an Azure virtual network. Which?",
        "options": {
            "A": "Point-to-site VPN",
            "B": "Site-to-site VPN",
            "C": "ExpressRoute Direct",
            "D": "Virtual network peering"
        },
        "ans": "A",
        "why": "A Point-to-Site (P2S) VPN connection connects an individual client device (laptop/PC) securely to an Azure Virtual Network over the internet.",
        "traps": {
            "B": "Site-to-Site (S2S) connects an entire branch office or on-premises network gateway to Azure.",
            "C": "ExpressRoute Direct connects 10/100 Gbps enterprise datacenters to Microsoft routers.",
            "D": "Virtual network peering connects two Azure virtual networks together."
        }
    },
    {
        "id": 29,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.2 Private and public endpoints",
        "q": "You want private access from your virtual network to one specific Azure service instance, such as one storage account. Which feature?",
        "options": {
            "A": "Azure Private Link",
            "B": "Public IP address",
            "C": "Resource lock",
            "D": "Tag"
        },
        "ans": "A",
        "why": "Azure Private Link provides private connectivity to a specific Azure PaaS instance via a private IP address located within your virtual network.",
        "traps": {
            "B": "A Public IP exposes the service endpoint to the public internet.",
            "C": "A resource lock protects resources from deletion or modification.",
            "D": "A tag is metadata used for taxonomy and cost allocation."
        }
    },
    {
        "id": 30,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.3 Storage tiers",
        "q": "Rarely accessed data must be stored at the lowest storage cost and you accept hours of retrieval time. Which blob tier?",
        "options": {
            "A": "Hot",
            "B": "Cool",
            "C": "Archive",
            "D": "Premium"
        },
        "ans": "C",
        "why": "The Archive tier offers the lowest storage cost and highest retrieval cost. It is an offline tier with a 180-day minimum retention and rehydration time that can take up to 15 hours.",
        "traps": {
            "A": "Hot has the highest storage cost with millisecond retrieval for active data.",
            "B": "Cool is an online tier for data accessed infrequently (minimum 30 days).",
            "D": "Premium offers ultra-low latency SSD block storage at higher storage cost."
        }
    },
    {
        "id": 31,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.3 Redundancy",
        "q": "Which redundancy keeps copies across three or more availability zones in the primary region?",
        "options": {
            "A": "LRS",
            "B": "ZRS",
            "C": "RA-GRS",
            "D": "None of these"
        },
        "ans": "B",
        "why": "ZRS (Zone-Redundant Storage) synchronously replicates your data across three Azure availability zones in the primary region, providing at least 12 nines (99.9999999999%) of durability.",
        "traps": {
            "A": "LRS copies data three times within a single datacenter in the primary region.",
            "C": "RA-GRS copies to a paired secondary region, but uses LRS locally in both regions.",
            "D": "ZRS is the exact matching option."
        }
    },
    {
        "id": 32,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.3 Redundancy",
        "q": "Which option lets you READ from the secondary region at any time?",
        "options": {
            "A": "LRS",
            "B": "ZRS",
            "C": "GRS",
            "D": "RA-GRS"
        },
        "ans": "D",
        "why": "RA-GRS (Read-Access Geo-Redundant Storage) allows read access to your replicated data in the secondary region even when the primary region is functioning normally.",
        "traps": {
            "A": "LRS is local to a single datacenter.",
            "B": "ZRS is local to availability zones within one primary region.",
            "C": "Standard GRS keeps the secondary region inaccessible for reads until an explicit failover."
        }
    },
    {
        "id": 33,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.3 Migration options",
        "q": "You must move many terabytes of data to Azure and the network is too slow. Which?",
        "options": {
            "A": "Azure Data Box",
            "B": "Azure Advisor",
            "C": "Azure Policy",
            "D": "Cloud Shell"
        },
        "ans": "A",
        "why": "Azure Data Box is a ruggedized physical storage appliance (up to ~80 TB) shipped to your facility, loaded offline over local network, and returned to Microsoft to ingest into Azure.",
        "traps": {
            "B": "Azure Advisor provides optimization recommendations.",
            "C": "Azure Policy audits and enforces governance rules.",
            "D": "Cloud Shell is a browser-based admin terminal."
        }
    },
    {
        "id": 34,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.3 Compare storage services",
        "q": "Which service stores unstructured data such as images and backups as objects?",
        "options": {
            "A": "Queue Storage",
            "B": "Blob Storage",
            "C": "Table Storage",
            "D": "Azure Files"
        },
        "ans": "B",
        "why": "Azure Blob Storage is Microsoft's object storage solution optimized for storing massive amounts of unstructured data such as text, images, videos, and backup archives.",
        "traps": {
            "A": "Queue Storage is used for asynchronous application messaging (up to 64 KB).",
            "C": "Table Storage is a NoSQL key-value attribute store.",
            "D": "Azure Files provides managed SMB/NFS file shares mounted like network drives."
        }
    },
    {
        "id": 35,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.4 Authentication methods",
        "q": "Requiring a password plus a code from an authenticator app is an example of:",
        "options": {
            "A": "Single sign-on",
            "B": "Multifactor authentication",
            "C": "Passwordless only",
            "D": "Conditional deletion"
        },
        "ans": "B",
        "why": "Multifactor authentication (MFA) requires two or more distinct verification factors: something you know (password) and something you have (phone/authenticator app).",
        "traps": {
            "A": "Single Sign-On (SSO) allows logging in once to access multiple applications.",
            "C": "Passwordless eliminates passwords altogether (e.g. FIDO2 security keys, Windows Hello).",
            "D": "Conditional deletion is a made-up term."
        }
    },
    {
        "id": 36,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.4 Conditional Access",
        "q": "A policy states: if the sign-in is from an unknown country, require MFA. Which feature?",
        "options": {
            "A": "Azure Policy",
            "B": "Microsoft Entra Conditional Access",
            "C": "Resource locks",
            "D": "Azure Advisor"
        },
        "ans": "B",
        "why": "Microsoft Entra Conditional Access uses if-then statements: evaluating signals (location, user risk, device state) and enforcing decisions (block, or allow with MFA).",
        "traps": {
            "A": "Azure Policy governs Azure infrastructure resources, not user identity sign-ins.",
            "C": "Resource locks prevent deletion or modification of Azure resources.",
            "D": "Azure Advisor gives cloud best-practice recommendations."
        }
    },
    {
        "id": 37,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.4 Azure RBAC",
        "q": "You give a technician permission to restart VMs in one resource group only. Which feature?",
        "options": {
            "A": "Azure RBAC",
            "B": "Azure Policy",
            "C": "Tags",
            "D": "Azure Arc"
        },
        "ans": "A",
        "why": "Azure Role-Based Access Control (RBAC) allows you to grant granular permissions (such as VM Contributor or custom restart actions) scoped specifically to a Resource Group.",
        "traps": {
            "B": "Azure Policy enforces resource compliance properties, not user permissions.",
            "C": "Tags are metadata labels for categorization and billing.",
            "D": "Azure Arc extends Azure control plane to external infrastructure."
        }
    },
    {
        "id": 38,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.4 Zero Trust",
        "q": "Which set matches the Zero Trust principles?",
        "options": {
            "A": "Trust the network, trust users, trust devices",
            "B": "Verify explicitly, use least-privilege access, assume breach",
            "C": "Block everything",
            "D": "Encrypt only data in transit"
        },
        "ans": "B",
        "why": "The three foundational Zero Trust principles defined by Microsoft are: 1. Verify explicitly, 2. Use least-privilege access, and 3. Assume breach.",
        "traps": {
            "A": "Zero Trust assumes no user, device, or network is implicitly trusted.",
            "C": "Zero Trust validates and facilitates secure access rather than blocking all activity.",
            "D": "Zero Trust requires end-to-end encryption for data both in transit and at rest."
        }
    },
    {
        "id": 39,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.4 Directory services",
        "q": "An old application needs domain join and LDAP but you do not want to manage domain controllers. Which service?",
        "options": {
            "A": "Microsoft Entra Domain Services",
            "B": "Azure Cosmos DB",
            "C": "Azure Monitor",
            "D": "Azure Migrate"
        },
        "ans": "A",
        "why": "Microsoft Entra Domain Services provides managed Active Directory services (domain join, Group Policy, LDAP, Kerberos/NTLM) without requiring you to deploy or patch domain controllers.",
        "traps": {
            "B": "Cosmos DB is a globally distributed NoSQL database.",
            "C": "Azure Monitor is a telemetry collection and observability service.",
            "D": "Azure Migrate is an assessment and migration tool."
        }
    },
    {
        "id": 40,
        "area": "Area 2: Azure Architecture and Services",
        "tag": "2.4 Defender for Cloud",
        "q": "Which service gives a secure score and recommendations for your cloud security posture across Azure and other clouds?",
        "options": {
            "A": "Microsoft Defender for Cloud",
            "B": "Azure Advisor only",
            "C": "Service Health",
            "D": "Azure DNS"
        },
        "ans": "A",
        "why": "Microsoft Defender for Cloud is a Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) providing a unified Secure Score across Azure, AWS, and GCP.",
        "traps": {
            "B": "Azure Advisor gives general operational/cost advice, but Defender for Cloud is the dedicated security posture tool.",
            "C": "Service Health informs you about Azure outages and planned maintenance.",
            "D": "Azure DNS provides domain hosting and resolution."
        }
    },

    # AREA 3: AZURE MANAGEMENT AND GOVERNANCE
    {
        "id": 41,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.1 Pricing calculator",
        "q": "Which free tool estimates the cost of Azure services before you deploy?",
        "options": {
            "A": "Pricing calculator",
            "B": "Azure Monitor",
            "C": "Resource Health",
            "D": "Bicep"
        },
        "ans": "A",
        "why": "The Azure Pricing Calculator is a free public web tool used to estimate expected service costs based on selected regions, SKUs, and usage tiers before deployment.",
        "traps": {
            "B": "Azure Monitor tracks logs and metrics of running resources.",
            "C": "Resource Health tracks the uptime and availability of individual resources.",
            "D": "Bicep is an infrastructure-as-code template language."
        }
    },
    {
        "id": 42,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.1 Tags",
        "q": "You tag a resource group with Environment=Prod. What happens to the resources inside by default?",
        "options": {
            "A": "They automatically inherit it",
            "B": "They do not inherit it",
            "C": "They are deleted",
            "D": "They are locked"
        },
        "ans": "B",
        "why": "Tags applied to a resource group are NOT inherited by the resources inside by default. To enforce tag inheritance, you must configure an Azure Policy rule.",
        "traps": {
            "A": "Resource tags do not automatically propagate downwards unlike RBAC permissions or locks.",
            "C": "Tagging does not trigger deletion.",
            "D": "Tagging does not lock resources."
        }
    },
    {
        "id": 43,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.1 Cost Management",
        "q": "Which Cost Management feature notifies you when spending nears a limit you set?",
        "options": {
            "A": "Budget alerts",
            "B": "Resource locks",
            "C": "Availability zones",
            "D": "Blueprints"
        },
        "ans": "A",
        "why": "Budget alerts in Microsoft Cost Management notify administrators when spending reaches predefined monetary or percentage thresholds of an assigned budget.",
        "traps": {
            "B": "Resource locks protect against deletions and updates, not spending thresholds.",
            "C": "Availability zones are physical datacenter clusters.",
            "D": "Blueprints was an environment orchestration tool (now transitioning to template specs)."
        }
    },
    {
        "id": 44,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.1 Cost optimization",
        "q": "Committing to a one-year or three-year term for specific resources to get a discount is called:",
        "options": {
            "A": "Reservations",
            "B": "Spot VMs",
            "C": "Tagging",
            "D": "Peering"
        },
        "ans": "A",
        "why": "Azure Reservations (and Savings Plans) give substantial discounts off pay-as-you-go rates in exchange for a committed 1-year or 3-year term of consistent usage.",
        "traps": {
            "B": "Spot VMs provide discounts on unused spare capacity that Azure can evict at any time.",
            "C": "Tagging organizes resources for cost reporting.",
            "D": "Peering connects virtual networks."
        }
    },
    {
        "id": 45,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.1 Reduce cost",
        "q": "Which benefit lets you apply existing Windows Server or SQL Server licences to Azure to reduce cost?",
        "options": {
            "A": "Azure Hybrid Benefit",
            "B": "Azure Arc",
            "C": "Conditional Access",
            "D": "Region pairing"
        },
        "ans": "A",
        "why": "Azure Hybrid Benefit allows organizations with active Software Assurance on on-premises Windows Server or SQL Server licenses to bring those licenses to Azure, significantly reducing VM compute charges.",
        "traps": {
            "B": "Azure Arc manages hybrid infrastructure, but is not the licensing discount program.",
            "C": "Conditional Access is an Entra ID security policy engine.",
            "D": "Region pairing is a disaster recovery architecture."
        }
    },
    {
        "id": 46,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.2 Purview",
        "q": "Which Microsoft Purview area is about helping govern, protect and manage data wherever it lives?",
        "options": {
            "A": "It is a DNS service",
            "B": "It is a data governance, security and compliance solution set",
            "C": "It is a VM size",
            "D": "It is a billing report"
        },
        "ans": "B",
        "why": "Microsoft Purview is a comprehensive family of solutions encompassing data governance (data maps, catalogs), data security, and compliance across on-premises, multicloud, and SaaS data.",
        "traps": {
            "A": "DNS is handled by Azure DNS and Traffic Manager.",
            "C": "Purview is not related to virtual machine compute sizes.",
            "D": "Billing reports are managed within Microsoft Cost Management."
        }
    },
    {
        "id": 47,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.2 Azure Policy",
        "q": "Which service evaluates resources against rules such as 'only allow these regions' and flags or blocks non-compliance?",
        "options": {
            "A": "Azure Policy",
            "B": "Azure RBAC",
            "C": "Azure Advisor",
            "D": "Azure CLI"
        },
        "ans": "A",
        "why": "Azure Policy evaluates resource configurations against business rules declared in JSON (e.g. allowed locations, allowed VM SKUs) and can audit or deny non-compliant deployments.",
        "traps": {
            "B": "Azure RBAC controls what users are authorized to do, not whether the resource conforms to organizational compliance rules.",
            "C": "Azure Advisor provides best-practice tips, but cannot enforce or block deployments.",
            "D": "Azure CLI is a command line tool."
        }
    },
    {
        "id": 48,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.2 Azure Policy vs RBAC",
        "q": "What is the main difference between Azure Policy and RBAC?",
        "options": {
            "A": "Policy controls what users can do; RBAC checks resource compliance",
            "B": "Policy checks resource state against rules; RBAC controls what actions a user may perform",
            "C": "They are identical",
            "D": "RBAC applies only to storage"
        },
        "ans": "B",
        "why": "Azure Policy inspects resource properties against rules regardless of user permissions; Azure RBAC determines what actions a specific user or identity can perform at a given scope.",
        "traps": {
            "A": "This swaps their definitions.",
            "C": "They are distinct, complementary governance mechanisms.",
            "D": "RBAC applies to all Azure Resource Manager resources, not just storage."
        }
    },
    {
        "id": 49,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.2 Resource locks",
        "q": "Which lock level lets users read and modify a resource but not delete it?",
        "options": {
            "A": "ReadOnly",
            "B": "CanNotDelete",
            "C": "Archive",
            "D": "Immutable"
        },
        "ans": "B",
        "why": "A CanNotDelete (Delete in portal) lock allows authorized users to read and modify a resource, but prevents anyone from deleting it.",
        "traps": {
            "A": "ReadOnly blocks both modification and deletion.",
            "C": "Archive is a storage access tier.",
            "D": "Immutable storage is a blob feature for WORM (Write Once, Read Many) compliance."
        }
    },
    {
        "id": 50,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.2 Resource locks",
        "q": "You apply a CanNotDelete lock to a resource group. What happens to resources in it?",
        "options": {
            "A": "They inherit the lock",
            "B": "They are unaffected",
            "C": "They are deleted",
            "D": "The lock is removed"
        },
        "ans": "A",
        "why": "Resource locks are inherited by all child resources inside that scope, including any new resources deployed later into that resource group.",
        "traps": {
            "B": "Child resources are definitely protected through inheritance.",
            "C": "Locks never cause resource deletion.",
            "D": "Locks remain in effect until explicitly removed by an Owner."
        }
    },
    {
        "id": 51,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.2 Resource locks",
        "q": "A ReadOnly lock is on a storage account. Which statement is TRUE?",
        "options": {
            "A": "It controls control plane operations, not data inside the account via the data plane",
            "B": "It encrypts the data",
            "C": "It deletes the account",
            "D": "It blocks all reads"
        },
        "ans": "A",
        "why": "Resource locks apply strictly to the Azure Resource Manager control plane (managing the account), not to data plane operations (reading/writing blobs within containers).",
        "traps": {
            "B": "Locks do not perform encryption.",
            "C": "A ReadOnly lock prevents deletion.",
            "D": "ReadOnly allows reading configuration and properties."
        }
    },
    {
        "id": 52,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.3 Cloud Shell",
        "q": "Which tool is a browser-based terminal with Bash or PowerShell that signs you in automatically?",
        "options": {
            "A": "Azure Cloud Shell",
            "B": "Storage Explorer",
            "C": "Azure Migrate",
            "D": "Data Box"
        },
        "ans": "A",
        "why": "Azure Cloud Shell is an authenticated, browser-accessible terminal providing both Bash and PowerShell experiences pre-configured with popular command-line tools.",
        "traps": {
            "B": "Azure Storage Explorer is a desktop GUI application for managing files and blobs.",
            "C": "Azure Migrate is an assessment and migration tool.",
            "D": "Data Box is a physical data transfer appliance."
        }
    },
    {
        "id": 53,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.3 CLI and PowerShell",
        "q": "Which statement about Azure CLI and Azure PowerShell is TRUE?",
        "options": {
            "A": "Only one can manage Azure",
            "B": "Both call Azure Resource Manager to manage resources",
            "C": "They only work in the portal",
            "D": "They cannot create resource groups"
        },
        "ans": "B",
        "why": "Both Azure CLI and Azure PowerShell are cross-platform command-line tools that execute requests against the Azure Resource Manager (ARM) REST APIs.",
        "traps": {
            "A": "Both tools are fully supported for Azure resource management.",
            "C": "Both can be installed locally on Windows, macOS, and Linux, or run in Cloud Shell.",
            "D": "Both can easily create resource groups (az group create / New-AzResourceGroup)."
        }
    },
    {
        "id": 54,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.3 Azure Arc",
        "q": "Which service lets you manage on-premises servers and other clouds as if they were in Azure?",
        "options": {
            "A": "Azure Arc",
            "B": "Azure DNS",
            "C": "Azure Files",
            "D": "Azure Cloud Shell"
        },
        "ans": "A",
        "why": "Azure Arc projects non-Azure resources (on-premises servers, VMware, AWS, GCP, Kubernetes) into Azure Resource Manager so they can be managed with Azure RBAC, policies, and tags.",
        "traps": {
            "B": "Azure DNS manages domain name resolution.",
            "C": "Azure Files is managed file shares.",
            "D": "Azure Cloud Shell is an administrative command terminal."
        }
    },
    {
        "id": 55,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.3 ARM and ARM templates",
        "q": "What does 'declarative' mean for an ARM template?",
        "options": {
            "A": "You list each step command in order",
            "B": "You describe the desired end state and ARM works out how to deploy it",
            "C": "You write C# code",
            "D": "It cannot be repeated"
        },
        "ans": "B",
        "why": "Declarative syntax means you state 'what' the infrastructure should look like at the end; Azure Resource Manager handles ordering dependencies and deploying resources in parallel.",
        "traps": {
            "A": "Listing step-by-step commands is imperative syntax (like a script).",
            "C": "ARM templates are written in JSON or Bicep, not C#.",
            "D": "Declarative templates are idempotent and designed to be repeated safely."
        }
    },
    {
        "id": 56,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.3 Infrastructure as code",
        "q": "Bicep is best described as:",
        "options": {
            "A": "A VM size",
            "B": "A declarative language for deploying Azure resources that compiles to ARM templates",
            "C": "A monitoring dashboard",
            "D": "A pricing tier"
        },
        "ans": "B",
        "why": "Bicep is a domain-specific, declarative language that uses clean, concise syntax to deploy Azure resources by compiling directly down into standard ARM template JSON.",
        "traps": {
            "A": "Bicep is not a compute VM size.",
            "C": "Bicep is not a monitoring dashboard.",
            "D": "Bicep is an IaC language, not a pricing tier."
        }
    },
    {
        "id": 57,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.4 Azure Advisor",
        "q": "Which tool gives personalized recommendations across reliability, security, performance, cost and operational excellence?",
        "options": {
            "A": "Azure Advisor",
            "B": "Azure Policy",
            "C": "Azure Arc",
            "D": "Azure Files"
        },
        "ans": "A",
        "why": "Azure Advisor analyzes your configuration and usage telemetry to provide personalized, actionable recommendations categorized into the 5 pillars of the Well-Architected Framework.",
        "traps": {
            "B": "Azure Policy enforces compliance rules, but does not provide general optimization advice.",
            "C": "Azure Arc extends Azure management to hybrid environments.",
            "D": "Azure Files is cloud file storage."
        }
    },
    {
        "id": 58,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.4 Service Health",
        "q": "Which service tells you about the health of ONE specific virtual machine?",
        "options": {
            "A": "Azure status",
            "B": "Service Health",
            "C": "Resource Health",
            "D": "Pricing calculator"
        },
        "ans": "C",
        "why": "Azure Resource Health provides minute-by-minute status and diagnostic guidance regarding the operational health of an individual specific Azure resource (like one VM).",
        "traps": {
            "A": "Azure Status provides a global view of all Azure services across all regions.",
            "B": "Service Health notifies you of outages and planned maintenance affecting your subscriptions/regions.",
            "D": "The pricing calculator estimates costs."
        }
    },
    {
        "id": 59,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.4 Azure Monitor / Log Analytics",
        "q": "Which language is used to query data in Log Analytics workspaces?",
        "options": {
            "A": "SQL only",
            "B": "Kusto Query Language (KQL)",
            "C": "Python",
            "D": "Bash"
        },
        "ans": "B",
        "why": "Log Analytics workspaces are queried using Kusto Query Language (KQL), a powerful read-only query language designed for fast log search and analytics.",
        "traps": {
            "A": "SQL is used for relational databases, not the native Azure Monitor log workspace.",
            "C": "Python can interact via APIs, but queries are authored in KQL.",
            "D": "Bash is a shell scripting language."
        }
    },
    {
        "id": 60,
        "area": "Area 3: Azure Management and Governance",
        "tag": "3.4 Application Insights",
        "q": "Which Azure Monitor capability gives application performance monitoring for live web apps?",
        "options": {
            "A": "Application Insights",
            "B": "Azure DNS",
            "C": "Azure Policy",
            "D": "Data Box"
        },
        "ans": "A",
        "why": "Application Insights is an Azure Monitor feature that provides Application Performance Monitoring (APM) to track live web application performance, exceptions, traces, and usage telemetry.",
        "traps": {
            "B": "Azure DNS hosts DNS records.",
            "C": "Azure Policy audits resource compliance.",
            "D": "Data Box is an offline data appliance."
        }
    }
]
