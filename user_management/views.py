from django.shortcuts import render
from user_management.forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect

from django.urls import reverse


def manage_user(request):
    if request.method == 'POST':
        print("in method post")
        print(request.POST.get('email'))
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Members Add Successfully')
            return HttpResponseRedirect(reverse('index_field'))
        else:
            print('something missing')
            messages.error(request, 'Something missing !')
            return render(request, 'register.html',)
    else:
        return render(request, 'register.html')
