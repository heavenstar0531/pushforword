from django.urls import path, include
from rest_framework import routers

from leases.views import (
    LeaseCreate, LeasesList, LeaseViewSet, LeaseDetail, LeaseMemberCreate,
    MoveInCostCreate, LeaseClientCreate, ClientLeasesList,
    ResendLeaseInvitation, ClientLease, SignAgreementView, DeleteLeaseMember,
    UpdateRentalApplication, UploadRentalAppDoc, DeleteRentalAppDoc,
    RentalApplicationDetail, DownloadRentalDocuments, LeaseUpdateView,
    ChangeLeaseStatusView, UpdateEditingRentalApplication, GenerateRentalPDF)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'private', LeaseViewSet)

urlpatterns = [
    path('', LeasesList.as_view(), name='list'),
    path('', include(router.urls)),
    path('<uuid:pk>/create', LeaseCreate.as_view(), name='create'),
    path('<uuid:pk>/edit', LeaseUpdateView.as_view(), name='edit'),
    path('detail/<uuid:pk>', LeaseDetail.as_view(), name='detail'),
    path('client/', ClientLeasesList.as_view(), name='client'),
    path('client/<uuid:pk>', ClientLease.as_view(), name='detail-client'),
    path('agreement/<uuid:pk>', SignAgreementView.as_view(), name='agreement'),
    path('<uuid:pk>/create-member',
         LeaseMemberCreate.as_view(),
         name='create-member'),
    path('<uuid:pk>/delete-member',
         DeleteLeaseMember.as_view(),
         name='delete-member'),
    path('<uuid:pk>/create-client',
         LeaseClientCreate.as_view(),
         name='create-client'),
    path('<uuid:pk>/create-moveincost',
         MoveInCostCreate.as_view(),
         name='create-moveincost'),
    path('<uuid:pk>/send-invitation',
         ResendLeaseInvitation.as_view(),
         name='send-invitation'),
    path('<uuid:pk>/update-application',
         UpdateRentalApplication.as_view(),
         name='update-application'),
    path('<uuid:pk>/create-rental-doc',
         UploadRentalAppDoc.as_view(),
         name='create-rental-doc'),
    path('<uuid:pk>/delete-rental-doc',
         DeleteRentalAppDoc.as_view(),
         name='delete-rental-doc'),
    path('<uuid:pk>/rental-detail',
         RentalApplicationDetail.as_view(),
         name='rental-detail'),
    path('<uuid:pk>/rental-download',
         DownloadRentalDocuments.as_view(),
         name='rental-download'),
    path('<uuid:pk>/change-status',
         ChangeLeaseStatusView.as_view(),
         name='change-status'),
    path('<uuid:pk>/editing',
         UpdateEditingRentalApplication.as_view(),
         name='editing'),
    path('<uuid:pk>/generate-pdf',
         GenerateRentalPDF.as_view(),
         name='generate-pdf'),
]
