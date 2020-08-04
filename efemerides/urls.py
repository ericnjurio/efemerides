from django.urls import path

from .views import commemoration_detail

urlpatterns = [
    path('efemerides/', commemoration_detail),
]
