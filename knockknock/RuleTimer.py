# Copyright (c) 2009 Moxie Marlinspike
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#

import subprocess
import time
import threading

from .AddressType import isIPv6

class RuleTimer(threading.Thread):

    def __init__(self, openDuration, description, addrIsIPv6):
        self.openDuration = openDuration
        self.description  = description
        self.addrIsIPv6 = addrIsIPv6
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(self.openDuration)
        if self.addrIsIPv6:
            command = 'ip6tables -D ' + self.description
        else:
            command = 'iptables -D ' + self.description

        command = command.split()

        subprocess.call(command, shell=False)
