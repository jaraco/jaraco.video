from comtypes import GUID, COMMETHOD
from comtypes.client import GetModule
from comtypes import CoClass, IUnknown
from ctypes import POINTER, Structure, c_longlong, c_long, HRESULT
from ctypes.wintypes import (RECT, DWORD, LONG, WORD, ULONG, HWND,
	UINT, LPCOLESTR, LCID, LPVOID)
from ctypes import windll

from comtypes.gen.DirectShowLib import (FilterGraph, CaptureGraphBuilder2,
	ICreateDevEnum, typelib_path, IBaseFilter, IBindCtx, IMoniker,
	IAMStreamConfig, IAMVideoControl)
from comtypes.gen.DexterLib import SampleGrabber, tag_AMMediaType

from jaraco.structures import binary

_quartz = GetModule('quartz.dll')
IMediaControl = _quartz.IMediaControl
IVideoWindow = _quartz.IVideoWindow

class VidCapError(Exception): pass

# WinError.h
E_INVALIDARG = c_long(0x80070057).value
E_POINTER = c_long(0x80004003).value
# vfwmsgs.h
VFW_E_NOT_CONNECTED = c_long(0x80040209).value
VFW_E_WRONG_STATE = c_long(0x80040227).value

CLSID_VideoInputDeviceCategory = GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}")

CLSID_SystemDeviceEnum = GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
class DeviceEnumerator(CoClass):
	_reg_clsid_ = CLSID_SystemDeviceEnum
	_com_interfaces_ = [ICreateDevEnum]
	_idlflags_ = []
	_typelib_path_ = typelib_path
	_reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)

MEDIATYPE_Video = GUID('{73646976-0000-0010-8000-00AA00389B71}')
MEDIATYPE_Interleaved = GUID('{73766169-0000-0010-8000-00aa00389b71}')
MEDIASUBTYPE_RGB24 = GUID('{e436eb7d-524f-11ce-9f53-0020af0ba770}')
FORMAT_VideoInfo = GUID('{05589f80-c356-11ce-bf01-00aa0055595a}')

PIN_CATEGORY_CAPTURE = GUID('{fb6c4281-0353-11d1-905f-0000c0cc16ba}')

REFERENCE_TIME = c_longlong

PINDIR_INPUT = 0
PINDIR_OUTPUT = 1

OA_TRUE = -1
OA_FALSE = 0

class BITMAPINFOHEADER(Structure):
	_fields_ = (
		('size', DWORD),
		('width', LONG),
		('height', LONG),
		('planes', WORD),
		('bit_count', WORD),
		('compression', DWORD),
		('image_size', DWORD),
		('x_pels_per_meter', LONG),
		('y_pels_per_meter', LONG),
		('clr_used', DWORD),
		('clr_important', DWORD),
		)

class VIDEOINFOHEADER(Structure):
	_fields_ = (
		('source', RECT),
		('target', RECT),
		('bit_rate', DWORD),
		('bit_error_rate', DWORD),
		('avg_time_per_frame', REFERENCE_TIME),
		('bmi_header', BITMAPINFOHEADER),
	)

class CAUUID(Structure):
	_fields_ = (
		('element_count', ULONG),
		('elements', POINTER(GUID)),
		)

LPUNKNOWN = POINTER(IUnknown)
CLSID = GUID
LPCLSID = POINTER(CLSID)

OleCreatePropertyFrame = windll.oleaut32.OleCreatePropertyFrame
OleCreatePropertyFrame.restype = HRESULT
OleCreatePropertyFrame.argtypes = (
	HWND, # [in] hwndOwner
	UINT, # [in] x
	UINT, # [in] y
	LPCOLESTR, # [in] lpszCaption
	ULONG, # [in] cObjects
	POINTER(LPUNKNOWN), # [in] ppUnk
	ULONG, # [in] cPages
	LPCLSID, # [in] pPageClsID
	LCID, # [in] lcid
	DWORD, # [in] dwReserved
	LPVOID, # [in] pvReserved
	)

class ISpecifyPropertyPages(IUnknown):
	_case_insensitive_ = True
	_iid_ = GUID('{B196B28B-BAB4-101A-B69C-00AA00341D07}')
	_idlflags_ = []
	_methods_ = [
		COMMETHOD([], HRESULT, 'GetPages',
			(['out'], POINTER(CAUUID), 'pPages'),
			),
		]


def FreeMediaType(mt):
	"""http://msdn.microsoft.com/en-us/library/dd375807(VS.85).aspx"""
	if mt.cbFormat != 0:
		windll.ole32.CoTaskMemFree(mt.pbFormat)
		mt.cbFormat = 0

def DeleteMediaType(mt):
	"""http://msdn.microsoft.com/en-us/library/dd375432(VS.85).aspx"""
	FreeMediaType(mt)
	# I don't think we need to free the media type; comtypes should
	#  handle that
	#windll.ole32.CoTaskMemFree(mt)

class VideoControlFlags(binary.Flags):
	_names = 'flip_horizontal flip_vertical external_trigger_enable trigger'.split()
