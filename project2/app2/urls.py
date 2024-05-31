from django.urls import path
from app2 import views

urlpatterns =[
    path('', views.index, name = 'index'),
    path('cecilia', views.pageHola, name = 'pageHola'),
]

#patterns =[
 #   path('', views.pageHola, name = 'pageHola'),
#]