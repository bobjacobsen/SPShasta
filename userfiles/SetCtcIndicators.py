#
# Set start-up conditions for the SP Shasta
#
# By putting the turnout commands in a separate class, they'll
# run independently after the "start" operation

import jmri

class setStartup(jmri.jmrit.automat.AbstractAutomaton) :      
  def init(self):
    return
  def handle(self):
    # delay long enough for debug init to run if present and polling to start if not
    self.waitMsec(8000)         # time is in milliseconds
    
    print "SetCtcIndicators starts"

    # init internal sensors, not present on layout
    sensors.getSensor("TC 20").setState(INACTIVE)
    sensors.getSensor("TC 21").setState(INACTIVE)
    sensors.getSensor("TC 22").setState(INACTIVE)
    sensors.getSensor("TC 23").setState(INACTIVE)

    # init internal sensors for Bell Controls
    sensors.provideSensor("IS-BELL-BLACKBUTTEW").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-BLACKBUTTEE").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-GRASSLAKEW").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-GRASSLAKEE").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-DORRISW").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-DORRISE").setState(ACTIVE)
    sensors.provideSensor("IS-BELL-TEXUM").setState(ACTIVE)

    # set the default call-on state to off
    turnouts.getTurnout("Call On Mode 38").setState(CLOSED)
    turnouts.getTurnout("Call On Mode 40").setState(CLOSED)

    # set the default state of turnout locks to unlocked
    turnouts.getTurnout("Lock 86").setState(THROWN)

    # set the default state of train order boards to off
    turnouts.getTurnout("TO Signal GL Westbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal GL Eastbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal BB Eastbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal BB Westbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal DR Westbound").setState(CLOSED)
    turnouts.getTurnout("TO Signal DR Eastbound").setState(CLOSED)

    # Black Butte lunars on but dark
    signals.getSignalHead("40 R BB Lunar Left").setAppearance(LUNAR)
    signals.getSignalHead("40 R BB Lunar Left").setLit(False)
    signals.getSignalHead("40 R BB Lunar Right").setAppearance(LUNAR)
    signals.getSignalHead("40 R BB Lunar Right").setLit(False)

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

    # force mode transition to get a stable set of states
    if sensors.getSensor("CTC Mode").state == ACTIVE :
        sensors.getSensor("CTC Mode").setState(INACTIVE)
        self.waitMsec(250)
        sensors.getSensor("CTC Mode").setState(ACTIVE)
    else :
        sensors.getSensor("CTC Mode").setState(ACTIVE)
        self.waitMsec(250)
        sensors.getSensor("CTC Mode").setState(INACTIVE)
    
    print "SetCtcIndicators done"
    
    return False              # all done, don't repeat again

setStartup().start()          # create one of these, and start it running
