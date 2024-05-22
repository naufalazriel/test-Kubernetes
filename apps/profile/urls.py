from django.urls import include, path
from apps.profile.views.profile_views import *

app_name = "profile"
urlpatterns = [
    path("", ProfileListCreateAPIView.as_view(), name="profile-list-create"), # filter by id_user, id_jabatan, atau id_departemen
    path("", ProfileListCreateAPIView.as_view(), name="profile-create"), # filter by id_user, id_jabatan, atau id_departemen
    path("update/<user_id>/", ProfileUpdateRetrieveAPIView.as_view(), name="profile-update"),

    path("sekretaris/", SekretarisListCreateAPIView.as_view(), name="sekretaris-list-create"), # filter by id_user atasan
    path("sekretaris/retrieve/<int:pk>/", SekretarisUpdateRetrieveDestroyAPIView.as_view(), name="sekretaris-update"),
    path("sekretaris/retrieve/<int:pk>/", SekretarisUpdateRetrieveDestroyAPIView.as_view(), name="sekretaris-detail"),
    path("sekretaris/retrieve/<int:pk>/", SekretarisUpdateRetrieveDestroyAPIView.as_view(), name="sekretaris-destroy"),

    path("delegasi/", DelegasiListCreateAPIView.as_view(), name="delegasi-list-create"), # filter by id_user atasan
    path("delegasi/retrieve/<int:pk>/", DelegasiUpdateRetrieveDestroyAPIView.as_view(), name="delegasi-update"),
    path("delegasi/retrieve/<int:pk>/", DelegasiUpdateRetrieveDestroyAPIView.as_view(), name="delegasi-detail"),
    path("delegasi/retrieve/<int:pk>/", DelegasiUpdateRetrieveDestroyAPIView.as_view(), name="delegasi-destroy"),
]