
from comtypes import POINTER
from comtypes import GUID, CLSCTX_INPROC
from comtypes.client import CreateObject
from comtypes import CoClass
from comtypes.gen.DirectShowLib import (FilterGraph, CaptureGraphBuilder2,
	ICreateDevEnum, typelib_path, IBaseFilter, IBindCtx, IMoniker)

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

CLSID_SampleGrabber = GUID('{A000F4C1-083F-D311-9F0B-006008039E37}')
class SampleGrabber(CoClass):
	_reg_clsid_ = CLSID_SampleGrabber
	_com_interfaces_ = [IBaseFilter, ISampleGrabber]
	# ...

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
		
		# self.grabber = CreateObject(SampleGrabber)
		#self.filter_graph.AddFilter(self.grabber, "Grabber")

def test():
	d = Device()

if __name__ == '__main__': test()