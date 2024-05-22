from django.urls import include, path
from .views import *

app_name = "lampiran"
urlpatterns = [
    path("", LampiranListCreateView.as_view(), name="lampiran-list"),
    path("<int:pk>/", LampiranRetrieveUpdateDelete.as_view(), name="lampiran-detail"),
]