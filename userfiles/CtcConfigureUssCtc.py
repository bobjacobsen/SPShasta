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

def arrayList(contents) :
    retval = java.util.ArrayList()
    for item in contents : 
        retval.add(item)
    return retval

# The code line is shared by all Stations

codeline = CodeLine("CTC Code Line Driver", "IT CODE MOD 1", "IT CODE MOD 2", "IT CODE MOD 3", "IT CODE MOD 4")
bell = PhysicalBell("CTC Bell")
vbell = VetoedBell("CTC Bell Cutout", bell)

# ===== Set up Station 1/2 ===== (TODO: NOT FULLY CONFIGURED)

button = CodeButton("CTC 02 Code A", "CTC 02 Code")
station = Station("1/2", codeline, button)

turnout = TurnoutSection("Helix Level 2 B", "CTC 01 N", "CTC 01 R", "CTC 01 N", "CTC 01 R", station)
station.add(turnout)

# ===== Set up Station 3/4 ===== (TODO: NOT FULLY CONFIGURED)

button = CodeButton("CTC 04 Code A", "CTC 04 Code")
station = Station("3/4", codeline, button)

turnout = TurnoutSection("Helix Level 2 A", "CTC 03 N", "CTC 03 R", "CTC 03 N", "CTC 03 R", station)
station.add(turnout)

# ===== Set up Station 5/6 ===== (TODO: NOT FULLY CONFIGURED)

button = CodeButton("CTC 06 Code A", "CTC 06 Code")
station = Station("5/6", codeline, button)

station.add(TrackCircuitSection("TC 07","CTC TC 07", station)) # 5 OS

turnout = TurnoutSection("Helix Level 1", "CTC 05 N", "CTC 05 R", "CTC 05 N", "CTC 05 R", station)
station.add(turnout)

station.add(MaintainerCallSection("CTC 06 Call","MC 6", station))

# ===== Set up Station 7/8 =====

button = CodeButton("CTC 08 Code A", "CTC 08 Code")
station = Station("7/8", codeline, button)

station.add(TrackCircuitSection("TC 08","CTC TC 08", station)) # 5-7 track
station.add(TrackCircuitSection("TC 09","CTC TC 09", station, bell)) # Redding approach
station.add(TrackCircuitSection("TC 10","CTC TC 10", station, vbell)) # OS 7

turnout = TurnoutSection("TO 07", "CTC 07 N", "CTC 07 R", "CTC 07 N", "CTC 07 R", station)
station.add(turnout)

rightward = arrayList(["08 R from Helix", "08 R from Staging"])
leftward  = arrayList(["08 L Upper", "08 L Lower"])
signal = SignalHeadSection(rightward, leftward, "CTC 08 L", "CTC 08 C", "CTC 08 R", "CTC 08 L", "CTC 08 R", station);
station.add(signal)

occupancyLock = OccupancyLock("TC 10")
routeLock = RouteLock(["08 R from Helix", "08 R from Staging", "08 L Upper", "08 L Lower"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal)]));

# ===== Set up Station 9/10 =====

button = CodeButton("CTC 10 Code A", "CTC 10 Code")
station = Station("9/10", codeline, button)

station.add(TrackCircuitSection("TC 11","CTC TC 11", station)) # 7-9
station.add(TrackCircuitSection("TC 12","CTC TC 12", station, vbell)) # OS 9

turnout = TurnoutSection("TO 09", "CTC 09 N", "CTC 09 R", "CTC 09 N", "CTC 09 R", station)
station.add(turnout)

rightward = arrayList(["10 R Upper", "10 R Lower"])
leftward  = arrayList(["10 L Main", "10 L Siding"])
signal = SignalHeadSection(rightward, leftward, "CTC 10 L", "CTC 10 C", "CTC 10 R", "CTC 10 L", "CTC 10 R", station);
station.add(signal)

occupancyLock = OccupancyLock("TC 12")
routeLock = RouteLock(["10 R Upper", "10 R Lower", "10 L Main", "10 L Siding"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal)]));

# ===== Set up Station 13/14/16 =====

button = CodeButton("CTC 14 Code A", "CTC 14 Code")
station = Station("13/14/16", codeline, button)

station.add(TrackCircuitSection("TC 13","CTC TC 13", station)) # 9-13 siding
station.add(TrackCircuitSection("TC 14","CTC TC 14", station)) # 9-13 main
station.add(TrackCircuitSection("TC 15","CTC TC 15", station, vbell)) # OS 13 siding
station.add(TrackCircuitSection("TC 16","CTC TC 16", station, vbell)) # OS 13 main

turnout = TurnoutSection("TO 13", "CTC 13 N", "CTC 13 R", "CTC 13 N", "CTC 13 R", station)
station.add(turnout)

