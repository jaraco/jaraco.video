
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
		
		raise NotImplementedError, "Complete implementation stops here"
"""
    AM_MEDIA_TYPE MediaType;
    hr = self->ob_pGrab->GetConnectedMediaType(&MediaType);
    if (FAILED(hr))
    {
        PyErr_SetString(VidcapError, "Getting the sample grabber's connected media type failed.");
        return NULL;
    }

    // Get a pointer to the video header.
    VIDEOINFOHEADER *pVideoHeader = (VIDEOINFOHEADER*)MediaType.pbFormat;

    long size   = pVideoHeader->bmiHeader.biSizeImage;
    long width  = pVideoHeader->bmiHeader.biWidth;
    long height = pVideoHeader->bmiHeader.biHeight;

    // Free the format block
    //FreeMediaType(MediaType); // this would need the DirectShow Base Classes
    CoTaskMemFree(MediaType.pbFormat);

    // Allocate memory.
    //void *buffer = malloc(size);
    void *buffer = PyMem_Malloc(size);
    if (!buffer)
    {
        PyErr_NoMemory();
        return NULL;
    }

    hr = self->ob_pControl->Run(); // fixme: xxx
    // Copy the image into the buffer.
    while (true)
    {
        hr = self->ob_pGrab->GetCurrentBuffer(&size, (long *)buffer);
        if (hr == VFW_E_WRONG_STATE)
            Sleep(100);
        else
            break;
    }
    if (FAILED(hr))
    {
        switch (hr)
        {
        case E_INVALIDARG:
            PyErr_SetString(VidcapError, "Getting the sample grabber's current buffer failed (Samples are not being buffered).");
            break;
        case E_POINTER:
            PyErr_SetString(VidcapError, "Getting the sample grabber's current buffer failed (NULL pointer argument).");
            break;
        case VFW_E_NOT_CONNECTED:
            PyErr_SetString(VidcapError, "Getting the sample grabber's current buffer failed (The filter is not connected).");
            break;
        case VFW_E_WRONG_STATE:
            PyErr_SetString(VidcapError, "Getting the sample grabber's current buffer failed (The filter did not buffer a sample yet).");
            break;
        default:
            PyErr_SetString(VidcapError, "UNKNOWN CASE!!");
        }
        PyMem_Free(buffer);
        return NULL;
    }

    // Return the buffer.
    PyObject *value;
    value = Py_BuildValue("(s#,l,l)", buffer, size, width, height);

    //free(buffer);
    PyMem_Free(buffer);

    return value;
"""


def test():
	d = Device(show_video_window=True)
	buffer, width, height = d.get_buffer()

if __name__ == '__main__': test()