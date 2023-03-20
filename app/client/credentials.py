# -----------------------------------------------------------------------------------
# File   :   credentials.py
# Author :   Mélodie Ohan
# Version:   16-03-2023 - original (dedicated to RIA1)
# Remarks:   -
# -----------------------------------------------------------------------------------

import os
from configparser import ConfigParser

from client.errors.credentials_config_file_not_found_error import CredentialsConfigFileNotFoundError


class Credentials:
    """Configuration class
    Credentials read the data contained in secret.credentials.ini file
    """

    _config: ConfigParser

    def __init__(self):
        """Constructor
        Open the credential file and start to read it
        """
        if not os.environ.get('CONFIG_FILE_PATH'):
            raise CredentialsConfigFileNotFoundError("Config file directory is not set.")
        self._config = ConfigParser()
        config_path = os.environ.get('CONFIG_FILE_PATH')
        self._config.read(config_path)

    def _credentials_are_set(self, section_name: str, options: list[str]) -> bool:
        """ Check if a section and its options exist in the config file
        :param section_name: str
        :param options: list[str]
        :return: bool
        """
        if not section_name or not options or not self._config.has_section(section_name):
            return False
        for option in options:
            if not self._config.has_option(section_name, option):
                return False
        return True
