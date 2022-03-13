from django.shortcuts import render, redirect
from .forms import SearchForm
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic.base import View
import pickle
from datasketch import MinHash, MinHashLSHForest
import time
import numpy as np
from tkinter import filedialog
import pandas as pd

# Create your views here.

def home(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            response_time = form.cleaned_data['response_time']
            availability = form.cleaned_data['availability']
            throughput = form.cleaned_data['throughput']
            successability = form.cleaned_data['successability']
            reliability = form.cleaned_data['reliability']
            compliance = form.cleaned_data['compliance']
            best_practices = form.cleaned_data['best_practices']
            latency = form.cleaned_data['latency']
            documentation = form.cleaned_data['documentation']
            service_name = form.cleaned_data['service_name']
            Wsdl_address = form.cleaned_data['Wsdl_address']

            print(response_time, availability)
            
            text = response_time + " " + availability + " " + throughput + " " + successability + " " + reliability + " " + compliance + " " + best_practices + " " + latency + " " + documentation + " " + service_name

            pickle_in1 = open("dict.pickledb", "rb")
            database = pickle.load(pickle_in1)

            perms = 256
            num_results = 10

            start_time = time.time()

            print(start_time)

            pickle_in = open("dict.pickle", "rb")
            example_dict = pickle.load(pickle_in)

            tokens = preprocess(text)
            m = MinHash(num_perm=perms)
            for s in tokens:
                m.update(s.encode('utf8'))

            idx_array = np.array(example_dict.query(m, num_results))
            #if len(idx_array) == 0:
            #    return None # if your query is empty, return none

            #prepei na dw pws 8a ta emfanizw ola
            result = database.iloc[idx_array]['Service Name'] 

            print('It took %s seconds to build forest.' %(time.time()-start_time))

            print(result)
            
            return render(request,'search/home.html', {'form' : form, 'result' : result })
    form = SearchForm
    return render(request,'search/home.html', {'form' : form})

def preprocess(text):
    tokens = text.lower()
    tokens = tokens.split()
    return tokens


def about(request):
    return render(request,'search/about.html',)


