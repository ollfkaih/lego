from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from lego.utils.tasks import send_email
from lego.apps.users.serializers.request_interest_group import RequestNewInterestGroupSerializer
from django.conf import settings


class RequestInterestGroupViewSet(viewsets.GenericViewSet):

    permission_classes = (permissions.AllowAny,)
    serializer_class = RequestNewInterestGroupSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        group_name = serializer.validated_data["group_name"]
        description = serializer.validated_data["description"]
        from_name = request.user.full_name
        from_email = request.user.email
        
        send_email.delay(
            to_email=[settings.INTERESTGROUP_REQUEST_EMAIL],
            context={
            "group_name": group_name, 
            "description": description,
            "from_name": from_name,
            "from_email": from_email,
        },
        subject=f"Søknad om opprettelse av ny interessegruppe",
        plain_template="groups/interestgroup_request.txt",
        html_template="groups/interestgroup_request.html",
        )

        return Response(serializer.validated_data, status=status.HTTP_202_ACCEPTED)