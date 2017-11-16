from django import forms
from userDetails.models import memberDetails,memberSocialNetworks

class memberDetailsForm(forms.ModelForm):
	class Meta:
		model= memberDetails
		fields = '__all__'
		exclude = ['memberRegistrationDate','memberUserNumber']

	def __init__(self, *args, **kwargs):
		super(memberDetailsForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.pk:
		    self.fields['memberURLUserName'].widget.attrs['readonly'] = True
		    
	def clean_sku(self):
		if self.instance and self.instance.pk:
			return self.instance.memberURLUserName
		else:
			return self.cleaned_data['memberURLUserName']

class memberSocialNetworksForm(forms.ModelForm):
	class Meta:
		model= memberSocialNetworks
		fields = '__all__'
		exclude = ['memberUserNumber']