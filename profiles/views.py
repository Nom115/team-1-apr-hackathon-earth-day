from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile

# Create your views here.
@login_required
def profile(request):
    """ A view to return profile page """
    
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profiles/profile.html', context)
