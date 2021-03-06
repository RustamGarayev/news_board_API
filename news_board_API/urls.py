"""news_board_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path("admin/", admin.site.urls),
]

# API urls
urlpatterns += [
    path("api/v1/", include("api.urls")),
    path(
        "api-schema/",
        get_schema_view(
            title="News Board Project API",
            description="API developed to show endpoints and their functionality",
        ),
        name="api-schema",
    ),
    path(
        "",
        TemplateView.as_view(
            template_name="documentation.html",
            extra_context={"schema_url": "api-schema"},
        ),
        name="swagger-ui",
    ),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
