from django.urls import include, path
from apps.departemen.views import *

app_name = "departemen"
urlpatterns = [
    path("", DepartemenListCreateAPIView.as_view(), name="departemen-list"),
    path("", DepartemenListCreateAPIView.as_view(), name="departemen-create"),
    path("retrieve/<str:pk>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-detail"),
    path("retrieve/<str:pk>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-update"),
    path("retrieve/<str:pk>/", DepartemenRetrieveUpdateDestroyAPIView.as_view(), name="departemen-delete"),
]