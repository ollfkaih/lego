SPRING = "spring"
AUTUMN = "autumn"

SEMESTER = ((SPRING, SPRING), (AUTUMN, AUTUMN))

COMPANY_PRESENTATION = "company_presentation"
COURSE = "course"
LUNCH_PRESENTATION = "lunch_presentation"
BEDEX = "bedex"
DIGITAL_PRESENTATION = "digital_presentation"
OTHER = "other"
SPONSOR = "sponsor"
START_UP = "start_up"

COMPANY_EVENTS = (
    (COMPANY_PRESENTATION, COMPANY_PRESENTATION),
    (LUNCH_PRESENTATION, LUNCH_PRESENTATION),
    (COURSE, COURSE),
    (DIGITAL_PRESENTATION, DIGITAL_PRESENTATION),
    (BEDEX, BEDEX),
    (OTHER, OTHER),
    (SPONSOR, SPONSOR),
    (START_UP, START_UP),
)

TRANSLATED_EVENTS = {
    COMPANY_PRESENTATION: "Bedriftspresentasjon",
    LUNCH_PRESENTATION: "Lunsjpresentasjon",
    COURSE: "Kurs",
    DIGITAL_PRESENTATION: "Digital presentasjon",
    BEDEX: "BedEx (vinter 2021)",
    OTHER: "Alternativt arrangement",
    START_UP: "Start-up kveld",
}

COLLABORATION = "collaboration"
README = "readme"
ITDAGENE = "itdagene"
LABAMBA_SPONSOR = "labamba_sponsor"

OTHER_OFFERS = (
    (COLLABORATION, COLLABORATION),
    (README, README),
    (ITDAGENE, ITDAGENE),
    (LABAMBA_SPONSOR, LABAMBA_SPONSOR),
)

TRANSLATED_OTHER_OFFERS = {
    COLLABORATION: "Samarbeid med andre linjeforeninger",
    README: "Annonsering i readme",
    ITDAGENE: "Stand på itDAGENE",
    LABAMBA_SPONSOR: "Sponsing av LaBamba",
}

COLLABORATION_ONLINE = "collaboration_online"
COLLABORATION_OMEGA = "collaboration_omega"
COLLABORATION_REVUE = "collaboration_revue"
COLLABORATION_ANNIVERSARY = "collaboration_anniversary"
COLLABORATION_REVUE_ANNIVERSARY = "collaboration_revue_anniversary"

COLLABORATIONS = (
    (COLLABORATION_ONLINE, COLLABORATION_ONLINE),
    (COLLABORATION_OMEGA, COLLABORATION_OMEGA),
    (COLLABORATION_REVUE, COLLABORATION_REVUE),
    (COLLABORATION_ANNIVERSARY, COLLABORATION_ANNIVERSARY),
    (COLLABORATION_REVUE_ANNIVERSARY, COLLABORATION_REVUE_ANNIVERSARY),
)

TRANSLATED_COLLABORATIONS = {
    COLLABORATION_ONLINE: "Online linjeforening",
    COLLABORATION_OMEGA: "Omega linjeforening",
    COLLABORATION_REVUE: "Abakusrevyen",
    COLLABORATION_ANNIVERSARY: "Abakus jubileum",
    COLLABORATION_REVUE_ANNIVERSARY: "Abakusrevy jubileum",
}

CONTACT_IN_OSLO = "contact_in_oslo"
INTERESTED = "interested"
NOT_INTERESTED = "not_interested"
CONTACTED = "contacted"
NOT_CONTACTED = "not_contacted"

SEMESTER_STATUSES = (
    (COMPANY_PRESENTATION, COMPANY_PRESENTATION),
    (COURSE, COURSE),
    (LUNCH_PRESENTATION, LUNCH_PRESENTATION),
    (BEDEX, BEDEX),
    (CONTACT_IN_OSLO, CONTACT_IN_OSLO),
    (INTERESTED, INTERESTED),
    (NOT_INTERESTED, NOT_INTERESTED),
    (CONTACTED, CONTACTED),
    (NOT_CONTACTED, NOT_CONTACTED),
)
