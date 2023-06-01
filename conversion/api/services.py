import os
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from django.conf import settings
from .serializers import FileSerializer

from api.tasks import convert_xl_to_csv

class FileService():
    def __init__(self):
        pass
    def convert_excel_to_csv(self, request, format=None):
        # Check if a file was uploaded
        if 'file' not in request.FILES:
            return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': 'No File Found!'})
        
        file = request.FILES['file']
        
        # Check if the file is an Excel file
        if not file.name.endswith('.xlsx') and not file.name.endswith('.xls'):
            return Response({'data': None, 'code': status.HTTP_400_BAD_REQUEST, 'message': 'Invalid file format. Only Excel files are supported'})
        
        try:
            # Read the Excel file using pandas
            # df = pd.read_excel(file)
            
            # # Convert DataFrame to CSV
            # csv_data = df.to_csv(index=False)
            # serializer = FileSerializer(request.data)
            # # Generate a unique filename for the CSV file
            # if serializer.is_valid():
            data = pd.read_excel(file)
            csv_filename = 'converted_file.csv'
            convert_xl_to_csv.delay(data, csv_filename)
            
            # # Save the CSV file in the media directory
            # csv_file_path = os.path.join(settings.MEDIA_ROOT, csv_filename)
            # with open(f'media/{csv_filename}', 'w') as csv_file:
            #     csv_file.write(csv_data)
            
            # Generate the download link for the CSV file
            download_link = request.build_absolute_uri(settings.MEDIA_URL + csv_filename)

            
            return Response({'download_link': download_link, 'code': status.HTTP_200_OK, 'message': 'Successfull!'})
        except Exception as e:
            return Response({'data': None, 'code': status.HTTP_500_INTERNAL_SERVER_ERROR, 'message': str(e)})

