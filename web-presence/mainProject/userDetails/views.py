from django.shortcuts import render
from userDetails.forms import memberDetailsForm
import datetime
from userDetails.models import memberDetails
from django.contrib.auth import get_user_model
# Create your views here.

class member():

	def editMember(self,request):
		user = get_user_model()
		print ('user id is:',user.id)
		my_record = memberDetails.objects.get(memberUserNumber=request.user.id)
		form = memberDetailsForm(instance=my_record)
		if form.is_valid():
			save_it=form.save(commit = False)
			save_it.memberRegistrationDate = datetime.datetime.now()
			save_it.memberUserNumber=request.user
			form.save()

		context={'form':form}
		return render(request,'editMember.html',context=context)

obj=member()
