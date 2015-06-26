from nexpy.api import nexus as nx
import model.nexus_template
from helper.spectrum import sp2
from helper.spectrum import fermisurface
import glob
import copy
import numpy as np

if __name__ == '__main__':
    # sp2file = nximporter.sp2("test.sp2")
    # (result,entry) = sp2file.parse()
    # root = nx.NXroot(entry)
    # root.save('test.nxs')
	# print root.tree
	files = glob.glob('./data/*.sp2')
	

	i = 1
	entities = []
	for thefile in files:
		print "-----------------------------------"
		entry = None
		root = None
		entryid = "entry"+str(i)
		sp2file = sp2(thefile)
		result = sp2file.parseToNx(rotation=0.25*i)
		entities.append(sp2file.nxEntry)
		i += 1
		root = nx.NXroot(copy.deepcopy(sp2file.nxEntry))
		root.save('./data/test2/'+entryid+'.nxs')
		del root
	print "-----------------------------------"


	print "Parsing fermisurface"
	fermisurface = fermisurface()
	result = fermisurface.parseListOfEntriesToNx(entities)
	print "Fermisurface done"
	
	root = nx.NXroot(fermisurface.nxEntry)
	root.save('./data/test2/fermisurface.nxs')
	print root.tree

