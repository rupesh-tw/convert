from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    # User
    path('file-conversion/', UserVerificationView.as_view(), name='file-conversion'),
]