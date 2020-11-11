from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render
# Create your views here.
import requests
from django.views.decorators.csrf import csrf_exempt
from pylabz.models import Contact
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from pylabz.models import Contact
from pylabz.serializers import ContactSerializer
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer

from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

# from django.db.models import Count
# q =  Contact.objects.annotate(Count('firstname'))
# print(q)#`retreive row from dajngo model
# print(q[2].firstname)
# print(q[5].email)
# print(Contact)
# print(dir(Contact))



# t =  Contact.objects.filter(firstname='deepakq').update(firstname='deepak rayathurai')
# print('sadasdasdasd',t)


# t =  Contact.objects.get(firstname='asasdasdkaudiuad')
# t.firstname = 'Not a avlid name'
# t.save()

# for eachitem in Contact.objects.all():
# 	print(eachitem.firstname,eachitem.email)


user_dict= {'deepak': 'admin'}

def index(request):
	# url = 'http://www.datacamp.com'
	# url_check = requests.get(url,verify=False)
	# return HttpResponse(f'the status of the {url} is  \n {url_check.status_code}')
	return render(request,'base.html')

@csrf_exempt
def validate(request):
	# write_some_logic_to validata
	if user in user_dict and user_dict.get(usr)==pwd:
			return HttpResponse('user is valid')
	else:
		return HttpResponse('Invalid user')

#get the data and  inserting the data as row to model
def contact(request):
    if request.method=="POST":
    	print('Hey ia am here')
    	# print(request.POST['csrfmiddlewaretoken'])
    	# print(request.POST['firstname'])
    	firstname= request.POST.get('firstname')
    	print(firstname)
    	email= request.POST.get('email')
    	print(email)
    	ins =  Contact(firstname = firstname,email = email)
    	ins.save()
    	return render(request,'failurepage.html')

@csrf_exempt
@api_view(['GET','POST'])
def contact_list(request):
    if request.method == 'GET':
    	# print(request.query_params['id_'])
    	# contacts= Contact.objects.filter(id=id_).values()

    	# return JsonResponse({"models_to_return": list(contacts)})
    	return Response({'name':'deepak'})

    elif request.method == 'POST':
        return JsonResponse('hello post', status=400)

# class CustomBrowsableAPIRenderer(BrowsableAPIRenderer):
#     def get_default_renderer(self, view):
#         return JSONRenderer()





# Models ----- Database

#  Db has  to be created   either  through settings.py and  through conventional 

#  CREATE TABLE  student('id' serial not Null primary key,
#  	'fisr_name' varchar(30) not NULL',
#  	'last_name' varchar(34) not NULL,
#  	)
#             class mapped as db
#  ORM ---Object relationship mapping 

#  class ------TABLE
#  each variable with fields ---- fields
# # schema has to becrated
# # palying through data






