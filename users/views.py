from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from .forms import UserRegisterForm
import pickle
from datasketch import MinHash, MinHashLSHForest
import time
import numpy as np
from tkinter import filedialog
import pandas as pd


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request,'users/profile.html')

#-----------------------------------------------------------------------------------------------------

def preprocess(text):
    tokens = text.lower()
    tokens = tokens.split()
    return tokens

def predict(request):
    text = 'googlesearchservice'

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
    if len(idx_array) == 0:
        return None # if your query is empty, return none

    result = database.iloc[idx_array]['Service Name'] 

    print('It took %s seconds to build forest.' %(time.time()-start_time))

    print(result)

    return render(request,'users/profile.html')