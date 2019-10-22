from django.urls import path
from .views import *

urlpatterns = [
    path('', allpost, name='allpost'),
    path('<int:blog_id>/', detail, name='detail')
]
