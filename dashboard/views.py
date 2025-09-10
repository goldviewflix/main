from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from kyc.models import KYCProfile

@login_required
def dashboard(request):
    try:
        kyc_profile = request.user.kyc_profile
    except KYCProfile.DoesNotExist:
        kyc_profile = None

    context = {
        'kyc_profile': kyc_profile,
    }
    return render(request, 'dashboard/dashboard.html', context)
