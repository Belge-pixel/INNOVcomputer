from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
from blog.models import New
from formations.models import Formation
from users.models import User
from .models import StaffProfile
from .forms import StaffProfileForm

def staff_required(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(staff_required)
def home(request):
    try:
        profile = request.user.staff_profile
    except StaffProfile.DoesNotExist:
        profile = None

    context = {
        'profile': profile,
    }    
    return render(request, 'staff/home.html', context)

@user_passes_test(staff_required)
def dashboard(request):
    total_users = User.objects.count()
    total_posts = New.objects.count()
    total_formations = Formation.objects.count()
    total_revenue = "15,420 $"  # Valeur placeholder

    context = {
        'total_users': total_users,
        'total_posts': total_posts,
        'total_formations': total_formations,
        'total_revenue': total_revenue,
        'current_date': timezone.now(),
    }
    return render(request, 'staff/dashboard.html', context)
