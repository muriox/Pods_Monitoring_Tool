from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard),
    path('pods/', views.device_request),
    path('create_post/', views.create_post),
    path('dashboard/setup_post/', views.setup_post),
    path('dashboard/get_data_request/', views.get_data_request),
    path('roll/', views.roll),
    path('show_contents_data/', views.show_contents_data), # test
    path('create_contents_data/', views.create_contents_data), # test
    #url(r'^$', views.employee_signup),
]

