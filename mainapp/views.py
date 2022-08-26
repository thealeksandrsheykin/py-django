from django.http import HttpResponse
from django.views.generic import View

#  FBV

# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.

# def hello_world(request):
#     return HttpResponse('Hello World')

def check_kwargs(request,**kwargs):
    return HttpResponse(f'kwargs:<br>{kwargs}')


#CBV



class HelloWorldView(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Hello World')




