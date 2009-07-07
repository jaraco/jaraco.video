
"""
vidcap.py

(c) 2009 Jason R. Coombs

A port of the C++ extension-based version by Markus Gritsch:
 http://videocapture.sourceforge.net/

"""

# Since the Gritsch's implementation supports through Python 2.6,
#  I'll assume Python 2.6 or greater.
from __future__ import print_function

import datetime
import re
from time import sleep
import logging

from comtypes import POINTER
from comtypes import GUID, CLSCTX_INPROC, COMMETHOD
from comtypes.client import CreateObject, GetModule
from comtypes import CoClass, IUnknown, COMError
from ctypes import (cast, POINTER, Structure, c_longlong,
	create_string_buffer, byref, c_long)
from ctypes.wintypes import (RECT, DWORD, LONG, WORD, ULONG, HWND,
	UINT, LPCOLESTR, LCID, LPVOID, HRESULT)
from ctypes import windll

from comtypes.gen.DirectShowLib import (FilterGraph, CaptureGraphBuilder2,
	ICreateDevEnum, typelib_path, IBaseFilter, IBindCtx, IMoniker,
	IAMStreamConfig, IAMVideoControl,)
from comtypes.gen.DexterLib import (SampleGrabber, tag_AMMediaType)

from PIL import Image, ImageFont, ImageDraw

log = logging.getLogger(__name__)

_quartz = GetModule('quartz.dll')
IMediaControl = _quartz.IMediaControl

class error(Exception):
	pass

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

def consume(iterable):
	for x in iterable: pass

