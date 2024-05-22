from django.urls import include, path
from .views import *

app_name = "surat"
urlpatterns = [ 
    path("", SuratListCreateView.as_view(), name="surat-list"),
    path("<int:pk>", SuratRetrieveUpdateDelete.as_view(), name="surat-detail"),
    path("disposisi/", DisposisiListCreateView.as_view(), name="disposisi-list"),
    path("disposisi/details/<int:pk>/", DisposisiRetrieve.as_view(), name="surat-detail"),
]