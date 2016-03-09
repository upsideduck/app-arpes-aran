from GenericData import *
import pyopencl as cl
import os


class ArpesData(GenericData):

	# k-space data
	kdata = None
	ky = None
	kx = None
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
	dataType = CONST_DATATYPE_ARPES

	def __init__(self, nxRoot, entryId = 0):
		super(ArpesData, self).__init__(nxRoot, entryId)
		self.reinitializeData()

	def reinitializeData(self):
		super(ArpesData, self).reinitializeData()
		self.adata = self.root.NXentry[self.entryId].analyser.data
		self.E = self.root.NXentry[self.entryId].analyser.energies
		self.a = self.root.NXentry[self.entryId].analyser.angles
		if len(self.adata.shape) == 3:
			self.arotation = self.root.NXentry[self.entryId].analyser.rangles
		else:
			self.arotation = None

		vmin_index = np.unravel_index(self.root.NXentry[self.entryId].analyser.data.argmin(), self.root.NXentry[self.entryId].analyser.data.shape)
		self.vmin = int(self.root.NXentry[self.entryId].analyser.data[vmin_index])
		vmax_index = np.unravel_index(self.root.NXentry[self.entryId].analyser.data.argmax(), self.root.NXentry[self.entryId].analyser.data.shape)
		self.vmax = int(self.root.NXentry[self.entryId].analyser.data[vmax_index])
		self.setAngleSpace()

	def setAngleSpace(self):
		if len(self.adata.shape) == 2:
			self.axis1 = self.a
			self.axis2 = self.E
			self.axis3 = None
			self.axis1name = CONST_ZAXIS_EVSPA
			self.axis2name = CONST_ZAXIS_AVSPA
			self.axis3name = None
		elif len(self.adata.shape) == 3:
			self.axis1 = self.arotation
			self.axis2 = self.a
			self.axis3 = self.E
			self.axis1name = CONST_ZAXIS_EVSA
			self.axis2name = CONST_ZAXIS_EVSPA
			self.axis3name = CONST_ZAXIS_AVSPA
		
		self.title = self.root.NXentry[self.entryId].title
		self.data = self.adata		# Last since it will emit updated data signal

	def setkSpace(self):
		if len(self.kdata.shape) == 2:
			self.axis1 = self.a
			self.axis2 = self.E
			self.axis3 = None
			self.axis1name = CONST_ZAXIS_EVSPA
			self.axis2name = CONST_ZAXIS_AVSPA
			self.axis3name = None
		elif len(self.adata.shape) == 3:
			self.axis1 = self.ky
			self.axis2 = self.kx
			self.axis3 = self.E
			self.axis1name = CONST_ZAXIS_EVSkA
			self.axis2name = CONST_ZAXIS_EVSkPA
			self.axis3name = CONST_ZAXIS_AVSPA
		self.title = self.root.NXentry[self.entryId].title
		self.data = self.kdata 			# Last since it will emit updated data signal



