##
# Config
###
from configparser import SafeConfigParser
config = SafeConfigParser()
config.read('ini/config.ini')

CONST_ZAXIS_AVSPA = "Energy"
CONST_ZAXIS_EVSA = "Rotation angle"
CONST_ZAXIS_EVSkA = "ky"
CONST_ZAXIS_EVSPA = "Emission angle"
CONST_ZAXIS_EVSkPA = "kx"

CONST_3DPLOTTYPES = ("Emis Angle vs Rot Angle", "Emis Angle vs Energy", "Rot Angle vs Energy")
CONST_3DPLOTTYPE_EAVSRA = 0
CONST_3DPLOTTYPE_EAVSE = 1
CONST_3DPLOTTYPE_RAVSE = 2

CONST_HISTOGRAM_FIGURE = 1

R_ANGLE_COLUMN_NR = 3
CONST_TALBEHEADERS = ['File name', 'E Angle', 'Width', 'R Angle', 'High[eV]', 'Low[eV]', 'Wf[eV]' ]
CONST_AUTOCOLUMNALT = ("none",CONST_TALBEHEADERS[3])

DATA_ROOT_FOLDER = config.get('Data','DefaultFolder')
#DATA_ROOT_FOLDER = "/Users"

CONST_DATATYPE_GENERIC = 1
CONST_DATATYPE_ARPES = 2

CONST_ROI_HOR_LIST = 0
CONST_ROI_VER_LIST = 1
CONST_ROI_BOTH_LIST = 2

## Debug state on = 1 else 0
CONST_DEBUG_STATE = 0