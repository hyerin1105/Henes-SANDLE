from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

# Create your views here.
def main(request):
    return render(request,'main.html')
def goods(request):
    return render(request,'goods.html')
def complete(request):
    return render(request,'complete.html')