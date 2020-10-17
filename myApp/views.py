from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.views.generic.base import TemplateView
from django.core.signing import BadSignature

from .utilities import signer
from .forms import RegisterUserForm
from .forms import ChangeUserInfoForm
from .models import User, Specialty, Appointment


def index(request):
	bbs = Specialty.objects.all()
	# l = []
	# # for bb in bbs:
	# # 	l.append(dict(
	# # 		nameRol = bb.nameRol,
	# # 		# userSpec = User.objects.filter(pk=bb.userId)[0]
	# # 		userSpec = bb.userId
	# # 	))
	#
	# l.append(dict(
	# 	nameRol = "Cpec",
	# 	# userSpec = User.objects.filter(pk=bb.userId)[0]
	# 	userSpec = "user"
	# ))
	context = {'bbs': bbs}
	return render(request, 'main/profile.html', context)


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


class BBPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
	template_name = 'main/passwordChange.html'
	success_url = reverse_lazy('myApp:profile')
	success_message = 'Пароль пользователя изменен'


class RegisterUserView(CreateView):
	model = User
	template_name = 'main/registerUser.html'
	form_class = RegisterUserForm
	success_url = reverse_lazy('myApp:login')


class RegisterDoneView(TemplateView):
	template_name = 'main/registerDone.html'


def user_activate(request, sign):
	try:
		username = signer.unsign(sign)
	except BadSignature:
		return render(request, 'main/bad_signature.html')
	user = get_object_or_404(User, username=username)
	# if user.is_activated:
	# 	template = 'main/userIsActivated.html'
	# else:
	# 	template = 'main/activationDone.html'
	# 	user.is_activated = True
	# 	user.is_active = True
	# 	user.save()

	template = 'main/activationDone.html'
	user.save()
	return render(request, template)

@login_required
def specialty(request):
	bbs = Specialty.objects.filter()
	context = {'bbs': bbs}
	return render(request, 'main/profile.html', context)


@login_required
def userAppointment(request, sign):
	if not sign:
		return render(request, 'main/bad_signature.html')
	specialty = get_object_or_404(Specialty, id=sign)
	write = Appointment(userId=request.user, docId=specialty)
	write.save()
	return render(request, 'main/appointment.html')
