from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Shop, User, Pickles
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from .forms import UserRegisterForm, UserUpdateForm
import pickle
from datasketch import MinHash, MinHashLSHForest
import time
import numpy as np
from tkinter import filedialog
import pandas as pd
from django import forms
from .forms import UploadFileForm

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
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request,'users/profile.html', context)


def shop(request):
    context = {
        'shops': Shop.objects.all()
    }
    return render(request, 'users/shop.html', context)

class ShopListView(ListView):
    model = Shop
    template_name = 'users/shop.html'
    context_object_name = 'shops'

class ShopCreateView(LoginRequiredMixin, CreateView):
    model = Shop
    fields = ['store_name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ShopUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Shop
    fields = ['store_name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        shop = self.get_object()
        if self.request.user == shop.user:
            return True
        return False

class ShopDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Shop
    success_url = '/'

    def test_func(self):
        shop = self.get_object()
        if self.request.user == shop.user:
            return True
        return False

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        file_before = request.FILES['file_before']
        file_after = request.FILES['file_after']
        pickle = Pickles.objects.create(store_pickle_before = file_before, store_pickle_after=file_after)
        pickle.save()
        return HttpResponse("The shop with id " + str(pickle.pk) + "has the file: " + str(pickle.store_pickle_after))
    else:
        form = UploadFileForm()
    return render(request, 'users/upload.html', {'form': form})