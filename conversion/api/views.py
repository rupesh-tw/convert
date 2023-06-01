"""
File Views.
"""

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api.services import FileService


file_service = FileService()

class UserVerificationView(APIView):
    def post(self, request, format=None):
        result = file_service.convert_excel_to_csv(request, format=None)
        return Response(result.data, status=result.data["code"])
    