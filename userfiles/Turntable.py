# Drive a PTC Turntable, including powering
# the tracks via relays
#
# Author: Bob Jacobsen, copyright 2005, 2011, 2015, 2016
#
# IM1 keeps track of current move
# CS2001 - CS2022 track selection sensors
# CS2023 - tail/cab selection
# CT2033 - CT2041 (was CT2025 - CT2033) power control
#

import jarray
import jmri

import java
import javax

def moveZeroCCW(offset) :
    for name in TrackPositions.keys() :
        val = int(TrackPositions[name]) + offset
        if (val < 0) : val = val + 13200
        if (val >= 13200) : val = val - 13200
        TrackPositions[name] = str( val )
    for name in TrackPositions.keys() :
        memories.provideMemory(name).value = TrackPositions[name]

TrackPositions = dict()

TrackPositions["IMTRKWESTLEADH1"]  = "13189"
TrackPositions["IMTRKWESTLEADH2"]  = "13189"
TrackPositions["IMTRKWESTLEADT1"]  = "6591"
TrackPositions["IMTRKWESTLEADT2"]  = "6591"

TrackPositions["IMTRKMALLET1H1"]  = "12769"
TrackPositions["IMTRKMALLET1H2"]  = "12769"
TrackPositions["IMTRKMALLET1T1"]  = "6182"
TrackPositions["IMTRKMALLET1T2"]  = "6182"

TrackPositions["IMTRKMALLET2H1"]  = "12409"
TrackPositions["IMTRKMALLET2H2"]  = "12409"
TrackPositions["IMTRKMALLET2T1"]  = "5812"
TrackPositions["IMTRKMALLET2T2"]  = "5812"

TrackPositions["IMTRKSANDH1"]  = "12099"
TrackPositions["IMTRKSANDH2"]  = "12099"
TrackPositions["IMTRKSANDT1"]  = "5505"
TrackPositions["IMTRKSANDT2"]  = "5505"

TrackPositions["IMTRK1H1"]  = "11763"
TrackPositions["IMTRK1H2"]  = "11763"
TrackPositions["IMTRK1T1"]  = "5169"
TrackPositions["IMTRK1T2"]  = "5169"

TrackPositions["IMTRK2H1"]  = "11499"
TrackPositions["IMTRK2H2"]  = "11499"
TrackPositions["IMTRK2T1"]  = "4916"
TrackPositions["IMTRK2T2"]  = "4916"

TrackPositions["IMTRK3H1"]  = "11236"
TrackPositions["IMTRK3H2"]  = "11236"
TrackPositions["IMTRK3T1"]  = "4657"
TrackPositions["IMTRK3T2"]  = "4657"

TrackPositions["IMTRK4H1"]  = "10981"
TrackPositions["IMTRK4H2"]  = "10981"
TrackPositions["IMTRK4T1"]  = "4402"
TrackPositions["IMTRK4T2"]  = "4402"

TrackPositions["IMTRK5H1"]  = "10727"
TrackPositions["IMTRK5H2"]  = "10727"
TrackPositions["IMTRK5T1"]  = "4146"
TrackPositions["IMTRK5T2"]  = "4146"

TrackPositions["IMTRK6H1"]  = "10463"
TrackPositions["IMTRK6H2"]  = "10463"
TrackPositions["IMTRK6T1"]  = "3882"
TrackPositions["IMTRK6T2"]  = "3882"

TrackPositions["IMTRK7H1"]  = "10141"
TrackPositions["IMTRK7H2"]  = "10141"
TrackPositions["IMTRK7T1"]  = "3553"
TrackPositions["IMTRK7T2"]  = "3553"

TrackPositions["IMTRK8H1"]  = "9883"
TrackPositions["IMTRK8H2"]  = "9883"
TrackPositions["IMTRK8T1"]  = "3289"
TrackPositions["IMTRK8T2"]  = "3289"

TrackPositions["IMTRK9H1"]  = "9620"
TrackPositions["IMTRK9H2"]  = "9620"
TrackPositions["IMTRK9T1"]  = "3021"
TrackPositions["IMTRK9T2"]  = "3021"

