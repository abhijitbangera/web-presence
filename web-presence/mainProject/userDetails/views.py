from django.shortcuts import render
from userDetails.forms import memberDetailsForm,memberSocialNetworksForm
import datetime
from userDetails.models import memberDetails,memberSocialNetworks
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your views here.

class member():
	def __init__(self):
		user = get_user_model()
		print ('user id is:',user.id)

	def editMember(self,request):
		form = memberDetailsForm(request.POST or None)
		print ("editMember")
		if memberDetails.objects.filter(memberUserNumber=request.user.id).exists():	
			my_record = memberDetails.objects.get(memberUserNumber=request.user.id)
			form = memberDetailsForm(instance=my_record)
			if request.method=='POST':
				memberDetails.objects.filter(memberUserNumber=request.user.id).update(\
					memberName=request.POST['memberName'],memberGender=request.POST['memberGender'],memberLocation=request.POST['memberLocation'],\
					memberContactNumber=request.POST['memberContactNumber'],memberOccupation=request.POST['memberOccupation'],\
					memberAge=request.POST['memberAge'], memberEmail=request.POST['memberEmail']
					)
				my_record = memberDetails.objects.get(memberUserNumber=request.user.id)
				form = memberDetailsForm(instance=my_record)
		elif request.POST:
			user = get_user_model()
			if form.is_valid():
				print("valid")
				save_it=form.save(commit = False)
				save_it.memberUserNumber=request.user
				save_it.memberRegistrationDate=datetime.datetime.now()
				form.save()
		context={'form':form}
		return render(request,'editMember.html',context=context)

	def editWeb(self, request):
		form = memberSocialNetworksForm(request.POST or None)
		print ("editweb")
		if memberSocialNetworks.objects.filter(memberUserNumber=request.user.id).exists():
			my_record = memberSocialNetworks.objects.get(memberUserNumber=request.user.id)
			form = memberSocialNetworksForm(instance=my_record)
			if request.method=='POST':
				print("inside")
				print (request)
				memberSocialNetworks.objects.filter(memberUserNumber=request.user.id).update(\
					facebook=request.POST['facebook'],twitter=request.POST['twitter'],linkedin=request.POST['linkedin'],\
					github=request.POST['github'],googleplus=request.POST['googleplus'],\
					stackoverflow=request.POST['stackoverflow']
					)
				my_record = memberSocialNetworks.objects.get(memberUserNumber=request.user.id)
				form = memberSocialNetworksForm(instance=my_record)
		elif request.POST:
			if form.is_valid():
				print ("valid")
				save_it=form.save(commit = False)
				save_it.memberUserNumber=user
				form.save()
		context={'form':form}
		return render(request,'social.html',context=context)
	

obj=member()
