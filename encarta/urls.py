"""encarta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from user import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('events/', TemplateView.as_view(template_name='event.html'), name='events'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('events/last_year/', TemplateView.as_view(template_name='last_year.html'), name='last_year'),
    path('events/having_fun/', TemplateView.as_view(template_name='having_fun.html'), name='having_fun'),
    path('events/after_fun/', TemplateView.as_view(template_name='after_fun.html'), name='after_fun'),
    path('events/hit_events/', TemplateView.as_view(template_name='hit_events.html'), name='hit_events'),
    path('register/', views.register, name='register'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)