class Device(object):
	try:
		fonts = dict(
			normal = ImageFont.truetype('arial.ttf',10),
			bold = ImageFont.truetype('arialbd.ttf',10),
			)
	except:
		log.warning("PIL ImageFont construction failed, text ops will fail")
		
	def __init__(self, devnum=0, show_video_window=False):
		self.devnum = devnum
		self.show_video_window = show_video_window
		self.initialize()

	def initialize(self):
		self.filter_graph = CreateObject(FilterGraph)
		self.control = self.filter_graph.QueryInterface(IMediaControl)
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
		self.source = moniker.RemoteBindToObject(null_context,null_moniker,IBaseFilter._iid_)
		
		self.filter_graph.AddFilter(self.source, "VideoCapture")
		
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
			self.source,
			self.grabber,
			None,
			)
		
		window = self.filter_graph.QueryInterface(_quartz.IVideoWindow)
		window.AutoShow = self.show_video_window

		self.grabber.SetBufferSamples(True)
		self.grabber.SetOneShot(False)

	def teardown(self):
		if hasattr(self, 'control'):
			self.control.Stop()
			self.control.Release()
			del self.control
		if hasattr(self, 'grabber'):
			self.grabber.Release()
			del self.grabber
		if hasattr(self, 'graph_builder'):
			self.graph_builder.Release()
			del self.graph_builder
		if hasattr(self, 'filter_graph'):
			self.filter_graph.Release()
			del self.filter_graph

	def display_capture_filter_properties(self):
		self.control.Stop()
		self._do_property_pages(self.source)

	@staticmethod
	def _do_property_pages(subject):
		spec_pages = subject.QueryInterface(ISpecifyPropertyPages)
		cauuid = spec_pages.GetPages()
		if cauuid.element_count > 0:
			# self.teardown()
			# self.initialize()
			OleCreatePropertyFrame(
				windll.user32.GetTopWindow(None),
				0, 0, None,
				1, byref(cast(subject, LPUNKNOWN)),
				cauuid.element_count, cauuid.elements,
				0, 0, None)
			windll.ole32.CoTaskMemFree(cauuid.elements)
			# self.teardown()
			# self.initialize()

	def display_capture_pin_properties(self):
		self.control.Stop()
		self._do_property_pages(self._get_stream_config())

	def _get_graph_builder_interface(self, interface):
		args = [
				PIN_CATEGORY_CAPTURE,
				MEDIATYPE_Interleaved,
				self.source,
				interface._iid_,
				]
		try:
			result = self.graph_builder.RemoteFindInterface(*args)
		except COMError as e:
			args[1] = MEDIATYPE_Video
			result = self.graph_builder.RemoteFindInterface(*args)
		return cast(result, POINTER(interface)).value

	def _get_stream_config(self):
		return self._get_graph_builder_interface(IAMStreamConfig)

	def _get_video_control(self):
		return self._get_graph_builder_interface(IAMVideoControl)

	def set_resolution(self, width, height):
		self.control.Stop()
		stream_config = self._get_stream_config()
		p_media_type = stream_config.GetFormat()
		media_type = p_media_type.contents
		if media_type.formattype != FORMAT_VideoInfo:
			raise VidCapError("Cannot query capture format")
		p_video_info_header = cast(media_type.pbFormat, POINTER(VIDEOINFOHEADER))
		hdr = p_video_info_header.contents.bmi_header
		hdr.width, hdr.height = width, height
		stream_config.SetFormat(media_type)
		DeleteMediaType(media_type)
		#stream_config.Release()
		#self.teardown()
		#self.initialize()

	def get_buffer(self):
		media_type = tag_AMMediaType()
		self.grabber.GetConnectedMediaType(media_type)
		
		p_video_info_header = cast(media_type.pbFormat, POINTER(VIDEOINFOHEADER))
		
		# windll.ole32.CoTaskMemFree(media_type.pbFormat) ?
		
		hdr = p_video_info_header.contents.bmi_header
		size = hdr.image_size
		width = hdr.width
		height = hdr.height
		assert size % 4 == 0
		buffer = create_string_buffer(size)
		long_p_buffer = cast(buffer, POINTER(c_long))
		size = c_long(size)
		
		self.control.Run()
		
		try:
			while(True):
				# call the function directly, as the in/out symantics of
				# argtypes isn't working here.
				try:
					GetCurrentBuffer = self.grabber._ISampleGrabber__com_GetCurrentBuffer
					GetCurrentBuffer(byref(size), long_p_buffer)
				except COMError as e:
					if e.args[0] == VFW_E_WRONG_STATE:
						sleep(.100)
					else:
						raise
				else:
					break
		except COMError as e:
			
			error_map = dict(
				E_INVALIDARG="Samples are not being buffered",
				E_POINTER="NULL pointer argument",
				VFW_E_NOT_CONNECTED="The filter is not connected",
				VFW_E_WRONG_STATE="The filter did not buffer a sample yet",
			)
			code = e[0]
			unknown_error = 'Unknown Error ({0:x})'.format(code)
			msg = "Getting the sample grabber's current buffer failed ({0}).".format(error_map.get(code, unknown_error))
			raise VidCapError(msg)
		
		return bytes(buffer[:size.value]), (width, height)

	def get_image(self, timestamp=None, font='normal', textpos='bottom-left'):
		"""Returns a PIL Image instance.

		timestamp:  None    ...       no timestamp (the default)
		            simple  ...       simple timestamp
		            shadow  ...       timestamp with shadow
		            outline ...       timestamp with outline
		            thick-outline ... timestamp with thick outline

		font:  normal ... normal font (the default)
		       bold   ... bold font

		textpos: The position of the timestamp can be specified by a string
		         containing a combination of two words specifying the vertical
		         and horizontal position of the timestamp.  Abbreviations
		         are allowed.
		         Vertical positions: top or bottom
		         Horizontal positions: left, center, right
		         
		         defaults to 'bottom-left'
		"""
		buffer, dimensions = self.get_buffer()
		# todo, what is 'BGR', 0, -1 ?
		img = Image.fromstring('RGB', dimensions, buffer, 'raw', 'BGR', 0, -1)
		if timestamp:
			text = str(datetime.datetime.now())
			self._add_text(img, text, font, textpos, timestamp)
		return img

	def _add_text(self, img, text, font, textpos, shadow_style):
		font = self.fonts[font]
		text_size = font.getsize(text)
		tw, th = (dim - 2 for dim in font.getsize(text))
		iw, ih = img.size
		vert_pos, horiz_pos = re.split('[ -]+', textpos.lower())
		try:
			x = dict(l=2, c=(iw-tw)//2, r=iw-tw-2)[horiz_pos[0]]
			y = dict(t=-1, b=ih-th-2)[vert_pos[0]]
			text_coords = (x,y)
		except Exception:
			raise ValueError("Invalid textpos {0}".format(textpos))

		draw = ImageDraw.Draw(img)
		locs = self._get_shadow_draw_locations(text_coords, shadow_style)
		textcolor = 0xffffff
		shadowcolor = 0x000000
		consume((draw.text(loc, text, font, fill=shadowcolor) for loc in locs))
		draw.text(text_coords, text, font=font, fill=textcolor)

	@staticmethod
	def _get_shadow_draw_locations(origin, shadow_style):
		x, y = origin
		outline_locs = ((x-1, y), (x+1, y), (x, y-1), (x, y+1))
		shadow_draw_locations = dict(
			simple = (),
			shadow = ((x+1, y), (x, y+1), (x+1, y+1)),
			outline = outline_locs,
			)
		shadow_draw_locations['thick-outline'] = (
			outline_locs + ((x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1))
			)
		locs = shadow_draw_locations.get(shadow_style)
		if locs is None:
			raise ValueError("Unknown shadow style {0}".format(shadow_style))
		return locs

	def save_snapshot(self, filename, timestamp=None,
		font='normal', textpos='bottom-left', *args, **kwargs):
		"""
		Saves a snapshot to a file.

		The filetype is inferred from the filename extension. Everything that
		PIL can handle can be specified (foo.jpg, foo.gif, foo.bmp, ...).

		filename: String containing the name of the resulting file.

		timestamp:	see get_image()

		font:	see get_image()

		textpos:	see get_image()

		Any additional arguments are passed to the save() method of the image
		class.
		For example you can specify the compression level of a JPEG image using
		'quality=95'.
		"""
		self.get_image(timestamp, font, textpos).save(filename, **kwargs)

def test():
	global d, buffer, width, height
	d = Device(show_video_window=False)
	d.save_snapshot('foo.jpg', timestamp='simple')

def find_name(name):
	"For testing only; search for a name in the libraries"
	from comtypes.gen import DirectShowLib, DexterLib
	from ctypes import wintypes
	import comtypes
	for lib in DirectShowLib, DexterLib, wintypes, comtypes, _quartz:
		res = [x for x in dir(lib) if name.lower() in x.lower()]
		if res:
			print('found {0} in {1} as {2}'.format(name, lib, ', '.join(res)))

if __name__ == '__main__': test()