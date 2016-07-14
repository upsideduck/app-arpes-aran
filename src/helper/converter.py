import re
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt
from nexpy.api import nexus as nx
import os
import model.nexus_template as nxtemplate
from igor import binarywave as igorbw
from copy import *


######################################
##
##	A @spectrum parses detector data
##  into 
class Spectrum:
	nxEntry = None

	
class Arpes2DSpectrumConverter(Spectrum):
	
	@classmethod
	def SP2ToNx(self, inputfile, entryId = None ,rotation=None):
		fh = open(inputfile)
		lines = fh.readlines()
		entryname = os.path.basename(inputfile).split('.')[0]
		header = {}
		wave = []
		axes = []
	
		validFile = 0

		print "---- Start: sp2->nexus ----"
		print "Parsing: " + entryname

		#Loop through and find header data
		headerCount = 0
		for line in lines:
			#Chack if line contains information regadingdata size 
			descriptor = re.compile("^(\d+).(\d+).(\d+)$",re.IGNORECASE)
			headerdata1 = re.compile("(?<=#\s)(\w+)\s+\=\s+(-?\d*\.?\d*)\s+(-?\d*\.?\d*)\s+#\s+\[(\w+)\]",re.IGNORECASE)
			headerdata2 = re.compile('(?<=#\s)(\w+)\s+\=\s+(\"(\w+)\"|\d+)',re.IGNORECASE)
			rd = descriptor.search(line)
			rhd1 = headerdata1.search(line)
			rhd2 = headerdata2.search(line)
			if rhd1:
				headerData = rhd1.groups()
				if len(headerData) > 1:
					header[headerData[0]] = [headerData[i] for i in range(1,len(headerData))]
				headerCount += 1
			elif rhd2:
				headerData = rhd2.groups()
				header[headerData[0]] = headerData[1]
				headerCount += 1
			elif line[0] == "#":
				headerCount += 1
			elif line.strip() == "P2":
				validFile = 1
				headerCount += 1
			elif rd:
				dataDescriptors = rd.groups()
				headerCount += 1
				break
			else:
				break

		#Check if file valid and header and data size found
		if validFile and len(header) > 0 and len(dataDescriptors) > 0:
			print "File seems valid"
		else:
			print "File not valid"
			return -1

		print "Exporting  corrected image"
		#Corrected image
		rowsC = int(dataDescriptors[1])
		columnsC = int(dataDescriptors[0])
		corrBuffer = lines[headerCount:rowsC*columnsC+headerCount]
		correctedWave = Arpes2DSpectrumConverter.__dataMatrix(corrBuffer,rowsC,columnsC)

		#Check if RAW data available, then load it
		# if lines[rowsC*columnsC+headerCount].strip() == "P2":
		# 	r = descriptor.search(lines[rowsC*columnsC+headerCount+1])
		# 	dataDescriptors = r.groups()
		# 	rowsR = int(dataDescriptors[1])
		# 	columnsR = int(dataDescriptors[0])
		# 	rawBuffer = lines[headerCount+rowsC*columnsC+2:rowsC*columnsC+rowsR*columnsR+headerCount+2]		#2 is for the extra "P2" and datadescriptors for the raw data
		# 	rawWave = self.__dataMatrix(rawBuffer,rowsR,columnsR)

		#fig = plt.figure()
		#ax1 = fig.add_subplot(211)
		#ax1.set_title('Corrected image')
		#ax1.imshow(correctedWave,extent=[float(header["ERange"][0]),float(header["ERange"][1]),float(header["aRange"][0]),float(header["aRange"][1])],aspect='auto')
		#ax2 = fig.add_subplot(212)
		#ax2.set_title('Raw image')
		#ax2.imshow(rawWave,aspect='auto')
		#plt.show()
		wave = correctedWave
		axes = [[float(header["aRange"][0]) + (float(header["aRange"][1])-float(header["aRange"][0]))/(rowsC-1)*i for i in range(0,rowsC)],[float(header["ERange"][0]) + (float(header["ERange"][1])-float(header["ERange"][0]))/(columnsC-1)*i for i in range(0,columnsC)]]

		print "Create nexus format"
		#Nexus format
		if(entryId == None):
			entry = nxtemplate.arpes('entry1')
		else:
			entry = nxtemplate.arpes(entryId)

		entry.title = entryname
		#Meta data
		entry.instrument.analyser.pass_energy = header["Ep"][0]
		entry.instrument.analyser.pass_energy.units = header["Ep"][2]
		entry.instrument.analyser.lens_mode = header["lensmode"]
		entry.instrument.analyser.kinetic_energy = header["Ek"][0]
		entry.instrument.analyser.kinetic_energy.units = header["Ek"][2]
		entry.instrument.manipulator.rangle = rotation
		entry.instrument.manipulator.rangle.units = 'deg'

		#Data
		data = nx.NXfield(wave, name='data')
		energies = nx.NXfield(axes[1],units=header["ERange"][2],name='energies')
		angles = nx.NXfield(axes[0],units=header["aRange"][2],name='angles')
		entry.analyser = nx.NXdata(data,(angles,energies))

		print "Done with "+entryname
		self.nxEntry = entry
		print "---- End: sp2->nexus ------"
		return self

	@staticmethod
	def __dataMatrix(listOfValues, rows, columns):
		#Clean Corrected buffer
		buff = [int(line.strip()) for line in listOfValues]
		#Create array from data
		#wave = np.asarray(buff[0:columns])
		#for i in range(1,rows):
		#	wave = np.vstack((wave,np.asarray(buff[i*columns:i*columns+columns])))
		wave = np.asarray(buff)
		wave = wave.reshape(rows,columns)
		return wave

	@classmethod
	def ibwToNx(self, inputfile, entryId = None ,rotation=None):
		filecontent = igorbw.load(inputfile)
		filename = os.path.basename(inputfile).split('.')[0]
		header = {}
		entryname = None
		wave = []
		axes = []

		print "---- Start: ibw->nexus ----"
		print "Parsing: " + filename

		#Loop through and find header data
		entryname = filecontent['wave']['wave_header']['bname']
		wave = np.asarray(copy(filecontent['wave']['wData']))

		note = filecontent['wave']['note']
		noteList = [x.split('=') for x in note.split('\r')]
		noteList = [x for x in noteList if len(x) == 2]
		noteDict = dict(noteList)


		#Check if file is loaded correctly
		if entryname and len(wave.shape) == 2:
			print "File seems valid"
		else:
			print "File not valid"
			return -1

		axesSteps = filecontent['wave']['wave_header']['sfA']
		axesInit = filecontent['wave']['wave_header']['sfB']
		axesDim = filecontent['wave']['wave_header']['nDim']
		axesUnits = filecontent['wave']['wave_header']['dimUnits']

		axes = [np.linspace(axesInit[0],axesDim[0]*axesSteps[0]+axesInit[0],axesDim[0]), np.linspace(axesInit[1],axesDim[1]*axesSteps[1]+axesInit[1],axesDim[1])]
		units = [''.join(axesUnits[0]),''.join(axesUnits[1])]

		print "Create nexus format"
		#Nexus format
		if(entryId == None):
			entry = nxtemplate.arpes('entry1')
		else:
			entry = nxtemplate.arpes(entryId)

		entry.title = entryname
		#Meta data
		if 'Ep' in noteDict:
			entry.instrument.analyser.pass_energy = noteDict['Ep']
			entry.instrument.analyser.pass_energy.units = 'eV'
		if 'LensMode' in noteDict:
			entry.instrument.analyser.lens_mode = noteDict["LensMode"].strip('\x00')
		if 'Ek' in noteDict:
			entry.instrument.analyser.kinetic_energy = noteDict["Ek"]
			entry.instrument.analyser.kinetic_energy.units = 'eV'
		#entry.instrument.manipulator.rangle = rotation
		#entry.instrument.manipulator.rangle.units = 'deg'


		if int(wave.shape[0]) == len(axes[0]) and int(wave.shape[1]) == len(axes[1]):
			wave = wave.transpose()

		#Data
		data = nx.NXfield(wave, name='data')
		energies = nx.NXfield(axes[0],units=units[0],name='energies')
		angles = nx.NXfield(axes[1],units=units[1],name='angles')
		entry.analyser = nx.NXdata(data,(angles,energies))

		print "Done with "+entryname
		self.nxEntry = entry
		print "---- End: ibw->nexus ------"
		return self


