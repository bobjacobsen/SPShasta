#
# Common startup sequence for SP Shasta
#
# Here instead of preferences to make it easier to maintain
#

import java
import java.io

import jmri
cm = jmri.InstanceManager.getDefault(jmri.ConfigureManager)

# allow substitutions from internal DTD
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/TurnOffXmlValidation.py"))

# set DELAYED Turnouts to operate faster at start
jmri.implementation.AbstractTurnout.DELAYED_FEEDBACK_INTERVAL = 100

# Original composite file, replaced by refactored files
#cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:FullConfig.xml")))

cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:BasicConfig.xml")))
# Logix for CTC, replaced by ussctc package in CtcConfigureUssCtc.py
#cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CtcLogix.xml")))

# load scripts needed by CTC controls
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CombineSensors.py"))
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CombineTurnouts.py"))
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/SensorGroupAutoItem.py"))
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/SignalFollower.py"))

# start with Turntable controls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:TurntableControls.xml")))
execfile(jmri.util.FileUtil.getExternalFilename("preference:Turntable.py"))

# add layout controls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:SignalMastControls.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:MtShastaCrossingPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLWpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLYpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLEpanel.xml")))

# CTC displays
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:LeftPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:MidPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:BWpanel.xml")))

# cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CtcModeControl.xml"))) # Not doing anything now

# Show configuration not complete in status memory on panels
memories.getMemory("IMUSS CTC:CODELINE:1:LOG").setValue('Configuration still running')

# BBop display
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:OperatorPanel.xml")))

# Helix panel controls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:HelixPanelLogic.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:HelixInnerPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:HelixOuterPanel.xml")))

# Weed staging control
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:WeedStagingThroat.xml")))

# C/MRI controls
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CmriNodeTool.py"))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CmriNodeStatus.xml")))
# turn off node 9
memo = jmri.InstanceManager.getList(jmri.jmrix.cmri.CMRISystemConnectionMemo).get(0)
memo.getNodeFromSystemName("CS9001", memo.getTrafficController()).setSensorsActive(False)
# start driving sensors from C/MRI status
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CmriNodeMonitor.py"))

# bring up rest of layout controls - this delays before operating
execfile(jmri.util.FileUtil.getExternalFilename("preference:ConfigureLayoutLogic.py"))

# add the APB signals MtShasta to KFalls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:APB.xml")))

# open the clock control windows
jmri.jmrit.simpleclock.SimpleClockAction().actionPerformed(None)
jmri.jmrix.nce.clockmon.ClockMonPanel.Default().actionPerformed(None)

# start web server
jmri.web.server.WebServerAction().actionPerformed(None)

# new CTC controls, done last so that turnouts are in final state  - this delays before operating
execfile(jmri.util.FileUtil.getExternalFilename("preference:ConfigureCtcControlLogic.py"))

# add a diagnostic switchboard - comment out most of the time, just for diagnostics
# cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CTC_switchpanel.xml")))


print "shasta_common_startup done"
