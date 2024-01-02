# smartdataorganizer_app/urls.py
from django.urls import path
from .views import UploadFileView, ChooseColumnsView, DownloadFileView, home

urlpatterns = [
    path('', home, name='home'),
    path('upload/', UploadFileView.as_view(), name='upload_file'),
    path('choose_columns/<int:spreadsheet_id>/', ChooseColumnsView.as_view(), name='choose_columns'),
    path('download_file/<int:spreadsheet_id>/', DownloadFileView.as_view(), name='download_file'),
]
