# -----------------------------------------------------------------------------------
# File   :   credentials.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from client.credentials import Credentials
from client.errors.credentials_missing_config_value_error import CredentialsMissingConfigValueError


class AwsCredentials(Credentials):
    """Configuration class
    AwsCredentials retrieves the data contained in the section AWS of the secret.credentials.ini
    """

    _region_name: str
    _access_key_id: str
    _secret_access_key: str

    def __init__(self):
        super().__init__()
        if not self._credentials_are_set('AWS', ['REGION_NAME', 'REGION_NAME', 'SECRET_ACCESS_KEY']):
            raise CredentialsMissingConfigValueError("The AWS section of the configuration file has missing attributes")
        self._region_name = self._config.get('AWS', 'REGION_NAME')
        self._access_key_id = self._config.get('AWS', 'ACCESS_KEY_ID')
        self._secret_access_key = self._config.get('AWS', 'SECRET_ACCESS_KEY')

    @property
    def region_name(self):
        return self._region_name

    @property
    def access_key_id(self):
        return self._access_key_id

    @property
    def secret_access_key(self):
        return self._secret_access_key
