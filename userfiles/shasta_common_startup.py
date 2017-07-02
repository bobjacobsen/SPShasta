# 
# Common startup sequence for SP Shasta
#
# Here instead of preferences to make it easier to maintain
#

import jmri
cm = jmri.InstanceManager.getDefault(jmri.ConfigureManager)

# allow substitutions from internal DTD
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/TurnOffXmlValidation.py"))

# Original composite file, replaced by refactored files
#cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:FullConfig.xml")))

cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:BasicConfig.xml")))
#cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CtcLogix.xml")))

# load scripts needed by CTC controls
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CombineSensors.py"))
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CombineTurnouts.py"))

# start with special controls
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:TurntableControls.xml")))
execfile(jmri.util.FileUtil.getExternalFilename("preference:Turntable.py"))

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
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CmriNodeStatus.xml")))

# start signal followers
execfile(jmri.util.FileUtil.getExternalFilename("program:jython/SignalFollower.py"))
SignalFollowerListener().set("CH2001","CH2001R")
SignalFollowerListener().set("CH2002","CH2002R")

execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CmriNodeMonitor.py"))

execfile(jmri.util.FileUtil.getExternalFilename("preference:SetCtcIndicators.py"))

# start web server
jmri.web.server.WebServerAction().actionPerformed(None)

# new CTC controls, done last so that turnouts are in final state
execfile(jmri.util.FileUtil.getExternalFilename("preference:CtcConfigureUssCtc.py"))

print "shasta_common_startup done"
