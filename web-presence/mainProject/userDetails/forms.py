from django import forms
from userDetails.models import memberDetails

class memberDetailsForm(forms.ModelForm):
	class Meta:
		model= memberDetails
		fields = '__all__'
		exclude = ['memberRegistrationDate','memberUserNumber']