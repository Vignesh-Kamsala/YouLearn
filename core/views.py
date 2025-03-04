from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
import yt_dlp

class SubmitVideoAPIView(APIView):
    def post(self, request):
        url = request.data.get("url")
        if not url:
            return Response({"error": "URL is required"}, status=400)
        
        video = Video(url=url)
        try:
            with yt_dlp.YoutubeDL({"writesubtitles": True, "subtitleslangs": ["en"]}) as ydl:
                info = ydl.extract_info(url, download=False)
                transcript = info.get("automatic_captions", {}).get("en", [{}])[0].get("url", "")
            video.transcript = transcript or "No transcript available"
            video.save()
            serializer = VideoSerializer(video)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)