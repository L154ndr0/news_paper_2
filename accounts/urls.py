from django.urls import path
from .views import SignUpViews

urlpatterns = [
    path("signup/", SignUpViews.as_view(), name="signup"),
]