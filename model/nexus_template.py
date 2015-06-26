from nexpy.api import nexus as nx

def arpes(entryName):
	#Create NeXus object
	entry = nx.NXentry(name=entryName)
	entry.instrument = nx.NXinstrument(nx.NXdetector(name='analyser'),nx.NXmonochromator(name='monochromator'),nx.NXgroup(name='manipulator'))
	entry.instrument.analyser.pass_energy = nx.NXfield(units='')
	entry.instrument.analyser.lens_mode = nx.NXfield()
	entry.instrument.analyser.kinetic_energy = nx.NXfield(units='')
	entry.instrument.manipulator.rangle = nx.NXfield(units='')

	data = nx.NXfield(name='data')
	entry.analyser = nx.NXdata(data)

	return entry