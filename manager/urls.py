from manager import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


app_name = "manager"

urlpatterns = [
    path("", views.index, name="index"),
    path("equipments/", views.EquipmentListView.as_view(), name="equipments"),
    path(
        "equipment/<uuid:pk>",
        views.EquipmentDetailView.as_view(),
        name="equipment-detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

