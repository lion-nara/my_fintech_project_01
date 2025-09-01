from django.urls import path
from . import views

app_name = "photos"

urlpatterns = [
    path("", views.photo_list, name="list"),
    path("upload/", views.photo_upload, name="upload"),
    path("<int:photo_id>/delete/", views.photo_delete, name="delete"),
]
