from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('login/',views.user_login, name='login'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
   
    # #change passwords urls
    # path('password_change/', auth_views.PasswordChangeView.as_view(),
    #     name='password_change'),
    # path('password_change/done', auth_views.PasswordChangeDoneView.as_view(),
    #     name= 'password_change_done'),


    # #resetting password urls
    # path('password_reset/', auth_views.PasswordResetView.as_view(),
    # name='password_reset'), 
    # path('password_reset/done/',
    # auth_views.PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    # path('reset/<uidb64>/<token>/',
    # auth_views.PasswordResetConfirmView.as_view(),
    # name='password_reset_confirm'),
    # path('reset/done/',
    # auth_views.PasswordResetCompleteView.as_view(),
    # name='password_reset_complete'),


    path('',views.dashboard, name = 'dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register,name='register'),
    path('edit/', views.edit, name='edit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

