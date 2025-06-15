# chatbot/utils.py
from .models import Formation

def get_chatbot_response(message):
    message = message.lower()

    formations = Formation.objects.all()
    for formation in formations:
        for mot_cle in formation.mots_cles:
            if mot_cle.lower() in message:
                return (
                    f"La formation '{formation.nom}' appartient au domaine '{formation.domaine}' "
                    f"et est de niveau '{formation.niveau}'."
                )

    return "Je n'ai pas compris votre question. Pouvez-vous reformuler ?"
