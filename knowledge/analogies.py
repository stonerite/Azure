"""
East African Real-Life Analogies for AZ-900 Core Concepts.
Multi-lingual explanations in English, Kiswahili, and Sheng.
Always maintains official Azure terms in English and bolded.
"""

from typing import Dict, Any, Optional

ANALOGIES: Dict[str, Dict[str, Dict[str, str]]] = {
    "shared_responsibility": {
        "English": {
            "title": "Shared Responsibility Model",
            "simple": "In cloud computing, security and management tasks are divided between you (the customer) and Microsoft. You ALWAYS own your data and identities, while Microsoft ALWAYS manages physical security, hardware, and datacenters.",
            "analogy": "Think of renting a stall in a busy market like Gikomba or Toi. The market management secures the perimeter fence, maintains the main gate, and fixes the roof. But inside your stall, your goods, your cash register, and deciding which employees have keys are 100% your responsibility.",
            "term": "**Shared Responsibility Model**: Customer ALWAYS retains responsibility for data, identities, and device access; Microsoft ALWAYS manages physical datacenters and physical hosts.",
            "tip": "Exam Tip: Even in SaaS (like Microsoft 365), you never hand over responsibility for your data or user accounts to Microsoft!"
        },
        "Kiswahili": {
            "title": "Mtindo wa Uwajibikaji wa Pamoja (Shared Responsibility Model)",
            "simple": "Katika wingu (cloud), majukumu ya usalama yamegawanywa kati yako (mteja) na Microsoft. Mteja DAIMA anawajibika na data zake na akaunti za watumiaji, huku Microsoft ikisimamia majengo na mashine za vituo vya data.",
            "analogy": "Fikiria kukodisha kibanda katika soko la Kariakoo au Gikomba. Mwenye soko anahakikisha geti kuu linafungwa, uzio uko salama, na paa halivuji. Lakini mali zako ndani ya kibanda, droo ya pesa, na nani anayeshika funguo ni jukumu lako wewe mwenyewe kwa asilimia mia moja.",
            "term": "**Shared Responsibility Model**: Mteja HUWA anawajibika na data, akaunti za watumiaji na mipangilio; Microsoft HUWA inawajibika na vituo vya data na mashine za kimwili.",
            "tip": "Kidokezo cha Mtihani: Kumbuka kuwa hata kwenye huduma za SaaS (kama Microsoft 365), data na usalama wa akaunti daima hubaki kwa mteja!"
        },
        "Sheng": {
            "title": "Shared Responsibility Model (Mgawanyo wa Kazi)",
            "simple": "Kwa cloud, security na usimamizi zimegawanywa kati yako na Microsoft kulingana na huduma unayotumia. Wewe ndiye unamiliki data na akaunti zako, Microsoft wanashughulikia majengo na maserver.",
            "analogy": "Piga picha umekodi kibanda pale Gikomba ama Toi market. Mwenye soko anachunga lango kuu, stima kuu na fence ya nje. Lakini mzigo ulioweka ndani ya duka, droo ya chapaa na nani anashika funguo ni hesabu yako buda!",
            "term": "**Shared Responsibility Model**: Mteja HUWA anamiliki data na credentials zote; Microsoft HUWA wanadhibiti physical datacenters na maunzi ya chuma.",
            "tip": "Exam tip: Hata ukitumia SaaS (kama Microsoft 365), Microsoft hawashughulikii data yako au password zako—hiyo ni kibarua chako!"
        }
    },
    "regions_and_zones": {
        "English": {
            "title": "Regions and Availability Zones",
            "simple": "An Azure **Region** is a geographic location containing one or more datacenters connected by a low-latency network. An **Availability Zone** is a physically separate datacenter within that region, equipped with independent power, cooling, and networking.",
            "analogy": "Imagine an M-Pesa agent running a money transfer business in Nairobi. The **Region** is Nairobi city. The **Availability Zones** are three separate shops in CBD, Westlands, and Upper Hill. If power blackouts hit Westlands completely, the shops in CBD and Upper Hill keep processing customer transactions without disruption.",
            "term": "**Availability Zone** protects against a single physical datacenter failure within a region. **Region Pairs** (hundreds of miles apart) protect against regional disasters.",
            "tip": "Exam Tip: Availability Zones are within the same region. Region Pairs connect two distant regions (at least 300 miles apart) for disaster recovery."
        },
        "Kiswahili": {
            "title": "Kanda na Maeneo ya Upatikanaji (Regions and Availability Zones)",
            "simple": "**Region** ni eneo la kijiografia lenye vituo vya data vilivyounganishwa. **Availability Zone** ni kituo cha data kilichojitegemea ndani ya region hiyo kikiwa na umeme, mfumo wa kupoza, na mtandao wake.",
            "analogy": "Piga picha ya mtandao wa mawakala wa M-Pesa jijini Nairobi. **Region** ni jiji zima la Nairobi. **Availability Zones** ni maduka matatu tofauti yaliyopo CBD, Westlands, na Upper Hill. Iwapo hitilafu ya umeme itatokea Westlands, maduka ya CBD na Upper Hill yanaendelea kutoa huduma bila tatizo.",
            "term": "**Availability Zone** hulinda dhidi ya hitilafu katika jengo moja la datacenter. **Region Pairs** hulinda dhidi ya majanga makubwa ya kikanda.",
            "tip": "Kidokezo cha Mtihani: Usichanganye Availability Zones (ambazo ziko ndani ya region moja) na Region Pairs (miji miwili iliyo mbali zaidi ya maili 300)."
        },
        "Sheng": {
            "title": "Regions na Availability Zones",
            "simple": "**Region** ni mji mzima (kama Nairobi) wenye ma-datacenter. **Availability Zone** ni jumba maalum la datacenter lililotengwa likiwa na stima yake, cooling, na network inayojitegemea.",
            "analogy": "Imagine agent mkubwa wa M-Pesa akiwa na maduka matatu: duka moja liko CBD, la pili Westlands, na la tatu Upper Hill. Kila duka lina jenereta yake na safe yake. Stima ikikatika Westlands yote, wateja watahudumiwa CBD na Upper Hill bila kuzubaa!",
            "term": "**Availability Zone** inalinda asirudi zero jengo moja likipata hitilafu. Kila region inayounga mkono zones huwa na angalau zones tatu (3).",
            "tip": "Exam tip: Usichanganye Availability Zones (zote ziko ndani ya region moja) na **Region Pairs** (miji miwili iliyo mbali zaidi ya maili 300 kwa disaster recovery)."
        }
    },
    "iaas_paas_saas": {
        "English": {
            "title": "IaaS vs PaaS vs SaaS",
            "simple": "Cloud service models differ by management level: **IaaS** gives you virtual machines where you manage the OS, runtime, and apps; **PaaS** manages the infrastructure and OS so you only deploy code; **SaaS** provides fully managed software ready for immediate end-user consumption.",
            "analogy": "Think of lunch options in town:\n• **IaaS**: Buying raw meat and vegetables from the market—you cook it, set the table, and wash all dishes yourself.\n• **PaaS**: Buying pre-marinated food at a food stall where gas and cookware are provided—you just season it to taste and cook your recipe.\n• **SaaS**: Ordering a ready-made meal (chips and chicken) at a restaurant—you simply sit down and eat immediately.",
            "term": "**IaaS** (Azure Virtual Machines), **PaaS** (Azure App Service, Azure Functions), **SaaS** (Microsoft 365, Dynamics 365).",
            "tip": "Exam Tip: If an exam question mentions 'customer is responsible for OS updates or patching', the answer is ALWAYS IaaS!"
        },
        "Kiswahili": {
            "title": "Mifumo ya Huduma: IaaS, PaaS, na SaaS",
            "simple": "**IaaS** inakupa kompyuta pepe (virtual machine) ambapo unasimamia mfumo endeshi (OS) na programu. **PaaS** inakuruhusu kuweka kodi (code) yako bila kujali mashine. **SaaS** ni programu iliyokamilika unayotumia moja kwa moja.",
            "analogy": "Fikiria chakula cha mchana:\n• **IaaS**: Kununua nyama mbichi na viungo sokoni—unapika na kuosha vyombo mwenyewe.\n• **PaaS**: Kununua vyakula vilivyotayarishwa tayari—kazi yako ni kuweka kikaangoni na kuonja chumvi tu.\n• **SaaS**: Kuingia mgahawani na kuagiza chakula tayari—unakula moja kwa moja bila kujua jiko limeendeshwaje.",
            "term": "**IaaS** (Azure Virtual Machines), **PaaS** (Azure App Service), **SaaS** (Microsoft 365).",
            "tip": "Kidokezo cha Mtihani: Swali likitaja mteja kusimamia mfumo endeshi (OS) na ulinzi wake wa ndani, jibu daima ni **IaaS**."
        },
        "Sheng": {
            "title": "IaaS, PaaS, na SaaS (Madaraja ya Cloud)",
            "simple": "**IaaS** ni mashine unapewa usimamie OS na ma-app. **PaaS** unaweka tu code yako bila kubeba mzigo wa server. **SaaS** ni app kamili tayari unatumia straight.",
            "analogy": "Mfano wa food ya mchana mtaani:\n• **IaaS**: Unanunua nyama mbichi na unga sokoni—unapika na kuosha masufuria mwenyewe.\n• **PaaS**: Unanunua nyama iliyokatwa na viungo tayari kwa kibanda—kazi yako ni kuwasha gas na kukaanga kulingana na ladha yako.\n• **SaaS**: Unaagiza takeaway ya chips kuku—iko tayari unagonga kisha unaendelea na harakati zako!",
            "term": "**IaaS** (Azure Virtual Machines), **PaaS** (Azure App Service, Azure Functions), **SaaS** (Microsoft 365).",
            "tip": "Exam tip: Swali la mtihani likitaja 'Customer is responsible for patching the OS', jibu daima ni **IaaS** bila kubahatisha!"
        }
    },
    "elasticity_and_scalability": {
        "English": {
            "title": "Scalability and Elasticity",
            "simple": "**Scalability** is the ability of a system to handle increased load by adding resources. **Elasticity** is the dynamic, automated scaling of resources out during traffic spikes and in when demand decreases to minimize cost.",
            "analogy": "Think of passenger matatus on Thika Superhighway. During the morning rush hour from Kasarani to CBD, SACCOs deploy 50 extra matatus to handle the massive rush (**scaling out**). By midday, 40 matatus park at the stage and turn off engines to avoid wasting fuel (**scaling in**).",
            "term": "**Vertical Scaling (Scale Up)** means increasing CPU/RAM on an existing VM. **Horizontal Scaling (Scale Out)** means adding more identical VM instances (e.g. **Virtual Machine Scale Sets**).",
            "tip": "Exam Tip: Elasticity means automatic resource adjustments matching current demand without manual intervention."
        },
        "Kiswahili": {
            "title": "Upanukaji na Unyumbufu (Scalability and Elasticity)",
            "simple": "**Scalability** ni uwezo wa mfumo kupanuka ili kumudu ongezeko la watumiaji. **Elasticity** ni uwezo wa mfumo kujirekebisha wenyewe kiotomatiki kulingana na idadi ya wateja kwa wakati husika.",
            "analogy": "Fikiria usafiri wa daladala au matatu wakati wa asubuhi. Watu wakiwa wengi kuelekea kazini, magari 50 huongezwa barabarani kuhudumia abiria (**scaling out**). Mchana abiria wakipungua, magari 40 hupumzika ili kuzuia matumizi ya mafuta bure (**scaling in**).",
            "term": "**Scale Up** (kuongeza uwezo wa kompyuta moja) dhidi ya **Scale Out** (kuongeza idadi ya kompyuta zinazofanana kama kwenye **Virtual Machine Scale Sets**).",
            "tip": "Kidokezo cha Mtihani: Elasticity inahusu mifumo kujiongeza na kujipunguza yenyewe kiotomatiki bila mfanyakazi kushinikiza kitufe."
        },
        "Sheng": {
            "title": "Scalability na Elasticity (Kupanuka ki-Mtaani)",
            "simple": "**Scalability** ni kuongeza nguvu mzigo ukiongezeka. **Elasticity** ni mfumo kujiongeza na kujipunguza wenyewe ki-automaat kulingana na shughuli.",
            "analogy": "Piga hesabu ya matatu za Thika Road au Rongai. Asubuhi watu wakienda job, SACCO inatupa matatu 50 barabarani zibebe raia (**scale out**). Mchana rush hour ikiisha, matatu 40 zinapaki stage zikizima engine zisiunguze mafuta bure (**scale in**).",
            "term": "**Scale Up** ni kuongeza engine kubwa kwa gari moja (RAM/CPU zaidi). **Scale Out** ni kuongeza matatu nyingine pacha (**Virtual Machine Scale Sets**).",
            "tip": "Exam tip: Ukiona neno 'automatic' na 'dynamic spikes', jua unazungumzia **Elasticity**!"
        }
    },
    "policy_vs_rbac": {
        "English": {
            "title": "Azure Policy vs Azure RBAC",
            "simple": "**Azure RBAC (Role-Based Access Control)** governs WHO can perform actions on resources. **Azure Policy** evaluates resource properties to ensure compliance with standards, regardless of who created the resource.",
            "analogy": "In a gated residential estate: **Azure RBAC** is the security gate access pass given to residents determining who can enter which gate and who has access to the clubhouse. **Azure Policy** is the estate building code: 'All houses must have green tile roofs and no commercial trucks may park inside'. Even if you hold the master gate pass (Owner role), you cannot paint your roof bright orange!",
            "term": "**Azure RBAC** controls user permissions (actions). **Azure Policy** enforces resource properties and compliance rules.",
            "tip": "Exam Tip: An Owner on a subscription will still be BLOCKED from creating a disallowed resource if Azure Policy has an explicit 'Deny' rule!"
        },
        "Kiswahili": {
            "title": "Azure Policy dhidi ya Azure RBAC",
            "simple": "**Azure RBAC** inasimamia NANI anaruhusiwa kufanya NINI. **Azure Policy** inakagua sifa za rasilimali ili kuhakikisha zinafuata sheria za usalama, bila kujali nani anayeziunda.",
            "analogy": "Kwenye makazi yenye geti maalum: **RBAC** ni kitambulisho au ufunguo unaotolewa kwa wakazi kuamua nani anaingia mlango upi. **Azure Policy** ni sheria za jumuia: 'Nyumba zote lazima ziwe na paa la kijani na hakuna malori yanayoruhusiwa kupaki'. Hata ukiwa mwenye nyumba (Owner), huwezi kupaka paa lako rangi nyekundu kinyume cha sheria!",
            "term": "**Azure RBAC** (ruhusa za watumiaji) dhidi ya **Azure Policy** (ufuatiliaji wa sheria na viwango vya rasilimali).",
            "tip": "Kidokezo cha Mtihani: Mtu mwenye ruhusa ya 'Owner' bado atazuiwa kuunda rasilimali ikiwa Azure Policy inakataza aina hiyo ya rasilimali au eneo husika!"
        },
        "Sheng": {
            "title": "Azure Policy vs Azure RBAC (Sheria vs Funguo)",
            "simple": "**Azure RBAC** inacheki NANI anafanya NINI. **Azure Policy** inacheki RASILIMALI ikoje na inatii sheria gani za kampuni.",
            "analogy": "Kwenye gated community ya mtaa: **RBAC** ni pass ya security getini ya nani anaruhusiwa kuingia door gani. **Azure Policy** ni sheria ya estate: 'Hakuna kujenga nyumba bila mabati ya kijani na hakuna kuingiza lori'. Hata ukiwa na funguo ya mwenye nyumba (Owner role), estate security haitakuruhusu upake mabati ya yellow!",
            "term": "**Azure RBAC** inahusu user permissions. **Azure Policy** inahusu resource compliance na restrictions.",
            "tip": "Exam tip: Hata ukiwa Owner kwa subscription, **Azure Policy** ikiwa na 'Deny' rule, itakublock kabisa!"
        }
    }
}

