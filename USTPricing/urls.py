from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<evepraisalID>/results/', views.results, name='results'),
]
