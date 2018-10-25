# Copyright 2018 AT&T Intellectual Property.  All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging

__all__ = ('PeglegBaseException', 'GitException', 'GitAuthException',
           'GitProxyException', 'GitSSHException', 'GitConfigException',
           'GitInvalidRepoException')

LOG = logging.getLogger(__name__)


class PeglegBaseException(Exception):
    """The base Pegleg exception for everything."""

    message = "Base Pegleg exception"

    def __init__(self, message=None, **kwargs):
        self.message = message or self.message
        try:
            self.message = self.message.format(**kwargs)
        except KeyError:
            LOG.warning("Missing kwargs")
        super().__init__(self.message)


class GitException(PeglegBaseException):
    """Exception when an error occurs cloning a Git repository."""
    message = ('Git exception occurred: [%(location)s] may not be a valid '
               'git repository. Details: %(details)s')


class GitAuthException(PeglegBaseException):
    """Exception that occurs when authentication fails for cloning a repo."""
    message = ('Failed to authenticate for repo %(repo_url)s with ssh-key '
               'at path %(ssh_key_path)s')


class GitProxyException(PeglegBaseException):
    """Exception when cloning through proxy."""
    message = 'Could not resolve proxy [%(location)s]'


class GitSSHException(PeglegBaseException):
    """Exception that occurs when an SSH key could not be found."""
    message = 'Failed to find specified SSH key: %(ssh_key_path)s'


class GitConfigException(PeglegBaseException):
    """Exception that occurs when reading Git repo config fails."""
    message = 'Failed to read Git config file for repo path: %(repo_path)s'


class GitInvalidRepoException(PeglegBaseException):
    """Exception raised when an invalid repository is detected."""
    message = 'The repository path or URL is invalid: %(repo_path)s'


#
# PKI EXCEPTIONS
#


class IncompletePKIPairError(PeglegBaseException):
    """Exception for incomplete private/public keypair."""
    message = ("Incomplete keypair set %(kinds)s for name: %(name)s")


class PassphraseSchemaNotFoundException(PeglegBaseException):
    """Failed to find schema for Passphrases rendering."""
    message = ('Could not find Passphrase schema for rendering Passphrases!')


class PassphraseCatalogNotFoundException(PeglegBaseException):
    """Failed to find Catalog for Passphrases generation."""
    message = ('Could not find the Passphrase Catalog to generate '
               'the site Passphrases!')


class GenesisBundleEncryptionException(PeglegBaseException):
    """Exception raised when encryption of the genesis bundle fails."""

    message = 'Encryption is required for genesis bundle, but no encryption ' \
              'policy or key is specified.'


class GenesisBundleGenerateException(PeglegBaseException):
    """
    Exception raised when pormenade engine fails to build the genesis
    bundle.
    """

    message = 'Bundle generation failed on deckhand validation.'
