from django import forms
from .models import New


class NewForm(forms.ModelForm):
    """
    Formulaire de création et d’édition d’un article du blog.
    Basé sur le modèle New.
    """
    class Meta:
        model = New

        # ✅ Champs que l’utilisateur peut modifier manuellement
        fields = [
            'new_title',
            'new_content',
            'new_excerpt',
            'new_image',
            'new_category',
            'new_tags',
            'new_status',
        ]

        # ✅ Libellés lisibles pour l’interface
        labels = {
            'new_title': 'Titre',
            'new_content': 'Contenu',
            'new_excerpt': 'Résumé',
            'new_image': 'Image',
            'new_category': 'Catégorie',
            'new_tags': 'Mots-clés',
            'new_status': 'Statut',
        }

        # ✅ Widgets stylisés (compatibles avec TailwindCSS)
        widgets = {
            # Champ titre
            'new_title': forms.TextInput(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 '
                    'focus:border-indigo-500 placeholder-gray-400'
                ),
                'placeholder': "Titre de l'article",
            }),

            # Champ contenu
            'new_content': forms.Textarea(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-3 h-48 resize-vertical focus:outline-none '
                    'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 '
                    'placeholder-gray-400'
                ),
                'placeholder': "Rédige ton article ici...",
            }),

            # Champ résumé
            'new_excerpt': forms.Textarea(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-3 h-24 resize-vertical focus:outline-none '
                    'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 '
                    'placeholder-gray-400'
                ),
                'placeholder': "Courte description ou introduction...",
            }),

            # Champ image
            'new_image': forms.ClearableFileInput(attrs={
                'class': (
                    'mt-2 mb-4 block w-full text-sm rounded-lg border border-gray-300 '
                    'file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 '
                    'file:bg-indigo-50 file:text-indigo-700 hover:file:bg-indigo-100 '
                    'cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500'
                ),
            }),

            # Champ catégorie
            'new_category': forms.TextInput(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 '
                    'focus:border-indigo-500 placeholder-gray-400'
                ),
                'placeholder': 'Ex: Technologie, Santé, Éducation...',
            }),

            # Champ tags
            'new_tags': forms.TextInput(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 '
                    'focus:border-indigo-500 placeholder-gray-400'
                ),
                'placeholder': 'Ex: innovation, IA, tendances...',
            }),

            # Champ statut (menu déroulant)
            'new_status': forms.Select(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-2 bg-white focus:outline-none focus:ring-2 '
                    'focus:ring-indigo-500 focus:border-indigo-500'
                ),
            }),
        }
