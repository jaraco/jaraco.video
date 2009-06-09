
from comtypes import POINTER
from comtypes import GUID, CLSCTX_INPROC
from comtypes.client import CreateObject
from comtypes import CoClass
from comtypes.gen.DirectShowLib import (FilterGraph, CaptureGraphBuilder2,
	ICreateDevEnum, typelib_path, IBaseFilter, IBindCtx, IMoniker)
from comtypes.gen.DexterLib import (SampleGrabber, tag_AMMediaType)
from ctypes import cast, POINTER, Structure, c_longlong
from ctypes.wintypes import RECT, DWORD, LONG, WORD

class error(Exception):
	pass

class VidCapError(Exception): pass

def FAILED(hr):
	"http://msdn.microsoft.com/en-us/library/ms693474(VS.85).aspx"
	return hr < 0

# WinError.h
E_INVALIDARG = 0x80070057
E_POINTER = 0x80004003
# vfwmsgs.h
VFW_E_NOT_CONNECTED = 0x80040209
VFW_E_WRONG_STATE = 0x80040227

CLSID_VideoInputDeviceCategory = GUID("{860BB310-5D01-11d0-BD3B-00A0C911CE86}")

CLSID_SystemDeviceEnum = GUID('{62BE5D10-60EB-11d0-BD3B-00A0C911CE86}')
class DeviceEnumerator(CoClass):
	_reg_clsid_ = CLSID_SystemDeviceEnum
	_com_interfaces_ = [ICreateDevEnum]
	_idlflags_ = []
	_typelib_path_ = typelib_path
	_reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)

MEDIATYPE_Video = GUID('{73646976-0000-0010-8000-00AA00389B71}')
MEDIASUBTYPE_RGB24 = GUID('{e436eb7d-524f-11ce-9f53-0020af0ba770}')
FORMAT_VideoInfo = GUID('{05589f80-c356-11ce-bf01-00aa0055595a}')

PIN_CATEGORY_CAPTURE = GUID('{fb6c4281-0353-11d1-905f-0000c0cc16ba}')

REFERENCE_TIME = c_longlong

class BITMAPINFOHEADER(Structure):
	_fields_ = (
		('size', DWORD),
		('width', LONG),
		('height', LONG),
		('planes', WORD),
		('bit_count', WORD),
		('compression', DWORD),
		('size_image', DWORD),
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

class Device(object):
	def __init__(self, devnum=0, show_video_window=False):
		self.devnum = devnum
		self.show_video_window = show_video_window
		self.filter_graph = CreateObject(FilterGraph)
		self.graph_builder = CreateObject(CaptureGraphBuilder2)
		self.graph_builder.SetFiltergraph(self.filter_graph)
		dev_enum = CreateObject(DeviceEnumerator)
		class_enum = dev_enum.CreateClassEnumerator(CLSID_VideoInputDeviceCategory, 0)
		#del dev_enum
		
		# for now, assume one device
		try:
			(moniker, fetched) = class_enum.RemoteNext(1)
		except ValueError:
			raise RuntimeError("Device not found")
		
		# del class_enum
		
		null_context = POINTER(IBindCtx)()
		null_moniker = POINTER(IMoniker)()
		filter_ob = moniker.RemoteBindToObject(null_context,null_moniker,IBaseFilter._iid_)
		
		self.filter_graph.AddFilter(filter_ob, "VideoCapture")
		
		self.grabber = CreateObject(SampleGrabber)
		self.filter_graph.AddFilter(self.grabber, "Grabber")
		
		mt = tag_AMMediaType()
		mt.majortype = MEDIATYPE_Video
		mt.subtype = MEDIASUBTYPE_RGB24;
		mt.formattype = FORMAT_VideoInfo;
		
		self.grabber.SetMediaType(mt)
		
		self.graph_builder.RenderStream(
			PIN_CATEGORY_CAPTURE,
			MEDIATYPE_Video,
			filter_ob,
			self.grabber,
			None,
			)
		
		if not self.show_video_window:
			raise NotImplementedError
			"""
					IVideoWindow *pWindow;

					hr = self->ob_pGraph->QueryInterface(IID_IVideoWindow, (void **)&pWindow);
					if (FAILED(hr))
					{
						PyErr_SetString(VidcapError, "Video Window interface could not be found.");
						cleanup(self);
						return FALSE;
					}

					hr = pWindow->put_AutoShow(OAFALSE);
					if (FAILED(hr))
					{
						PyErr_SetString(VidcapError, "Video Window hiding failed.");
						cleanup(self);
						return FALSE;
					}

					pWindow->Release();
			"""

		self.grabber.SetBufferSamples(True)
		self.grabber.SetOneShot(False)
		
	
	def get_buffer(self):
		media_type = tag_AMMediaType()
		self.grabber.GetConnectedMediaType(media_type)
		
		p_video_info_header = cast(media_type.pbFormat, POINTER(VIDEOINFOHEADER))
		
		# windll.ole32.CoTaskMemFree(media_type.pbFormat) ?
		
		size = p_video_info_header.bmi_header.size # .contents.bmi_header.size?
		width = p_video_info_header.bmi_header.width
		height = p_video_info_header.bmi_header.height
		size = DWORD(size)
		buffer = ctypes.create_string_buffer(size)
		
		self.filter_graph.Run()
		
		while(True):
			# long_p_buffer = cast(buffer, c_long_p)
			res = self.grabber.GetCurrentBuffer(byref(size), buffer))
			sleep(100) if res == VFW_E_WRONG_STATE else break
		
		if FAILED(res):
			error_map = dict(
				E_INVALIDARG="Samples are not being buffered",
				E_POINTER="NULL pointer argument",
				VFW_E_NOT_CONNECTED="The filter is not connected",
				VFW_E_WRONG_STATE="The filter did not buffer a sample yet",
			)
			unknown_error = 'Unknown Error ({0:x})'.format(res)
			msg = "Getting the sample grabber's current buffer failed ({0}).".format(error_map.get(res, unknown_error))
			raise VidcapError(msg)
		
		return bytes(buffer)[:size], width, height

def test():
	d = Device(show_video_window=True)
	buffer, width, height = d.get_buffer()

if __name__ == '__main__': test()