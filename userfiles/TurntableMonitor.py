class MyListener(java.beans.PropertyChangeListener):
  def propertyChange(self, event):
    print
    print "change",event.propertyName, "from", event.oldValue, "to", event.newValue
    print "source systemName", event.source.systemName, "userName", event.source.userName

m = MyListener()
#turnouts.getTurnout("CT2034").addPropertyChangeListener(m)
sensors.getSensor("CS2001").addPropertyChangeListener(m)
sensors.getSensor("CS2002").addPropertyChangeListener(m)
sensors.getSensor("CS2003").addPropertyChangeListener(m)
sensors.getSensor("CS2004").addPropertyChangeListener(m)
sensors.getSensor("CS2005").addPropertyChangeListener(m)
sensors.getSensor("CS2006").addPropertyChangeListener(m)
sensors.getSensor("CS2007").addPropertyChangeListener(m)
sensors.getSensor("CS2008").addPropertyChangeListener(m)
sensors.getSensor("CS2009").addPropertyChangeListener(m)
sensors.getSensor("CS2010").addPropertyChangeListener(m)
sensors.getSensor("CS2011").addPropertyChangeListener(m)
sensors.getSensor("CS2012").addPropertyChangeListener(m)
sensors.getSensor("CS2013").addPropertyChangeListener(m)
sensors.getSensor("CS2014").addPropertyChangeListener(m)
sensors.getSensor("CS2015").addPropertyChangeListener(m)
sensors.getSensor("CS2016").addPropertyChangeListener(m)
sensors.getSensor("CS2017").addPropertyChangeListener(m)
sensors.getSensor("CS2018").addPropertyChangeListener(m)
sensors.getSensor("CS2019").addPropertyChangeListener(m)
sensors.getSensor("CS2020").addPropertyChangeListener(m)
sensors.getSensor("CS2021").addPropertyChangeListener(m)
sensors.getSensor("CS2022").addPropertyChangeListener(m)
sensors.getSensor("CS2023").addPropertyChangeListener(m)
sensors.getSensor("CS2024").addPropertyChangeListener(m)