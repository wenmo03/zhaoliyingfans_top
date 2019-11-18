from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def user_profile(request):
    html = '''
    <center><h1>UserProfile</h1></center>
    '''
    return HttpResponse(html)