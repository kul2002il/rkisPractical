from django.urls import path
from . import views
from .views import BBLoginView, BBLogoutView, ChangeUserInfoView, BBPasswordChangeView, RegisterUserView,\
    RegisterDoneView, user_activate, userAppointment

app_name = 'myApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', BBLoginView.as_view(), name="login"),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name="logout"),
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),

    path('specialisty/', views.specialty, name='specialisty'),
    path('appointment/<str:sign>/', userAppointment, name='appointmentUser'),
]

