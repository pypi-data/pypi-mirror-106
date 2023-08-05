"""
Type annotations for sms-voice service client.

[Open documentation](./client.md)

Usage::

    ```python
    import boto3
    from mypy_boto3_sms_voice import SMSVoiceClient

    client: SMSVoiceClient = boto3.client("sms-voice")
    ```
"""
from typing import Any, Dict, Type

from botocore.client import ClientMeta

from .type_defs import (
    EventDestinationDefinitionTypeDef,
    GetConfigurationSetEventDestinationsResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    SendVoiceMessageResponseTypeDef,
    VoiceMessageContentTypeDef,
)

__all__ = ("SMSVoiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    AlreadyExistsException: Type[BotocoreClientError]
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    InternalServiceErrorException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]


class SMSVoiceClient:
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client)
    [Show boto3-stubs documentation](./client.md)
    """

    meta: ClientMeta
    exceptions: Exceptions

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.can_paginate)
        [Show boto3-stubs documentation](./client.md#can_paginate)
        """

    def create_configuration_set(self, ConfigurationSetName: str = None) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set)
        [Show boto3-stubs documentation](./client.md#create_configuration_set)
        """

    def create_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestination: EventDestinationDefinitionTypeDef = None,
        EventDestinationName: str = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.create_configuration_set_event_destination)
        [Show boto3-stubs documentation](./client.md#create_configuration_set_event_destination)
        """

    def delete_configuration_set(self, ConfigurationSetName: str) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set)
        [Show boto3-stubs documentation](./client.md#delete_configuration_set)
        """

    def delete_configuration_set_event_destination(
        self, ConfigurationSetName: str, EventDestinationName: str
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.delete_configuration_set_event_destination)
        [Show boto3-stubs documentation](./client.md#delete_configuration_set_event_destination)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.generate_presigned_url)
        [Show boto3-stubs documentation](./client.md#generate_presigned_url)
        """

    def get_configuration_set_event_destinations(
        self, ConfigurationSetName: str
    ) -> GetConfigurationSetEventDestinationsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.get_configuration_set_event_destinations)
        [Show boto3-stubs documentation](./client.md#get_configuration_set_event_destinations)
        """

    def list_configuration_sets(
        self, NextToken: str = None, PageSize: str = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.list_configuration_sets)
        [Show boto3-stubs documentation](./client.md#list_configuration_sets)
        """

    def send_voice_message(
        self,
        CallerId: str = None,
        ConfigurationSetName: str = None,
        Content: VoiceMessageContentTypeDef = None,
        DestinationPhoneNumber: str = None,
        OriginationPhoneNumber: str = None,
    ) -> SendVoiceMessageResponseTypeDef:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.send_voice_message)
        [Show boto3-stubs documentation](./client.md#send_voice_message)
        """

    def update_configuration_set_event_destination(
        self,
        ConfigurationSetName: str,
        EventDestinationName: str,
        EventDestination: EventDestinationDefinitionTypeDef = None,
    ) -> Dict[str, Any]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.73/reference/services/sms-voice.html#SMSVoice.Client.update_configuration_set_event_destination)
        [Show boto3-stubs documentation](./client.md#update_configuration_set_event_destination)
        """
