from django.urls import path
from apps.customer.api.views import CustomerView

urlpatterns = [
    path('',CustomerView.as_view()),
]