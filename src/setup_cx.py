import sys
from cx_Freeze import setup, Executable

#####
## NOTES:
#	
#	def load_h5py(finder, module):
# 		"""h5py module has a number of implicit imports"""
#		finder.IncludeModule('h5py.defs')
# 		finder.IncludeModule('h5py.utils')
# 		finder.IncludeModule('h5py._proxy')
# 		try:
# 		   finder.IncludeModule('h5py._errors')
# 		   finder.IncludeModule('h5py.h5ac')
# 		except:
# 		   pass
# 		try:
# 		   finder.IncludeModule('h5py.api_gen')
# 		except:
# 		   pass
#
#	ADDED TO CX_FREEZE hooks.py
#	----------------------------------------------------------
#	
#	def _find_pyopencl_include_path():
# 		from pkg_resources import Requirement, resource_filename
#    	return ''
#    	#return resource_filename(Requirement.parse("pyopencl"), "pyopencl/cl")
#	
#	return '' in pyopencl __init__.py	

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["h5py","pyopencl","OpenGL","pyqtgraph","pytools"], 
					 "excludes": ["tkinter","collections.abc"],
				"include_files": ["cl/","ini/"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "ARAN",
        version = "0.5",
        description = "ARPES data analysis",
        options = {"build_exe": build_exe_options},
        executables = [Executable("ARAN.py", base=base)])
