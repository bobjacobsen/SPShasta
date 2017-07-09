#
# Set start-up conditions for the SP Shasta
#
# This is the general python configuration, not including the CTC logic itself

import jmri

class SetCtcIndicators(jmri.jmrit.automat.AbstractAutomaton) :      
  def init(self):
    return
  def handle(self):
    # delay long enough for debug init to run if present and polling to start if not
    self.waitMsec(8000)         # time is in milliseconds
    
    print "SetCtcIndicators starts"

    # start signal followers
    SignalFollowerListener().set("CH2001","CH2001R")
    SignalFollowerListener().set("CH2002","CH2002R")

    # Define followers for CTC sensor groups
    SensorGroupAutoItem().set("IS CTC 02 C",["CTC 02 R", "CTC 02 L"])
    SensorGroupAutoItem().set("IS CTC 04 C",["CTC 04 R", "CTC 04 L"])
    SensorGroupAutoItem().set("IS CTC 06 C",["CTC 06 R", "CTC 06 L"])
    SensorGroupAutoItem().set("IS CTC 08 C",["CTC 08 R", "CTC 08 L"])
    SensorGroupAutoItem().set("IS CTC 10 C",["CTC 10 R", "CTC 10 L"])
    SensorGroupAutoItem().set("IS CTC 14 C",["CTC 14 R", "CTC 14 L"])
    SensorGroupAutoItem().set("IS CTC 16 C",["CTC 16 R", "CTC 16 L"])
    SensorGroupAutoItem().set("IS CTC 18 C",["CTC 18 R", "CTC 18 L"])
    SensorGroupAutoItem().set("IS CTC 20 C",["CTC 20 R", "CTC 20 L"])
    SensorGroupAutoItem().set("IS CTC 22 C",["CTC 22 R", "CTC 22 L"])
    SensorGroupAutoItem().set("IS CTC 26 C",["CTC 26 R", "CTC 26 L"])
    SensorGroupAutoItem().set("IS CTC 28 C",["CTC 28 R", "CTC 28 L"])
    SensorGroupAutoItem().set("IS CTC 30 C",["CTC 30 R", "CTC 30 L"])
    SensorGroupAutoItem().set("IS CTC 32 C",["CTC 32 R", "CTC 32 L"])
    SensorGroupAutoItem().set("IS CTC 34 C",["CTC 34 R", "CTC 34 L"])
    SensorGroupAutoItem().set("IS CTC 36 C",["CTC 36 R", "CTC 36 L"])
    SensorGroupAutoItem().set("IS CTC 38 C",["CTC 38 R", "CTC 38 L"])
    SensorGroupAutoItem().set("IS CTC 40 C",["CTC 40 R", "CTC 40 L"])
    SensorGroupAutoItem().set("IS CTC 42 C",["CTC 42 R", "CTC 42 L"])

    # set the default call-on state to off
    turnouts.getTurnout("Call On Mode 38").setState(CLOSED)
    turnouts.getTurnout("Call On Mode 40").setState(CLOSED)

    # Black Butte lunars on but dark
    signals.getSignalHead("40 R BB Lunar Left").setAppearance(LUNAR)
    signals.getSignalHead("40 R BB Lunar Left").setLit(False)
    signals.getSignalHead("40 R BB Lunar Right").setAppearance(LUNAR)
    signals.getSignalHead("40 R BB Lunar Right").setLit(False)

    # set the default state of turnout locks to unlocked
    turnouts.getTurnout("Lock 86").setState(THROWN)

    # init internal sensors for Operator Bell Controls
    sensors.provideSensor("IS-BELL-BLACKBUTTEW").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-BLACKBUTTEE").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-GRASSLAKEW").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-GRASSLAKEE").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-DORRISW").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-DORRISE").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-TEXUM").setState(ACTIVE)

    # set the default state of train order boards to off
    turnouts.getTurnout("TO Signal GL Westbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal GL Eastbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal BB Eastbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal BB Westbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal DR Westbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal DR Eastbound").setState(CLOSED)

    # push & unpush buttons at Grass Lake for main
    sensors.provideSensor("GLE PB Main Track").setState(ACTIVE)
    sensors.provideSensor("GLW PB Main Track").setState(ACTIVE)
    sensors.provideSensor("GLY PB Main").setState(ACTIVE)
    self.waitMsec(500)
    sensors.provideSensor("GLE PB Main Track").setState(INACTIVE)
    sensors.provideSensor("GLW PB Main Track").setState(INACTIVE)
    sensors.provideSensor("GLY PB Main").setState(INACTIVE)
    
    # set up the outside signal mast
    turnouts.getTurnout("CT9001").setState(THROWN)
    turnouts.getTurnout("CT9002").setState(THROWN)
    turnouts.getTurnout("CT9003").setState(THROWN)
    turnouts.getTurnout("CT9004").setState(THROWN)
    turnouts.getTurnout("ITSIGNALMASTAUTO").setState(CLOSED)
    
    print "SetCtcIndicators done"
    
    return False              # all done, don't repeat again

SetCtcIndicators().start()          # create one of these, and start it running
