from django.utils import timezone
from rest_framework import viewsets

from lego.apps.joblistings.filters import JoblistingFilterSet
from lego.apps.joblistings.models import Joblisting
from lego.apps.companies.models import Company
from lego.apps.users.models import User
from lego.apps.joblistings.serializer import (
    JoblistingCreateAndUpdateSerializer,
    JoblistingDetailedSerializer,
    JoblistingSerializer,
)
from lego.apps.permissions.api.views import AllowedPermissionsMixin


class JoblistingViewSet(AllowedPermissionsMixin, viewsets.ModelViewSet):
    pagination_class = None
    filter_class = JoblistingFilterSet
    ordering = "-created_at"

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return JoblistingCreateAndUpdateSerializer

        elif self.action in ["retrieve", "destroy"]:
            return JoblistingDetailedSerializer

        return JoblistingSerializer

    def get_queryset(self):
        if self.action == "list":
            return Joblisting.objects.filter(
                visible_from__lte=timezone.now(), visible_to__gte=timezone.now()
            )
        return Joblisting.objects.all()


    def create(self, request, *args, **kwargs):
        # Get list of subscribers
        ## Subscription is a ManyToManyField
        Company.objects.filter(subscription=request.data.company)
        # Create notifications and send them to the subscribers
        return super().create()