# 
# Common startup sequence for SP Shasta
#
# Here instead of preferences to make it easier to maintain
#

import jmri

cm = jmri.InstanceManager.getDefault(jmri.ConfigureManager)

execfile(jmri.util.FileUtil.getExternalFilename("program:jython/TurnOffXmlValidation.py"))

cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:FullConfig.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CtcModeControl.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:CmriNodeStatus.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:SignalMastControls.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:MtShastaCrossingPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLWpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLYpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:GLEpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:BWpanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:LeftPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:MidPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:OperatorPanel.xml")))
cm.load(java.io.File(jmri.util.FileUtil.getExternalFilename("preference:TurntableControls.xml")))

execfile(jmri.util.FileUtil.getExternalFilename("program:jython/SignalFollower.py"))
SignalFollowerListener().set("CH2001","CH2001R")
SignalFollowerListener().set("CH2002","CH2002R")

execfile(jmri.util.FileUtil.getExternalFilename("program:jython/CmriNodeMonitor.py"))

execfile(jmri.util.FileUtil.getExternalFilename("preference:Turntable.py"))

execfile(jmri.util.FileUtil.getExternalFilename("preference:CtcDebugInit.py"))
execfile(jmri.util.FileUtil.getExternalFilename("preference:SetCtcIndicators.py"))

print "shasta_common_startup done"