"""
URL configuration for portfolio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name='home'),

    # Projects
    path('projects/', views.project_list, name='projects'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),

    # Personal Information
    path('personal-information/', views.personal_information, name='personal_information'),

    # Contact / Inquiry
    path('contact/', views.inquiry, name='contact'),

    # Testimonies
    path('testimonies/', views.testimony_list, name='testimony_list'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/<int:id>/', views.testimony_detail, name='testimony_detail'),
    # Admin
    path('admin/', admin.site.urls),
]

handler404 = 'portfolio.views.custom_404'
handler500 = 'portfolio.views.custom_500'