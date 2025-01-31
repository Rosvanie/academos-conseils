from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


class TypeFormation(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='type_formation_images/', blank=True, null=True)

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    type_formation = models.ForeignKey(TypeFormation, on_delete=models.CASCADE, related_name="categories")
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} ({self.type_formation.nom})"


class Thematique(models.Model):
    type_formation = models.ForeignKey(TypeFormation, on_delete=models.CASCADE, related_name="thematiques")
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name="thematiques")
    nom = models.CharField(max_length=100)
    code_prefix = models.CharField(max_length=3, default='')

    def __str__(self):
        return f"{self.nom} ({self.type_formation.nom})"


class Formation(models.Model):
    thematique = models.ForeignKey(Thematique, on_delete=models.CASCADE, related_name="formations")
    titre = models.CharField(max_length=200)
    duree = models.PositiveIntegerField(help_text="Durée de la formation")
    unite_duree = models.CharField(max_length=10, choices=[('heures', 'Heures'), ('jours', 'Jours'), ('semaines', 'Semaines'), ('mois', 'Mois')], default='heures')
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=20, unique=True, editable=False, default='')
    image = models.ImageField(upload_to='formations/', blank=True, null=True)  # Champ image

    def __str__(self):
        return f"{self.titre} - {self.code}"

    @property
    def prix_formate(self):
        prix_sans_decimales = int(self.prix)
        return f"{prix_sans_decimales:,}".replace(',', ' ')

    @property
    def image_url(self):
        """ Retourne l'URL de l'image ou une image par défaut si absente """
        if self.image:
            return self.image.url
        return "/static/img/formations/M&RH.png"  # Chemin de l'image par défaut


class Technique(models.Model):
    module = models.ForeignKey('Module', on_delete=models.CASCADE, related_name='techniques', null=True)
    contenu = models.CharField(max_length=200)

    def __str__(self):
        return self.contenu


class Module(models.Model):
    programme = models.ForeignKey('Programme', on_delete=models.CASCADE, related_name='modules', null=True)
    nom = models.CharField(max_length=200, null=True)
    ordre = models.PositiveIntegerField(default=1)  # Ordre du module
    techniques_brutes = models.TextField(help_text="Entrez chaque technique sur une ligne séparée", blank=True)

    @property
    def titre(self):
        return f"Module {self.ordre} - {self.nom}"

    def __str__(self):
        return f"{self.titre} (Module {self.ordre})"

    def sauvegarder_techniques(self):
        """Crée des instances de Technique à partir de la liste de techniques brutes."""
        # Supprime les techniques actuelles associées pour éviter les doublons
        self.techniques.all().delete()
        
        # Crée des nouvelles techniques en se basant sur chaque ligne de `techniques_brutes`
        techniques = self.techniques_brutes.strip().split('\n')
        for technique_contenu in techniques:
            Technique.objects.create(module=self, contenu=technique_contenu.strip())
            
            
            

class Programme(models.Model):
    formation = models.ForeignKey('Formation', on_delete=models.CASCADE, related_name="programmes")
    description_quoi = models.TextField(help_text="Qu'est-ce que la formation ?")
    description_pourquoi = models.TextField(help_text="Pourquoi se certifier ?")
    objectifs = models.TextField(help_text="Objectifs de la formation")
    public_cible = models.TextField("Public Cible", help_text="Entrez chaque public cible sur une nouvelle ligne", null=True)
    prerequis = models.TextField("Prérequis", help_text="Entrez chaque prérequis sur une nouvelle ligne", null=True)
    moyens_peda = models.TextField("Moyens pédagogiques", help_text="Entrez chaque moyen pédagogique sur une nouvelle ligne", null=True)
    inclus = models.TextField(help_text="Éléments inclus dans la formation", blank=True)

    def __str__(self):
        return f"Programme de {self.formation.titre}"

    def ajouter_module_et_techniques(self, nom_module, techniques=None):
        """
        Ajoute un module et ses techniques associées directement à ce programme.
        :param nom_module: Nom du module à ajouter.
        :param techniques: Liste de contenus de techniques à ajouter (ex. ["Technique 1", "Technique 2"])
        """
        # Détermine l'ordre du module en fonction du dernier ordre existant dans ce programme
        dernier_module = self.modules.order_by('ordre').last()
        nouvel_ordre = dernier_module.ordre + 1 if dernier_module else 1

        # Crée le module
        module = Module.objects.create(programme=self, nom=nom_module, ordre=nouvel_ordre)

        # Ajoute chaque technique associée au module
        if techniques:
            for contenu_technique in techniques:
                Technique.objects.create(module=module, contenu=contenu_technique)

        return module



class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