def get_concept_explanation(topic_key: str, lang: str = "English") -> Optional[str]:
    """Retrieve formatted explanation for a given concept and language."""
    topic = ANALOGIES.get(topic_key)
    if not topic:
        return None
    
    # Normalize language fallback
    lang_key = "English"
    if lang.lower() in ["sheng"]:
        lang_key = "Sheng"
    elif lang.lower() in ["kiswahili", "swahili"]:
        lang_key = "Kiswahili"
        
    data = topic.get(lang_key) or topic.get("English", {})
    
    follow_up = "Want a quick check question on this? (Reply **'Quiz me'** or **'Yes'**)"
    if lang_key == "Sheng":
        follow_up = "Unataka nikupe swali ya haraka kwa hii? (Sema **'Quiz me'** au **'Yes'**)"
    elif lang_key == "Kiswahili":
        follow_up = "Je, ungependa swali la kujipima kwenye mada hii? (Sema **'Quiz me'** au **'Ndio'**)"
        
    return (
        f"**Simple definition:** {data.get('simple')}\n\n"
        f"**Real-life example:** {data.get('analogy')}\n\n"
        f"**Azure term to remember:** {data.get('term')}\n\n"
        f"**Exam tip:** {data.get('tip')}\n\n"
        f"{follow_up}"
    )

def list_concept_topics() -> list:
    """Return all available analogy concept keys."""
    return list(ANALOGIES.keys())
