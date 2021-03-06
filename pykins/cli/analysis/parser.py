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
from pykins.build import JenkinsBuild


def create_analysis_parser(client_subparsers, parent_parser):
    """Creates analysis parser"""
    analysis_parser = client_subparsers.add_parser("analyze",
                                                   parents=[parent_parser])
    analysis_parser.add_argument('job', help='job name')
    analysis_parser.set_defaults(cls=JenkinsBuild, func='analyze')
