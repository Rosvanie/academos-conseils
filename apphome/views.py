from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import NewsletterSubscriberForm
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from .forms import *





# Create your views here.

def index(request):
    types_formation = TypeFormation.objects.all()[:4]  # Récupérer les 4 premiers types de formation
    formations_a_la_une = Formation.objects.order_by('?')[:3]  # Récupérer les 3 formations les plus récentes('-id')
    
    return render(request, "index.html", {
        'types_formation': types_formation,
        'formations_a_la_une': formations_a_la_une
    })
    
    
def about(request):
    return render(request, "apropos.html")

def services(request):
    return render(request, "services.html")

def formations(request):
    # Récupérer tous les types de formation
    types_formation = TypeFormation.objects.prefetch_related('thematiques')

    # Créer une liste pour stocker les données à afficher
    formations_data = []
    for type_formation in types_formation:
        # Compter le nombre de thématiques et de formations associées
        thematiques_count = type_formation.thematiques.count()
        formations_count = sum(t.formations.count() for t in type_formation.thematiques.all())
        
        formations_data.append({
            'type_formation': type_formation,
            'thematiques_count': thematiques_count,
            'formations_count': formations_count,
        })

    return render(request, "formations.html", {'formations_data': formations_data})

def contacts(request):
    return render(request, "contact.html")

def manages(request):
    return render(request, "manage.html")

def Accompagnes(request):
    return render(request, "Accompagne.html")

def audits(request):
    return render(request, "audit.html")

def conseils(request):
    return render(request, "conseil.html")

def salles(request):
    return render(request, "salle.html")

def devis(request):
    return render(request, "devis.html")

def thematic(request, type_formation_id):
    # Récupérer le type de formation par son identifiant
    type_formation = get_object_or_404(TypeFormation, id=type_formation_id)
    
    # Récupérer les thématiques associées à ce type de formation
    thematiques = type_formation.thematiques.all()

    return render(request, "thematic.html", {
        'type_formation': type_formation,
        'thematiques': thematiques,
    })   
    
def programs(request, formation_id):
    # Récupérer la formation par son identifiant
    formation = get_object_or_404(Formation, id=formation_id)
    # Récupérer les programmes associés à cette formation
    programmes = Programme.objects.filter(formation=formation)

    return render(request, "program.html", {'formation': formation, 'programmes': programmes})



def recherche(request):
    query = request.GET.get('q', '')  # Récupère la requête de recherche
    results = []

    if query:
        # Effectuer une recherche sur le modèle Formation, en cherchant dans le champ 'titre'
        formations = Formation.objects.filter(titre__icontains=query)
        
        for formation in formations:
            results.append({
                'id': formation.id,  # Ajout de l'ID de la formation
                'title': formation.titre,  # Utilisation du champ 'titre'
                'url': f"/programme/{formation.id}/"  # Lien vers la page de la formation
            })

    return JsonResponse({'results': results})

def formation_detail(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    return render(request, 'formation_detail.html', {'formation': formation})





def newsletter_signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if NewsletterSubscriber.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà abonné.")
            return redirect('base')

        # Envoi d'un email de confirmation
        send_mail(
            "Confirmez votre abonnement",
            "Cliquez sur ce lien pour confirmer votre abonnement : http://127.0.0.1:8000/confirmer_abonnement?email=" + email,
            "ton-email@gmail.com",
            [email],
            fail_silently=False,
        )

        messages.success(request, "Un email de confirmation vous a été envoyé.")
        return redirect('base')

    return render(request, 'index.html')
