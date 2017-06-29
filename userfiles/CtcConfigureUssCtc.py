# Configure SP Shasta CTC machine support
#
# Exensively uses the jmri.jmrit.ussctc package capabilities
#
# Author: Bob Jacobsen, copyright 2016-17
# 

import jmri
from jmri.jmrit.ussctc import *
import jarray
import java.util

# The code line is shared by all Stations

codeline = CodeLine("CTC Code Line Driver", "IT CODE MOD 1", "IT CODE MOD 2", "IT CODE MOD 3", "IT CODE MOD 4")

# Set up Station 7/8

button = CodeButton("CTC 08 Code A", "CTC 08 Code")
turnout = TurnoutSection("TO 07", "CTC 07 N", "CTC 07 R", "CTC 07 N", "CTC 07 R", codeline)

rList = java.util.ArrayList()
rList.add("08 R from Helix")
rList.add("08 R from Staging")
lList = java.util.ArrayList()
lList.add("08 L Upper")
lList.add("08 L Lower")
signals = SignalHeadSection(rList, lList, "CTC 08 L", "CTC 08 C", "CTC 08 R", "CTC 08 L", "CTC 08 R", codeline);

station = Station(codeline, button)
station.add(turnout)
station.add(signals)

button.addStation(station)
turnout.addStation(station)
signals.addStation(station)

occupancyLock = OccupancyLock("CS9");
routeLock = RouteLock(["08 R from Helix", "08 R from Staging", "08 L Upper", "08 L Lower"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock]));
