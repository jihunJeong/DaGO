from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.views.generic import FormView
from .forms import RegisterForm, LoginForm
import datetime
from .models import User


# Create your views here.
def login(request):
    if request.method == 'GET':
        form = LoginForm()
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session['user'] = form.email
            return redirect('/')

    return render(request, 'user/login.html', {'form' : form})

def logout(request):
    if request.session.get('user'):
        del (request.session['user'])

    return redirect('/')


class RegisterView(FormView):
    template_name = "user/register.html"
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        email = form.data.get('email')
        password = form.data.get('password')
        nickname = form.data.get('nickname')
        contact = form.data.get('contact')
        address = form.data.get('address')
        # user = User(
        #     email=email,
        #     password=make_password(password),
        #     nickname = nickname,
        #     contact = contact,
        #     address = address,
        #     level='user'
        # )
        user = User(
            email=email,
            password=make_password(password),
            nickname = nickname,
            contact = contact,
            address = address,
            enroll_date = datetime.datetime.now().strftime('%Y-%m-%d'),
            rule_id='1',
            # credit_id='1',
        )
        user.save()

        self.request.session['user'] = email
        return super().form_valid(form)


class LoginView(FormView):
    template_name = "user/login.html"
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)