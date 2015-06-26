from GenericData import *

class ArpesData(GenericData):

	# Original data
	root = None
	# k-space data
	kdata = None
	krotation = None
	k = None
	# angle-space data
	adata = None
	arotation = None
	a = None
	E = None

	# Misc
	vmin = 0
	vmax = 1
	thread = None
	createMapWorker = None

	def __init__(self, nxRoot):
		super(ArpesData, self).__init__(nxRoot)
		self.root = nxRoot
		self.adata = self.root.entry1.analyser.data
		self.E = self.root.entry1.analyser.energies
		self.a = self.root.entry1.analyser.angles
		if len(self.adata.shape) == 3:
			self.arotation = self.root.entry1.analyser.rangles
		else:
			self.arotation = None

		vmin_index = np.unravel_index(nxRoot.entry1.analyser.data.argmin(), nxRoot.entry1.analyser.data.shape)
		self.vmin = int(nxRoot.entry1.analyser.data[vmin_index])
		vmax_index = np.unravel_index(nxRoot.entry1.analyser.data.argmax(), nxRoot.entry1.analyser.data.shape)
		self.vmax = int(nxRoot.entry1.analyser.data[vmax_index])
		self.setAngleSpace()

	def setAngleSpace(self):
		self.axis1 = self.E
		self.axis2 = self.a
		if len(self.adata.shape) == 3:
			self.axis3 = self.arotation
		else:
			self.axis3 = None
		self.axis1name = CONST_ZAXIS_AVSPA
		self.axis2name = CONST_ZAXIS_EVSPA
		self.axis3name = CONST_ZAXIS_EVSA
		self.title = self.root.entry1.title
		self.data = self.adata		# Last since it will emit updated data signal

	def setkSpace(self):
		self.axis1 = self.E
		self.axis2 = self.k
		if len(self.kdata.shape) == 3:
			self.axis3 = self.krotation
		else:
			self.axis3 = None
		self.axis1ame = CONST_ZAXIS_AVSPA
		self.axis2name = CONST_ZAXIS_EVSkPA
		self.axis3name = CONST_ZAXIS_EVSkA
		self.title = self.root.entry1.title
		self.data = self.kdata 			# Last since it will emit updated data signal



class MakeMapWorker(QtCore.QObject):

	progress = QtCore.Signal(float)
	finished = QtCore.Signal(tuple)
 	energy = None
 	angle = None
 	pangle = None
 	data = None


 	def __init__(self,root):
 		super(MakeMapWorker, self).__init__()
 		self.energy = root.entry1.analyser.energies
 		self.angle = root.entry1.analyser.angles
 		self.data = root.entry1.analyser.data
 		if len(root.entry1.analyser.data.shape) == 3:
 			self.pangle = root.entry1.analyser.rangles
		
	@QtCore.Slot()
	def makekMapFrom2D(self):
		k,kdata_out = self.makekMap(np.asarray(self.energy),np.asarray(self.angle),np.asarray(self.data))
		self.finished.emit((k,None,kdata_out))

	@QtCore.Slot()
	def makekMapFrom3D(self):
		k = None
		krotation = None
		kdata= None
		kdata1 = None
		kdata2 = None
		totalIterations = len(self.pangle) + len(self.angle)
		currentIteration = 0.0
		self.progress.emit(currentIteration/totalIterations)
		kdata = np.copy(np.asarray(self.data))
		# Angular direction
		for i in range(0,len(self.pangle)):
			k,kdata_out = self.makekMap(np.asarray(self.energy),np.asarray(self.angle),np.asarray(self.data[i,:,:]))
			kdata[i,:,:] = kdata_out
			currentIteration += 1
			self.progress.emit(currentIteration/totalIterations)
		# rotation angle direction
		for i in range(0,len(self.angle)):
			krotation,kdata_out = self.makekMap(np.asarray(self.energy),np.asarray(self.pangle),np.asarray(kdata[:,i,:]))
			kdata[:,i,:] = kdata_out
			currentIteration += 1
			self.progress.emit(currentIteration/totalIterations)
		self.finished.emit((k,krotation,kdata))


	def makekMap(self,energy,angle,data):
		E_min = energy.min()
		E_max = energy.max()
		E_delta =(np.diff(energy))[0]
		E_len = len(energy)
			
		A_min = angle.min()
		A_max = angle.max()
		A_delta = (np.diff(angle))[0]
		A_len = len(angle)

		datak = np.zeros_like(data)
		kindex = np.zeros_like(data)

		k_min = 0.512 * np.sqrt(E_max) * np.sin(A_min * np.pi/180)
		k_max = 0.512 * np.sqrt(E_max) * np.sin(A_max * np.pi/180)
		#k_delta = (k_max - k_min) / (A_len - 1)
		k = np.linspace(k_min,k_max,A_len)
		
		for i in range(0,E_len):
			E = energy[i]
			#print E
			A = np.arcsin( k / 0.512 / np.sqrt(E) ) * 180/np.pi
			
			low_values_indices = A < A_min  # Where values are low
			high_values_indices = A > A_max  # Where values are high
			A[low_values_indices] = A_min
			A[high_values_indices] = A_min
			
			Aindex = np.round(np.abs(A - A_min)/A_delta)
			Aindex = Aindex.astype(int)

			data[0,:] = 0
			kindex[:,i] = Aindex
			if np.count_nonzero(datak[:,i]) > 0:
				datak[:,i] = (datak[:,i] + data[Aindex,i])/2
			else:
				datak[:,i] = data[Aindex,i]
		return (k,datak)