class MakeMapWorker(QtCore.QObject):

	progress = QtCore.Signal(float)
	finished = QtCore.Signal(tuple)
 	energy = None
 	angle = None
 	rangle = None
 	data = None

 	entryId = 0

 	def __init__(self,root):
 		super(MakeMapWorker, self).__init__()
 		self.energy = root.NXentry[self.entryId].analyser.energies
 		self.angle = root.NXentry[self.entryId].analyser.angles
 		self.data = root.NXentry[self.entryId].analyser.data
 		if len(root.NXentry[self.entryId].analyser.data.shape) == 3:
 			self.rangle = root.NXentry[self.entryId].analyser.rangles
		
	@QtCore.Slot()
	def makekMapFrom2D(self):
		k,kdata_out = self.makekMap(np.asarray(self.energy),np.asarray(self.angle),np.asarray(self.data))
		self.finished.emit((k,None,kdata_out))

	# @QtCore.Slot()
	# def makekMapFrom3D(self):
	# 	k = None
	# 	krotation = None
	# 	kdata= None
	# 	kdata1 = None
	# 	kdata2 = None
	# 	totalIterations = len(self.pangle) + len(self.angle)
	# 	currentIteration = 0.0
	# 	self.progress.emit(currentIteration/totalIterations)
	# 	kdata = np.copy(np.asarray(self.data))
	# 	# Angular direction
	# 	for i in range(0,len(self.pangle)):
	# 		k,kdata_out = self.makekMap(np.asarray(self.energy),np.asarray(self.angle),np.asarray(self.data[i,:,:]))
	# 		kdata[i,:,:] = kdata_out
	# 		currentIteration += 1
	# 		self.progress.emit(currentIteration/totalIterations)
	# 	# rotation angle direction
	# 	for i in range(0,len(self.angle)):
	# 		krotation,kdata_out = self.makekMap(np.asarray(self.energy),np.asarray(self.pangle),np.asarray(kdata[:,i,:]))
	# 		kdata[:,i,:] = kdata_out
	# 		currentIteration += 1
	# 		self.progress.emit(currentIteration/totalIterations)
	# 	self.finished.emit((k,krotation,kdata))

	@QtCore.Slot()
	def makekMapFrom3D(self):
		kx = None
		ky = None
		kdata = None
		totalIterations = 1
		currentEnergyIteration = 0.0

		A_min = self.angle.min()
		A_max = self.angle.max()
		AR_min = self.rangle.min()
		AR_max = self.rangle.max()
		E_min = self.energy.min()
		E_max = self.energy.max()

		## Calculate axes

		if A_min > 0: 
			A_zero1 = A_min
		else:
			if A_max < 0:
				A_zero1 = A_max
			else:
				A_zero1 = 0
		

		if A_min >=0:
			A_zero2 = A_max
		else:
			if A_max < 0:
				A_zero2 = A_min
			else:
				if A_max > -A_min:
					A_zero2 = A_max
				else:
					A_zero2 = A_min
		
		kx1 = 0.512*np.sqrt(E_max)*np.sin(A_min*np.pi/180)
		kx2 = 0.512*np.sqrt(E_max)*np.sin(A_max*np.pi/180)

		if AR_max >= 0:
			ky2 = 0.512*np.sqrt(E_max)*np.sin(AR_max*np.pi/180)*np.cos(A_zero1*np.pi/180)
		else:
			ky2 = 0.512*np.sqrt(E_min)*np.sin(AR_max*np.pi/180)*np.cos(A_zero2*np.pi/180)
		

		if AR_min >= 0:
			ky1 = 0.512*np.sqrt(E_min)*np.sin(AR_min*np.pi/180)*np.cos(A_zero1*np.pi/180)
		else:
			ky1 = 0.512*np.sqrt(E_max)*np.sin(AR_min*np.pi/180)*np.cos(A_zero2*np.pi/180)	

		kx = np.linspace(kx1,kx2,len(self.angle))
		ky = np.linspace(ky1,ky2,len(self.rangle))

		kdata = np.zeros((len(ky),len(kx),len(self.energy)))
		## Transform to k-space
		energy1 =  float(self.energy[0])
		#energy2 = PE-WF+ energy1 - KF
		energy2 = energy1
		#C1 = 1/(0.512*np.sqrt(energy2))
		C2 = 180/np.pi

		n_max = len(kx)-1
		m_max = len(ky)-1

		k_n0 = float(kx[0])
		k_m0 = float(ky[0])

		delta_k_n = float(kx[1]-kx[0])
		delta_k_m = float(ky[1]-ky[0])

		i_max = len(kx)-1
		j_max = len(ky)-1

		phi0 = float(self.angle[0])
		theta0 = float(self.rangle[0])

		delta_phi = float(self.angle[1]-self.angle[0])
		delta_theta = float(self.rangle[1]-self.rangle[0])
		os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'
		currentEnergyIteration = 0.0
		totalIterations = len(self.energy)

		self.ctx = cl.create_some_context()
		self.queue = cl.CommandQueue(self.ctx, properties=cl.command_queue_properties.PROFILING_ENABLE,)			
		
		f = open('model/kxky.cl', 'r')
		fstr = "".join(f.readlines())
		self.program = cl.Program(self.ctx, fstr).build()
		mf = cl.mem_flags

		for e in range(0,len(self.energy)):
			E = self.energy[e]
			C1 = 1/(0.512*np.sqrt(float(E)))
			inputArr = np.zeros(self.data[:,:,e].shape, dtype=np.float32)
			inputArr = self.data[:,:,e].astype(np.float32)

			outputArr = np.zeros((inputArr.shape[0],inputArr.shape[1]), dtype=np.float32) 


			input_buf = cl.Buffer(self.ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=inputArr)
			output_buf = cl.Buffer(self.ctx, mf.WRITE_ONLY, outputArr.nbytes)
			self.program.kxky(self.queue, outputArr.shape, None, np.float32(k_n0), np.float32(k_m0), np.float32(delta_k_n), np.float32(delta_k_m), np.float32(C1), np.float32(C2), np.float32(phi0), np.float32(theta0), np.float32(delta_phi), np.float32(delta_theta), np.int32(j_max), np.int32(i_max), input_buf, output_buf)
			#self.program.kxkytest(self.queue, outputArr.shape, None, input_buf, output_buf)
			cl.enqueue_read_buffer(self.queue, output_buf, outputArr).wait()
			kdata[:,:,e] = outputArr
			

		self.finished.emit((kx,ky,kdata))

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