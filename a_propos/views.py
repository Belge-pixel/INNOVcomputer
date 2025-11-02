from django.shortcuts import render
from expertise.models import Expertise
from formations.models import Formation
# Create your views here.
def about(request):
    expertises =None
    formations=None
    formations = Formation.objects.all().order_by('-id')
    expertises = Expertise.objects.all().order_by('-id')
    context ={'expertises':expertises,"formation_list":formations}
    return render(request, 'a_propos/about.html',context=context)
