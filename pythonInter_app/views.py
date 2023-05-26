'''
from django.shortcuts import render
from pythonInter_app.models import User
from django.http import JsonResponse

def user_list(request):
    users = User.objects.all()
    data = {
        'users': list(users.values())
        }
    return JsonResponse(data)

def user_details(request, pk):
    user = User.objects.get(pk=pk)
    data = {
        'name': user.name,
        'Self_description': user.Self_description,
        'available': user.available
    }
    return JsonResponse(data)
'''