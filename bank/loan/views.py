
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PersonForm

import pickle
import numpy as np

# Create your views here.
def home(request):
    return HttpResponse('Welcome to the page')

def predict(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            age = form.cleaned_data['age']
            income = form.cleaned_data['income']
            family = form.cleaned_data['family']
            ccavg = form.cleaned_data['ccavg']
            education = form.cleaned_data['education']
            mortgage = form.cleaned_data['mortgage']
            sec_account = form.cleaned_data['sec_account']
            cd_account = form.cleaned_data['cd_account']
            online = form.cleaned_data['online']
            credit_card = form.cleaned_data['credit_card']

            X=np.asarray([25,100000,2,5000,3,456,0,0,0,1])
            #X = np.asarray([age,income,family,ccavg,education,mortgage,sec_account,cd_account,online,credit_card])
            X = X.reshape(-1,1)
            model = pickle.load(open(r'F:\django loan\bank\loan\final', 'rb'))
            y_pred = model.predict(X)
            if y_pred[0] == 1:
                return HttpResponse("Success")
            else:
                return HttpResponse('Failed')
    else:
        form = PersonForm()
        return render(request,'predict.html',locals())