TrackPositions["IMTRK10H1"]  = "9343"
TrackPositions["IMTRK10H2"]  = "9343"
TrackPositions["IMTRK10T1"]  = "2753"
TrackPositions["IMTRK10T2"]  = "2753"

TrackPositions["IMTRK11H1"]  = "9075"
TrackPositions["IMTRK11H2"]  = "9075"
TrackPositions["IMTRK11T1"]  = "2490"
TrackPositions["IMTRK11T2"]  = "2490"

TrackPositions["IMTRK12H1"]  = "8808"
TrackPositions["IMTRK12H2"]  = "8808"
TrackPositions["IMTRK12T1"]  = "2229"
TrackPositions["IMTRK12T2"]  = "2229"

TrackPositions["IMTRK13H1"]  = "8542"
TrackPositions["IMTRK13H2"]  = "8542"
TrackPositions["IMTRK13T1"]  = "1961"
TrackPositions["IMTRK13T2"]  = "1961"

TrackPositions["IMTRK14H1"]  = "8278"
TrackPositions["IMTRK14H2"]  = "8278"
TrackPositions["IMTRK14T1"]  = "1697"
TrackPositions["IMTRK14T2"]  = "1697"

TrackPositions["IMTRK15H1"]  = "8021"
TrackPositions["IMTRK15H2"]  = "8021"
TrackPositions["IMTRK15T1"]  = "1436"
TrackPositions["IMTRK15T2"]  = "1436"

TrackPositions["IMTRKMACHINE2H1"]  = "6186"
TrackPositions["IMTRKMACHINE2H2"]  = "6186"
TrackPositions["IMTRKMACHINE2T1"]  = "12795"
TrackPositions["IMTRKMACHINE2T2"]  = "12795"

TrackPositions["IMTRKMACHINE1H1"]  = "5936"
TrackPositions["IMTRKMACHINE1H2"]  = "5936"
TrackPositions["IMTRKMACHINE1T1"]  = "12545"
TrackPositions["IMTRKMACHINE1T2"]  = "12545"

TrackPositions["IMTRKEASTLEADH1"]  = "5027"
TrackPositions["IMTRKEASTLEADH2"]  = "5027"
TrackPositions["IMTRKEASTLEADT1"]  = "11619"
TrackPositions["IMTRKEASTLEADT2"]  = "11619"



# load position memories
for name in TrackPositions.keys() :
    memories.provideMemory(name).value = TrackPositions[name]
    
memories.provideMemory("IMTRKPOSITION").value = "0"

