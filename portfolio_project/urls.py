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
    # =====================================================
    # PUBLIC PORTFOLIO
    # =====================================================

    path('', views.home, name='home'),

    path(
        'projects/',
        views.project_list,
        name='projects'
    ),

    path(
        'projects/<int:id>/',
        views.project_detail,
        name='project_detail'
    ),

    path(
        'personal-information/',
        views.personal_information,
        name='personal_information'
    ),

    path(
        'contact/',
        views.inquiry,
        name='contact'
    ),

    path(
        'testimonies/',
        views.testimony_list,
        name='testimony_list'
    ),

    path(
        'testimonies/add/',
        views.add_testimony,
        name='add_testimony'
    ),

    path(
        'testimonies/<int:id>/',
        views.testimony_detail,
        name='testimony_detail'
    ),


    # =====================================================
    # ADMIN SIGN-IN
    # =====================================================

    path(
        'admin-login/',
        views.admin_login,
        name='admin_login'
    ),

    path(
        'admin-logout/',
        views.admin_logout,
        name='admin_logout'
    ),


    # =====================================================
    # ADMIN DASHBOARD
    # =====================================================

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    path(
        'projects/add/',
        views.add_project,
        name='add_project'
    ),

    path(
        'tech-stacks/add/',
        views.add_tech_stack,
        name='add_tech_stack'
    ),


    # =====================================================
    # DJANGO ADMIN
    # =====================================================

    path(
        'admin/',
        admin.site.urls
    ),
]


handler404 = 'portfolio.views.custom_404'
handler500 = 'portfolio.views.custom_500'