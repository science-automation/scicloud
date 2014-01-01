'''
Cloud Multiprocessing Interface

sciscicloud.mp has effectively the same interface as scicloud.

All jobs will be run locally, on multiple processors, via the multiprocessing library

Sample usage::

    import sciscicloud.mp
    jid = sciscicloud.mp.call(lambda: 3*3)
    >> Returns a job identifier
    scicloud.mp.result(jid)
    >> Returns 9
'''
'''
Copyright (c) 2010 `PiCloud, Inc. <http://www.picloud.com>`_.  All rights reserved.

email: contact@piscicloud.com

The scicloud package is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This package is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this package; if not, see 
http://www.gnu.org/licenses/lgpl-2.1.html    
'''

import sys

import scicloudinterface
from . import scicloud

__scicloud = None
__type = None
__immutable = False

#function bindings
call = None
map = None
status = None
join = None
result = None
kill = None
connection_info = None

__all__ = ["call", "map", "status", "result", "iresult", "join", "kill", "info", 
           "delete", "connection_info", "finished_statuses", "close","c1","c2","m1"]

def _launch_scicloud():
    scicloudinterface._setscicloud(sys.modules[__name__], 'mp')
    
_launch_scicloud()

def _getscicloud():
    """Return internal scicloud object. Only for internal use"""
    return __scicloud
