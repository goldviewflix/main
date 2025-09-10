from django.db import models
from django.contrib.auth.models import User

class KYCProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='kyc_profile')

    DOCUMENT_TYPE_CHOICES = (
        ('AADHAR', 'Aadhar Card'),
        ('PASSPORT', 'Passport'),
    )
    document_type = models.CharField(max_length=10, choices=DOCUMENT_TYPE_CHOICES)

    pan_number = models.CharField(max_length=10)
    pan_card_image = models.ImageField(upload_to='kyc/pan/')

    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    aadhar_front_image = models.ImageField(upload_to='kyc/aadhar/', blank=True, null=True)
    aadhar_back_image = models.ImageField(upload_to='kyc/aadhar/', blank=True, null=True)

    passport_number = models.CharField(max_length=20, blank=True, null=True)
    passport_front_image = models.ImageField(upload_to='kyc/passport/', blank=True, null=True)
    passport_back_image = models.ImageField(upload_to='kyc/passport/', blank=True, null=True)

    selfie_image = models.ImageField(upload_to='kyc/selfies/')

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"KYC Profile for {self.user.username}"
