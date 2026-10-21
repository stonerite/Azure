"""
Structured AZ-900 (July 2026 Skills Measured) Exam Syllabus and Domain Specifications.
"""

from typing import Dict, Any, List

SYLLABUS: Dict[str, Dict[str, Any]] = {
    "area_1": {
        "id": 1,
        "name": "Describe cloud concepts",
        "weight": "25-30%",
        "objectives": [
            {
                "id": "1.1",
                "title": "Describe cloud computing",
                "subtopics": [
                    "Definition of cloud computing",
                    "Shared responsibility model (Customer data/identity vs Microsoft datacenter/hardware)",
                    "Cloud models: Public, Private, Hybrid, Multi-cloud",
                    "Consumption-based model and CapEx vs OpEx",
                    "Serverless computing"
                ]
            },
            {
                "id": "1.2",
                "title": "Benefits of using cloud services",
                "subtopics": [
                    "High availability and scalability (Vertical vs Horizontal)",
                    "Reliability, fault tolerance, and predictability",
                    "Security, governance, and compliance",
                    "Manageability (Azure Portal, Azure CLI, Azure PowerShell, ARM/Bicep)"
                ]
            },
            {
                "id": "1.3",
                "title": "Cloud service types",
                "subtopics": [
                    "IaaS (Infrastructure as a Service - VMs, disks, VNETs)",
                    "PaaS (Platform as a Service - App Service, Azure SQL, Functions)",
                    "SaaS (Software as a Service - Microsoft 365, Dynamics 365)",
                    "Shared responsibility across IaaS, PaaS, and SaaS"
                ]
            }
        ]
    },
    "area_2": {
        "id": 2,
        "name": "Describe Azure architecture and services",
        "weight": "35-40%",
        "objectives": [
            {
                "id": "2.1",
                "title": "Core architectural components",
                "subtopics": [
                    "Regions, Region Pairs, and Sovereign Regions (Azure Government, 21Vianet)",
                    "Availability Zones (at least 3 independent zones per supported region)",
                    "Datacenters and Geographies",
                    "Resources, Resource Groups, Subscriptions, and Management Groups (Hierarchy)"
                ]
            },
            {
                "id": "2.2",
                "title": "Azure compute and networking services",
                "subtopics": [
                    "Compute types: VMs, Virtual Machine Scale Sets, Azure App Service, Azure Functions",
                    "Container options: Azure Container Instances (ACI), Azure Kubernetes Service (AKS)",
                    "Azure Virtual Networks (VNETs), Subnets, Peering, and VPN Gateway",
                    "Azure ExpressRoute (dedicated private connection bypassing public internet)",
                    "Azure DNS, Network Security Groups (NSGs)"
                ]
            },
            {
                "id": "2.3",
                "title": "Azure storage services",
                "subtopics": [
                    "Storage accounts and services: Blob Storage, Azure Files, Azure Disks, Azure Queues",
                    "Storage tiers: Hot, Cool, Cold, and Archive",
                    "Data redundancy: LRS, ZRS, GRS, GZRS",
                    "Azure Storage Explorer, AzCopy, and Azure Data Box"
                ]
            },
            {
                "id": "2.4",
                "title": "Azure identity, access, and security",
                "subtopics": [
                    "Microsoft Entra ID (formerly Azure AD) vs traditional Active Directory",
                    "Authentication methods: Single Sign-On (SSO), MFA, Passwordless",
                    "Conditional Access policies and Zero Trust security model",
                    "Role-Based Access Control (Azure RBAC) vs Azure Policy",
                    "Defense in depth layered security"
                ]
            }
        ]
    },
    "area_3": {
        "id": 3,
        "name": "Describe Azure management and governance",
        "weight": "30-35%",
        "objectives": [
            {
                "id": "3.1",
                "title": "Cost management in Azure",
                "subtopics": [
                    "Factors affecting costs (resource type, consumption, maintenance, geography)",
                    "Pricing Calculator vs Total Cost of Ownership (TCO) Calculator",
                    "Azure Cost Management + Billing, budgets, and cost alerts",
                    "Cost-saving strategies: Reserved Instances, Azure Hybrid Benefit, Spot VMs"
                ]
            },
            {
                "id": "3.2",
                "title": "Governance and compliance features",
                "subtopics": [
                    "Azure Policy and Initiatives (policy sets)",
                    "Resource Locks (CanNotDelete vs ReadOnly)",
                    "Azure Tags for taxonomy and cost tracking (tags not inherited by default)",
                    "Microsoft Purview and Service Trust Portal"
                ]
            },
            {
                "id": "3.3",
                "title": "Managing and deploying Azure resources",
                "subtopics": [
                    "Management tools: Azure Portal, Azure Mobile App, Azure PowerShell, Azure CLI, Cloud Shell",
                    "Infrastructure as Code (IaC): Azure Resource Manager (ARM) templates and Bicep",
                    "Azure Arc (hybrid and multi-cloud management)"
                ]
            },
            {
                "id": "3.4",
                "title": "Monitoring tools in Azure",
                "subtopics": [
                    "Azure Monitor (metrics, logs, Application Insights, Log Analytics)",
                    "Azure Service Health (Status, Service health, Resource health)",
                    "Azure Advisor (Cost, Security, Reliability, Operational Excellence, Performance)"
                ]
            }
        ]
    }
}

EXAM_FACTS = {
    "code": "AZ-900",
    "title": "Microsoft Azure Fundamentals",
    "duration_minutes": 45,
    "passing_score": 700,
    "max_score": 1000,
    "retake_policy": "Retake allowed 24 hours after first attempt; 14 days after subsequent attempts (max 5 per year)",
    "official_weightings": {
        "Cloud Concepts": "25-30%",
        "Azure Architecture and Services": "35-40%",
        "Azure Management and Governance": "30-35%"
    }
}

def get_area_summary(area_key: str, lang: str = "English") -> str:
    """Return an informative overview of a skill area in the specified language."""
    area = SYLLABUS.get(area_key)
    if not area:
        return "Unknown skill area."
        
    title = area["name"]
    weight = area["weight"]
    
    if lang.lower() == "sheng":
        lines = [f"**{title}** (Uzito kwenye mtihani: {weight}):"]
        for obj in area["objectives"]:
            lines.append(f"• **{obj['id']}** - **{obj['title']}**")
            for sub in obj["subtopics"][:3]:
                lines.append(f"   - {sub}")
        lines.append("\nUnataka tuchambue mada gani hapa, au nikupe swali (sema **'Quiz me'**)?")
        return "\n".join(lines)
    elif lang.lower() in ["kiswahili", "swahili"]:
        lines = [f"**{title}** (Uzito katika mtihani: {weight}):"]
        for obj in area["objectives"]:
            lines.append(f"• **{obj['id']}** - **{obj['title']}**")
            for sub in obj["subtopics"][:3]:
                lines.append(f"   - {sub}")
        lines.append("\nJe, ungependa tujifunze mada ipi katika eneo hili, au ujaribu swali (sema **'Quiz me'**)?")
        return "\n".join(lines)
    else:
        lines = [f"**{title}** (Official Exam Weight: {weight}):"]
        for obj in area["objectives"]:
            lines.append(f"• **{obj['id']}** - **{obj['title']}**")
            for sub in obj["subtopics"][:3]:
                lines.append(f"   - {sub}")
        lines.append("\nWhich topic would you like to explore, or should we take a quick quiz (say **'Quiz me'**)?")
        return "\n".join(lines)
