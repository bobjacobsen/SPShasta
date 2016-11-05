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

# load position memories
memories.provideMemory("IMTRKWESTLEADH1").value  = "13189"
memories.provideMemory("IMTRKWESTLEADH2").value  = "13189"
memories.provideMemory("IMTRKWESTLEADT1").value  = "6591"
memories.provideMemory("IMTRKWESTLEADT2").value  = "6591"

memories.provideMemory("IMTRKMALLET1H1").value  = "12769"
memories.provideMemory("IMTRKMALLET1H2").value  = "12769"
memories.provideMemory("IMTRKMALLET1T1").value  = "6182"
memories.provideMemory("IMTRKMALLET1T2").value  = "6182"

memories.provideMemory("IMTRKMALLET2H1").value  = "12409"
memories.provideMemory("IMTRKMALLET2H2").value  = "12409"
memories.provideMemory("IMTRKMALLET2T1").value  = "5812"
memories.provideMemory("IMTRKMALLET2T2").value  = "5812"

memories.provideMemory("IMTRKSANDH1").value  = "12099"
memories.provideMemory("IMTRKSANDH2").value  = "12099"
memories.provideMemory("IMTRKSANDT1").value  = "5505"
memories.provideMemory("IMTRKSANDT2").value  = "5505"

memories.provideMemory("IMTRK1H1").value  = "11763"
memories.provideMemory("IMTRK1H2").value  = "11763"
memories.provideMemory("IMTRK1T1").value  = "5169"
memories.provideMemory("IMTRK1T2").value  = "5169"

memories.provideMemory("IMTRK2H1").value  = "11499"
memories.provideMemory("IMTRK2H2").value  = "11499"
memories.provideMemory("IMTRK2T1").value  = "4916"
memories.provideMemory("IMTRK2T2").value  = "4916"

memories.provideMemory("IMTRK3H1").value  = "11236"
memories.provideMemory("IMTRK3H2").value  = "11236"
memories.provideMemory("IMTRK3T1").value  = "4657"
memories.provideMemory("IMTRK3T2").value  = "4657"

memories.provideMemory("IMTRK4H1").value  = "10981"
memories.provideMemory("IMTRK4H2").value  = "10981"
memories.provideMemory("IMTRK4T1").value  = "4402"
memories.provideMemory("IMTRK4T2").value  = "4402"

memories.provideMemory("IMTRK5H1").value  = "10727"
memories.provideMemory("IMTRK5H2").value  = "10727"
memories.provideMemory("IMTRK5T1").value  = "4146"
memories.provideMemory("IMTRK5T2").value  = "4146"

memories.provideMemory("IMTRK6H1").value  = "10463"
memories.provideMemory("IMTRK6H2").value  = "10463"
memories.provideMemory("IMTRK6T1").value  = "3882"
memories.provideMemory("IMTRK6T2").value  = "3882"

memories.provideMemory("IMTRK7H1").value  = "10141"
memories.provideMemory("IMTRK7H2").value  = "10141"
memories.provideMemory("IMTRK7T1").value  = "3553"
memories.provideMemory("IMTRK7T2").value  = "3553"

memories.provideMemory("IMTRK8H1").value  = "9883"
memories.provideMemory("IMTRK8H2").value  = "9883"
memories.provideMemory("IMTRK8T1").value  = "3289"
memories.provideMemory("IMTRK8T2").value  = "3289"

memories.provideMemory("IMTRK9H1").value  = "9620"
memories.provideMemory("IMTRK9H2").value  = "9620"
memories.provideMemory("IMTRK9T1").value  = "3021"
memories.provideMemory("IMTRK9T2").value  = "3021"

memories.provideMemory("IMTRK10H1").value  = "9343"
memories.provideMemory("IMTRK10H2").value  = "9343"
memories.provideMemory("IMTRK10T1").value  = "2753"
memories.provideMemory("IMTRK10T2").value  = "2753"

memories.provideMemory("IMTRK11H1").value  = "9075"
memories.provideMemory("IMTRK11H2").value  = "9075"
memories.provideMemory("IMTRK11T1").value  = "2490"
memories.provideMemory("IMTRK11T2").value  = "2490"

memories.provideMemory("IMTRK12H1").value  = "8808"
memories.provideMemory("IMTRK12H2").value  = "8808"
memories.provideMemory("IMTRK12T1").value  = "2229"
memories.provideMemory("IMTRK12T2").value  = "2229"

memories.provideMemory("IMTRK13H1").value  = "8542"
memories.provideMemory("IMTRK13H2").value  = "8542"
memories.provideMemory("IMTRK13T1").value  = "1961"
memories.provideMemory("IMTRK13T2").value  = "1961"

memories.provideMemory("IMTRK14H1").value  = "8278"
memories.provideMemory("IMTRK14H2").value  = "8278"
memories.provideMemory("IMTRK14T1").value  = "1697"
memories.provideMemory("IMTRK14T2").value  = "1697"

memories.provideMemory("IMTRK15H1").value  = "8021"
memories.provideMemory("IMTRK15H2").value  = "8021"
memories.provideMemory("IMTRK15T1").value  = "1436"
memories.provideMemory("IMTRK15T2").value  = "1436"

memories.provideMemory("IMTRKMACHINE2H1").value  = "6186"
memories.provideMemory("IMTRKMACHINE2H2").value  = "6186"
memories.provideMemory("IMTRKMACHINE2T1").value  = "12795"
memories.provideMemory("IMTRKMACHINE2T2").value  = "12795"

memories.provideMemory("IMTRKMACHINE1H1").value  = "5936"
memories.provideMemory("IMTRKMACHINE1H2").value  = "5936"
memories.provideMemory("IMTRKMACHINE1T1").value  = "12545"
memories.provideMemory("IMTRKMACHINE1T2").value  = "12545"

memories.provideMemory("IMTRKEASTLEADH1").value  = "5027"
memories.provideMemory("IMTRKEASTLEADH2").value  = "5027"
memories.provideMemory("IMTRKEASTLEADT1").value  = "11619"
memories.provideMemory("IMTRKEASTLEADT2").value  = "11619"

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
spinnermodel = javax.swing.SpinnerNumberModel(0, 0, 2*13200, 1)
spinner.setModel(spinnermodel)
frame.getContentPane().add(spinner)
b = javax.swing.JButton("+20")
frame.getContentPane().add(b)
def TurnTableAdd20(event) :
    spinnermodel.value = spinnermodel.value+20
    return
b.actionPerformed = TurnTableAdd20
b = javax.swing.JButton("+5")
frame.getContentPane().add(b)
def TurnTableAdd5(event) :
    spinnermodel.value = spinnermodel.value+5
    return
b.actionPerformed = TurnTableAdd5
b = javax.swing.JButton("-5")
frame.getContentPane().add(b)
def TurnTableSub5(event) :
    spinnermodel.value = spinnermodel.value-5
    return
b.actionPerformed = TurnTableSub5
b = javax.swing.JButton("-20")
frame.getContentPane().add(b)
def TurnTableSub20(event) :
    spinnermodel.value = spinnermodel.value-20
    return
b.actionPerformed = TurnTableSub20
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
b = javax.swing.JButton("Set")
frame.getContentPane().add(b)
def TurnTableSet(event) :
    print "Set ", memories.provideMemory("IMTRKLASTMEM").value, " to ", spinnermodel.value
    memories.provideMemory(memories.provideMemory("IMTRKLASTMEM").value).value = str(spinnermodel.value)
    controller.doMove(str(spinnermodel.value))
    return
b.actionPerformed = TurnTableSet
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

