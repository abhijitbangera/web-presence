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
		form = memberDetailsForm()
		if memberDetails.objects.filter(memberUserNumber=request.user.id).exists():	
			my_record = memberDetails.objects.get(memberUserNumber=request.user.id)
			form = memberDetailsForm(instance=my_record)
			if request.method=='POST':
				print ("yesssss")
				print (request.POST)
				memberDetails.objects.filter(memberUserNumber=request.user.id).update(\
					memberName=request.POST['memberName'],memberGender=request.POST['memberGender'],memberLocation=request.POST['memberLocation'],\
					memberContactNumber=request.POST['memberContactNumber'],memberOccupation=request.POST['memberOccupation'],\
					memberAge=request.POST['memberAge'], memberEmail=request.POST['memberEmail']
					)
				my_record = memberDetails.objects.get(memberUserNumber=request.user.id)
				form = memberDetailsForm(instance=my_record)

		context={'form':form}
		return render(request,'editMember.html',context=context)

obj=member()
