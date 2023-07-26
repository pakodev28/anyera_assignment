from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_title = "PET API ADMIN"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("grappelli/", include("grappelli.urls")),
    path("api/", include("api.urls")),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
