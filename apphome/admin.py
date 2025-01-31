from django.contrib import admin
from .models import *
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

# Inline pour Technique
class TechniqueInline(admin.StackedInline):
    model = Technique
    extra = 1  # Nombre de champs vides pour ajouter des techniques

# Inline pour Module avec TechniqueInline
class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1  # Nombre de champs vides pour ajouter des modules
    inlines = [TechniqueInline]  # Ajoute TechniqueInline dans chaque module

# Admin pour Programme avec ModuleInline imbriqué
@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('formation', 'description_quoi')
    fields = ('formation', 'description_quoi', 'objectifs', 'public_cible', 'prerequis', 'moyens_peda','inclus')
    formfield_overrides = {
        models.TextField: {'widget': admin.widgets.AdminTextareaWidget(attrs={'rows': 4, 'cols': 40})},
    }
    inlines = [ModuleInline]  # Ajoute ModuleInline pour chaque programme



# Configuration des autres modèles
@admin.register(TypeFormation)
class TypeFormationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'image')
    search_fields = ('nom',)

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_formation')
    list_filter = ('type_formation',)
    search_fields = ('nom', 'type_formation__nom')

@admin.register(Thematique)
class ThematiqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_formation', 'categorie')
    list_filter = ('type_formation', 'categorie')
    search_fields = ('nom', 'type_formation__nom', 'categorie__nom')

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'thematique', 'code', 'duree', 'unite_duree', 'afficher_prix')
    list_filter = ('thematique__type_formation', 'thematique', 'unite_duree')
    search_fields = ('titre', 'thematique__nom', 'thematique__type_formation__nom', 'code')

    fieldsets = (
        (None, {
            'fields': ('titre', 'thematique')
        }),
        ('Détails de la formation', {
            'fields': ('duree', 'unite_duree', 'prix'),
            'description': "Spécifiez la durée et l'unité de la formation.",
        }),
    )
    
    readonly_fields = ('code',)

    def afficher_prix(self, obj):
        return obj.prix_formate
    afficher_prix.short_description = 'Prix (en CFA)'


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)  # Ajout d'une virgule pour en faire un tuple
    search_fields = ('email',)  # Ajout d'une virgule pour en faire un tuple
