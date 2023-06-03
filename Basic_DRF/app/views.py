from django.shortcuts import render,HttpResponse
import json
# Create your views here.
def drf_HTML_Response(request):
    
    
    
    
    emp={
        'ename':'narendra',
        'esal':100000,
        'eage':22,
        'eaddr':"Hyderabad"
    }
    # this how we send HTML response to the user.
    res="employee name is {}<br> employee salary is {}<br> employee location is {}".format(emp['ename'],emp['esal'],emp['eaddr'])
    return HttpResponse(res)
    
    
def drf_json_response(request):
    # I want to send in Json format.
    # dumps () method is used to convert dict to json object
    emp={
        'ename':'narendra',
        'esal':100000,
        'eage':22,
        'eaddr':"Hyderabad"
    }
    json_data=json.dumps(emp)
    return HttpResponse(json_data,content_type='application/json') 
    # this is the order version of converting dict datatype to json.abs(x)
    
from django.http import JsonResponse
def drf_json_newer(request):
    emp={
        'ename':'narendra',
        'esal':100000,
        'eage':22,
        'eaddr':"Hyderabad"
    }
    # simpler and easy to use this
    # JsonResponse(emp) this will convert dict to json data
    return JsonResponse(emp)



#  How do python communicate with Django application?

# we will use requests module for communicating with the django application


# import requests
# BASE_URL='http://localhost:8000/'
# ENDPOINT='api/'
# r=requests.get(BASE_URL+ENDPOINT)
# # r will request data from the above URL and that will get use a data
# print(type(r))
# data=r.json()
# print(data['ename])



#  we can use HTTPie module to send http request from command prompt
# pip install httpie
# http localhost:8000/api/