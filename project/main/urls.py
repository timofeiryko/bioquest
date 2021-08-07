from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('problems', views.problems, name='problems'),
    path('personal', views.personal, name='personal'),
    path('about', views.about, name='about'),
    path('add', views.add, name='add'),
    path('instructions', views.instructions, name='instructions')
]
