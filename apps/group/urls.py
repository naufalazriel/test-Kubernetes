from django.urls import include, path
from .views import *

app_name = "group"
urlpatterns = [ 
    path("", GroupListCreateView.as_view(), name="group-list"),
    path("", GroupListCreateView.as_view(), name="group-create"),
    path("retrieve/<int:pk>/", GroupRetrieveUpdateDelete.as_view(), name="group-detail"),
    path("retrieve/<int:pk>/", GroupRetrieveUpdateDelete.as_view(), name="group-update"),
    path("retrieve/<int:pk>/", GroupRetrieveUpdateDelete.as_view(), name="group-delete"),
]