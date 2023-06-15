from django.urls import path
from .views import home,predictDiabetes,predictHeartAttack,about,result
urlpatterns = [
    path('',home,name='home'),
    path('diabetes/',predictDiabetes,name='diabetes'),
    path('heart-attack/',predictHeartAttack,name='heart-attack'),
    path('about',about,name='about'),
    path('result/<int:id>/',result,name='result')
]
