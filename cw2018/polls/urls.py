from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('login', views.login, name='login'),
    path('admin.html', views.admin, name='admin'),
    path('addnew', views.addnew, name='addnew'),
    path('organisation.html', views.organisation, name='organisation.html'),
    path('error.html', views.error, name='error'),
    path('organisation', views.organisation, name='organisation'),
    path('order', views.order, name='order'),
    path('edit', views.edit, name='edit'),
]
