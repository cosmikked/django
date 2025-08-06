from django.urls import path
from . import views 

app_name = "polls" # namespaces the urls of this app to avoid ambiguous references when using url keyword in templates
urlpatterns = [
    path('', views.index, name='index'), # root of the app -- will call the index view
    path('<int:question_id>/', views.detail, name = 'detail'), # second part of route must match argument in the view function used
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote')
]