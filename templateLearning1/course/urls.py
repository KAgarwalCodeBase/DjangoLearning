from django.urls import path
from . import views
urlpatterns = [
    path('dj/',views.djangoLearning),
    path('py/',views.pythonLearning)
]
