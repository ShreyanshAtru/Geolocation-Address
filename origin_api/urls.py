from django.urls import path

from .views import AddressAPIView

urlpatterns = [
    path("address", AddressAPIView.as_view()),
]
