from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import HttpResponseRedirect, render
from store.models import Customer

from accounts.forms import FormRegistrazione


def registrazione_view(request):
    if request.method == "POST":
        form = FormRegistrazione(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password1"]
            User.objects.create_user(username=username, password=password, email=email)
            user = authenticate(username=username, password=password)
            Customer.objects.create(user=user,name=username,email=email)
            login(request, user)
            return HttpResponseRedirect("/")
    else:
        form = FormRegistrazione()
    context = {"form": form}
    return render(request, "accounts/registrazione.html", context)
