from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/<evepraisalID>', views.results, name='results'),
]
