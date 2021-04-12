from django.urls import path
from . import views
urlpatterns= [  path('',views.learn),
                path('dj/', views.learn_django),
                path('py/', views.learn_python),
]