# feedback/tasks.py
import pandas as pd
import os
from celery import shared_task
from django.conf import settings


@shared_task()
def convert_xl_to_csv(file, csv_filename):
    # df = pd.read_excel(file)
    
    # Convert DataFrame to CSV
    csv_data = file.to_csv(index=False)
    
    # Generate a unique filename for the CSV file
    
    # Save the CSV file in the media directory
    csv_file_path = os.path.join(settings.MEDIA_ROOT, csv_filename)
    with open(f'media/{csv_filename}', 'w') as csv_file:
        csv_file.write(csv_data)