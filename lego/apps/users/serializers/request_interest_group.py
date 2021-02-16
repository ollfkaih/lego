
from rest_framework import exceptions, serializers

from lego.apps.users.constants import GROUP_COMMITTEE
from lego.apps.users.models import AbakusGroup
from lego.utils.fields import PrimaryKeyRelatedFieldNoPKOpt
from lego.utils.functions import verify_captcha

class RequestNewInterestGroupSerializer(serializers.Serializer):
    group_name = serializers.CharField(max_length=80)
    description = serializers.CharField()
    captcha_response = serializers.CharField()

    def validate_captcha_response(self, captcha_response):
        if not verify_captcha(captcha_response):
            raise exceptions.ValidationError("invalid_captcha")
        return captcha_response
