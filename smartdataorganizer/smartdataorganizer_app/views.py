# smartdataorganizer_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest
from django.contrib import messages
import pandas as pd
from .forms import UploadForm
from .models import Spreadsheet
from io import BytesIO

def home(request):
    return render(request, 'smartdataorganizer/home.html')


class UploadFileView(View):
    template_name = 'smartdataorganizer/upload_file.html'

    def get(self, request):
        # Handle GET requests here
        return render(request, self.template_name, {'form': UploadForm()})

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            spreadsheet = form.save(commit=False)
            spreadsheet.name = "Some default name"
            spreadsheet.save()
            return redirect('choose_columns', spreadsheet_id=spreadsheet.id)
        return render(request, self.template_name, {'form': form})


class ChooseColumnsView(View):
    template_name = 'smartdataorganizer/choose_columns.html'

    def get(self, request, spreadsheet_id):
        spreadsheet = get_object_or_404(Spreadsheet, id=spreadsheet_id)
        column_names = get_column_names(spreadsheet)  # Implement this function to get column names
        return render(request, self.template_name, {'spreadsheet': spreadsheet, 'column_names': column_names})

def get_column_names(spreadsheet):
    return spreadsheet.get_column_names()


class DownloadFileView(View):
    def generate_download_file(self, spreadsheet, selected_columns):
        # Replace the hardcoded data with actual data from the spreadsheet
        data = spreadsheet.get_data()  # Assuming you have a method to get data from the spreadsheet
        df = pd.DataFrame(data)

        # Filter the DataFrame to include only the selected columns
        df = df[selected_columns]

        # Create a BytesIO object to write the Excel data to
        excel_data = BytesIO()
        df.to_excel(excel_data, index=False, engine='xlsxwriter')

        # Seek to the beginning of the stream
        excel_data.seek(0)

        # Set the appropriate response headers
        response = HttpResponse(excel_data.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=download_file.xlsx'

        # Add a success message
        messages.success(self.request, 'Data transformed and downloaded successfully.')

        return response

    def post(self, request, spreadsheet_id):
        spreadsheet = get_object_or_404(Spreadsheet, id=spreadsheet_id)

        selected_columns = request.POST.getlist('selected_columns')

        # Check if columns are selected
        if not selected_columns:
            messages.error(request, 'No columns selected.')
            return HttpResponseBadRequest("No columns selected.")

        return self.generate_download_file(spreadsheet, selected_columns)

