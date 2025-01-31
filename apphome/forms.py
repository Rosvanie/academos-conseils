from django import forms
from .models import *



class RechercheForm(forms.Form):
    q = forms.CharField(max_length=100, required=False)



class NewsletterSubscriberForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']  # Supprimer "password"

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NewsletterSubscriber.objects.filter(email=email).exists():
            raise forms.ValidationError("Cette adresse email est déjà abonnée.")
        return email
