# Copyright (C) 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import googlecl

service_name = __name__.split('.')[-1]
LOGGER_NAME = googlecl.LOGGER_NAME + '.' + service_name
SECTION_HEADER = service_name.upper()

def MapAccessString(access_string, default_value='private'):
  if not access_string:
    return default_value
  # It seems to me that 'private' is less private than 'protected'
  # but I'm going with what Picasa seems to be using.
  access_string_mappings = {'public': 'public',
                            'private': 'protected',
                            'protected': 'private',
                            'draft': 'private',
                            'hidden': 'private',
                            'link': 'private'}
  try:
    return access_string_mappings[access_string]
  except KeyError:
    import re
    if access_string.find('link') != -1:
      return 'private'
  return default_value