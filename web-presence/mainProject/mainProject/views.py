from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests

def get_stackOverFlow(user_id):
	r = requests.get('https://api.stackexchange.com/2.2/users/'+user_id+'?order=desc&sort=reputation&site=stackoverflow')
	print (r.text)
	print ('---')
	x=r.json()
	print x
	for i in x['items']:
		rep=i['reputation']
	print rep



@login_required
def home(request):
    return render(request, 'home.html')

get_stackOverFlow('4136116')