from django.urls import path
from . import views
urlpatterns=[
 path('',views.fab,name='fab')

]