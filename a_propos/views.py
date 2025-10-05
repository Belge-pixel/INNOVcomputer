from django.shortcuts import render
from expertise.models import Expertise
from formations.models import Formation
# Create your views here.
def about(request):
    expertises =None
    formations=None
    formations = Formation.objects.all()
    expertises = Expertise.objects.all()
    context ={'expertises':expertises,"formations":formations}
    return render(request, 'a_propos/about.html',context=context)