rightward = arrayList(["14 R Main"])
leftward  = arrayList(["14 L Main"])
signal1 = SignalHeadSection(rightward, leftward, "CTC 14 L", "CTC 14 C", "CTC 14 R", "CTC 14 L", "CTC 14 R", station);
station.add(signal1)

rightward = arrayList(["16 R Siding"])
leftward  = arrayList(["16 L Siding"])
signal2 = SignalHeadSection(rightward, leftward, "CTC 16 L", "CTC 16 C", "CTC 16 R", "CTC 16 L", "CTC 16 R", station);
station.add(signal2)

occupancyLock = CombinedLock([OccupancyLock("TC 15"), OccupancyLock("TC 16")])
routeLock = RouteLock(["14 R Main", "16 R Siding", "14 L Main", "16 L Siding"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal1), TimeLock(signal2)]));

# ===== Set up Station 17/18/20 =====

button = CodeButton("CTC 18 Code A", "CTC 18 Code")
station = Station("17/18/20", codeline, button)

station.add(TrackCircuitSection("TC 17","CTC TC 17", station)) # 13-17 main
station.add(TrackCircuitSection("TC 18","CTC TC 18", station)) # 13-17 siding
station.add(TrackCircuitSection("TC 19","CTC TC 19", station, vbell)) # OS 17 main
station.add(TrackCircuitSection("TC 20","CTC TC 20", station, vbell)) # OS 17 siding

turnout = TurnoutSection("TO 17", "CTC 17 N", "CTC 17 R", "CTC 17 N", "CTC 17 R", station)
station.add(turnout)

rightward = arrayList(["18 R"])
leftward  = arrayList([])
signal1 = SignalHeadSection(rightward, leftward, "CTC 18 L", "CTC 18 C", "CTC 18 R", "CTC 18 L", "CTC 18 R", station);
station.add(signal1)

rightward = arrayList(["20 R Upper", "20 R Lower"])
leftward  = arrayList([])
signal2 = SignalHeadSection(rightward, leftward, "CTC 20 L", "CTC 20 C", "CTC 20 R", "CTC 20 L", "CTC 20 R", station);
station.add(signal2)

station.add(MaintainerCallSection("CTC 18 Call","MC 18", station))

occupancyLock = CombinedLock([OccupancyLock("TC 19"), OccupancyLock("TC 20")])
routeLock = RouteLock(["20 R Upper", "20 R Lower", "18 R"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal1), TimeLock(signal2)]));

# ===== Set up Station 21/22 =====

button = CodeButton("CTC 22 Code A", "CTC 22 Code")
station = Station("21/22", codeline, button)

station.add(TrackCircuitSection("TC 21","CTC TC 21", station)) # siding 17 - xover
station.add(TrackCircuitSection("TC 22","CTC TC 22", station)) # 17-21 main
station.add(TrackCircuitSection("TC 23","CTC TC 23", station)) # xover - 21 siding
station.add(TrackCircuitSection("TC 24","CTC TC 24", station, vbell)) # OS 21

turnout = TurnoutSection("TO 21", "CTC 21 N", "CTC 21 R", "CTC 21 N", "CTC 21 R", station)
station.add(turnout)

rightward = arrayList(["22 R Main", "22 R Siding"])
leftward  = arrayList(["22 L Upper", "22 L Lower"])
signal = SignalHeadSection(rightward, leftward, "CTC 22 L", "CTC 22 C", "CTC 22 R", "CTC 22 L", "CTC 22 R", station);
station.add(signal)

occupancyLock = OccupancyLock("TC 24")
routeLock = RouteLock(["22 R Main", "22 R Siding", "22 L Upper", "22 L Lower"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal)]));

# ===== Set up Station 25/26 =====

button = CodeButton("CTC 26 Code A", "CTC 26 Code")
station = Station("25/26", codeline, button)

CombineSensors().set("TC 25", ["TC 25 Lower (bridge)","TC 25 Upper (shasta)"])
station.add(TrackCircuitSection("TC 25","CTC TC 25", station)) # 21-25
station.add(TrackCircuitSection("TC 26","CTC TC 26", station, vbell)) # OS 25

turnout = TurnoutSection("TO 25", "CTC 25 N", "CTC 25 R", "CTC 25 N", "CTC 25 R", station)
station.add(turnout)

rightward = arrayList(["26 R Upper", "26 R Lower"])
leftward  = arrayList(["26 L Main", "26 L Siding"])
signal = SignalHeadSection(rightward, leftward, "CTC 26 L", "CTC 26 C", "CTC 26 R", "CTC 26 L", "CTC 26 R", station);
station.add(signal)

