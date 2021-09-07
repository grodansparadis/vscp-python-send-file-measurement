"""
// File: send_file_measurement.py
//
// Usage: echo 1.45 | send_file_measurement.py host user password guid type unit sensorindex zone subzone
// class is always = 1040 (str measurement)
//
// Described here https://github.com/grodansparadis/vscp-samples/tree/master/samples/python
//
// This program is free software; you can redistribute it and/or
// modify it under the terms of the GNU General Public License
// as published by the Free Software Foundation; either version
// 2 of the License, or (at your option) any later version.
//
// This file is part of the VSCP (http://www.vscp.org)
//
// Copyright (C) 2000-2021
// Ake Hedman, Grodans Paradis AB, <akhe@grodansparadis.com>
//
// This file is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this file see the file COPYING.  If not, write to
// the Free Software Foundation, 59 Temple Place - Suite 330,
// Boston, MA 02111-1307, USA.
//
//

"""

import getpass
import sys
import telnetlib

# host user password guid type unit sensorindex zone, subzone
if ( len(sys.argv) < 6 ):
    sys.exit("Wrong number of parameters - aborting")

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
guid = sys.argv[4]
type = sys.argv[5]

unit = 0
if ( len(sys.argv) > 6 ):
    unit = sys.argv[6]

sensorindex = 0
if ( len(sys.argv) > 7 ):
    sensorindex = sys.argv[7]

zone = 0
if ( len(sys.argv) > 8 ):
    zone = sys.argv[8]

subzone = 0
if ( len(sys.argv) > 9 ):
    subzone = sys.argv[9]


import getpass
import sys
import telnetlib

# host user password guid type unit sensorindex zone, subzone
if ( len(sys.argv) < 6 ):
    sys.exit("Wrong number of parameters - aborting")

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
guid = sys.argv[4]
type = sys.argv[5]

unit = 0
if ( len(sys.argv) > 6 ):
    unit = sys.argv[6]

sensorindex = 0
if ( len(sys.argv) > 7 ):
    sensorindex = sys.argv[7]

zone = 0
if ( len(sys.argv) > 8 ):
    zone = sys.argv[8]

subzone = 0
if ( len(sys.argv) > 9 ):
    subzone = sys.argv[9]

import getpass
import sys
import telnetlib

# host user password guid type unit sensorindex zone, subzone
if ( len(sys.argv) < 6 ):
    sys.exit("Wrong number of parameters - aborting")

host = sys.argv[1]
user = sys.argv[2]
password = sys.argv[3]
guid = sys.argv[4]
type = sys.argv[5]

unit = 0
if ( len(sys.argv) > 6 ):
    unit = sys.argv[6]

sensorindex = 0
if ( len(sys.argv) > 7 ):
    sensorindex = sys.argv[7]

zone = 0
if ( len(sys.argv) > 8 ):
    zone = sys.argv[8]

subzone = 0
if ( len(sys.argv) > 9 ):
    subzone = sys.argv[9]




