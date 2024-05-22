from django.urls import include, path
from apps.jabatan.views import *

app_name = "jabatan"
urlpatterns = [
    path("", JabatanListCreateAPIView.as_view(), name="jabatan-list"),
    path("", JabatanListCreateAPIView.as_view(), name="jabatan-create"),
    path("retrieve/<str:pk>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-detail"),
    path("retrieve/<str:pk>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-update"),
    path("retrieve/<str:pk>/", JabatanRetrieveUpdateDestroyAPIView.as_view(), name="jabatan-delete"),
]