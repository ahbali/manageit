from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

import manager

app_name = "manager"

urlpatterns = [] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

