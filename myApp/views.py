from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import ChangeUserInfoForm
from .models import User


def index(request):
	return render(request, 'main/index.html')


class BBLoginView(LoginView):
	template_name = 'main/login.html'


@login_required
def profile(request):
	return render(request, 'main/profile.html')


class BBLogoutView(LoginRequiredMixin, LogoutView):
	template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
	model = User
	template_name = 'main/changeUserInfo.html'
	form_class = ChangeUserInfoForm
	success_url = reverse_lazy('myApp:profile')
	success_message = 'Личные данные пользователя изменены'

	def dispatch(self, request, *args, **kwargs):
		self.user_id = request.user.pk
		return super().dispatch(request, *args, **kwargs)

	def get_object(self, queryset=None):
		if not queryset:
			queryset = self.get_queryset()
		return get_object_or_404(queryset, pk=self.user_id)
