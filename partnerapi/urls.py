from django.urls import path, include
from .views import (
    PartnerApiView,
    PartnerDetailApiView
)

urlpatterns = [
    path('', PartnerApiView.as_view()),
    path('<int:partner_id>/', PartnerDetailApiView.as_view()),
]