class TurntableDriver(jmri.jmrit.automat.AbstractAutomaton) :
    def init(self):     
        # array of input to wait for later
        self.sensorArray = jarray.array([
        sensors.provideSensor("CS2001"), 
        sensors.provideSensor("CS2002"), 
        sensors.provideSensor("CS2003"), 
        sensors.provideSensor("CS2004"), 
        sensors.provideSensor("CS2005"), 
        sensors.provideSensor("CS2006"), 
        sensors.provideSensor("CS2007"), 
        sensors.provideSensor("CS2008"), 
        sensors.provideSensor("CS2009"), 
        sensors.provideSensor("CS2010"), 
        sensors.provideSensor("CS2011"), 
        sensors.provideSensor("CS2012"), 
        sensors.provideSensor("CS2013"), 
        sensors.provideSensor("CS2014"), 
        sensors.provideSensor("CS2015"), 
        sensors.provideSensor("CS2016"), 
        sensors.provideSensor("CS2017"), 
        sensors.provideSensor("CS2018"), 
        sensors.provideSensor("CS2019"), 
        sensors.provideSensor("CS2020"), 
        sensors.provideSensor("CS2021"), 
        sensors.provideSensor("CS2022")
        ], jmri.Sensor)
        
        return
        
    def moveToTrk(self, trackName, sensor) :
        # execute a specific request
        mem = memories.provideMemory("IM1")
        mem.setValue(trackName)
        self.calculateAndMove(trackName)
        # wait for sensor to clear
        self.waitSensorInactive(sensors.provideSensor(sensor))
        return 1
    
    def calculateAndMove(self, trackName) :
        # check head/tail
        if (sensors.provideSensor("CS2024").getKnownState() == ACTIVE) :
            cab = "H"
        else :
            cab = "T"
        # find and save target
        d1 = int(memories.provideMemory("IMTRK"+trackName+cab+"1").getValue())
        d2 = int(memories.provideMemory("IMTRK"+trackName+cab+"2").getValue())
        p = int(memories.provideMemory("IMTRKPOSITION").getValue())
        #
        # find which position to move to
        turnsize = 13200*2
        deld1 = min([abs(p-d1), abs(p-(d1-turnsize)), abs(p-(d1+turnsize))])
        deld2 = min([abs(p-d2), abs(p-(d2-turnsize)), abs(p-(d2+turnsize))])
        if (deld1 > deld2) :
            pos = d2
            memories.provideMemory("IMTRKLASTMEM").value = "IMTRK"+trackName+cab+"2"
        else :
            pos = d1
            memories.provideMemory("IMTRKLASTMEM").value = "IMTRK"+trackName+cab+"1"
        
        pos = d1;
        memories.provideMemory("IMTRKLASTMEM").value = "IMTRK"+trackName+cab+"1"
        # pos now holds new position to move to
        print "Moving to ", trackName, cab," at ",pos
        # send as C/MRI packet
        self.doMove(str(pos))
        return 1
    
    def doMove(self, position) :
        # record new position
        memories.provideMemory("IMTRKPOSITION").setValue(position)
        # tell CMRI to do the move
        self.tellCMRI(position)
        return
        
    def tellCMRI(self, position) :
        # send as C/MRI packet
        t = "000000"+position
        
        # node 10 (A) is now the signal mast; no connection to turntable controller
        
        m = jmri.jmrix.cmri.serial.SerialMessage(7)
        m.setElement(0, 0x30+10)
        m.setElement(1, 0x6D)
        m.setElement(2, 0x30+int(t[len(t)-5]))
        m.setElement(3, 0x30+int(t[len(t)-4]))
        m.setElement(4, 0x30+int(t[len(t)-3]))
        m.setElement(5, 0x30+int(t[len(t)-2]))
        m.setElement(6, 0x30+int(t[len(t)-1]))
        m.setTimeout(5)
        jmri.jmrix.cmri.serial.SerialTrafficController.instance().sendSerialMessage(m,None)
        return
            
    def handle(self):
        # wait for one of the sensors to be active
        self.waitSensorActive(self.sensorArray)

        # remember the commanded position
        mem = memories.provideMemory("IM1")
        mem.setValue("none")

        # start the move
        if (sensors.getSensor("CS2001").getState() == ACTIVE) :
            self.moveToTrk("1","CS2001")
        if (sensors.getSensor("CS2002").getState() == ACTIVE) :
            self.moveToTrk("2","CS2002")
        if (sensors.getSensor("CS2003").getState() == ACTIVE) :
            self.moveToTrk("3","CS2003")
        if (sensors.getSensor("CS2004").getState() == ACTIVE) :
            self.moveToTrk("4","CS2004")
        if (sensors.getSensor("CS2005").getState() == ACTIVE) :
            self.moveToTrk("5","CS2005")
        if (sensors.getSensor("CS2006").getState() == ACTIVE) :
            self.moveToTrk("6","CS2006")
        if (sensors.getSensor("CS2007").getState() == ACTIVE) :
            self.moveToTrk("7","CS2007")
        if (sensors.getSensor("CS2008").getState() == ACTIVE) :
            self.moveToTrk("8","CS2008")
        if (sensors.getSensor("CS2009").getState() == ACTIVE) :
            self.moveToTrk("9","CS2009")
        if (sensors.getSensor("CS2010").getState() == ACTIVE) :
            self.moveToTrk("10","CS2010")
        if (sensors.getSensor("CS2011").getState() == ACTIVE) :
            self.moveToTrk("11","CS2011")
        if (sensors.getSensor("CS2012").getState() == ACTIVE) :
            self.moveToTrk("12","CS2012")
        if (sensors.getSensor("CS2013").getState() == ACTIVE) :
            self.moveToTrk("13","CS2013")
        if (sensors.getSensor("CS2014").getState() == ACTIVE) :
            self.moveToTrk("14","CS2014")
        if (sensors.getSensor("CS2015").getState() == ACTIVE) :
            self.moveToTrk("15","CS2015")

        # cases below here are sensors without power tracks
        if (sensors.getSensor("CS2016").getState() == ACTIVE) :
            self.moveToTrk("MACHINE2","CS2016")
        if (sensors.getSensor("CS2017").getState() == ACTIVE) :
            self.moveToTrk("MACHINE1","CS2017")
        if (sensors.getSensor("CS2018").getState() == ACTIVE) :
            self.moveToTrk("EASTLEAD","CS2018")
        if (sensors.getSensor("CS2019").getState() == ACTIVE) :
            self.moveToTrk("SAND","CS2019")
        if (sensors.getSensor("CS2020").getState() == ACTIVE) :
            self.moveToTrk("MALLET2","CS2020")
        if (sensors.getSensor("CS2021").getState() == ACTIVE) :
            self.moveToTrk("MALLET1","CS2021")
        if (sensors.getSensor("CS2022").getState() == ACTIVE) :
            self.moveToTrk("WESTLEAD","CS2022")

        if (sensors.getSensor("ISTRKSET").getState() == ACTIVE) :
            self.moveToTrk("SET","ISTRKSET")

        # set the power
        self.setPower()
        
        return 1
    
    # setPower sets up the relays each time called
    def setPower(self):

        # turn off all power
        turnouts.provideTurnout("Duns TT Card 1 Bit 1").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 1 Bit 2").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 1 Bit 4").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 2 Bit 1").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 2 Bit 2").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 2 Bit 4").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 3 Bit 1").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 3 Bit 2").setState(THROWN)
        turnouts.provideTurnout("Duns TT Card 3 Bit 4").setState(THROWN)
        
        # set power from stored value
        mem = memories.provideMemory("IM1")
        print "set power for", mem.getValue()
        
        # tracks on first card
        if (mem.getValue() == "1") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 1").setState(CLOSED)
        if (mem.getValue() == "2") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 2").setState(CLOSED)
        if (mem.getValue() == "3") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 1").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 1 Bit 2").setState(CLOSED)
        if (mem.getValue() == "4") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 4").setState(CLOSED)
        if (mem.getValue() == "5") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 1").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 1 Bit 4").setState(CLOSED)
        if (mem.getValue() == "6") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 2").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 1 Bit 4").setState(CLOSED)
        if (mem.getValue() == "7") :
            turnouts.provideTurnout("Duns TT Card 1 Bit 1").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 1 Bit 2").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 1 Bit 4").setState(CLOSED)
        
        # tracks on second card
        if (mem.getValue() == "8") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 1").setState(CLOSED)
        if (mem.getValue() == "9") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 2").setState(CLOSED)
        if (mem.getValue() == "10") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 1").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 2 Bit 2").setState(CLOSED)
        if (mem.getValue() == "11") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 4").setState(CLOSED)
        if (mem.getValue() == "12") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 1").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 2 Bit 4").setState(CLOSED)
        if (mem.getValue() == "13") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 2").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 2 Bit 4").setState(CLOSED)
        if (mem.getValue() == "14") :
            turnouts.provideTurnout("Duns TT Card 2 Bit 1").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 2 Bit 2").setState(CLOSED)
            turnouts.provideTurnout("Duns TT Card 2 Bit 4").setState(CLOSED)
        
        # tracks on third card
        if (mem.getValue() == "15") :
            turnouts.provideTurnout("Duns TT Card 3 Bit 1").setState(CLOSED)
        
        # the rest of the tracks are constant power, so
        # need not be handled
        return

