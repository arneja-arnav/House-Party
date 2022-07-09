from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('join',index),
    path('create',index),
    path('room/<str:roomCode>', index) # the ':' is used for providing an argument in the URL by passing a variable in the form of a parameter, will appear as ? in the URL
    
]
