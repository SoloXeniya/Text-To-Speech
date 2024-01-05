from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import TextToSpeechView, TextToSpeechDetailView, DownloadVoiceView



urlpatterns = [
    path("text-to-speech/", TextToSpeechView.as_view(), name="text-to-speech-list"),
    path("text-to-speech/<int:id>/", TextToSpeechDetailView.as_view(), name="text-to-speech-detail"),
    path("download-voice/<int:id>/", DownloadVoiceView.as_view(), name="download-voice"),
]