# end of TurntableDriver class definition

# start one of these up
controller = TurntableDriver()
controller.start()

# now open update window
frame = javax.swing.JFrame()
frame.setLayout(java.awt.FlowLayout())

turnTableLabel = javax.swing.JLabel("no memory yet")
frame.getContentPane().add(turnTableLabel)
spinner = javax.swing.JSpinner()
spinnermodel = javax.swing.SpinnerNumberModel(0, -500, 2*13200, 1)
spinner.setModel(spinnermodel)
frame.getContentPane().add(spinner)
b = javax.swing.JButton("+20")
b.setToolTipText("Just increments spinner")

frame.getContentPane().add(b)
def TurnTableAdd20(event) :
    spinnermodel.value = spinnermodel.value+20
    return
b.actionPerformed = TurnTableAdd20
b.setToolTipText("Just increments spinner")

b = javax.swing.JButton("+5")
frame.getContentPane().add(b)
def TurnTableAdd5(event) :
    spinnermodel.value = spinnermodel.value+5
    return
b.actionPerformed = TurnTableAdd5
b.setToolTipText("Just decrements spinner")

b = javax.swing.JButton("-5")
frame.getContentPane().add(b)
def TurnTableSub5(event) :
    spinnermodel.value = spinnermodel.value-5
    return
