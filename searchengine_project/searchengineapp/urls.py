from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_document, name='upload_document'),
    path('document/<int:document_id>/', views.document_detail, name='document_detail'),
    path('search/', views.search_document, name='search_document'),
    path('search_results/', views.search_results, name='search_results'),
    
]
