from django import forms
from .models import Expertise

class ExpertiseForm(forms.ModelForm):
    class Meta:
        model = Expertise
        fields = ['titre', 'description', 'icone', 'image']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 shadow-sm placeholder-gray-400 transition',
                'placeholder': 'Titre de l’expertise'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 shadow-sm placeholder-gray-400 transition',
                'rows': 5,
                'placeholder': 'Description de l’expertise'
            }),
            'icone': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 shadow-sm placeholder-gray-400 transition',
                'placeholder': 'Nom de l’icône, ex: fa-solid fa-code'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'w-full border border-gray-300 rounded-xl px-4 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500 shadow-sm transition'
            }),
        }