b.actionPerformed = TurnTableSub5
b.setToolTipText("Just decrements spinner")

b = javax.swing.JButton("-20")
frame.getContentPane().add(b)
def TurnTableSub20(event) :
    spinnermodel.value = spinnermodel.value-20
    return
b.actionPerformed = TurnTableSub20
b.setToolTipText("Just decrements spinner")

b = javax.swing.JButton("Backoff")
frame.getContentPane().add(b)
def TurnTableBackoff(event) :
    spot = spinnermodel.value - 200
    if (spot < 0) :
        spot = spot + 13200
    print "Backoff to ", spot
    controller.doMove(str(spot))
    return
b.actionPerformed = TurnTableBackoff
b.setToolTipText("Move to spinner-200 then to spinner")

b = javax.swing.JButton("Set")
frame.getContentPane().add(b)
def TurnTableSet(event) :
    print "Set ", memories.provideMemory("IMTRKLASTMEM").value, " to ", spinnermodel.value
    memories.provideMemory(memories.provideMemory("IMTRKLASTMEM").value).value = str(spinnermodel.value)
    controller.doMove(str(spinnermodel.value))
    return
b.actionPerformed = TurnTableSet
b.setToolTipText("Set value into last memory and move")

b = javax.swing.JButton("Increment All")
frame.getContentPane().add(b)
def AddToAll(event) :
    print "Increment All by", spinnermodel.value
    moveZeroCCW(int(spinnermodel.value))
    # not setting position, as memory might not be set; just command move
    # controller.doMove(str(memories.provideMemory(memories.provideMemory("IMTRKLASTMEM").value).value))
    return
b.actionPerformed = AddToAll

b = javax.swing.JButton("Save")
frame.getContentPane().add(b)
def TurnTableSave(event) :
    print "Save "
    tracks = ["WESTLEAD", "MALLET1", "MALLET2", "SAND"]
    for trk in range(1,15+1) :
        tracks = tracks+[str(trk)]
    file = open("pythonsave.txt", "w")
    tracks = tracks+["Machine2", "Machine1", "EastLead"]
    for trk in tracks :
        TurnTableSaveOne("IMTRK"+trk+"H1", file)
        TurnTableSaveOne("IMTRK"+trk+"H2", file)
        TurnTableSaveOne("IMTRK"+trk+"T1", file)
        TurnTableSaveOne("IMTRK"+trk+"T2", file)
        file.writelines("\n")
    file.close()
    return
def TurnTableSaveOne(name, file) :
    file.writelines("memories.provideMemory(\""+name+"\").value  = \""+memories.provideMemory(name).value+"\"\n")
    return
b.actionPerformed = TurnTableSave


class TurnTableMemoryListener(java.beans.PropertyChangeListener):
  def propertyChange(self, event):
    if (event.propertyName == "value") :
        turnTableLabel.text = event.newValue
        spinnermodel.value = int(memories.provideMemory(event.newValue).value)
    return
memories.provideMemory("IMTRKLASTMEM").propertyChangeListener = TurnTableMemoryListener()

frame.pack()
frame.title = "Turntable Calibration"
frame.setVisible(True)

