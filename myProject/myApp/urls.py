from django.urls import path
from myApp import views

urlpatterns = [
    path('',views.index), # '' mean first pages
    path('about',views.about),
    path('form',views.form),
    path('edit/<personID>',views.edit),
    path('delete/<personID>',views.delete)
]