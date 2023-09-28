from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def taskList(request):
  return HttpResponse("TO_DO_LIST and more!")
