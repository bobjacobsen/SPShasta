# SPShasta
Configuration information for the [SP Shasta model railroad](http://www.spshastaroute.org/).

The railroad uses [JMRI](http://jmri.org) for controls, see their [SP Shasta page](http://jmri.org/community/examples/SPShasta.shtml).

## Files
profiles - profiles for various startup conditions

userfiles/shasta_common_startup.py - controls all the program configuration

BasicConfig.xml - configuration information, but not panels, for the control system

BWpanel.xml - animated track schematic of layout
LeftPanel.xml - Levers and lamps on left CTC panel
MidPanel.xml - Levers and lamps on middle CTC panel

Turntable.py - Controls power to the turntable tail tracks, positions the turntable in response to buttons
TurntableControls.xml - panel for configuring turntable ops, settings

SetCtcIndicates.py.txt - initial powerup for the CTC machine

CtcDebugInit.py - sets inputs for when running without real layout, machine present

## Additional older/obsolete files:

LowerXOverPanel.xml - A debugging panel that shows some signals near the lower Dunsmuir crossover, this is only temporary

TurntableMonitor.py - print a message when any of the turntable inputs change

LeftWing.xml - screen panel for the left part of the CTC machine; uses LeftBackground.gif as background

