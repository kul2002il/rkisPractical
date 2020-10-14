from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'main/index.html')


class BBLoginView(LoginView):
	template_name = 'main/login.html'


@login_required
def profile(request):
	return render(request, 'main/profile.html')


class BBLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'main/logout.html'
