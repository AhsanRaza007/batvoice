from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt




urlpatterns = [
    path('audio', views.TranscriptView.as_view(), name='transcript-view'),
    path('audio/<int:pk>', csrf_exempt(views.TranscriptDetail.as_view()), name='transcript-update'),
    path('audio/getAll', views.TranscriptList.as_view(), name='transcript-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
