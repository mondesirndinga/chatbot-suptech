from .models import Formation

class ChatbotService:
    @staticmethod
    def get_response(user_input):
        user_input = user_input.lower()

        # Type de contenu demandé
        ask_requirements = any(word in user_input for word in ['condition', 'admission', 'requis', 'prérequis'])
        ask_careers = any(word in user_input for word in ['débouché', 'carrière', 'métier', 'emploi'])

        # Domaines et niveaux détectés
        domain_keywords = {
            'gestion': ['gestion', 'marketing', 'finance', 'comptabilité', 'management', 'ressources humaines', 'économie'],
            'droit': ['droit', 'juridique'],
            'informatique': ['informatique', 'info', 'programmation', 'réseaux', 'systèmes', 'télécom', 'ingénieur'],
            'spécialisés': ['cyber', 'cybersécurité', 'data', 'science', 'logistique', 'transport']
        }

        level_keywords = {
            'licence': ['licence', 'licences', 'bac+3'],
            'mastere': ['mastère', 'master', 'mastères', 'bac+5'],
            'ingenieur': ['ingénieur', 'cycle', 'préparatoire']
        }

        detected_domain = None
        detected_level = None

        for key, keywords in domain_keywords.items():
            if any(k in user_input for k in keywords):
                detected_domain = key
                break

        for key, keywords in level_keywords.items():
            if any(k in user_input for k in keywords):
                detected_level = key
                break

        # ✅ Réponses dynamiques spéciales
        if "diplôme national" in user_input and "ingénieur" in user_input:
            formations = Formation.objects.filter(type='ingenieur', domaine='informatique')
            if formations.exists():
                response = "<strong>1- Diplômes Nationaux d'Ingénieur :</strong><br><br>"
                for f in formations:
                    response += f"• {f.nom}<br>"
                return response

        if "licence" in user_input and "informatique" in user_input:
            formations = Formation.objects.filter(type='licence', domaine='informatique')
            if formations.exists():
                response = "<strong>2- Licences Informatiques :</strong><br><br>"
                for f in formations:
                    response += f"• {f.nom}<br>"
                return response

        if "mastère" in user_input and "informatique" in user_input:
            formations = Formation.objects.filter(type='mastere', domaine='informatique')
            if formations.exists():
                response = "<strong>3- Mastères Informatiques :</strong><br><br>"
                for f in formations:
                    response += f"• {f.nom}<br>"
                return response

        # ✅ Requête générale
        formations = Formation.objects.all()

        if detected_domain:
            formations = formations.filter(domaine=detected_domain)

        if detected_level:
            formations = formations.filter(type=detected_level)

        if not formations.exists():
            return "Je n’ai trouvé aucune formation correspondant à votre demande."

        response = ""

        if ask_requirements:
            response += "<strong>Conditions d'admission :</strong><br><br>"
            for f in formations:
                response += f"<u>{f.nom}</u> :<br>{f.conditions_admission or 'Non spécifié'}<br><br>"

        elif ask_careers:
            response += "<strong>Débouchés :</strong><br><br>"
            for f in formations:
                response += f"<u>{f.nom}</u> :<br>{f.debouches or 'Non spécifié'}<br><br>"

        else:
            response += "<strong>Formations Trouvées :</strong><br><br>"
            for f in formations:
                response += f"• {f.nom}<br>"

        return response.strip()
