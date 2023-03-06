from django.urls import path
from buildings_app.views import all_objects, new_building, edit_building, delete_building

urlpatterns = [
    path('all/', all_objects, name="all_objects"),
    path('new/', new_building, name="new_building"),
    path('edit/<int:id>/', edit_building, name="edit_building"),
    path('delete/<int:id>/', delete_building, name="delete_building"),

]