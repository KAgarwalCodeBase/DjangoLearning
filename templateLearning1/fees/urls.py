from django.urls import path
from . import views
urlpatterns = [
    path('dj/',views.djangoFees),
    path('py/',views.pythonFees)
]
