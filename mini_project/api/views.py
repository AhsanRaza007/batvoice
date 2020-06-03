from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Transcript
from api.serializers import TranscriptSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Create your views here.

class TranscriptView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TranscriptSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                jsonResponse = serializer.data
                jsonResponse['response'] = 'success'
                return Response(jsonResponse, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def get(self, request, format='json'):
        transcript = Transcript.objects.filter(transcribed = False, user = None)[0]
        transcript.user = request.user.username
        transcript.save()

        serializer = TranscriptSerializer(transcript)
        jsonResponse = serializer.data
        #jsonResponse['id'] = transcript.id
        return Response(jsonResponse)



class TranscriptDetail(APIView):

    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format='json'):
        transcript = Transcript.objects.get(id=pk)
        serializer = TranscriptSerializer(transcript, data=request.data)
        if serializer.is_valid():
            serializer.save()
            jsonResponse = serializer.data
            return Response(jsonResponse)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranscriptList(generics.ListAPIView):
    serializer_class = TranscriptSerializer

    def get_queryset(self):
        user = self.request.user.username
        return Transcript.objects.filter(user=user)
