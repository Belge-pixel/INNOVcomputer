from django import forms
from .models import New

class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['new_title', 'new_content', 'new_image']
        labels = {
            'new_title': 'Titre',
            'new_content': 'Contenu',
            'new_image': 'Image',
        }
        widgets = {
            # Champ titre
            'new_title': forms.TextInput(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 '
                    'focus:border-indigo-500 placeholder-gray-400'
                ),
                'placeholder': 'Titre de l\'article',
            }),

            # Champ contenu
            'new_content': forms.Textarea(attrs={
                'class': (
                    'mt-2 mb-4 block w-full rounded-lg border border-gray-300 '
                    'px-4 py-3 h-40 resize-vertical focus:outline-none '
                    'focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 '
                    'placeholder-gray-400'
                ),
                'placeholder': 'Écris le contenu ici...',
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
        }
