from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatInteraction
from .services import ChatbotService
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import CustomUser
from .utils import get_chatbot_response
import traceback
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chatbot.models import Formation
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import json

def chat_view(request):
    return render(request, 'chatbot/chat.html')

import unidecode

@csrf_exempt
@login_required
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def chat_api(request):
    message = request.data.get('message', '').lower()
    message_clean = unidecode.unidecode(message)  # supprime les accents pour comparaison souple

        # 👇 Réponse personnalisée pour "bonjour" ou "bonsoir"
    if "bonjour" in message_clean:
        return Response({
            "status": "success",
            "response": "Bonjour je suis l'assistant d'orientation de Suptech conçu par Parolien et Mondesir. Quelle formation voulez-vous ?"
        })

    if "bonsoir" in message_clean:
        return Response({
            "status": "success",
            "response": "Bonsoir je suis l'assistant d'orientation de Suptech conçu par Parolien et Mondesir. Quelle formation voulez-vous ?"
        })


    try:
        # Réponses personnalisées robustes (détection souple sans accents)
        if "mastere professionnel" in message_clean and "cyber securite" in message_clean:
            return Response({
                "status": "success",
                "response": """<p style='color:#003366; font-weight:bold;'>Mastère Professionnel en Cyber sécurité</p>
<p>OBJECTIF: Vous souhaitez décrocher un poste dans une entreprise spécialisée en sécurité informatique, cyber sécurité ou Audit ?</p>
<p>Vous rêvez d'être un expert en cyber sécurité ?</p>
<p>SUPTECH vous propose le mastère professionnel en Cyber Sécurité.</p><br>
<p style='font-weight:bold;'>CONDITIONS D'ADMISSION :</p>
<ul>
<li>Niveau M1 : Les étudiants titulaires de licences en sciences et techniques, en mathématiques ou en informatique.</li>
<li>Niveau M2 : Les étudiants qui ont validé le M1 en Cyber sécurité ou le M1 d'un mastère équivalent.</li>
</ul>
<p style='font-weight:bold;'>Poursuites d'études :</p>
<ul>
<li>Mastère spécialisé</li>
<li>Doctorat en sécurité informatique</li>
<li>Doctorat en systèmes d'information</li>
<li>Formation continue en sécurité IT</li>
<li>Certifications professionnelles (CISSP, CISA, etc.)</li>
</ul>
<p style='font-weight:bold;'>Débouchés :</p>
<ul>
<li>Expert en cybersécurité</li>
<li>Auditeur sécurité</li>
<li>Analyste SOC</li>
<li>RSSI</li>
<li>Consultant sécurité IT</li>
</ul>"""
            })

        if "mastere professionnel" in message_clean and "data science" in message_clean:
            return Response({
                "status": "success",
                "response": """<p style='color:#003366; font-weight:bold;'>Mastère Professionnel en Data Science</p>
<p>OBJECTIF: Vous voulez intégrer des établissements disposant d'une fouille de données massives ?</p>
<p>Opérer en tant qu'analyste des données, Expert IT ou consultant SAAS ?</p>
<p>SUPTECH vous propose le nouveau mastère professionnel en Data Science, c'est le diplôme qu'il vous faut pour saisir de nouvelles opportunités de carrière.</p><br>
<p style='font-weight:bold;'>CONDITIONS D'ADMISSION :</p>
<ul>
<li>Niveau M1 : Les étudiants titulaires de licences en sciences et techniques, en mathématiques ou en informatique.</li>
<li>Niveau M2 : Les étudiants qui ont validé le M1 en Data Science ou le M1 d'un mastère équivalent.</li>
</ul>
<p style='font-weight:bold;'>Poursuites d'études :</p>
<ul>
<li>Mastère spécialisé</li>
<li>Doctorat en data science</li>
<li>Doctorat en intelligence artificielle</li>
<li>Certifications professionnelles (TensorFlow, Python, etc.)</li>
<li>Formation continue en machine learning</li>
</ul>
<p style='font-weight:bold;'>Débouchés :</p>
<ul>
<li>Data scientist</li>
<li>Analyste big data</li>
<li>Ingénieur machine learning</li>
<li>Consultant IA</li>
<li>Expert en intelligence artificielle</li>
</ul>"""
            })

        if "mastere professionnel" in message_clean and "logistique" in message_clean and "transport" in message_clean:
            return Response({
                "status": "success",
                "response": """<p style='color:#003366; font-weight:bold;'>Mastère Professionnel en Logistique du Transport et le Développement Durable</p>
<p>OBJECTIF: Vous souhaitez être un Analyste de mobilité urbaine ou de trafic urbain ?</p>
<p>Le domaine de la logistique du transport vous intéresse ?</p>
<p>SUPTECH vous accompagne et vous apporte le soutien indispensable à la réussite de votre formation avec le mastère professionnel en Logistique du Transport et le Développement Durable.</p><br>
<p style='font-weight:bold;'>CONDITIONS D'ADMISSION :</p>
<ul>
<li>Niveau M1 : Les étudiants titulaires de licences ou maîtrise en économie/gestion dans les différentes spécialités (Finance, Économie, Management, Marketing, GRH...).</li>
<li>Niveau M2 : Les étudiants qui ont validé le M1 en Logistique du Transport et le Développement Durable ou le M1 d'un mastère équivalent après étude de dossier par la commission d'admission.</li>
</ul>
<p style='font-weight:bold;'>Poursuites d'études :</p>
<ul>
<li>Mastère spécialisé en logistique</li>
<li>Doctorat en logistique et transport</li>
<li>Certifications en gestion de la supply chain</li>
<li>Formation continue en management logistique</li>
<li>Préparation à des concours en transport</li>
</ul>
<p style='font-weight:bold;'>Débouchés :</p>
<ul>
<li>Responsable logistique</li>
<li>Planificateur transport</li>
<li>Analyste mobilité</li>
<li>Consultant en logistique</li>
<li>Manager supply chain</li>
</ul>"""
            })

        # Détection des demandes de débouchés et poursuites d'études combinées
        if any(word in message_clean for word in ["poursuite", "que faire après", "débouchés", "débouché", "carrière", "métiers", "emplois", "avenir professionnel", "opportunité"]):

            if "licence" in message_clean:
                return Response({
                    "status": "success",
                    "response": """<p><strong>Poursuites après une Licence :</strong><br>
                    Mastère professionnel, préparation concours, insertion professionnelle selon spécialité.
                    <br><br><strong>Débouchés après une Licence :</strong><br>
                    Chargé de mission, Assistant manager, Technicien, etc.
                    </p>"""
                })

            elif "mastere" in message_clean or "mastère" in message_clean:
                return Response({
                    "status": "success",
                    "response": """<p><strong>Poursuites après un Mastère :</strong><br>
                    Doctorat (si admissible), insertion dans le secteur privé ou public selon spécialité.
                    <br><br><strong>Débouchés après un Mastère :</strong><br>
                    Chef de projet, Consultant, Ingénieur, Expert en informatique, etc.
                    </p>"""
                })

            elif "ingenieur" in message_clean or "ingénieur" in message_clean:
                return Response({
                    "status": "success",
                    "response": """<p><strong>Poursuites après un diplôme d’ingénieur :</strong><br>
                    Spécialisation, mastère spécialisé, MBA, doctorat, etc.
                    <br><br><strong>Débouchés après un diplôme d’ingénieur :</strong><br>
                    Ingénieur R&D, Chef de projet, Consultant, etc.
                    </p>"""
                })

        # Détection des conditions d'admission
        if "condition d'admission" in message_clean or "conditions d'admission" in message_clean:
            if "licence 1" in message_clean or "l1" in message_clean:
                return Response({
                    "status": "success",
                    "response": """<p><strong>Conditions d'admission – Licence 1 :</strong><br>
                    Baccalauréat toutes séries ou équivalent reconnu.</p>"""
                })
            elif "mastere" in message_clean or "mastère" in message_clean:
                return Response({
                    "status": "success",
                    "response": """<p><strong>Conditions d'admission – Mastère :</strong><br>
                    M1 : Licence scientifique/technique ou équivalent. M2 : M1 validé dans le même domaine ou équivalent après étude du dossier.</p>"""
                })
            elif "ingénieur" in message_clean or "cycle ingénieur" in message_clean:
                return Response({
                    "status": "success",
                    "response": """<p><strong>Conditions d'admission – Cycle ingénieur :</strong><br>
                    Accès après classes préparatoires, DUT, BTS, ou licence scientifique selon spécialité, avec étude du dossier ou concours.</p>"""
                })

                

        # Logique de détection classique
        types = ['licence', 'mastere', 'mastère', 'ingenieur', 'ingénieur']
        domaines = ['informatique', 'gestion', 'telecom', 'télécom', 'droit']

        type_detecte = next((t for t in types if t in message), None)
        domaine_detecte = next((d for d in domaines if d in message), None)

        # Normalisation
        if type_detecte in ['mastère', 'mastere']:
            type_detecte = 'mastère'
        if type_detecte in ['ingenieur', 'ingénieur']:
            type_detecte = 'ingénieur'
        if domaine_detecte == 'télécom':
            domaine_detecte = 'telecom'

        # Requête dynamique insensible à la casse avec distinct
        formations = Formation.objects.all()
        if type_detecte:
            formations = formations.filter(type__icontains=type_detecte)
        if domaine_detecte:
            formations = formations.filter(domaine__icontains=domaine_detecte)

        noms = list(set(f.nom for f in formations))  # suppression des doublons

        if noms:
            html_response = "<p style='color:#003366; font-weight:bold;'>Voici les formations correspondantes :</p><ul style='padding-left: 20px;'>"
            for nom in noms:
                html_response += f"<li style='margin-bottom: 6px; color: #003366;'>{nom}</li>"
            html_response += "</ul>"

            return Response({
                "status": "success",
                "response": html_response
            })
        else:
            return Response({
                "status": "success",
                "response": "<p style='color: #b30000;'>Je n’ai pas trouvé de formation correspondant à ta demande.</p>"
            })

    except Exception as e:
        return Response({
            "status": "error",
            "response": f"<p style='color:red;'>Erreur serveur : {str(e)}</p>"
        }, status=500)









def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        current_class = request.POST['classe']  # <-- ce champ HTML est "classe"
        formation = request.POST['formation']

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déjà utilisé.")
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Adresse e-mail déjà utilisée.")
            return redirect('register')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            age=age,
            current_class=current_class,  # <-- utilise le vrai nom du champ
            formation=formation
        )
        messages.success(request, "Inscription réussie avec sucess")
        return redirect('login')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        identifier = request.POST.get('identifier', '')
        password = request.POST.get('password', '')

        # Vérifie si l'identifiant est un email ou un nom d'utilisateur
        from django.contrib.auth import get_user_model
        User = get_user_model()
        try:
            user = User.objects.get(email=identifier)
            username = user.username
        except User.DoesNotExist:
            username = identifier

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')  # Remplace 'chatbot' par le nom exact de ta page chatbot
        else:
            messages.error(request, "Identifiants invalides. Veuillez réessayer.")

    return render(request, 'login.html')
    
    from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def chatbot_view(request):
    return render(request, 'chatbot/chat.html')



