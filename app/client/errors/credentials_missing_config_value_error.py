# -----------------------------------------------------------------------------------
# File   :   credentials_missing_config_value_error.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

from client.errors.credentials_error import CredentialsError


class CredentialsMissingConfigValueError(CredentialsError):
    pass
