
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from django.urls import path



urlpatterns = [
    path("", get_student),
    path("add/", create_student),
    path("delete/<int:student_id>" , delete_student),
    path("update/<int:student_id>" , update_Student),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