station.add(MaintainerCallSection("CTC 26 Call","MC 26/28", station))

occupancyLock = OccupancyLock("TC 26")
routeLock = RouteLock(["26 R Upper", "26 R Lower", "26 L Main", "26 L Siding"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal)]));

# ===== Set up Station 27/28 =====

button = CodeButton("CTC 28 Code A", "CTC 28 Code")
station = Station("27/28", codeline, button)

station.add(TrackCircuitSection("TC 27","CTC TC 27", station)) # 25-27 main
station.add(TrackCircuitSection("TC 28","CTC TC 28", station)) # 25-27 siding
station.add(TrackCircuitSection("TC 29","CTC TC 29", station, vbell)) # OS 27

turnout = TurnoutSection("TO 27", "CTC 27 N", "CTC 27 R", "CTC 27 N", "CTC 27 R", station)
station.add(turnout)

rightward = arrayList(["28 R Main", "28 R Siding"])
leftward  = arrayList(["28 L Upper", "28 L Lower"])
signal = SignalHeadSection(rightward, leftward, "CTC 28 L", "CTC 28 C", "CTC 28 R", "CTC 28 L", "CTC 28 R", station);
station.add(signal)

station.add(MaintainerCallSection("CTC 28 Call","MC 26/28", station))

occupancyLock = OccupancyLock("TC 29")
routeLock = RouteLock(["28 R Main", "28 R Siding", "28 L Upper", "28 L Lower"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal)]));

# ===== Set up Station 29/30 =====

button = CodeButton("CTC 30 Code A", "CTC 30 Code")
station = Station("29/30", codeline, button)

station.add(TrackCircuitSection("TC 30","CTC TC 30", station)) # 27-29
station.add(TrackCircuitSection("TC 31","CTC TC 31", station)) # OS 29

turnout = TurnoutSection("TO 29", "CTC 29 N", "CTC 29 R", "CTC 29 N", "CTC 29 R", station)
station.add(turnout)

rightward = arrayList(["30 R Upper", "30 R Lower"])
leftward  = arrayList(["30 L Main", "30 L Siding"])
signal = SignalHeadSection(rightward, leftward, "CTC 30 L", "CTC 30 C", "CTC 30 R", "CTC 30 L", "CTC 30 R", station);
station.add(signal)

station.add(MaintainerCallSection("CTC 30 Call","MC 30", station))

occupancyLock = OccupancyLock("TC 31")
routeLock = RouteLock(["30 R Upper", "30 R Lower", "30 L Main", "30 L Siding"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal)]));

# ===== Set up Station 31/32/34 =====

button = CodeButton("CTC 32 Code A", "CTC 32 Code")
station = Station("31/23/34", codeline, button)

station.add(TrackCircuitSection("TC 32","CTC TC 32", station)) # 29-31 main
station.add(TrackCircuitSection("TC 33","CTC TC 33", station)) # 29-31 siding
station.add(TrackCircuitSection("TC 34","CTC TC 34", station, vbell)) # OS 31 west
station.add(TrackCircuitSection("TC 35","CTC TC 35", station, vbell)) # OS 31 west

CombineTurnouts().set("TO 31", ["TO 31A","TO 31B"])
turnout = TurnoutSection("TO 31", "CTC 31 N", "CTC 31 R", "CTC 31 N", "CTC 31 R", station)
station.add(turnout)

rightward = arrayList(["32 R Lower", "32 R Upper"])
leftward  = arrayList(["32 L Siding"])
signal1 = SignalHeadSection(rightward, leftward, "CTC 32 L", "CTC 32 C", "CTC 32 R", "CTC 32 L", "CTC 32 R", station);
station.add(signal1)

rightward = arrayList(["34 R Siding"])
leftward  = arrayList(["34 L Lower", "34 L Upper"])
signal2 = SignalHeadSection(rightward, leftward, "CTC 34 L", "CTC 34 C", "CTC 34 R", "CTC 34 L", "CTC 34 R", station);
station.add(signal2)

station.add(MaintainerCallSection("CTC 32 Call","MC 32", station))

occupancyLock = CombinedLock([OccupancyLock("TC 34"), OccupancyLock("TC 35")])
routeLock = RouteLock(["32 R Lower", "32 R Upper", "34 R Siding", "34 L Lower", "34 L Upper", "32 L Siding"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal1), TimeLock(signal2)]));

# ===== Set up Station 35/36/38 =====

button = CodeButton("CTC 36 Code A", "CTC 36 Code")
station = Station("35/36/38", codeline, button)

