from django.urls import path
from . import views
from .views import BBLoginView, BBLogoutView, ChangeUserInfoView

app_name = 'myApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('accounts/login/', BBLoginView.as_view(), name="login"),
    path('accounts/profile/', views.profile, name="profile"),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/logout/', BBLogoutView.as_view(), name="logout"),
]

