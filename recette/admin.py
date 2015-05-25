from django.contrib import admin
from .models import Recette, Images, Etape, Type_Recette, Ingredient, Commentaire


class RecetteAdmin(admin.ModelAdmin):
    list_filter = ('titre', 'type_recette', 'difficulte', 'cout', 'temps_cuisson', 'temps_repos', 'note',
                   'date_creation', 'ingredients', 'etapes', 'images')
    date_hierarchy = 'date_creation'


class IngredientAdmin(admin.ModelAdmin):
    list_filter = ['nom_ingredient']


class EtapeAdmin(admin.ModelAdmin):
    list_filter = ('numero_etape', 'nom_etape')


class ImageAdmin(admin.ModelAdmin):
    list_filter = ['nom']


class Type_RecetteAdmin(admin.ModelAdmin):
    list_filter = ['type_recette']


class CommentaireAdmin(admin.ModelAdmin):
    list_filter = ['contenu', 'utilisateur']


# Register your models here.
admin.site.register(Recette, RecetteAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Etape, EtapeAdmin)
admin.site.register(Type_Recette, Type_RecetteAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Commentaire, CommentaireAdmin)
