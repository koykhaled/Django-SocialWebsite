from django.urls import path
from .views import dashboard
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
app_name = 'account'
urlpatterns = [
    # Authentiaction Urls
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # change password ulrs
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/',
         PasswordChangeDoneView.as_view(), name='password_change_done'),

    # rest password urls
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('', dashboard, name='dashboard'),
]