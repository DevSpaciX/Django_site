from django.urls import path
from groups import views

urlpatterns = [
    path('create/course/',views.CreateCourse.as_view(),name="create"),
    path('edit/<int:group_id>/course/',views.EditCourse.as_view(),name="edit"),
]