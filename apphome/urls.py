from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index , name = "base"),
    path('apropos/' , about, name= "about"),
    path('nos_services/', services, name= "service"),
    path('nos_formation/', formations, name= "formation"),
    path('contactez_nous/', contacts, name="contact"),
    
    path('management_de_la_performance/', manages, name="manage"),
    path('Accompagnement/', Accompagnes , name="accompagne"),
    path('audit/', audits, name="audit"),
    path('conseil/', conseils, name="conseil"),
    path('Nos_Salles_à_louer', salles, name="salle"),
    
    path('devis/', devis, name="devis"),
    path('thematic/<int:type_formation_id>/', thematic, name="thematic"),  # URL pour les thématiques par type de formation
    path('programme/<int:formation_id>/', programs, name="program"),
    
    path('recherche/', recherche, name='recherche'),
    path('formation/<int:pk>/', formation_detail, name='formation_detail'),
    path('newsletter_signup/', newsletter_signup, name='newsletter_signup'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    