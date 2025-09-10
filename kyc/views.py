from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import KYCProfileForm
from .models import KYCProfile

@login_required
def kyc_submission(request):
    try:
        kyc_profile = request.user.kyc_profile
    except KYCProfile.DoesNotExist:
        kyc_profile = None

    if request.method == 'POST':
        form = KYCProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_kyc_profile = form.save(commit=False)
            new_kyc_profile.user = request.user
            new_kyc_profile.save()
            return redirect('dashboard')
    else:
        form = KYCProfileForm()

    return render(request, 'kyc/kyc_submission.html', {
        'form': form,
        'kyc_profile': kyc_profile,
    })
