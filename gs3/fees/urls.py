from django.urls import path
from . import views
urlpatterns = [ path('',views.fees),
                path('dj/',views.fees_django),
                path('py/',views.fees_python)
                ]