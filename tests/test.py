from nexpy.api import nexus as nx
import model.nexus_template
from helper.converter import Arpes2DSpectrumConverter
from helper.converter import Arpes3DSpectrumConverter
import glob
import copy
import numpy as np


if __name__ == '__main__':
    # sp2file = nximporter.sp2("test.sp2")
    # (result,entry) = sp2file.parse()
    # root = nx.NXroot(entry)
    # root.save('test.nxs')
	# print root.tree
	files = glob.glob('./data/test2/*.sp2')
	

	i = 1
	entities = []
	for thefile in files:
		print "-----------------------------------"
		entry = None
		root = None
		entryid = "entry"+str(i)
		arpes2DSpectrum = Arpes2DSpectrumConverter.SP2ToNx(thefile,rotation=float(0.25*i))
		entities.append(arpes2DSpectrum.nxEntry)
		i += 1
		root = nx.NXroot(copy.deepcopy(arpes2DSpectrum.nxEntry))
		root.save('./data/test2/'+entryid+'.nxs')
		del root
	print "-----------------------------------"


	print "Parsing fermisurface"
	fermiSurfaceEntry = Arpes3DSpectrumConverter.listOfEntriesToNx(entities)
	root = nx.NXroot(fermiSurfaceEntry.nxEntry)
	print "Fermisurface done"
	root.save('./data/test2/fermisurface.nxs')
	print root.tree

