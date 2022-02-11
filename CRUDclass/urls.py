
from .views import *
from django.urls import path

urlpatterns = [

    path("list/", StudentListView.as_view(),name="student"),
    path("add", StudentCreateView.as_view()),
    path("<int:pk>/", StudentDetailView.as_view(),name = 'detile'),
    path("update/<int:pk>/", StudentUpdateView.as_view(), name = 'update'),
    path("delete/<int:pk>/", StudentdeleteView.as_view(), name = 'delete'),

]

