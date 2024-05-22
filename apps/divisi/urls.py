from django.urls import include, path
from apps.divisi.views import *

app_name = "divisi"
urlpatterns = [
    path("", DivisiListCreateAPIView.as_view(), name="divisi-list"),
    path("", DivisiListCreateAPIView.as_view(), name="divisi-create"),
    path("retrieve/<str:pk>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-detail"),
    path("retrieve/<str:pk>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-update"),
    path("retrieve/<str:pk>/", DivisiRetrieveUpdateDestroyAPIView.as_view(), name="divisi-delete"),
]