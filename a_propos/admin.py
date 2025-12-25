from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Formation)
admin.site.register(Cours)
admin.site.register(Chapitre)
admin.site.register(Expertise)


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('titre_mission', 'ordre', 'date_creation')
    list_editable = ('ordre',)
    search_fields = ('titre_mission',)
    ordering = ('ordre',)


@admin.register(Responsable)
class ResponsableAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'role_principal', 'specialite', 'ordre', 'date_creation')
    list_editable = ('ordre',)
    search_fields = ('prenom_responsable', 'nom_responsable', 'role_principal')
    ordering = ('ordre',)