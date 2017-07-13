# 
# Common startup sequence for SP Shasta
#
# Here instead of preferences to make it easier to maintain
#

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

# load scripts needed by CTC controls
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CombineSensors.py"))

# start with Turntable controls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:TurntableControls.xml")))
execfile(jmri.util.FileUtil.getExternalFilename("preference:Turntable.py"))

# add layout controls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:SignalMastControls.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:MtShastaCrossingPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLWpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLYpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLEpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:LeftPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:MidPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:OperatorPanel.xml")))

cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:BWpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CtcModeControl.xml")))

# C/MRI controls
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CmriNodeTool.py"))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CmriNodeStatus.xml")))

# Show configuration not complete in status memory on panels
memories.getMemory("IMUSS CTC:CODELINE:1:LOG").setValue('Configuration still running')

# start driving sensors from C/MRI status
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CmriNodeMonitor.py"))

execfile(jmri.util.FileUtil.getExternalFilename("preference:ConfigureLayoutLogic.py"))

# start web server
jmri.web.server.WebServerAction().actionPerformed(None)

# new CTC controls, done last so that turnouts are in final state
execfile(jmri.util.FileUtil.getExternalFilename("preference:ConfigureCtcControlLogic.py"))

print "shasta_common_startup done"
