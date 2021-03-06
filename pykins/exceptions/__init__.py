# Copyright 2020 Arie Bregman
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
import pykins.api.job as job_api


class Jenkins():
    """Represents a jenkins server."""

    def __init__(self, url, username=None, password=None):
        """Instantiates Jenkins object.

        :param url: the url for a given jenkins instance
        :param username: username for jenkins auth
        :param password: password for jenkins auth

        """
        self.url = url
        self.username = username
        self.password = password

    def get_jobs(self):
        """API endpoint for getting jobs object from Jenkins."""
        return job_api.get_jobs(self)
