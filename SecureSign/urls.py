"""SecureSign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Home import views as HomeView
from Login import views as LoginView
from CreateAccount import views as CreateAccountView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.index, name='index'),
    path('Contact/', HomeView.Contact, name='Contact'),
    path('UserDashboard/', include('UserDashboard.urls')),
    path('ManageDocument/', include('ManageDocument.urls')),
    path('CreateAccount/', CreateAccountView.CreateAccount, name='CreateAccount'),
    path('Login/', LoginView.login, name="Login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
