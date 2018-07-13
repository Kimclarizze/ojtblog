from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('register/', views.Register,name='Register'),
    path('signin/', views.Signin,name='Signin'),    
    path('welcome/', views.welcome, name='welcome'),
    path('logout/', views.Logout,name='Logout'),
    path('profile/', views.profile, name='profile'),
    path('accountsettings/', views.editprofile, name='accountsettings'),
    path('change_password/', views.change_password, name='changepassword'),
    path('home/', views.home, name='home'),
    path('base/', views.base, name='base'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
