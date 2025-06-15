from django.core.management.base import BaseCommand
from chatbot.models import Formation

class Command(BaseCommand):
    help = "Importe les formations dans la base de données"

    def handle(self, *args, **kwargs):

        # 1. Licence et Mastère en Droit
        Formation.objects.create(
            nom="Licence en Droit Privé",
            type="Licence",
            domaine="Droit",
            description=(
                "La Licence en Droit Privé forme aux principes du droit civil, pénal et commercial. "
                "Elle prépare aux carrières juridiques dans les cabinets, entreprises et institutions publiques."
            ),
            conditions_admission="Baccalauréat toutes séries, préférence pour les séries littéraires ou économiques.",
            mots_cles=[
                "droit", "droit privé", "juriste", "notaire", "licence droit", "avocat", "tribunal", "législation", 
                "sciences juridiques", "contentieux", "code civil", "procédures juridiques"
            ],
            ressources_pedagogiques=[
                "https://ressources.suptech.tn/droit/licence_droit_prive.pdf",
                "https://moodle.suptech.tn/course/view.php?id=21"
            ]
        )

        Formation.objects.create(
            nom="Mastère Professionnel en Droit des Affaires",
            type="Mastère",
            domaine="Droit",
            description=(
                "Ce mastère forme des spécialistes du droit des sociétés, fiscal et commercial. "
                "Il ouvre la voie à des postes de juriste d'entreprise, fiscaliste ou avocat en droit des affaires."
            ),
            conditions_admission="Licence en droit ou diplôme équivalent.",
            mots_cles=[
                "droit des affaires", "mastère droit", "juriste entreprise", "fiscalité", "avocat d'affaires", 
                "consultant juridique", "droit fiscal", "sociétés", "réglementation commerciale"
            ],
            ressources_pedagogiques=[
                "https://ressources.suptech.tn/droit/mastere_droit_affaires.pdf",
                "https://moodle.suptech.tn/course/view.php?id=38"
            ]
        )

        # 2. Mastère en Data Science
        Formation.objects.create(
            nom="Mastère Professionnel en Data Science",
            type="Mastère",
            domaine="Informatique",
            description=(
                "Ce mastère forme des experts en science des données, analyse statistique, big data et intelligence artificielle. "
                "Idéal pour les carrières en analyse de données, IT consulting ou développement de solutions IA."
            ),
            conditions_admission="M1 : Licence en sciences, mathématiques ou informatique. M2 : Validation du M1 équivalent.",
            mots_cles=[
                "data science", "analyse de données", "big data", "machine learning", "intelligence artificielle", 
                "python", "statistiques", "consultant IT", "cloud", "data engineer", "IA"
            ],
            ressources_pedagogiques=[
                "https://ressources.suptech.tn/informatique/mastere_data_science.pdf",
                "https://moodle.suptech.tn/course/view.php?id=45"
            ]
        )

        # 3. Diplômes Nationaux d’Ingénieur
        Formation.objects.create(
            nom="Cycle Préparatoire Informatique",
            type="Cycle Préparatoire",
            domaine="Ingénierie",
            description="Formation de base pour intégrer un cycle d’ingénieur en informatique ou télécom.",
            conditions_admission="Baccalauréat scientifique ou technique.",
            mots_cles=[
                "cycle préparatoire", "informatique", "maths", "physique", "prépa", "algèbre", "algorithmique"
            ],
            ressources_pedagogiques=[
                "https://ressources.suptech.tn/ingenieur/prepa_info.pdf"
            ]
        )

        Formation.objects.create(
            nom="Cycle Préparatoire MPI",
            type="Cycle Préparatoire",
            domaine="Ingénierie",
            description="Mathématiques, Physique et Informatique pour préparer les concours d’écoles d’ingénieurs.",
            conditions_admission="Bac scientifique.",
            mots_cles=["prépa MPI", "math", "physique", "informatique", "école d’ingénieur"],
            ressources_pedagogiques=["https://ressources.suptech.tn/ingenieur/prepa_mpi.pdf"]
        )

        Formation.objects.create(
            nom="Diplôme National d’Ingénieur en Informatique",
            type="Ingénieur",
            domaine="Informatique",
            description="Formation en génie informatique, systèmes, réseaux, et systèmes d'information.",
            conditions_admission="Cycle préparatoire réussi ou équivalent.",
            mots_cles=["ingénieur", "génie informatique", "systèmes", "réseaux", "SI", "IT", "programmation", "base de données"],
            ressources_pedagogiques=["https://ressources.suptech.tn/ingenieur/info.pdf"]
        )

        Formation.objects.create(
            nom="Diplôme National d’Ingénieur Télécom",
            type="Ingénieur",
            domaine="Télécommunications",
            description="Formation en réseaux mobiles, télécoms, services numériques et protocoles de communication.",
            conditions_admission="Cycle préparatoire ou équivalent.",
            mots_cles=["télécom", "réseaux mobiles", "5G", "services télécom", "protocoles", "IoT", "connectivité"],
            ressources_pedagogiques=["https://ressources.suptech.tn/ingenieur/telecom.pdf"]
        )

        # 4. Licences Informatiques
        licences_info = [
            ("Licence en Ingénierie des Systèmes Informatiques: Ingénierie des Réseaux et des Systèmes", 
             "Formation axée sur la conception, le déploiement et la sécurisation des réseaux et systèmes informatiques.",
             ["réseaux", "systèmes", "ingénierie informatique", "licence informatique", "IT", "infrastructure"]),
             
            ("Licence en Sciences de l'Informatique: Informatique et multimédia", 
             "Formation alliant développement web, design interactif, et traitement multimédia.",
             ["web", "multimédia", "informatique", "développement", "graphisme", "html", "css"]),
             
            ("Licence en Ingénierie des Systèmes Informatiques: Systèmes embarqués et IoT", 
             "Spécialisation dans la programmation embarquée, capteurs, microcontrôleurs, et objets connectés.",
             ["iot", "systèmes embarqués", "arduino", "microcontrôleur", "capteur", "temps réel"]),
             
            ("Licence en Informatique de Gestion: Informatique Décisionnelle", 
             "Formation mêlant informatique et management avec des outils de décision (BI, ERP).",
             ["gestion", "informatique décisionnelle", "ERP", "BI", "data", "management"]),
             
            ("Licence en Sciences de l'Informatique: Génie logiciel et Systèmes d’Information", 
             "Spécialisation en développement logiciel, bases de données et systèmes d'information.",
             ["génie logiciel", "systèmes d'information", "programmation", "UML", "licence info"])
        ]

        for nom, desc, mots_cles in licences_info:
            Formation.objects.create(
                nom=nom,
                type="Licence",
                domaine="Informatique",
                description=desc,
                conditions_admission="Baccalauréat scientifique ou technique.",
                mots_cles=mots_cles,
                ressources_pedagogiques=[
                    "https://ressources.suptech.tn/informatique/licences.pdf"
                ]
            )

        # 5. Mastères Informatiques
        masteres_info = [
            ("Mastère Professionnel en Sécurité des systèmes Informatiques, communicants et embarqués",
             "Spécialisation en cybersécurité, sécurité des réseaux, protocoles et sécurité embarquée.",
             ["cybersécurité", "réseaux", "protection", "systèmes embarqués", "cryptographie"]),
             
            ("Mastère Professionnel en Cloud Computing",
             "Formation en architectures cloud, services cloud (SaaS, IaaS, PaaS) et virtualisation.",
             ["cloud", "SaaS", "PaaS", "IaaS", "virtualisation", "serveurs distants"]),
             
            ("Mastère Professionnel en Data Science",
             "Double compétence en statistiques avancées, machine learning et big data.",
             ["data", "analyse", "statistique", "IA", "machine learning", "data mining"]),
             
            ("Mastère Professionnel en Cyber Sécurité",
             "Spécialisation avancée en cybersécurité, audit, et gouvernance des systèmes d'information.",
             ["sécurité", "cyber sécurité", "audit", "hacking éthique", "firewall", "SI"])
        ]

        for nom, desc, mots_cles in masteres_info:
            Formation.objects.create(
                nom=nom,
                type="Mastère",
                domaine="Informatique",
                description=desc,
                conditions_admission="Licence en informatique ou équivalent. M2 : validation du M1.",
                mots_cles=mots_cles,
                ressources_pedagogiques=[
                    "https://ressources.suptech.tn/informatique/masteres.pdf"
                ]
            )

        # 6. Licences en Gestion
        licences_gestion = [
            "Licence en Marketing", "Licence en Sciences Économiques", "Licence en Commerce et Finance Internationale",
            "Licence en Finance", "Licence en Comptabilité", "Licence en Management", "Licence en Gestion des Ressources Humaines"
        ]

        for nom in licences_gestion:
            Formation.objects.create(
                nom=nom,
                type="Licence",
                domaine="Gestion",
                description=f"{nom} forme les étudiants aux fondamentaux du domaine économique et de la gestion.",
                conditions_admission="Baccalauréat toutes séries.",
                mots_cles=[
                    "gestion", "marketing", "RH", "finance", "comptabilité", "licence économie", "management", "stratégie"
                ],
                ressources_pedagogiques=["https://ressources.suptech.tn/gestion/licences.pdf"]
            )

        # 7. Mastères en Gestion
        masteres_gestion = [
            "Mastère Professionnel en Commerce et Affaires Commerciales",
            "Mastère Professionnel en Ingénierie Financière",
            "Mastère Professionnel en Gestion des Organisations: Management",
            "Mastère Professionnel en Comptabilité des Systèmes d’Information",
            "Mastère Professionnel en Marketing et Commerce International",
            "Mastère Professionnel en Management Intégré: Qualité, Sécurité, Environnement",
            "Mastère Professionnel en Économie de l'Énergie et Développement Durable",
            "Mastère Professionnel en Économie Managériale et Industrielle",
            "Mastère Professionnel en Finance: Finance de Marché",
            "Mastère Professionnel en Gestion Commerciale: Hautes Études Commerciales",
            "Mastère Professionnel en Marketing Digital",
            "Mastère Professionnel en Économie Financière et Fiscale",
            "Mastère Professionnel en Gestion de la Relation Client",
            "Mastère Professionnel en Logistique du Transport et Développement Durable"
        ]

        for nom in masteres_gestion:
            Formation.objects.create(
                nom=nom,
                type="Mastère",
                domaine="Gestion",
                description=f"{nom} prépare les étudiants à des fonctions de haut niveau dans le domaine {nom.split('en ')[-1].lower()}.",
                conditions_admission="Licence en gestion, économie, marketing, finance ou équivalent.",
                mots_cles=[
                    "mastère gestion", "management", "économie", "marketing", "finance", "logistique", "développement durable"
                ],
                ressources_pedagogiques=["https://ressources.suptech.tn/gestion/masteres.pdf"]
            )
