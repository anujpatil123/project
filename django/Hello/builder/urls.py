from django.urls import path
import builder.views as views


urlpatterns = [
    path('', views.home, name='home'),
]


 