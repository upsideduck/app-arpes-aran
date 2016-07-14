from ext.nexpy.api import nexus as nx
from model.ArpesData import *
from helper.converter import Arpes2DSpectrumConverter

class SpectrumFile:

	@classmethod
	def load(self,filepath):
		data = None
		filepath = str(filepath)
		extension = filepath.split('.')[-1]
		r = (0,'',data)
		if extension == "nxs":
			try:
				loadeddata = nx.nxload(filepath,'r')
				## Check if data is ARPES, right now just load!
				if len(loadeddata.entries) != 1:		# How many entries do we have in the nexus file
					data = ArpesData(loadeddata, 0)		# Right now, just load the first one
				else:
					data = ArpesData(loadeddata)
				r = (True,str(data.title)+' loaded',data)
			except Exception, e:
				r = (False,"Error: File could not be loaded",data)
		elif extension == "sp2":
			try:
				arpes2DSpectrum = Arpes2DSpectrumConverter.SP2ToNx(filepath,rotation=float(0.0))
				root = nx.NXroot(arpes2DSpectrum.nxEntry)
				data = ArpesData(root)
				r = (True,str(data.title)+' loaded',data)
			except Exception, e:
				r = (False,"Error: File could not be loaded",data)
		elif extension == "ibw":
			try:
				arpes2DSpectrum = Arpes2DSpectrumConverter.ibwToNx(filepath,rotation=float(0.0))
				root = nx.NXroot(arpes2DSpectrum.nxEntry)
				data = ArpesData(root)
				r = (True,str(data.title)+' loaded',data)
			except Exception, e:
				r = (False,"Error: File could not be loaded",data)
		else:
			r = (False,"Error: Not a valid file",data)
		
		return r

	
