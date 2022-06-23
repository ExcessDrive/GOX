# Copyright 2022 <Alex DANDURAN--LEMBEZAT, Fetia BANNOUR, Stefania DUMBRAVA>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Usage: read the README.md file for instructions
"""

from pox.core import core                     # Main POX object
import pox.lib.util as poxutil                # Various util functions

from gox_db import DatabaseInstance
from gox_network import NetworkEventHandler
from pox.host_tracker.host_tracker import host_tracker
from pox.openflow.discovery import Discovery

# Create a logger for this component
log = core.getLogger()

class Gox(object):
    pass


@poxutil.eval_args
def launch (uri, username="neo4j", password="password"):
    """
    GOX launcher
    """

    core.registerNew(Gox)
    core.registerNew(DatabaseInstance, uri, username, password)
    core.registerNew(NetworkEventHandler, core.DatabaseInstance)
    core.registerNew(Discovery)
    core.registerNew(host_tracker, eat_packets=False) # TODO We can change the default ping source MAC. Should we pu the controller's ?
    

    # When your component is specified on the commandline, POX automatically
    # calls this function.

    # Add whatever parameters you want to this.  They will become
    # commandline arguments.  You can specify default values or not.
    # In this example, foo is required and bar is not.  You may also
    # specify a keyword arguments catch-all (e.g., **kwargs).

    # For example, you can execute this component as:
    # ./pox.py skeleton --foo=3 --bar=4

    # Note that arguments passed from the commandline are ordinarily
    # always strings, and it's up to you to validate and convert them.
    # The one exception is if a user specifies the parameter name but no
    # value (e.g., just "--foo").  In this case, it receives the actual
    # Python value True.
    # The @pox.util.eval_args decorator interprets them as if they are
    # Python literals.  Even things like --foo=[1,2,3] behave as expected.
    # Things that don't appear to be Python literals are left as strings.

    # If you want to be able to invoke the component multiple times, add
    # __INSTANCE__=None as the last parameter.  When multiply-invoked, it
    # will be passed a tuple with the following:
    # 1. The number of this instance (0...n-1)
    # 2. The total number of instances for this module
    # 3. True if this is the last instance, False otherwise
    # The last is just a comparison between #1 and #2, but is convenient.

    # log.warn("uri: %s (%s)", uri, type(uri))
    # log.warn("username: %s (%s)", username, type(username))
    # log.warn("password: %s (%s)", password, type(password))



