from django.urls import path
from .views import SubmitVideoAPIView

urlpatterns = [
    path("submit-video/", SubmitVideoAPIView.as_view(), name="submit_video"),
]