class Arpes3DSpectrumConverter(Spectrum):

	@classmethod
	def listOfEntriesToNx(self,listOfArpesEntries):
		nxEntry = nxtemplate.arpes('entry1')
		data = nx.NXfield(np.array([]),name='data')
		energies = nx.NXfield(units='eV',name='energies')
		angles = nx.NXfield(units='deg',name='angles')
		rangles = nx.NXfield(units='deg',name='rangles')
		nxEntry.analyser = nx.NXdata(data,(rangles,angles,energies))
		olddata = []

		# Add first entry manualy
		nrOfEntries = len(listOfArpesEntries)
		entry = listOfArpesEntries[0]
		nxEntry.title = "fermisurface"
		data = nx.NXfield([np.asarray(entry.analyser.data)],name='data')
		energies = entry.analyser.energies
		angles = entry.analyser.angles
		rangles = nx.NXfield([np.array(entry.instrument.manipulator.rangle)],units='deg',name='rangles')
		nxEntry.analyser = nx.NXdata(data,(rangles,angles,energies))

		# loop through the rest of the files
		for idx in range (1,nrOfEntries):
			entry = listOfArpesEntries[idx]
			olddata = np.asarray(nxEntry.analyser.data)
			nxEntry.analyser.data = nx.NXfield(np.append(olddata,[np.asarray(entry.analyser.data)],axis=0))
			nxEntry.analyser.rangles = nx.NXfield(np.append(np.asarray(nxEntry.analyser.rangles),entry.instrument.manipulator.rangle),units='deg',name='rangles')	


		self.nxEntry = nxEntry
		return self

	def DA30ZipToNx(self,pathZipFile):
		pass