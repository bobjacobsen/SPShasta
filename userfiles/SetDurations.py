# set timings
print "SetDurations setting timings"

jmri.implementation.AbstractTurnout.DELAYED_FEEDBACK_INTERVAL = 5000  # turnout throw time
print "Turnout throw delay: ", jmri.implementation.AbstractTurnout.DELAYED_FEEDBACK_INTERVAL/1000., "seconds"

jmri.jmrit.ussctc.CodeLine.CODE_SEND_DELAY = 3000
print "Code send delay: ", jmri.jmrit.ussctc.CodeLine.CODE_SEND_DELAY/1000., "seconds"

# jmri.jmrit.ussctc.CodeLine.START_PULSE_LENGTH left alone at 500 msec
# jmri.jmrit.ussctc.CodeLine.INTER_INDICATION_DELAY left alone at 500 msec

jmri.jmrit.ussctc.SignalHeadSection.MOVEMENT_DELAY = 5000
print"Signal movement delay: ", jmri.jmrit.ussctc.SignalHeadSection.MOVEMENT_DELAY/1000., "seconds"

jmri.jmrit.ussctc.SignalHeadSection.DEFAULT_RUN_TIME_LENGTH = 5000
memories.getMemory("IMUSS CTC:SIGNALHEADSECTION:1:TIME").setValue(jmri.jmrit.ussctc.SignalHeadSection.DEFAULT_RUN_TIME_LENGTH)
print "Running time for", jmri.jmrit.ussctc.SignalHeadSection.DEFAULT_RUN_TIME_LENGTH/1000., "seconds"

print "SetDurations done"
