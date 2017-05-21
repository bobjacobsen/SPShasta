# Set start-up conditions for the SP Shasta in debug mode.
#
# Do NOT run this while attached to the real machine!
# It overrides the actual switch inputs, which will have to
# be redone.
#
# By putting the commands in a separate class, they'll
# run independently after the "start" operation
#
# Author: Bob Jacobsen, copyright 2008
#
# The next line is maintained by CVS, please don't change it
# $Revision: 1.5 $
#

import jmri

class setDebugStartup(jmri.jmrit.automat.AbstractAutomaton) :      
  def init(self):
    return
  def handle(self):
    self.waitMsec(1000)
    
    print "CtcDebugInit starts"

    # sent all C/MRI sensors default INACTIVE
    list = sensors.getSystemNameList()
    for i in range(list.size()) :
        if (list.get(i)[0] == 'C') : 
            sensors.getSensor(list.get(i)).setState(INACTIVE)

    # sent all C/MRI turnouts default CLOSED
    list = turnouts.getSystemNameList()
    for i in range(list.size()) :
        if (list.get(i)[0] == 'C') : 
            turnouts.getTurnout(list.get(i)).setState(CLOSED)


    # set the CTC inputs as if machine is present
    # and levers are set to default positions
    sensors.getSensor("CTC 01 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 01 C").setState(INACTIVE)
    sensors.getSensor("CTC 01 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 02 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 02 C").setState(ACTIVE)
    sensors.getSensor("CTC 02 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 03 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 03 C").setState(INACTIVE)
    sensors.getSensor("CTC 03 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 04 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 04 C").setState(ACTIVE)
    sensors.getSensor("CTC 04 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 05 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 05 C").setState(INACTIVE)
    sensors.getSensor("CTC 05 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 06 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 06 C").setState(ACTIVE)
    sensors.getSensor("CTC 06 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 07 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 07 C").setState(INACTIVE)
    sensors.getSensor("CTC 07 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 08 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 08 C").setState(ACTIVE)
    sensors.getSensor("CTC 08 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 09 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 09 C").setState(INACTIVE)
    sensors.getSensor("CTC 09 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 10 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 10 C").setState(ACTIVE)
    sensors.getSensor("CTC 10 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 13 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 13 C").setState(INACTIVE)
    sensors.getSensor("CTC 13 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 14 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 14 C").setState(ACTIVE)
    sensors.getSensor("CTC 14 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 16 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 16 C").setState(ACTIVE)
    sensors.getSensor("CTC 16 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 17 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 17 C").setState(INACTIVE)
    sensors.getSensor("CTC 17 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 18 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 18 C").setState(ACTIVE)
    sensors.getSensor("CTC 18 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 20 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 20 C").setState(ACTIVE)
    sensors.getSensor("CTC 20 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 21 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 21 C").setState(INACTIVE)
    sensors.getSensor("CTC 21 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 22 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 22 C").setState(ACTIVE)
    sensors.getSensor("CTC 22 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 25 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 25 C").setState(INACTIVE)
    sensors.getSensor("CTC 25 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 26 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 26 C").setState(ACTIVE)
    sensors.getSensor("CTC 26 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 27 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 27 C").setState(INACTIVE)
    sensors.getSensor("CTC 27 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 28 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 28 C").setState(ACTIVE)
    sensors.getSensor("CTC 28 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 29 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 29 C").setState(INACTIVE)
    sensors.getSensor("CTC 29 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 30 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 30 C").setState(ACTIVE)
    sensors.getSensor("CTC 30 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 31 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 31 C").setState(INACTIVE)
    sensors.getSensor("CTC 31 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 32 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 32 C").setState(ACTIVE)
    sensors.getSensor("CTC 32 R").setState(INACTIVE)
    
    sensors.getSensor("CTC 34 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 34 C").setState(ACTIVE)
    sensors.getSensor("CTC 34 R").setState(INACTIVE)

    sensors.getSensor("CTC 35 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 35 C").setState(INACTIVE)
    sensors.getSensor("CTC 35 R").setState(INACTIVE)

    sensors.getSensor("CTC 36 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 36 C").setState(ACTIVE)
    sensors.getSensor("CTC 36 R").setState(INACTIVE)

    sensors.getSensor("CTC 38 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 38 C").setState(ACTIVE)
    sensors.getSensor("CTC 38 R").setState(INACTIVE)

    sensors.getSensor("CTC 39 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 39 C").setState(INACTIVE)
    sensors.getSensor("CTC 39 R").setState(INACTIVE)

    sensors.getSensor("CTC 40 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 40 C").setState(ACTIVE)
    sensors.getSensor("CTC 40 R").setState(INACTIVE)

    sensors.getSensor("CTC 41 N").setState(ACTIVE)
    sensors.getSensor("IS CTC 41 C").setState(INACTIVE)
    sensors.getSensor("CTC 41 R").setState(INACTIVE)

    sensors.getSensor("CTC 42 L").setState(INACTIVE)
    sensors.getSensor("IS CTC 42 C").setState(ACTIVE)
    sensors.getSensor("CTC 42 R").setState(INACTIVE)
    
    print "CtcDebugInit done"
    
    return False              # all done, don't repeat again

setDebugStartup().start()          # create one of these, and start it running

