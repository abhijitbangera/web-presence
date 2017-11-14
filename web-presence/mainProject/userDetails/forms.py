from django import forms
from userDetails.models import memberDetails,memberSocialNetworks

class memberDetailsForm(forms.ModelForm):
	class Meta:
		model= memberDetails
		fields = '__all__'
		exclude = ['memberRegistrationDate','memberUserNumber']

class memberSocialNetworksForm(forms.ModelForm):
	class Meta:
		model= memberSocialNetworks
		fields = '__all__'
		exclude = ['memberUserNumber']