from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.login,name="login"),
    path('sub', views.sub, name='sub'),
    path('stud', views.stud, name='stud'),
    path('marks', views.marks, name='marks'),
    path('search',views.search,name="search"),
 
]
