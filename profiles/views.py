from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileImageForm
from django.contrib.auth import get_user_model
from .models import UserProfile

# Create your views here.
@login_required
def profile(request):
    """ A view to return profile page """
    
    User = get_user_model()
    user_profile = get_object_or_404(UserProfile, user=request.user)
    instance = UserProfile.objects.get(pk=request.user.id)

    if request.method == 'POST':
        form = UserProfileImageForm(request.POST, request.FILES)

        if form.is_valid():
            for filename, file in request.FILES.items():
                instance.image = request.FILES[filename].name

            instance.user = User.objects.get(pk=request.user.id)
            instance.save()

            messages.success(
                request,
                'Hail EaRRRth hero, your snazzy new avatar has been uploaded'  # noqa ES501
            )
            return redirect(reverse('profile'))
    else:
        form = UserProfileImageForm(instance=request.user)
    context = {
        'user_profile_image_form': form,
        'user_profile': user_profile,
    }
    return render(request, 'profiles/profile.html', context)
