from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='projects'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
    path('personal-information/', views.personal_information, name='personal_information'),
    path('projects/add/', views.add_project, name='add_project'),
    path('contact/', views.inquiry, name='contact'),

    path('testimonies/', views.testimony_list, name='testimony_list'),
    path('testimonies/add/', views.add_testimony, name='add_testimony'),
    path('testimonies/<int:id>/', views.testimony_detail, name='testimony_detail'),
]