from django.shortcuts import render
from . import fake_ml

def run(request):
    return render(request,'index.html')


def run1(request):
    user = float(request.GET['age'])
    prediction = fake_ml.prediction(user)
    return render(request,'result.html',{'user': prediction})