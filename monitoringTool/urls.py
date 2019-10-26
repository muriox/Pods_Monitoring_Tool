from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    path('', views.internal_home),
    path('create_post/', views.create_post),
    path('dashboard/', views.dashboard),
    path('dashboard/setup_post/', views.setup_post),
    path('dashboard/get_data_request/', views.get_data_request),
    path('create_contents_data/', views.create_contents_data),      #
    path('pods/', views.device_request),                            #
    path('show_contents_data/', views.show_contents_data),          # For Dashboard testing
    #path('testing/', views.testing),
]

