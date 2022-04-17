from django.urls import path
from core import views


urlpatterns = [
    path("", views.BaseIndexView.as_view(), name="index"),
]
