from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages

from utils.token import account_activation_token

from .forms import SignupForm

# TODO: sign up / login with google and other websites + customize
# TODO: google Roboter test


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            message = render_to_string('register/verification.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')

            email = EmailMessage('Activation link has been sent to your email id', message, to=[to_email])
            email.send()

            return render(request, 'register/verification_link_sent.html')
    else:
        form = SignupForm()
    return render(request, 'register/signup.html', {'form': form})


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Your account has been successfully activated. You are now logged in.')
        return render(request, 'register/email_confirmed.html')
    else:
        return render(request, 'register/invalid_activation_link.html')


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.warning(request, "Invalid username or password.")
        else:
            messages.warning(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'register/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logout successfully!")
    return redirect('home')