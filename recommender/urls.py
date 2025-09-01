from django.urls import path
from . import views

urlpatterns =[
    path('movies/', views.movie_list, name='movies_list'),
    path('recommend/<str:movie>/', views.recommend_movie, name='recommend_movie'),

]