station.add(TrackCircuitSection("TC 36","CTC TC 36", station)) # 31-35 siding
station.add(TrackCircuitSection("TC 37","CTC TC 37", station)) # 31-35 main
station.add(TrackCircuitSection("TC 38","CTC TC 38", station, vbell)) # OS 35 east
station.add(TrackCircuitSection("TC 101","CTC TC 101", station, vbell)) # OS 35 west

turnout = TurnoutSection("TO 35A", "CTC 35 N", "CTC 35 R", "CTC 35 N", "CTC 35 R", station)
station.add(turnout)

rightward = arrayList(["36 R Azalea Main Upper", "36 R Azalea Main Lower"])
leftward  = arrayList(["36 L Azalea Bypass"])
signal1 = SignalHeadSection(rightward, leftward, "CTC 36 L", "CTC 36 C", "CTC 36 R", "CTC 36 L", "CTC 36 R", station);
station.add(signal2)

rightward = arrayList(["38 R Siding"])
leftward  = arrayList(["38 L Lower", "38 L Upper"])
signal1 = SignalHeadSection(rightward, leftward, "CTC 38 L", "CTC 38 C", "CTC 38 R", "CTC 38 L", "CTC 38 R", station);
station.add(signal2)

station.add(MaintainerCallSection("CTC 36 Call","MC 36", station))

occupancyLock = CombinedLock([OccupancyLock("TC 38"), OccupancyLock("TC 101")])
routeLock = RouteLock(["36 R Azalea Main Upper", "36 R Azalea Main Lower", "38 R Siding", "38 L Lower", "38 L Upper", "36 L Azalea Bypass"]);
turnout.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal1), TimeLock(signal2)]));

# ===== Set up Station 39/40/41/42 =====

button = CodeButton("CTC 40 Code A", "CTC 40 Code")
station = Station("39/40/41/42", codeline, button)

station.add(TrackCircuitSection("TC 39","CTC TC 39", station)) # 35-39 main
station.add(TrackCircuitSection("TC 102","CTC TC 102", station)) # 35-39 siding
station.add(TrackCircuitSection("TC 40","CTC TC 40", station, vbell)) # OS 39 west
station.add(TrackCircuitSection("TC 41","CTC TC 41", station, bell)) # 39 to BB main
station.add(TrackCircuitSection("TC 42","CTC TC 42", station, bell)) # 41 to BB siding
station.add(TrackCircuitSection("TC 43","CTC TC 43", station, bell)) # 41 to Weed
station.add(TrackCircuitSection("TC 103","CTC TC 103", station, vbell)) # OS 39 east

CombineTurnouts().set("TO 39", ["TO 39A","TO 39B"])
turnout1 = TurnoutSection("TO 39", "CTC 39 N", "CTC 39 R", "CTC 39 N", "CTC 39 R", station)
station.add(turnout1)

turnout2 = TurnoutSection("TO 41", "CTC 41 N", "CTC 41 R", "CTC 41 N", "CTC 41 R", station)
station.add(turnout2)

# "40 R 2nd on main" is an ABS signal protecting engineers from running over the back-set turnout at end of bypass
rightward = arrayList(["40 R Upper", "40 R Middle", "40 R Lower"])
leftward  = arrayList(["40 L Weed", "40 L Siding", "42 L Black Butte Main Upper"])  # bit of a hack with 42 L Upper, allows traffic over 39
signal = SignalHeadSection(rightward, leftward, "CTC 40 L", "CTC 40 C", "CTC 40 R", "CTC 40 L", "CTC 40 R", station);
station.add(signal)

rightward = arrayList(["42 R Bypass"])
leftward  = arrayList(["42 L Black Butte Main Lower"])  # no 42 L Upper as that's traffic over 39 in 40
signal = SignalHeadSection(rightward, leftward, "CTC 42 L", "CTC 42 C", "CTC 42 R", "CTC 42 L", "CTC 42 R", station);
station.add(signal)

station.add(MaintainerCallSection("CTC 42 Call","MC 42", station))

occupancyLock = CombinedLock([OccupancyLock("TC 40"), OccupancyLock("TC 103")])
routeLock = RouteLock(["40 R Upper", "40 R Middle", "40 R Lower", "40 L Weed", "40 L Siding", "42 R Bypass", "42 L Black Butte Main Upper", "42 L Black Butte Main Lower"]);
turnout1.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, TimeLock(signal1), TimeLock(signal2)]));

occupancyLock = OccupancyLock("TC 40")
routeLock = RouteLock(["40 L Weed", "40 L Siding"]);
routeLock2 = RouteLock(["40 R Upper", "40 R Middle", "40 R Lower"], [jmri.BeanSetting(turnouts.getTurnout("TO 39"), THROWN)]);
turnout2.addLocks(java.util.Arrays.asList([occupancyLock, routeLock, routeLock2, TimeLock(signal1), TimeLock(signal2)]));

