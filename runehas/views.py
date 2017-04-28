from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth import get_user_model, get_user
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponse, HttpResponseRedirect
from runehas.models import *
from accounts.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from userena.decorators import secure_required
from userena.utils import signin_redirect, get_profile_model, get_user_profile
from runehas.forms import *


# Create your views here.
def index(request):

    context_dict = locals()
    return render(request, "index.html", context_dict)


# Views for booking hostel (selecting and searching availability of hostel rooms to be booked)
@login_required()
def bookhostel(request):
    # Logic for selecting(searching) hostel preference to be booked
    form_class = SelectPreferenceForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)

    if form.is_valid():
        prefered_block = form.cleaned_data.get('prefered_block', None)
        prefered_room = form.cleaned_data.get('prefered_room', None)
        prefered_bed = form.cleaned_data.get('prefered_bed', None)

        return redirect('hostelbookingconfirmation')
    context_dict = {'form': form,}
    return render(request, "book_hostel.html", context_dict)


# Views for booking hostel (confirming selected room availability and completing booking and allocation process)
@login_required()
def confirmhostelbook(request):
    # Logic for confirming booking of hostel

    context_dict = locals()
    return render(request,"allocationconfirmation.html", context_dict)


# Views for booking hostel (showing and printing receipt of hostel allocation generated after completing allocation)
@login_required()
def printhostelreceipt(request):
    # Logic for booking hostel
    context_dict = locals()
    return render(request,"hostelreceipt.html", context_dict)

