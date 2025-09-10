from django import forms
from .models import KYCProfile

class KYCProfileForm(forms.ModelForm):
    class Meta:
        model = KYCProfile
        fields = [
            'document_type',
            'pan_number',
            'pan_card_image',
            'aadhar_number',
            'aadhar_front_image',
            'aadhar_back_image',
            'passport_number',
            'passport_front_image',
            'passport_back_image',
            'selfie_image',
        ]
        widgets = {
            'document_type': forms.RadioSelect,
        }
