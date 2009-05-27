# -*- coding: mbcs -*-
typelib_path = 'C:\\Users\\jaraco\\projects\\public\\VideoCapture-0.9-2\\src\\gen_ds\\DirectShow.tlb'
_lcid = 0 # change this if required
from ctypes import *
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from comtypes import GUID
from ctypes import HRESULT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes import _COSERVERINFO
from ctypes.wintypes import tagRECT
from ctypes.wintypes import tagSIZE
from ctypes.wintypes import tagRECT
WSTRING = c_wchar_p
from comtypes import IPersist
from ctypes.wintypes import _ULARGE_INTEGER
from comtypes import IUnknown
from ctypes.wintypes import _FILETIME
from ctypes.wintypes import _ULARGE_INTEGER
from ctypes.wintypes import _FILETIME
from comtypes.typeinfo import ULONG_PTR
from comtypes import _COAUTHINFO
from comtypes import CoClass
LONG_PTR = c_int
from comtypes.automation import VARIANT
from ctypes.wintypes import _LARGE_INTEGER
from comtypes.persist import IErrorLog
from comtypes import _COAUTHIDENTITY
from comtypes import wireHWND
from comtypes.persist import IPropertyBag
from comtypes import tagBIND_OPTS2
from comtypes.automation import VARIANT



# values for enumeration '__MIDL_IConfigInterleaving_0001'
INTERLEAVE_NONE = 0
INTERLEAVE_CAPTURE = 1
INTERLEAVE_FULL = 2
INTERLEAVE_NONE_BUFFERED = 3
__MIDL_IConfigInterleaving_0001 = c_int # enum
class IVMRSurface(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRSurface Interface'
    _iid_ = GUID('{A9849BBE-9EC8-4263-B764-62730F0D15D0}')
    _idlflags_ = []
IVMRSurface._methods_ = [
    COMMETHOD([], HRESULT, 'IsSurfaceLocked'),
    COMMETHOD([], HRESULT, 'LockSurface',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'lpSurface' )),
    COMMETHOD([], HRESULT, 'UnlockSurface'),
    COMMETHOD([], HRESULT, 'GetSurface',
              ( ['out'], POINTER(POINTER(c_ulong)), 'lplpSurface' )),
]
################################################################
## code template for IVMRSurface implementation
##class IVMRSurface_Impl(object):
##    def IsSurfaceLocked(self):
##        '-no docstring-'
##        #return 
##
##    def UnlockSurface(self):
##        '-no docstring-'
##        #return 
##
##    def LockSurface(self):
##        '-no docstring-'
##        #return lpSurface
##
##    def GetSurface(self):
##        '-no docstring-'
##        #return lplpSurface
##

class __MIDL___MIDL_itf_DirectShow_0345_0001(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0345_0001._fields_ = [
    ('dwDVAAuxSrc', c_ulong),
    ('dwDVAAuxCtl', c_ulong),
    ('dwDVAAuxSrc1', c_ulong),
    ('dwDVAAuxCtl1', c_ulong),
    ('dwDVVAuxSrc', c_ulong),
    ('dwDVVAuxCtl', c_ulong),
    ('dwDVReserved', c_ulong * 2),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0345_0001) == 32, sizeof(__MIDL___MIDL_itf_DirectShow_0345_0001)
assert alignment(__MIDL___MIDL_itf_DirectShow_0345_0001) == 4, alignment(__MIDL___MIDL_itf_DirectShow_0345_0001)

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0376_0001'
RenderPrefs_RestrictToInitialMonitor = 0
RenderPrefs_ForceOffscreen = 1
RenderPrefs_ForceOverlays = 2
RenderPrefs_AllowOverlays = 0
RenderPrefs_AllowOffscreen = 0
RenderPrefs_DoNotRenderColorKeyAndBorder = 8
RenderPrefs_Reserved = 16
RenderPrefs_PreferAGPMemWhenMixing = 32
RenderPrefs_Mask = 63
__MIDL___MIDL_itf_DirectShow_0376_0001 = c_int # enum
class IDVRGB219(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{58473A19-2BC8-4663-8012-25F81BABDDD1}')
    _idlflags_ = []
IDVRGB219._methods_ = [
    COMMETHOD([], HRESULT, 'SetRGB219',
              ( ['in'], c_int, 'bState' )),
]
################################################################
## code template for IDVRGB219 implementation
##class IDVRGB219_Impl(object):
##    def SetRGB219(self, bState):
##        '-no docstring-'
##        #return 
##

class __MIDL___MIDL_itf_DirectShow_0134_0009(Structure):
    pass
class __MIDL___MIDL_itf_DirectShow_0134_0005(Structure):
    pass
REGFILTERPINS2 = __MIDL___MIDL_itf_DirectShow_0134_0005
__MIDL___MIDL_itf_DirectShow_0134_0009._fields_ = [
    ('cPins2', c_ulong),
    ('rgPins2', POINTER(REGFILTERPINS2)),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0009) == 16, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0009)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0009) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0009)
class _AllocatorProperties(Structure):
    pass
_AllocatorProperties._fields_ = [
    ('cBuffers', c_int),
    ('cbBuffer', c_int),
    ('cbAlign', c_int),
    ('cbPrefix', c_int),
]
assert sizeof(_AllocatorProperties) == 16, sizeof(_AllocatorProperties)
assert alignment(_AllocatorProperties) == 4, alignment(_AllocatorProperties)

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0164_0001'
VfwCaptureDialog_Source = 1
VfwCaptureDialog_Format = 2
VfwCaptureDialog_Display = 4
__MIDL___MIDL_itf_DirectShow_0164_0001 = c_int # enum
class IDrawVideoImage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{48EFB120-AB49-11D2-AED2-00A0C995E8D5}')
    _idlflags_ = []
class _RemotableHandle(Structure):
    pass
wireHDC = POINTER(_RemotableHandle)
IDrawVideoImage._methods_ = [
    COMMETHOD([], HRESULT, 'DrawVideoImageBegin'),
    COMMETHOD([], HRESULT, 'DrawVideoImageEnd'),
    COMMETHOD([], HRESULT, 'DrawVideoImageDraw',
              ( ['in'], wireHDC, 'hdc' ),
              ( ['in'], POINTER(tagRECT), 'lprcSrc' ),
              ( ['in'], POINTER(tagRECT), 'lprcDst' )),
]
################################################################
## code template for IDrawVideoImage implementation
##class IDrawVideoImage_Impl(object):
##    def DrawVideoImageEnd(self):
##        '-no docstring-'
##        #return 
##
##    def DrawVideoImageBegin(self):
##        '-no docstring-'
##        #return 
##
##    def DrawVideoImageDraw(self, hdc, lprcSrc, lprcDst):
##        '-no docstring-'
##        #return 
##

class tagTIMECODE(Structure):
    pass
tagTIMECODE._fields_ = [
    ('wFrameRate', c_ushort),
    ('wFrameFract', c_ushort),
    ('dwFrames', c_ulong),
]
assert sizeof(tagTIMECODE) == 8, sizeof(tagTIMECODE)
assert alignment(tagTIMECODE) == 4, alignment(tagTIMECODE)

# values for enumeration 'tagAMTunerModeType'
AMTUNER_MODE_DEFAULT = 0
AMTUNER_MODE_TV = 1
AMTUNER_MODE_FM_RADIO = 2
AMTUNER_MODE_AM_RADIO = 4
AMTUNER_MODE_DSS = 8
tagAMTunerModeType = c_int # enum

# values for enumeration 'tagVideoProcAmpFlags'
VideoProcAmp_Flags_Auto = 1
VideoProcAmp_Flags_Manual = 2
tagVideoProcAmpFlags = c_int # enum
class tagVMRPRESENTATIONINFO(Structure):
    pass
tagVMRPRESENTATIONINFO._fields_ = [
    ('dwFlags', c_ulong),
    ('lpSurf', POINTER(c_ulong)),
    ('rtStart', c_longlong),
    ('rtEnd', c_longlong),
    ('szAspectRatio', tagSIZE),
    ('rcSrc', tagRECT),
    ('rcDst', tagRECT),
    ('dwTypeSpecificFlags', c_ulong),
    ('dwInterlaceFlags', c_ulong),
]
assert sizeof(tagVMRPRESENTATIONINFO) == 80, sizeof(tagVMRPRESENTATIONINFO)
assert alignment(tagVMRPRESENTATIONINFO) == 8, alignment(tagVMRPRESENTATIONINFO)

# values for enumeration '_AM_FILTER_FLAGS'
AM_FILTER_FLAGS_REMOVABLE = 1
_AM_FILTER_FLAGS = c_int # enum
class IFileSinkFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A2104830-7C70-11CF-8BCE-00AA00A3F1A6}')
    _idlflags_ = []
class IFileSinkFilter2(IFileSinkFilter):
    _case_insensitive_ = True
    _iid_ = GUID('{00855B90-CE1B-11D0-BD4F-00A0C911CE86}')
    _idlflags_ = []
class _AMMediaType(Structure):
    pass
IFileSinkFilter._methods_ = [
    COMMETHOD([], HRESULT, 'SetFileName',
              ( ['in'], WSTRING, 'pszFileName' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'GetCurFile',
              ( ['out'], POINTER(WSTRING), 'ppszFileName' ),
              ( ['out'], POINTER(_AMMediaType), 'pmt' )),
]
################################################################
## code template for IFileSinkFilter implementation
##class IFileSinkFilter_Impl(object):
##    def GetCurFile(self):
##        '-no docstring-'
##        #return ppszFileName, pmt
##
##    def SetFileName(self, pszFileName, pmt):
##        '-no docstring-'
##        #return 
##

IFileSinkFilter2._methods_ = [
    COMMETHOD([], HRESULT, 'SetMode',
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'GetMode',
              ( ['out'], POINTER(c_ulong), 'pdwFlags' )),
]
################################################################
## code template for IFileSinkFilter2 implementation
##class IFileSinkFilter2_Impl(object):
##    def GetMode(self):
##        '-no docstring-'
##        #return pdwFlags
##
##    def SetMode(self, dwFlags):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'tagCameraControlFlags'
CameraControl_Flags_Auto = 1
CameraControl_Flags_Manual = 2
tagCameraControlFlags = c_int # enum
class IPersistStream(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{00000109-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IMoniker(IPersistStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000F-0000-0000-C000-000000000046}')
    _idlflags_ = []
class ISequentialStream(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0C733A30-2A1C-11CE-ADE5-00AA0044773D}')
    _idlflags_ = []
class IStream(ISequentialStream):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000C-0000-0000-C000-000000000046}')
    _idlflags_ = []
IPersistStream._methods_ = [
    COMMETHOD([], HRESULT, 'IsDirty'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IStream), 'pstm' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], c_int, 'fClearDirty' )),
    COMMETHOD([], HRESULT, 'GetSizeMax',
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbSize' )),
]
################################################################
## code template for IPersistStream implementation
##class IPersistStream_Impl(object):
##    def Load(self, pstm):
##        '-no docstring-'
##        #return 
##
##    def GetSizeMax(self):
##        '-no docstring-'
##        #return pcbSize
##
##    def Save(self, pstm, fClearDirty):
##        '-no docstring-'
##        #return 
##
##    def IsDirty(self):
##        '-no docstring-'
##        #return 
##

class IBindCtx(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{0000000E-0000-0000-C000-000000000046}')
    _idlflags_ = []
class IEnumMoniker(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000102-0000-0000-C000-000000000046}')
    _idlflags_ = []
IMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteBindToObject',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riidResult' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvResult' )),
    COMMETHOD([], HRESULT, 'RemoteBindToStorage',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppvObj' )),
    COMMETHOD([], HRESULT, 'Reduce',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], c_ulong, 'dwReduceHowFar' ),
              ( ['in', 'out'], POINTER(POINTER(IMoniker)), 'ppmkToLeft' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkReduced' )),
    COMMETHOD([], HRESULT, 'ComposeWith',
              ( ['in'], POINTER(IMoniker), 'pmkRight' ),
              ( ['in'], c_int, 'fOnlyIfNotGeneric' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkComposite' )),
    COMMETHOD([], HRESULT, 'Enum',
              ( ['in'], c_int, 'fForward' ),
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
    COMMETHOD([], HRESULT, 'IsEqual',
              ( ['in'], POINTER(IMoniker), 'pmkOtherMoniker' )),
    COMMETHOD([], HRESULT, 'Hash',
              ( ['out'], POINTER(c_ulong), 'pdwHash' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], POINTER(IMoniker), 'pmkNewlyRunning' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'Inverse',
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmk' )),
    COMMETHOD([], HRESULT, 'CommonPrefixWith',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkPrefix' )),
    COMMETHOD([], HRESULT, 'RelativePathTo',
              ( ['in'], POINTER(IMoniker), 'pmkOther' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkRelPath' )),
    COMMETHOD([], HRESULT, 'GetDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['out'], POINTER(WSTRING), 'ppszDisplayName' )),
    COMMETHOD([], HRESULT, 'ParseDisplayName',
              ( ['in'], POINTER(IBindCtx), 'pbc' ),
              ( ['in'], POINTER(IMoniker), 'pmkToLeft' ),
              ( ['in'], WSTRING, 'pszDisplayName' ),
              ( ['out'], POINTER(c_ulong), 'pchEaten' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'ppmkOut' )),
    COMMETHOD([], HRESULT, 'IsSystemMoniker',
              ( ['out'], POINTER(c_ulong), 'pdwMksys' )),
]
################################################################
## code template for IMoniker implementation
##class IMoniker_Impl(object):
##    def RelativePathTo(self, pmkOther):
##        '-no docstring-'
##        #return ppmkRelPath
##
##    def GetTimeOfLastChange(self, pbc, pmkToLeft):
##        '-no docstring-'
##        #return pfiletime
##
##    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric):
##        '-no docstring-'
##        #return ppmkComposite
##
##    def Hash(self):
##        '-no docstring-'
##        #return pdwHash
##
##    def IsSystemMoniker(self):
##        '-no docstring-'
##        #return pdwMksys
##
##    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName):
##        '-no docstring-'
##        #return pchEaten, ppmkOut
##
##    def RemoteBindToStorage(self, pbc, pmkToLeft, riid):
##        '-no docstring-'
##        #return ppvObj
##
##    def Enum(self, fForward):
##        '-no docstring-'
##        #return ppenumMoniker
##
##    def Reduce(self, pbc, dwReduceHowFar):
##        '-no docstring-'
##        #return ppmkToLeft, ppmkReduced
##
##    def Inverse(self):
##        '-no docstring-'
##        #return ppmk
##
##    def RemoteBindToObject(self, pbc, pmkToLeft, riidResult):
##        '-no docstring-'
##        #return ppvResult
##
##    def IsEqual(self, pmkOtherMoniker):
##        '-no docstring-'
##        #return 
##
##    def IsRunning(self, pbc, pmkToLeft, pmkNewlyRunning):
##        '-no docstring-'
##        #return 
##
##    def CommonPrefixWith(self, pmkOther):
##        '-no docstring-'
##        #return ppmkPrefix
##
##    def GetDisplayName(self, pbc, pmkToLeft):
##        '-no docstring-'
##        #return ppszDisplayName
##

class IAMOpenProgress(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8E1C39A1-DE53-11CF-AA63-0080C744528D}')
    _idlflags_ = []
IAMOpenProgress._methods_ = [
    COMMETHOD([], HRESULT, 'QueryProgress',
              ( ['out'], POINTER(c_longlong), 'pllTotal' ),
              ( ['out'], POINTER(c_longlong), 'pllCurrent' )),
    COMMETHOD([], HRESULT, 'AbortOperation'),
]
################################################################
## code template for IAMOpenProgress implementation
##class IAMOpenProgress_Impl(object):
##    def QueryProgress(self):
##        '-no docstring-'
##        #return pllTotal, pllCurrent
##
##    def AbortOperation(self):
##        '-no docstring-'
##        #return 
##

class IMediaSeeking(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73880-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IMediaSeeking._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapabilities',
              ( ['out'], POINTER(c_ulong), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'CheckCapabilities',
              ( ['in', 'out'], POINTER(c_ulong), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'IsFormatSupported',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'QueryPreferredFormat',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'GetTimeFormat',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'IsUsingTimeFormat',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'SetTimeFormat',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pFormat' )),
    COMMETHOD([], HRESULT, 'GetDuration',
              ( ['out'], POINTER(c_longlong), 'pDuration' )),
    COMMETHOD([], HRESULT, 'GetStopPosition',
              ( ['out'], POINTER(c_longlong), 'pStop' )),
    COMMETHOD([], HRESULT, 'GetCurrentPosition',
              ( ['out'], POINTER(c_longlong), 'pCurrent' )),
    COMMETHOD([], HRESULT, 'ConvertTimeFormat',
              ( ['out'], POINTER(c_longlong), 'pTarget' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pTargetFormat' ),
              ( ['in'], c_longlong, 'Source' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pSourceFormat' )),
    COMMETHOD([], HRESULT, 'SetPositions',
              ( ['in', 'out'], POINTER(c_longlong), 'pCurrent' ),
              ( ['in'], c_ulong, 'dwCurrentFlags' ),
              ( ['in', 'out'], POINTER(c_longlong), 'pStop' ),
              ( ['in'], c_ulong, 'dwStopFlags' )),
    COMMETHOD([], HRESULT, 'GetPositions',
              ( ['out'], POINTER(c_longlong), 'pCurrent' ),
              ( ['out'], POINTER(c_longlong), 'pStop' )),
    COMMETHOD([], HRESULT, 'GetAvailable',
              ( ['out'], POINTER(c_longlong), 'pEarliest' ),
              ( ['out'], POINTER(c_longlong), 'pLatest' )),
    COMMETHOD([], HRESULT, 'SetRate',
              ( ['in'], c_double, 'dRate' )),
    COMMETHOD([], HRESULT, 'GetRate',
              ( ['out'], POINTER(c_double), 'pdRate' )),
    COMMETHOD([], HRESULT, 'GetPreroll',
              ( ['out'], POINTER(c_longlong), 'pllPreroll' )),
]
################################################################
## code template for IMediaSeeking implementation
##class IMediaSeeking_Impl(object):
##    def GetPositions(self):
##        '-no docstring-'
##        #return pCurrent, pStop
##
##    def GetCapabilities(self):
##        '-no docstring-'
##        #return pCapabilities
##
##    def GetStopPosition(self):
##        '-no docstring-'
##        #return pStop
##
##    def GetCurrentPosition(self):
##        '-no docstring-'
##        #return pCurrent
##
##    def SetPositions(self, dwCurrentFlags, dwStopFlags):
##        '-no docstring-'
##        #return pCurrent, pStop
##
##    def CheckCapabilities(self):
##        '-no docstring-'
##        #return pCapabilities
##
##    def IsFormatSupported(self, pFormat):
##        '-no docstring-'
##        #return 
##
##    def GetRate(self):
##        '-no docstring-'
##        #return pdRate
##
##    def GetPreroll(self):
##        '-no docstring-'
##        #return pllPreroll
##
##    def SetRate(self, dRate):
##        '-no docstring-'
##        #return 
##
##    def GetTimeFormat(self):
##        '-no docstring-'
##        #return pFormat
##
##    def QueryPreferredFormat(self):
##        '-no docstring-'
##        #return pFormat
##
##    def GetDuration(self):
##        '-no docstring-'
##        #return pDuration
##
##    def GetAvailable(self):
##        '-no docstring-'
##        #return pEarliest, pLatest
##
##    def SetTimeFormat(self, pFormat):
##        '-no docstring-'
##        #return 
##
##    def ConvertTimeFormat(self, pTargetFormat, Source, pSourceFormat):
##        '-no docstring-'
##        #return pTarget
##
##    def IsUsingTimeFormat(self, pFormat):
##        '-no docstring-'
##        #return 
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0370_0002'
VMRSample_SyncPoint = 1
VMRSample_Preroll = 2
VMRSample_Discontinuity = 4
VMRSample_TimeValid = 8
__MIDL___MIDL_itf_DirectShow_0370_0002 = c_int # enum
VMRPresentationFlags = __MIDL___MIDL_itf_DirectShow_0370_0002
class __MIDL___MIDL_itf_DirectShow_0134_0006(Structure):
    pass
REGFILTER2 = __MIDL___MIDL_itf_DirectShow_0134_0006

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0156_0001'
AM_STREAM_INFO_START_DEFINED = 1
AM_STREAM_INFO_STOP_DEFINED = 2
AM_STREAM_INFO_DISCARDING = 4
AM_STREAM_INFO_STOP_SEND_EXTRA = 16
__MIDL___MIDL_itf_DirectShow_0156_0001 = c_int # enum
class __MIDL___MIDL_itf_DirectShow_0134_0003(Structure):
    pass
REGPINMEDIUM = __MIDL___MIDL_itf_DirectShow_0134_0003
class IConfigInterleaving(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BEE3D220-157B-11D0-BD23-00A0C911CE86}')
    _idlflags_ = []
InterleavingMode = __MIDL_IConfigInterleaving_0001
IConfigInterleaving._methods_ = [
    COMMETHOD([], HRESULT, 'put_Mode',
              ( ['in'], InterleavingMode, 'mode' )),
    COMMETHOD([], HRESULT, 'get_Mode',
              ( ['out'], POINTER(InterleavingMode), 'pMode' )),
    COMMETHOD([], HRESULT, 'put_Interleaving',
              ( ['in'], POINTER(c_longlong), 'prtInterleave' ),
              ( ['in'], POINTER(c_longlong), 'prtPreroll' )),
    COMMETHOD([], HRESULT, 'get_Interleaving',
              ( ['out'], POINTER(c_longlong), 'prtInterleave' ),
              ( ['out'], POINTER(c_longlong), 'prtPreroll' )),
]
################################################################
## code template for IConfigInterleaving implementation
##class IConfigInterleaving_Impl(object):
##    def put_Interleaving(self, prtInterleave, prtPreroll):
##        '-no docstring-'
##        #return 
##
##    def get_Interleaving(self):
##        '-no docstring-'
##        #return prtInterleave, prtPreroll
##
##    def get_Mode(self):
##        '-no docstring-'
##        #return pMode
##
##    def put_Mode(self, mode):
##        '-no docstring-'
##        #return 
##

class _NORMALIZEDRECT(Structure):
    pass
_NORMALIZEDRECT._fields_ = [
    ('left', c_float),
    ('top', c_float),
    ('right', c_float),
    ('bottom', c_float),
]
assert sizeof(_NORMALIZEDRECT) == 16, sizeof(_NORMALIZEDRECT)
assert alignment(_NORMALIZEDRECT) == 4, alignment(_NORMALIZEDRECT)

# values for enumeration 'tagTunerInputType'
TunerInputCable = 0
TunerInputAntenna = 1
tagTunerInputType = c_int # enum
class IVMRImagePresenterConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRImagePresenterConfig Interface'
    _iid_ = GUID('{9F3A1C85-8555-49BA-935F-BE5B5B29D178}')
    _idlflags_ = []
class IVMRImagePresenterExclModeConfig(IVMRImagePresenterConfig):
    _case_insensitive_ = True
    u'IVMRImagePresenterExclModeConfig Interface'
    _iid_ = GUID('{E6F7CE40-4673-44F1-8F77-5499D68CB4EA}')
    _idlflags_ = []
IVMRImagePresenterConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetRenderingPrefs',
              ( ['in'], c_ulong, 'dwRenderFlags' )),
    COMMETHOD([], HRESULT, 'GetRenderingPrefs',
              ( ['out'], POINTER(c_ulong), 'dwRenderFlags' )),
]
################################################################
## code template for IVMRImagePresenterConfig implementation
##class IVMRImagePresenterConfig_Impl(object):
##    def GetRenderingPrefs(self):
##        '-no docstring-'
##        #return dwRenderFlags
##
##    def SetRenderingPrefs(self, dwRenderFlags):
##        '-no docstring-'
##        #return 
##

IVMRImagePresenterExclModeConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetXlcModeDDObjAndPrimarySurface',
              ( ['in'], POINTER(c_ulong), 'lpDDObj' ),
              ( ['in'], POINTER(c_ulong), 'lpPrimarySurf' )),
    COMMETHOD([], HRESULT, 'GetXlcModeDDObjAndPrimarySurface',
              ( ['out'], POINTER(POINTER(c_ulong)), 'lpDDObj' ),
              ( ['out'], POINTER(POINTER(c_ulong)), 'lpPrimarySurf' )),
]
################################################################
## code template for IVMRImagePresenterExclModeConfig implementation
##class IVMRImagePresenterExclModeConfig_Impl(object):
##    def GetXlcModeDDObjAndPrimarySurface(self):
##        '-no docstring-'
##        #return lpDDObj, lpPrimarySurf
##
##    def SetXlcModeDDObjAndPrimarySurface(self, lpDDObj, lpPrimarySurf):
##        '-no docstring-'
##        #return 
##

class IAMFilterMiscFlags(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2DD74950-A890-11D1-ABE8-00A0C905F375}')
    _idlflags_ = []
IAMFilterMiscFlags._methods_ = [
    COMMETHOD([], c_ulong, 'GetMiscFlags'),
]
################################################################
## code template for IAMFilterMiscFlags implementation
##class IAMFilterMiscFlags_Impl(object):
##    def GetMiscFlags(self):
##        '-no docstring-'
##        #return 
##

class ICaptureGraphBuilder2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{93E5A4E0-2D50-11D2-ABFA-00A0C9C6E38D}')
    _idlflags_ = []
class IFilterGraph(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689F-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IGraphBuilder(IFilterGraph):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A9-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IMediaFilter(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86899-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IBaseFilter(IMediaFilter):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86895-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IAMCopyCaptureFileProgress(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{670D1D20-A068-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []

# values for enumeration '_PinDirection'
PINDIR_INPUT = 0
PINDIR_OUTPUT = 1
_PinDirection = c_int # enum
class IPin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86891-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
ICaptureGraphBuilder2._methods_ = [
    COMMETHOD([], HRESULT, 'SetFiltergraph',
              ( ['in'], POINTER(IGraphBuilder), 'pfg' )),
    COMMETHOD([], HRESULT, 'GetFiltergraph',
              ( ['retval', 'out'], POINTER(POINTER(IGraphBuilder)), 'ppfg' )),
    COMMETHOD([], HRESULT, 'SetOutputFileName',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pType' ),
              ( ['in'], WSTRING, 'lpstrFile' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppf' ),
              ( ['out'], POINTER(POINTER(IFileSinkFilter)), 'ppSink' )),
    COMMETHOD([], HRESULT, 'RemoteFindInterface',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pType' ),
              ( ['in'], POINTER(IBaseFilter), 'pf' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppint' )),
    COMMETHOD([], HRESULT, 'RenderStream',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pType' ),
              ( ['in'], POINTER(IUnknown), 'pSource' ),
              ( ['in'], POINTER(IBaseFilter), 'pfCompressor' ),
              ( ['in'], POINTER(IBaseFilter), 'pfRenderer' )),
    COMMETHOD([], HRESULT, 'ControlStream',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pType' ),
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], POINTER(c_longlong), 'pstart' ),
              ( ['in'], POINTER(c_longlong), 'pStop' ),
              ( ['in'], c_ushort, 'wStartCookie' ),
              ( ['in'], c_ushort, 'wStopCookie' )),
    COMMETHOD([], HRESULT, 'AllocCapFile',
              ( ['in'], WSTRING, 'lpstr' ),
              ( ['in'], c_ulonglong, 'dwlSize' )),
    COMMETHOD([], HRESULT, 'CopyCaptureFile',
              ( ['in'], WSTRING, 'lpwstrOld' ),
              ( ['in'], WSTRING, 'lpwstrNew' ),
              ( ['in'], c_int, 'fAllowEscAbort' ),
              ( ['in'], POINTER(IAMCopyCaptureFileProgress), 'pCallback' )),
    COMMETHOD([], HRESULT, 'FindPin',
              ( ['in'], POINTER(IUnknown), 'pSource' ),
              ( ['in'], _PinDirection, 'pindir' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pType' ),
              ( ['in'], c_int, 'fUnconnected' ),
              ( ['in'], c_int, 'num' ),
              ( ['out'], POINTER(POINTER(IPin)), 'ppPin' )),
]
################################################################
## code template for ICaptureGraphBuilder2 implementation
##class ICaptureGraphBuilder2_Impl(object):
##    def FindPin(self, pSource, pindir, pCategory, pType, fUnconnected, num):
##        '-no docstring-'
##        #return ppPin
##
##    def RemoteFindInterface(self, pCategory, pType, pf, riid):
##        '-no docstring-'
##        #return ppint
##
##    def RenderStream(self, pCategory, pType, pSource, pfCompressor, pfRenderer):
##        '-no docstring-'
##        #return 
##
##    def ControlStream(self, pCategory, pType, pFilter, pstart, pStop, wStartCookie, wStopCookie):
##        '-no docstring-'
##        #return 
##
##    def GetFiltergraph(self):
##        '-no docstring-'
##        #return ppfg
##
##    def SetFiltergraph(self, pfg):
##        '-no docstring-'
##        #return 
##
##    def SetOutputFileName(self, pType, lpstrFile):
##        '-no docstring-'
##        #return ppf, ppSink
##
##    def AllocCapFile(self, lpstr, dwlSize):
##        '-no docstring-'
##        #return 
##
##    def CopyCaptureFile(self, lpwstrOld, lpwstrNew, fAllowEscAbort, pCallback):
##        '-no docstring-'
##        #return 
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0376_0002'
VMRMode_Windowed = 1
VMRMode_Windowless = 2
VMRMode_Renderless = 4
VMRMode_Mask = 7
__MIDL___MIDL_itf_DirectShow_0376_0002 = c_int # enum
VMRMode = __MIDL___MIDL_itf_DirectShow_0376_0002
class tagSTATSTG(Structure):
    pass
tagSTATSTG._fields_ = [
    ('pwcsName', WSTRING),
    ('type', c_ulong),
    ('cbSize', _ULARGE_INTEGER),
    ('mtime', _FILETIME),
    ('ctime', _FILETIME),
    ('atime', _FILETIME),
    ('grfMode', c_ulong),
    ('grfLocksSupported', c_ulong),
    ('clsid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('grfStateBits', c_ulong),
    ('reserved', c_ulong),
]
assert sizeof(tagSTATSTG) == 80, sizeof(tagSTATSTG)
assert alignment(tagSTATSTG) == 8, alignment(tagSTATSTG)
class IMediaSample(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689A-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMediaSample._methods_ = [
    COMMETHOD([], HRESULT, 'GetPointer',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'ppBuffer' )),
    COMMETHOD([], c_int, 'GetSize'),
    COMMETHOD([], HRESULT, 'GetTime',
              ( ['out'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['out'], POINTER(c_longlong), 'pTimeEnd' )),
    COMMETHOD([], HRESULT, 'SetTime',
              ( ['in'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['in'], POINTER(c_longlong), 'pTimeEnd' )),
    COMMETHOD([], HRESULT, 'IsSyncPoint'),
    COMMETHOD([], HRESULT, 'SetSyncPoint',
              ( [], c_int, 'bIsSyncPoint' )),
    COMMETHOD([], HRESULT, 'IsPreroll'),
    COMMETHOD([], HRESULT, 'SetPreroll',
              ( [], c_int, 'bIsPreroll' )),
    COMMETHOD([], c_int, 'GetActualDataLength'),
    COMMETHOD([], HRESULT, 'SetActualDataLength',
              ( [], c_int, '__MIDL_0010' )),
    COMMETHOD([], HRESULT, 'GetMediaType',
              ( [], POINTER(POINTER(_AMMediaType)), 'ppMediaType' )),
    COMMETHOD([], HRESULT, 'SetMediaType',
              ( [], POINTER(_AMMediaType), 'pMediaType' )),
    COMMETHOD([], HRESULT, 'IsDiscontinuity'),
    COMMETHOD([], HRESULT, 'SetDiscontinuity',
              ( [], c_int, 'bDiscontinuity' )),
    COMMETHOD([], HRESULT, 'GetMediaTime',
              ( ['out'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['out'], POINTER(c_longlong), 'pTimeEnd' )),
    COMMETHOD([], HRESULT, 'SetMediaTime',
              ( ['in'], POINTER(c_longlong), 'pTimeStart' ),
              ( ['in'], POINTER(c_longlong), 'pTimeEnd' )),
]
################################################################
## code template for IMediaSample implementation
##class IMediaSample_Impl(object):
##    def IsDiscontinuity(self):
##        '-no docstring-'
##        #return 
##
##    def IsSyncPoint(self):
##        '-no docstring-'
##        #return 
##
##    def SetMediaTime(self, pTimeStart, pTimeEnd):
##        '-no docstring-'
##        #return 
##
##    def SetPreroll(self, bIsPreroll):
##        '-no docstring-'
##        #return 
##
##    def GetTime(self):
##        '-no docstring-'
##        #return pTimeStart, pTimeEnd
##
##    def SetSyncPoint(self, bIsSyncPoint):
##        '-no docstring-'
##        #return 
##
##    def GetSize(self):
##        '-no docstring-'
##        #return 
##
##    def SetMediaType(self, pMediaType):
##        '-no docstring-'
##        #return 
##
##    def GetMediaType(self, ppMediaType):
##        '-no docstring-'
##        #return 
##
##    def SetTime(self, pTimeStart, pTimeEnd):
##        '-no docstring-'
##        #return 
##
##    def SetActualDataLength(self, __MIDL_0010):
##        '-no docstring-'
##        #return 
##
##    def SetDiscontinuity(self, bDiscontinuity):
##        '-no docstring-'
##        #return 
##
##    def GetActualDataLength(self):
##        '-no docstring-'
##        #return 
##
##    def GetMediaTime(self):
##        '-no docstring-'
##        #return pTimeStart, pTimeEnd
##
##    def GetPointer(self):
##        '-no docstring-'
##        #return ppBuffer
##
##    def IsPreroll(self):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'tagAM_SAMPLE_PROPERTY_FLAGS'
AM_SAMPLE_SPLICEPOINT = 1
AM_SAMPLE_PREROLL = 2
AM_SAMPLE_DATADISCONTINUITY = 4
AM_SAMPLE_TYPECHANGED = 8
AM_SAMPLE_TIMEVALID = 16
AM_SAMPLE_TIMEDISCONTINUITY = 64
AM_SAMPLE_FLUSH_ON_PAUSE = 128
AM_SAMPLE_STOPVALID = 256
AM_SAMPLE_ENDOFSTREAM = 512
AM_STREAM_MEDIA = 0
AM_STREAM_CONTROL = 1
tagAM_SAMPLE_PROPERTY_FLAGS = c_int # enum
class IVMRDeinterlaceControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRDeinterlaceControl Interface'
    _iid_ = GUID('{BB057577-0DB8-4E6A-87A7-1A8C9A505A0F}')
    _idlflags_ = []
class _VMRVideoDesc(Structure):
    pass
class _VMRDeinterlaceCaps(Structure):
    pass
IVMRDeinterlaceControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetNumberOfDeinterlaceModes',
              ( ['in'], POINTER(_VMRVideoDesc), 'lpVideoDescription' ),
              ( ['in', 'out'], POINTER(c_ulong), 'lpdwNumDeinterlaceModes' ),
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'lpDeinterlaceModes' )),
    COMMETHOD([], HRESULT, 'GetDeinterlaceModeCaps',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'lpDeinterlaceMode' ),
              ( ['in'], POINTER(_VMRVideoDesc), 'lpVideoDescription' ),
              ( ['in', 'out'], POINTER(_VMRDeinterlaceCaps), 'lpDeinterlaceCaps' )),
    COMMETHOD([], HRESULT, 'GetDeinterlaceMode',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'lpDeinterlaceMode' )),
    COMMETHOD([], HRESULT, 'SetDeinterlaceMode',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'lpDeinterlaceMode' )),
    COMMETHOD([], HRESULT, 'GetDeinterlacePrefs',
              ( ['out'], POINTER(c_ulong), 'lpdwDeinterlacePrefs' )),
    COMMETHOD([], HRESULT, 'SetDeinterlacePrefs',
              ( ['in'], c_ulong, 'dwDeinterlacePrefs' )),
    COMMETHOD([], HRESULT, 'GetActualDeinterlaceMode',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'lpDeinterlaceMode' )),
]
################################################################
## code template for IVMRDeinterlaceControl implementation
##class IVMRDeinterlaceControl_Impl(object):
##    def GetDeinterlaceMode(self, dwStreamId):
##        '-no docstring-'
##        #return lpDeinterlaceMode
##
##    def GetDeinterlaceModeCaps(self, lpDeinterlaceMode, lpVideoDescription):
##        '-no docstring-'
##        #return lpDeinterlaceCaps
##
##    def GetNumberOfDeinterlaceModes(self, lpVideoDescription):
##        '-no docstring-'
##        #return lpdwNumDeinterlaceModes, lpDeinterlaceModes
##
##    def SetDeinterlaceMode(self, dwStreamId, lpDeinterlaceMode):
##        '-no docstring-'
##        #return 
##
##    def GetDeinterlacePrefs(self):
##        '-no docstring-'
##        #return lpdwDeinterlacePrefs
##
##    def GetActualDeinterlaceMode(self, dwStreamId):
##        '-no docstring-'
##        #return lpDeinterlaceMode
##
##    def SetDeinterlacePrefs(self, dwDeinterlacePrefs):
##        '-no docstring-'
##        #return 
##

class IAMTimecodeReader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9B496CE1-811B-11CF-8C77-00AA006B6814}')
    _idlflags_ = []
class tagTIMECODE_SAMPLE(Structure):
    pass
IAMTimecodeReader._methods_ = [
    COMMETHOD([], HRESULT, 'GetTCRMode',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTCRMode',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'put_VITCLine',
              ( ['in'], c_int, 'Line' )),
    COMMETHOD([], HRESULT, 'get_VITCLine',
              ( ['out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([], HRESULT, 'GetTimecode',
              ( ['out'], POINTER(tagTIMECODE_SAMPLE), 'pTimecodeSample' )),
]
################################################################
## code template for IAMTimecodeReader implementation
##class IAMTimecodeReader_Impl(object):
##    def GetTCRMode(self, Param):
##        '-no docstring-'
##        #return pValue
##
##    def put_VITCLine(self, Line):
##        '-no docstring-'
##        #return 
##
##    def SetTCRMode(self, Param, Value):
##        '-no docstring-'
##        #return 
##
##    def get_VITCLine(self):
##        '-no docstring-'
##        #return pLine
##
##    def GetTimecode(self):
##        '-no docstring-'
##        #return pTimecodeSample
##


# values for enumeration 'tagCameraControlProperty'
CameraControl_Pan = 0
CameraControl_Tilt = 1
CameraControl_Roll = 2
CameraControl_Zoom = 3
CameraControl_Exposure = 4
CameraControl_Iris = 5
CameraControl_Focus = 6
tagCameraControlProperty = c_int # enum

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0164_0002'
VfwCompressDialog_Config = 1
VfwCompressDialog_About = 2
VfwCompressDialog_QueryConfig = 4
VfwCompressDialog_QueryAbout = 8
__MIDL___MIDL_itf_DirectShow_0164_0002 = c_int # enum
VfwCompressDialogs = __MIDL___MIDL_itf_DirectShow_0164_0002

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0145_0001'
AM_FILE_OVERWRITE = 1
__MIDL___MIDL_itf_DirectShow_0145_0001 = c_int # enum
class IAMLatency(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{62EA93BA-EC62-11D2-B770-00C04FB6BD3D}')
    _idlflags_ = []
class IAMPushSource(IAMLatency):
    _case_insensitive_ = True
    _iid_ = GUID('{F185FE76-E64E-11D2-B76E-00C04FB6BD3D}')
    _idlflags_ = []
IAMLatency._methods_ = [
    COMMETHOD([], HRESULT, 'GetLatency',
              ( ['in'], POINTER(c_longlong), 'prtLatency' )),
]
################################################################
## code template for IAMLatency implementation
##class IAMLatency_Impl(object):
##    def GetLatency(self, prtLatency):
##        '-no docstring-'
##        #return 
##

IAMPushSource._methods_ = [
    COMMETHOD([], HRESULT, 'GetPushSourceFlags',
              ( ['out'], POINTER(c_ulong), 'pFlags' )),
    COMMETHOD([], HRESULT, 'SetPushSourceFlags',
              ( ['in'], c_ulong, 'Flags' )),
    COMMETHOD([], HRESULT, 'SetStreamOffset',
              ( ['in'], c_longlong, 'rtOffset' )),
    COMMETHOD([], HRESULT, 'GetStreamOffset',
              ( ['out'], POINTER(c_longlong), 'prtOffset' )),
    COMMETHOD([], HRESULT, 'GetMaxStreamOffset',
              ( ['out'], POINTER(c_longlong), 'prtMaxOffset' )),
    COMMETHOD([], HRESULT, 'SetMaxStreamOffset',
              ( ['in'], c_longlong, 'rtMaxOffset' )),
]
################################################################
## code template for IAMPushSource implementation
##class IAMPushSource_Impl(object):
##    def SetMaxStreamOffset(self, rtMaxOffset):
##        '-no docstring-'
##        #return 
##
##    def GetPushSourceFlags(self):
##        '-no docstring-'
##        #return pFlags
##
##    def GetMaxStreamOffset(self):
##        '-no docstring-'
##        #return prtMaxOffset
##
##    def GetStreamOffset(self):
##        '-no docstring-'
##        #return prtOffset
##
##    def SetPushSourceFlags(self, Flags):
##        '-no docstring-'
##        #return 
##
##    def SetStreamOffset(self, rtOffset):
##        '-no docstring-'
##        #return 
##

class IVPManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVPManager Interface'
    _iid_ = GUID('{AAC18C18-E186-46D2-825D-A1F8DC8E395A}')
    _idlflags_ = []
IVPManager._methods_ = [
    COMMETHOD([], HRESULT, 'SetVideoPortIndex',
              ( ['in'], c_ulong, 'dwVideoPortIndex' )),
    COMMETHOD([], HRESULT, 'GetVideoPortIndex',
              ( ['out'], POINTER(c_ulong), 'pdwVideoPortIndex' )),
]
################################################################
## code template for IVPManager implementation
##class IVPManager_Impl(object):
##    def SetVideoPortIndex(self, dwVideoPortIndex):
##        '-no docstring-'
##        #return 
##
##    def GetVideoPortIndex(self):
##        '-no docstring-'
##        #return pdwVideoPortIndex
##


# values for enumeration 'AM_SEEKING_SeekingFlags'
AM_SEEKING_NoPositioning = 0
AM_SEEKING_AbsolutePositioning = 1
AM_SEEKING_RelativePositioning = 2
AM_SEEKING_IncrementalPositioning = 3
AM_SEEKING_PositioningBitsMask = 3
AM_SEEKING_SeekToKeyFrame = 4
AM_SEEKING_ReturnTime = 8
AM_SEEKING_Segment = 16
AM_SEEKING_NoFlush = 32
AM_SEEKING_SeekingFlags = c_int # enum
class __MIDL___MIDL_itf_DirectShow_0134_0002(Structure):
    pass
REGFILTERPINS = __MIDL___MIDL_itf_DirectShow_0134_0002
class IEnumPins(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86892-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IEnumPins._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cPins' ),
              ( ['out'], POINTER(POINTER(IPin)), 'ppPins' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cPins' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['retval', 'out'], POINTER(POINTER(IEnumPins)), 'ppenum' )),
]
################################################################
## code template for IEnumPins implementation
##class IEnumPins_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cPins):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, cPins):
##        '-no docstring-'
##        #return ppPins, pcFetched
##

class IVMRMixerBitmap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRMixerBitmap Interface'
    _iid_ = GUID('{1E673275-0257-40AA-AF20-7C608D4A0428}')
    _idlflags_ = []
class _VMRALPHABITMAP(Structure):
    pass
IVMRMixerBitmap._methods_ = [
    COMMETHOD([], HRESULT, 'SetAlphaBitmap',
              ( ['in'], POINTER(_VMRALPHABITMAP), 'pBmpParms' )),
    COMMETHOD([], HRESULT, 'UpdateAlphaBitmapParameters',
              ( ['in'], POINTER(_VMRALPHABITMAP), 'pBmpParms' )),
    COMMETHOD([], HRESULT, 'GetAlphaBitmapParameters',
              ( ['out'], POINTER(_VMRALPHABITMAP), 'pBmpParms' )),
]
################################################################
## code template for IVMRMixerBitmap implementation
##class IVMRMixerBitmap_Impl(object):
##    def GetAlphaBitmapParameters(self):
##        '-no docstring-'
##        #return pBmpParms
##
##    def SetAlphaBitmap(self, pBmpParms):
##        '-no docstring-'
##        #return 
##
##    def UpdateAlphaBitmapParameters(self, pBmpParms):
##        '-no docstring-'
##        #return 
##

class IMPEG2StreamIdMap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D0E04C47-25B8-4369-925A-362A01D95444}')
    _idlflags_ = []
class IEnumStreamIdMap(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{945C1566-6202-46FC-96C7-D87F289C6534}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IMPEG2StreamIdMap._methods_ = [
    COMMETHOD([], HRESULT, 'MapStreamId',
              ( ['in'], c_ulong, 'ulStreamId' ),
              ( ['in'], c_ulong, 'MediaSampleContent' ),
              ( ['in'], c_ulong, 'ulSubstreamFilterValue' ),
              ( ['in'], c_int, 'iDataOffset' )),
    COMMETHOD([], HRESULT, 'UnmapStreamId',
              ( ['in'], c_ulong, 'culStreamId' ),
              ( ['in'], POINTER(c_ulong), 'pulStreamId' )),
    COMMETHOD([], HRESULT, 'EnumStreamIdMap',
              ( ['out'], POINTER(POINTER(IEnumStreamIdMap)), 'ppIEnumStreamIdMap' )),
]
################################################################
## code template for IMPEG2StreamIdMap implementation
##class IMPEG2StreamIdMap_Impl(object):
##    def MapStreamId(self, ulStreamId, MediaSampleContent, ulSubstreamFilterValue, iDataOffset):
##        '-no docstring-'
##        #return 
##
##    def EnumStreamIdMap(self):
##        '-no docstring-'
##        #return ppIEnumStreamIdMap
##
##    def UnmapStreamId(self, culStreamId, pulStreamId):
##        '-no docstring-'
##        #return 
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0378_0002'
DeinterlaceTech_Unknown = 0
DeinterlaceTech_BOBLineReplicate = 1
DeinterlaceTech_BOBVerticalStretch = 2
DeinterlaceTech_MedianFiltering = 4
DeinterlaceTech_EdgeFiltering = 16
DeinterlaceTech_FieldAdaptive = 32
DeinterlaceTech_PixelAdaptive = 64
DeinterlaceTech_MotionVectorSteered = 128
__MIDL___MIDL_itf_DirectShow_0378_0002 = c_int # enum
VMRDeinterlaceTech = __MIDL___MIDL_itf_DirectShow_0378_0002
_VMRDeinterlaceCaps._fields_ = [
    ('dwSize', c_ulong),
    ('dwNumPreviousOutputFrames', c_ulong),
    ('dwNumForwardRefSamples', c_ulong),
    ('dwNumBackwardRefSamples', c_ulong),
    ('DeinterlaceTechnology', VMRDeinterlaceTech),
]
assert sizeof(_VMRDeinterlaceCaps) == 20, sizeof(_VMRDeinterlaceCaps)
assert alignment(_VMRDeinterlaceCaps) == 4, alignment(_VMRDeinterlaceCaps)
class IEnumFilters(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86893-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IFilterGraph._methods_ = [
    COMMETHOD([], HRESULT, 'AddFilter',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], WSTRING, 'pName' )),
    COMMETHOD([], HRESULT, 'RemoveFilter',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' )),
    COMMETHOD([], HRESULT, 'EnumFilters',
              ( ['out'], POINTER(POINTER(IEnumFilters)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'FindFilterByName',
              ( ['in'], WSTRING, 'pName' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' )),
    COMMETHOD([], HRESULT, 'ConnectDirect',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IPin), 'ppinIn' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'Reconnect',
              ( ['in'], POINTER(IPin), 'pPin' )),
    COMMETHOD([], HRESULT, 'Disconnect',
              ( ['in'], POINTER(IPin), 'pPin' )),
    COMMETHOD([], HRESULT, 'SetDefaultSyncSource'),
]
################################################################
## code template for IFilterGraph implementation
##class IFilterGraph_Impl(object):
##    def SetDefaultSyncSource(self):
##        '-no docstring-'
##        #return 
##
##    def Disconnect(self, pPin):
##        '-no docstring-'
##        #return 
##
##    def FindFilterByName(self, pName):
##        '-no docstring-'
##        #return ppFilter
##
##    def AddFilter(self, pFilter, pName):
##        '-no docstring-'
##        #return 
##
##    def ConnectDirect(self, ppinOut, ppinIn, pmt):
##        '-no docstring-'
##        #return 
##
##    def RemoveFilter(self, pFilter):
##        '-no docstring-'
##        #return 
##
##    def Reconnect(self, pPin):
##        '-no docstring-'
##        #return 
##
##    def EnumFilters(self):
##        '-no docstring-'
##        #return ppenum
##

class __MIDL___MIDL_itf_DirectShow_0355_0001(Structure):
    pass
STREAM_ID_MAP = __MIDL___MIDL_itf_DirectShow_0355_0001
IEnumStreamIdMap._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cRequest' ),
              ( ['in', 'out'], POINTER(STREAM_ID_MAP), 'pStreamIdMap' ),
              ( ['out'], POINTER(c_ulong), 'pcReceived' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cRecords' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumStreamIdMap)), 'ppIEnumStreamIdMap' )),
]
################################################################
## code template for IEnumStreamIdMap implementation
##class IEnumStreamIdMap_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cRecords):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppIEnumStreamIdMap
##
##    def Next(self, cRequest):
##        '-no docstring-'
##        #return pStreamIdMap, pcReceived
##

__MIDL___MIDL_itf_DirectShow_0355_0001._fields_ = [
    ('stream_id', c_ulong),
    ('dwMediaSampleContent', c_ulong),
    ('ulSubstreamFilterValue', c_ulong),
    ('iDataOffset', c_int),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0355_0001) == 16, sizeof(__MIDL___MIDL_itf_DirectShow_0355_0001)
assert alignment(__MIDL___MIDL_itf_DirectShow_0355_0001) == 4, alignment(__MIDL___MIDL_itf_DirectShow_0355_0001)
class IIPDVDec(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B8E8BD60-0BFE-11D0-AF91-00AA00B67A42}')
    _idlflags_ = []
IIPDVDec._methods_ = [
    COMMETHOD([], HRESULT, 'get_IPDisplay',
              ( ['out'], POINTER(c_int), 'displayPix' )),
    COMMETHOD([], HRESULT, 'put_IPDisplay',
              ( ['in'], c_int, 'displayPix' )),
]
################################################################
## code template for IIPDVDec implementation
##class IIPDVDec_Impl(object):
##    def put_IPDisplay(self, displayPix):
##        '-no docstring-'
##        #return 
##
##    def get_IPDisplay(self):
##        '-no docstring-'
##        #return displayPix
##

class IFilterGraph2(IGraphBuilder):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73882-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IGraphBuilder._methods_ = [
    COMMETHOD([], HRESULT, 'Connect',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IPin), 'ppinIn' )),
    COMMETHOD([], HRESULT, 'Render',
              ( ['in'], POINTER(IPin), 'ppinOut' )),
    COMMETHOD([], HRESULT, 'RenderFile',
              ( ['in'], WSTRING, 'lpcwstrFile' ),
              ( ['in'], WSTRING, 'lpcwstrPlayList' )),
    COMMETHOD([], HRESULT, 'AddSourceFilter',
              ( ['in'], WSTRING, 'lpcwstrFileName' ),
              ( ['in'], WSTRING, 'lpcwstrFilterName' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' )),
    COMMETHOD([], HRESULT, 'SetLogFile',
              ( ['in'], ULONG_PTR, 'hFile' )),
    COMMETHOD([], HRESULT, 'Abort'),
    COMMETHOD([], HRESULT, 'ShouldOperationContinue'),
]
################################################################
## code template for IGraphBuilder implementation
##class IGraphBuilder_Impl(object):
##    def Render(self, ppinOut):
##        '-no docstring-'
##        #return 
##
##    def Abort(self):
##        '-no docstring-'
##        #return 
##
##    def ShouldOperationContinue(self):
##        '-no docstring-'
##        #return 
##
##    def Connect(self, ppinOut, ppinIn):
##        '-no docstring-'
##        #return 
##
##    def SetLogFile(self, hFile):
##        '-no docstring-'
##        #return 
##
##    def RenderFile(self, lpcwstrFile, lpcwstrPlayList):
##        '-no docstring-'
##        #return 
##
##    def AddSourceFilter(self, lpcwstrFileName, lpcwstrFilterName):
##        '-no docstring-'
##        #return ppFilter
##

IFilterGraph2._methods_ = [
    COMMETHOD([], HRESULT, 'AddSourceFilterForMoniker',
              ( ['in'], POINTER(IMoniker), 'pMoniker' ),
              ( ['in'], POINTER(IBindCtx), 'pCtx' ),
              ( ['in'], WSTRING, 'lpcwstrFilterName' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' )),
    COMMETHOD([], HRESULT, 'ReconnectEx',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'RenderEx',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pvContext' )),
]
################################################################
## code template for IFilterGraph2 implementation
##class IFilterGraph2_Impl(object):
##    def AddSourceFilterForMoniker(self, pMoniker, pCtx, lpcwstrFilterName):
##        '-no docstring-'
##        #return ppFilter
##
##    def ReconnectEx(self, pPin, pmt):
##        '-no docstring-'
##        #return 
##
##    def RenderEx(self, ppinOut, dwFlags):
##        '-no docstring-'
##        #return pvContext
##

class _VMRFrequency(Structure):
    pass
_VMRFrequency._fields_ = [
    ('dwNumerator', c_ulong),
    ('dwDenominator', c_ulong),
]
assert sizeof(_VMRFrequency) == 8, sizeof(_VMRFrequency)
assert alignment(_VMRFrequency) == 4, alignment(_VMRFrequency)
_VMRVideoDesc._fields_ = [
    ('dwSize', c_ulong),
    ('dwSampleWidth', c_ulong),
    ('dwSampleHeight', c_ulong),
    ('SingleFieldPerSample', c_int),
    ('dwFourCC', c_ulong),
    ('InputSampleFreq', _VMRFrequency),
    ('OutputFrameFreq', _VMRFrequency),
]
assert sizeof(_VMRVideoDesc) == 36, sizeof(_VMRVideoDesc)
assert alignment(_VMRVideoDesc) == 4, alignment(_VMRVideoDesc)
class IAMVideoProcAmp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13360-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMVideoProcAmp._methods_ = [
    COMMETHOD([], HRESULT, 'GetRange',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'pMin' ),
              ( ['out'], POINTER(c_int), 'pMax' ),
              ( ['out'], POINTER(c_int), 'pSteppingDelta' ),
              ( ['out'], POINTER(c_int), 'pDefault' ),
              ( ['out'], POINTER(c_int), 'pCapsFlags' )),
    COMMETHOD([], HRESULT, 'Set',
              ( ['in'], c_int, 'Property' ),
              ( ['in'], c_int, 'lValue' ),
              ( ['in'], c_int, 'Flags' )),
    COMMETHOD([], HRESULT, 'Get',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'lValue' ),
              ( ['out'], POINTER(c_int), 'Flags' )),
]
################################################################
## code template for IAMVideoProcAmp implementation
##class IAMVideoProcAmp_Impl(object):
##    def Set(self, Property, lValue, Flags):
##        '-no docstring-'
##        #return 
##
##    def GetRange(self, Property):
##        '-no docstring-'
##        #return pMin, pMax, pSteppingDelta, pDefault, pCapsFlags
##
##    def Get(self, Property):
##        '-no docstring-'
##        #return lValue, Flags
##


# values for enumeration '_REM_FILTER_FLAGS'
REMFILTERF_LEAVECONNECTED = 1
_REM_FILTER_FLAGS = c_int # enum
class __MIDL___MIDL_itf_DirectShow_0156_0002(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0156_0002._fields_ = [
    ('tStart', c_longlong),
    ('tStop', c_longlong),
    ('dwStartCookie', c_ulong),
    ('dwStopCookie', c_ulong),
    ('dwFlags', c_ulong),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0156_0002) == 32, sizeof(__MIDL___MIDL_itf_DirectShow_0156_0002)
assert alignment(__MIDL___MIDL_itf_DirectShow_0156_0002) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0156_0002)
_VMRALPHABITMAP._fields_ = [
    ('dwFlags', c_ulong),
    ('hdc', wireHDC),
    ('pDDS', POINTER(c_ulong)),
    ('rSrc', tagRECT),
    ('rDest', _NORMALIZEDRECT),
    ('fAlpha', c_float),
    ('clrSrcKey', c_ulong),
]
assert sizeof(_VMRALPHABITMAP) == 64, sizeof(_VMRALPHABITMAP)
assert alignment(_VMRALPHABITMAP) == 8, alignment(_VMRALPHABITMAP)

# values for enumeration '_AMSTREAMSELECTINFOFLAGS'
AMSTREAMSELECTINFO_ENABLED = 1
AMSTREAMSELECTINFO_EXCLUSIVE = 2
_AMSTREAMSELECTINFOFLAGS = c_int # enum
class _PinInfo(Structure):
    pass
_PinInfo._fields_ = [
    ('pFilter', POINTER(IBaseFilter)),
    ('dir', _PinDirection),
    ('achName', c_ushort * 128),
]
assert sizeof(_PinInfo) == 272, sizeof(_PinInfo)
assert alignment(_PinInfo) == 8, alignment(_PinInfo)
class IAMResourceControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{8389D2D0-77D7-11D1-ABE6-00A0C905F375}')
    _idlflags_ = []
IAMResourceControl._methods_ = [
    COMMETHOD([], HRESULT, 'Reserve',
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_void_p, 'pvReserved' )),
]
################################################################
## code template for IAMResourceControl implementation
##class IAMResourceControl_Impl(object):
##    def Reserve(self, dwFlags, pvReserved):
##        '-no docstring-'
##        #return 
##

class AsyncFileReader(CoClass):
    u'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/filesourceasyncfilter.asp'
    _reg_clsid_ = GUID('{E436EBB5-524F-11CE-9F53-0020AF0BA770}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IFileSourceFilter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A6-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
AsyncFileReader._com_interfaces_ = [IFileSourceFilter, IBaseFilter]

class _RGNDATA(Structure):
    pass
class _RGNDATAHEADER(Structure):
    pass
_RGNDATAHEADER._fields_ = [
    ('dwSize', c_ulong),
    ('iType', c_ulong),
    ('nCount', c_ulong),
    ('nRgnSize', c_ulong),
    ('rcBound', tagRECT),
]
assert sizeof(_RGNDATAHEADER) == 32, sizeof(_RGNDATAHEADER)
assert alignment(_RGNDATAHEADER) == 4, alignment(_RGNDATAHEADER)
_RGNDATA._fields_ = [
    ('rdh', _RGNDATAHEADER),
    ('Buffer', c_char * 1),
]
assert sizeof(_RGNDATA) == 36, sizeof(_RGNDATA)
assert alignment(_RGNDATA) == 4, alignment(_RGNDATA)
class IAMStreamControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73881-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
AM_STREAM_INFO = __MIDL___MIDL_itf_DirectShow_0156_0002
IAMStreamControl._methods_ = [
    COMMETHOD([], HRESULT, 'StartAt',
              ( ['in'], POINTER(c_longlong), 'ptStart' ),
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'StopAt',
              ( ['in'], POINTER(c_longlong), 'ptStop' ),
              ( ['in'], c_int, 'bSendExtra' ),
              ( ['in'], c_ulong, 'dwCookie' )),
    COMMETHOD([], HRESULT, 'GetInfo',
              ( ['out'], POINTER(AM_STREAM_INFO), 'pInfo' )),
]
################################################################
## code template for IAMStreamControl implementation
##class IAMStreamControl_Impl(object):
##    def StopAt(self, ptStop, bSendExtra, dwCookie):
##        '-no docstring-'
##        #return 
##
##    def StartAt(self, ptStart, dwCookie):
##        '-no docstring-'
##        #return 
##
##    def GetInfo(self):
##        '-no docstring-'
##        #return pInfo
##

class IVMRMixerControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRMixerControl Interface'
    _iid_ = GUID('{1C1A17B0-BED0-415D-974B-DC6696131599}')
    _idlflags_ = []
IVMRMixerControl._methods_ = [
    COMMETHOD([], HRESULT, 'SetAlpha',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], c_float, 'Alpha' )),
    COMMETHOD([], HRESULT, 'GetAlpha',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(c_float), 'pAlpha' )),
    COMMETHOD([], HRESULT, 'SetZOrder',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], c_ulong, 'dwZ' )),
    COMMETHOD([], HRESULT, 'GetZOrder',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(c_ulong), 'pZ' )),
    COMMETHOD([], HRESULT, 'SetOutputRect',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['in'], POINTER(_NORMALIZEDRECT), 'pRect' )),
    COMMETHOD([], HRESULT, 'GetOutputRect',
              ( ['in'], c_ulong, 'dwStreamId' ),
              ( ['out'], POINTER(_NORMALIZEDRECT), 'pRect' )),
    COMMETHOD([], HRESULT, 'SetBackgroundClr',
              ( ['in'], c_ulong, 'ClrBkg' )),
    COMMETHOD([], HRESULT, 'GetBackgroundClr',
              ( ['in'], POINTER(c_ulong), 'lpClrBkg' )),
    COMMETHOD([], HRESULT, 'SetMixingPrefs',
              ( ['in'], c_ulong, 'dwMixerPrefs' )),
    COMMETHOD([], HRESULT, 'GetMixingPrefs',
              ( ['out'], POINTER(c_ulong), 'pdwMixerPrefs' )),
]
################################################################
## code template for IVMRMixerControl implementation
##class IVMRMixerControl_Impl(object):
##    def GetBackgroundClr(self, lpClrBkg):
##        '-no docstring-'
##        #return 
##
##    def GetZOrder(self, dwStreamId):
##        '-no docstring-'
##        #return pZ
##
##    def SetOutputRect(self, dwStreamId, pRect):
##        '-no docstring-'
##        #return 
##
##    def GetOutputRect(self, dwStreamId):
##        '-no docstring-'
##        #return pRect
##
##    def GetMixingPrefs(self):
##        '-no docstring-'
##        #return pdwMixerPrefs
##
##    def SetMixingPrefs(self, dwMixerPrefs):
##        '-no docstring-'
##        #return 
##
##    def SetAlpha(self, dwStreamId, Alpha):
##        '-no docstring-'
##        #return 
##
##    def GetAlpha(self, dwStreamId):
##        '-no docstring-'
##        #return pAlpha
##
##    def SetBackgroundClr(self, ClrBkg):
##        '-no docstring-'
##        #return 
##
##    def SetZOrder(self, dwStreamId, dwZ):
##        '-no docstring-'
##        #return 
##

class AviMux(CoClass):
    _reg_clsid_ = GUID('{E2510970-F137-11CE-8B67-00AA00A3F1A6}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IConfigAviMux(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{5ACD6AA0-F482-11CE-8B67-00AA00A3F1A6}')
    _idlflags_ = []
AviMux._com_interfaces_ = [IConfigAviMux, IBaseFilter]

class IAMExtTransport(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A03CD5F0-3045-11CF-8C44-00AA006B6814}')
    _idlflags_ = []
IAMExtTransport._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapability',
              ( ['in'], c_int, 'Capability' ),
              ( ['out'], POINTER(c_int), 'pValue' ),
              ( ['out'], POINTER(c_double), 'pdblValue' )),
    COMMETHOD([], HRESULT, 'put_MediaState',
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'get_MediaState',
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'put_LocalControl',
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'get_LocalControl',
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'GetStatus',
              ( ['in'], c_int, 'StatusItem' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'GetTransportBasicParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' ),
              ( ['out'], POINTER(WSTRING), 'ppszData' )),
    COMMETHOD([], HRESULT, 'SetTransportBasicParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' ),
              ( ['in'], WSTRING, 'pszData' )),
    COMMETHOD([], HRESULT, 'GetTransportVideoParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTransportVideoParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'GetTransportAudioParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTransportAudioParameters',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'put_Mode',
              ( ['in'], c_int, 'mode' )),
    COMMETHOD([], HRESULT, 'get_Mode',
              ( ['out'], POINTER(c_int), 'pMode' )),
    COMMETHOD([], HRESULT, 'put_Rate',
              ( ['in'], c_double, 'dblRate' )),
    COMMETHOD([], HRESULT, 'get_Rate',
              ( ['out'], POINTER(c_double), 'pdblRate' )),
    COMMETHOD([], HRESULT, 'GetChase',
              ( ['out'], POINTER(c_int), 'pEnabled' ),
              ( ['out'], POINTER(c_int), 'pOffset' ),
              ( ['out'], POINTER(ULONG_PTR), 'phEvent' )),
    COMMETHOD([], HRESULT, 'SetChase',
              ( ['in'], c_int, 'Enable' ),
              ( ['in'], c_int, 'Offset' ),
              ( ['in'], ULONG_PTR, 'hEvent' )),
    COMMETHOD([], HRESULT, 'GetBump',
              ( ['out'], POINTER(c_int), 'pSpeed' ),
              ( ['out'], POINTER(c_int), 'pDuration' )),
    COMMETHOD([], HRESULT, 'SetBump',
              ( ['in'], c_int, 'Speed' ),
              ( ['in'], c_int, 'Duration' )),
    COMMETHOD([], HRESULT, 'get_AntiClogControl',
              ( ['out'], POINTER(c_int), 'pEnabled' )),
    COMMETHOD([], HRESULT, 'put_AntiClogControl',
              ( ['in'], c_int, 'Enable' )),
    COMMETHOD([], HRESULT, 'GetEditPropertySet',
              ( ['in'], c_int, 'EditID' ),
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'SetEditPropertySet',
              ( ['in', 'out'], POINTER(c_int), 'pEditID' ),
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'GetEditProperty',
              ( ['in'], c_int, 'EditID' ),
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetEditProperty',
              ( ['in'], c_int, 'EditID' ),
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'get_EditStart',
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'put_EditStart',
              ( ['in'], c_int, 'Value' )),
]
################################################################
## code template for IAMExtTransport implementation
##class IAMExtTransport_Impl(object):
##    def GetTransportAudioParameters(self, Param):
##        '-no docstring-'
##        #return pValue
##
##    def GetBump(self):
##        '-no docstring-'
##        #return pSpeed, pDuration
##
##    def SetBump(self, Speed, Duration):
##        '-no docstring-'
##        #return 
##
##    def GetEditPropertySet(self, EditID):
##        '-no docstring-'
##        #return pState
##
##    def SetTransportBasicParameters(self, Param, Value, pszData):
##        '-no docstring-'
##        #return 
##
##    def SetChase(self, Enable, Offset, hEvent):
##        '-no docstring-'
##        #return 
##
##    def put_Mode(self, mode):
##        '-no docstring-'
##        #return 
##
##    def put_EditStart(self, Value):
##        '-no docstring-'
##        #return 
##
##    def put_Rate(self, dblRate):
##        '-no docstring-'
##        #return 
##
##    def GetTransportBasicParameters(self, Param):
##        '-no docstring-'
##        #return pValue, ppszData
##
##    def put_LocalControl(self, State):
##        '-no docstring-'
##        #return 
##
##    def GetTransportVideoParameters(self, Param):
##        '-no docstring-'
##        #return pValue
##
##    def SetEditPropertySet(self, State):
##        '-no docstring-'
##        #return pEditID
##
##    def get_AntiClogControl(self):
##        '-no docstring-'
##        #return pEnabled
##
##    def put_MediaState(self, State):
##        '-no docstring-'
##        #return 
##
##    def SetTransportAudioParameters(self, Param, Value):
##        '-no docstring-'
##        #return 
##
##    def GetStatus(self, StatusItem):
##        '-no docstring-'
##        #return pValue
##
##    def get_EditStart(self):
##        '-no docstring-'
##        #return pValue
##
##    def get_Rate(self):
##        '-no docstring-'
##        #return pdblRate
##
##    def put_AntiClogControl(self, Enable):
##        '-no docstring-'
##        #return 
##
##    def GetEditProperty(self, EditID, Param):
##        '-no docstring-'
##        #return pValue
##
##    def get_Mode(self):
##        '-no docstring-'
##        #return pMode
##
##    def GetCapability(self, Capability):
##        '-no docstring-'
##        #return pValue, pdblValue
##
##    def GetChase(self):
##        '-no docstring-'
##        #return pEnabled, pOffset, phEvent
##
##    def SetTransportVideoParameters(self, Param, Value):
##        '-no docstring-'
##        #return 
##
##    def get_MediaState(self):
##        '-no docstring-'
##        #return pState
##
##    def SetEditProperty(self, EditID, Param, Value):
##        '-no docstring-'
##        #return 
##
##    def get_LocalControl(self):
##        '-no docstring-'
##        #return pState
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0371_0001'
AMAP_PIXELFORMAT_VALID = 1
AMAP_3D_TARGET = 2
AMAP_ALLOW_SYSMEM = 4
AMAP_FORCE_SYSMEM = 8
AMAP_DIRECTED_FLIP = 16
AMAP_DXVA_TARGET = 32
__MIDL___MIDL_itf_DirectShow_0371_0001 = c_int # enum
VMRSurfaceAllocationFlags = __MIDL___MIDL_itf_DirectShow_0371_0001
class IVideoFrameStep(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{E46A9787-2B71-444D-A4B5-1FAB7B708D6A}')
    _idlflags_ = []
IVideoFrameStep._methods_ = [
    COMMETHOD([], HRESULT, 'Step',
              ( [], c_ulong, 'dwFrames' ),
              ( [], POINTER(IUnknown), 'pStepObject' )),
    COMMETHOD([], HRESULT, 'CanStep',
              ( [], c_int, 'bMultiple' ),
              ( [], POINTER(IUnknown), 'pStepObject' )),
    COMMETHOD([], HRESULT, 'CancelStep'),
]
################################################################
## code template for IVideoFrameStep implementation
##class IVideoFrameStep_Impl(object):
##    def Step(self, dwFrames, pStepObject):
##        '-no docstring-'
##        #return 
##
##    def CancelStep(self):
##        '-no docstring-'
##        #return 
##
##    def CanStep(self, bMultiple, pStepObject):
##        '-no docstring-'
##        #return 
##

class IAMStreamSelect(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C1960960-17F5-11D1-ABE1-00A0C905F375}')
    _idlflags_ = []
IAMStreamSelect._methods_ = [
    COMMETHOD([], HRESULT, 'Count',
              ( ['out'], POINTER(c_ulong), 'pcStreams' )),
    COMMETHOD([], HRESULT, 'Info',
              ( ['in'], c_int, 'lIndex' ),
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppmt' ),
              ( ['out'], POINTER(c_ulong), 'pdwFlags' ),
              ( ['out'], POINTER(c_ulong), 'plcid' ),
              ( ['out'], POINTER(c_ulong), 'pdwGroup' ),
              ( ['out'], POINTER(POINTER(c_ushort)), 'ppszName' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppObject' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'Enable',
              ( ['in'], c_int, 'lIndex' ),
              ( ['in'], c_ulong, 'dwFlags' )),
]
################################################################
## code template for IAMStreamSelect implementation
##class IAMStreamSelect_Impl(object):
##    def Count(self):
##        '-no docstring-'
##        #return pcStreams
##
##    def Info(self, lIndex):
##        '-no docstring-'
##        #return ppmt, pdwFlags, plcid, pdwGroup, ppszName, ppObject, ppunk
##
##    def Enable(self, lIndex, dwFlags):
##        '-no docstring-'
##        #return 
##

class IVMRSurfaceAllocatorNotify(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRSurfaceAllocatorNotify Interface'
    _iid_ = GUID('{AADA05A8-5A4E-4729-AF0B-CEA27AED51E2}')
    _idlflags_ = []
class IVMRSurfaceAllocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRSurfaceAllocator Interface'
    _iid_ = GUID('{31CE832E-4484-458B-8CCA-F4D7E3DB0B52}')
    _idlflags_ = []
IVMRSurfaceAllocatorNotify._methods_ = [
    COMMETHOD([], HRESULT, 'AdviseSurfaceAllocator',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(IVMRSurfaceAllocator), 'lpIVRMSurfaceAllocator' )),
    COMMETHOD([], HRESULT, 'SetDDrawDevice',
              ( ['in'], POINTER(c_ulong), 'lpDDrawDevice' ),
              ( ['in'], c_void_p, 'hMonitor' )),
    COMMETHOD([], HRESULT, 'ChangeDDrawDevice',
              ( ['in'], POINTER(c_ulong), 'lpDDrawDevice' ),
              ( ['in'], c_void_p, 'hMonitor' )),
    COMMETHOD([], HRESULT, 'RestoreDDrawSurfaces'),
    COMMETHOD([], HRESULT, 'NotifyEvent',
              ( ['in'], c_int, 'EventCode' ),
              ( ['in'], LONG_PTR, 'Param1' ),
              ( ['in'], LONG_PTR, 'Param2' )),
    COMMETHOD([], HRESULT, 'SetBorderColor',
              ( ['in'], c_ulong, 'clrBorder' )),
]
################################################################
## code template for IVMRSurfaceAllocatorNotify implementation
##class IVMRSurfaceAllocatorNotify_Impl(object):
##    def SetBorderColor(self, clrBorder):
##        '-no docstring-'
##        #return 
##
##    def NotifyEvent(self, EventCode, Param1, Param2):
##        '-no docstring-'
##        #return 
##
##    def RestoreDDrawSurfaces(self):
##        '-no docstring-'
##        #return 
##
##    def AdviseSurfaceAllocator(self, dwUserID, lpIVRMSurfaceAllocator):
##        '-no docstring-'
##        #return 
##
##    def ChangeDDrawDevice(self, lpDDrawDevice, hMonitor):
##        '-no docstring-'
##        #return 
##
##    def SetDDrawDevice(self, lpDDrawDevice, hMonitor):
##        '-no docstring-'
##        #return 
##

class IAMAudioRendererStats(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{22320CB2-D41A-11D2-BF7C-D7CB9DF0BF93}')
    _idlflags_ = []
IAMAudioRendererStats._methods_ = [
    COMMETHOD([], HRESULT, 'GetStatParam',
              ( ['in'], c_ulong, 'dwParam' ),
              ( ['out'], POINTER(c_ulong), 'pdwParam1' ),
              ( ['out'], POINTER(c_ulong), 'pdwParam2' )),
]
################################################################
## code template for IAMAudioRendererStats implementation
##class IAMAudioRendererStats_Impl(object):
##    def GetStatParam(self, dwParam):
##        '-no docstring-'
##        #return pdwParam1, pdwParam2
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0163_0001'
CompressionCaps_CanQuality = 1
CompressionCaps_CanCrunch = 2
CompressionCaps_CanKeyFrame = 4
CompressionCaps_CanBFrame = 8
CompressionCaps_CanWindow = 16
__MIDL___MIDL_itf_DirectShow_0163_0001 = c_int # enum
class IMemAllocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689C-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMemAllocator._methods_ = [
    COMMETHOD([], HRESULT, 'SetProperties',
              ( ['in'], POINTER(_AllocatorProperties), 'pRequest' ),
              ( ['out'], POINTER(_AllocatorProperties), 'pActual' )),
    COMMETHOD([], HRESULT, 'GetProperties',
              ( ['out'], POINTER(_AllocatorProperties), 'pProps' )),
    COMMETHOD([], HRESULT, 'Commit'),
    COMMETHOD([], HRESULT, 'Decommit'),
    COMMETHOD([], HRESULT, 'GetBuffer',
              ( ['out'], POINTER(POINTER(IMediaSample)), 'ppBuffer' ),
              ( ['in'], POINTER(c_longlong), 'pStartTime' ),
              ( ['in'], POINTER(c_longlong), 'pEndTime' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'ReleaseBuffer',
              ( ['in'], POINTER(IMediaSample), 'pBuffer' )),
]
################################################################
## code template for IMemAllocator implementation
##class IMemAllocator_Impl(object):
##    def ReleaseBuffer(self, pBuffer):
##        '-no docstring-'
##        #return 
##
##    def Decommit(self):
##        '-no docstring-'
##        #return 
##
##    def GetProperties(self):
##        '-no docstring-'
##        #return pProps
##
##    def Commit(self):
##        '-no docstring-'
##        #return 
##
##    def SetProperties(self, pRequest):
##        '-no docstring-'
##        #return pActual
##
##    def GetBuffer(self, pStartTime, pEndTime, dwFlags):
##        '-no docstring-'
##        #return ppBuffer
##

class IReferenceClock(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A86897-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IReferenceClock._methods_ = [
    COMMETHOD([], HRESULT, 'GetTime',
              ( ['out'], POINTER(c_longlong), 'pTime' )),
    COMMETHOD([], HRESULT, 'AdviseTime',
              ( ['in'], c_longlong, 'baseTime' ),
              ( ['in'], c_longlong, 'streamTime' ),
              ( ['in'], ULONG_PTR, 'hEvent' ),
              ( ['out'], POINTER(ULONG_PTR), 'pdwAdviseCookie' )),
    COMMETHOD([], HRESULT, 'AdvisePeriodic',
              ( ['in'], c_longlong, 'startTime' ),
              ( ['in'], c_longlong, 'periodTime' ),
              ( ['in'], ULONG_PTR, 'hSemaphore' ),
              ( ['out'], POINTER(ULONG_PTR), 'pdwAdviseCookie' )),
    COMMETHOD([], HRESULT, 'Unadvise',
              ( ['in'], ULONG_PTR, 'dwAdviseCookie' )),
]
################################################################
## code template for IReferenceClock implementation
##class IReferenceClock_Impl(object):
##    def GetTime(self):
##        '-no docstring-'
##        #return pTime
##
##    def AdvisePeriodic(self, startTime, periodTime, hSemaphore):
##        '-no docstring-'
##        #return pdwAdviseCookie
##
##    def AdviseTime(self, baseTime, streamTime, hEvent):
##        '-no docstring-'
##        #return pdwAdviseCookie
##
##    def Unadvise(self, dwAdviseCookie):
##        '-no docstring-'
##        #return 
##

class IFilterMapper2(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B79BB0B0-33C1-11D1-ABE1-00A0C905F375}')
    _idlflags_ = []
class IFilterMapper3(IFilterMapper2):
    _case_insensitive_ = True
    _iid_ = GUID('{B79BB0B1-33C1-11D1-ABE1-00A0C905F375}')
    _idlflags_ = []
IFilterMapper2._methods_ = [
    COMMETHOD([], HRESULT, 'CreateCategory',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'clsidCategory' ),
              ( ['in'], c_ulong, 'dwCategoryMerit' ),
              ( ['in'], WSTRING, 'Description' )),
    COMMETHOD([], HRESULT, 'UnregisterFilter',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pclsidCategory' ),
              ( ['in'], POINTER(c_ushort), 'szInstance' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Filter' )),
    COMMETHOD([], HRESULT, 'RegisterFilter',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'clsidFilter' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['in', 'out'], POINTER(POINTER(IMoniker)), 'ppMoniker' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pclsidCategory' ),
              ( ['in'], POINTER(c_ushort), 'szInstance' ),
              ( ['in'], POINTER(REGFILTER2), 'prf2' )),
    COMMETHOD([], HRESULT, 'EnumMatchingFilters',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_int, 'bExactMatch' ),
              ( ['in'], c_ulong, 'dwMerit' ),
              ( ['in'], c_int, 'bInputNeeded' ),
              ( ['in'], c_ulong, 'cInputTypes' ),
              ( [], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pInputTypes' ),
              ( ['in'], POINTER(REGPINMEDIUM), 'pMedIn' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pPinCategoryIn' ),
              ( ['in'], c_int, 'bRender' ),
              ( ['in'], c_int, 'bOutputNeeded' ),
              ( ['in'], c_ulong, 'cOutputTypes' ),
              ( [], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pOutputTypes' ),
              ( ['in'], POINTER(REGPINMEDIUM), 'pMedOut' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pPinCategoryOut' )),
]
################################################################
## code template for IFilterMapper2 implementation
##class IFilterMapper2_Impl(object):
##    def UnregisterFilter(self, pclsidCategory, szInstance, Filter):
##        '-no docstring-'
##        #return 
##
##    def CreateCategory(self, clsidCategory, dwCategoryMerit, Description):
##        '-no docstring-'
##        #return 
##
##    def EnumMatchingFilters(self, dwFlags, bExactMatch, dwMerit, bInputNeeded, cInputTypes, pInputTypes, pMedIn, pPinCategoryIn, bRender, bOutputNeeded, cOutputTypes, pOutputTypes, pMedOut, pPinCategoryOut):
##        '-no docstring-'
##        #return ppenum
##
##    def RegisterFilter(self, clsidFilter, Name, pclsidCategory, szInstance, prf2):
##        '-no docstring-'
##        #return ppMoniker
##

class ICreateDevEnum(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{29840822-5B84-11D0-BD3B-00A0C911CE86}')
    _idlflags_ = []
IFilterMapper3._methods_ = [
    COMMETHOD([], HRESULT, 'GetICreateDevEnum',
              ( ['out'], POINTER(POINTER(ICreateDevEnum)), 'ppenum' )),
]
################################################################
## code template for IFilterMapper3 implementation
##class IFilterMapper3_Impl(object):
##    def GetICreateDevEnum(self):
##        '-no docstring-'
##        #return ppenum
##

IAMCopyCaptureFileProgress._methods_ = [
    COMMETHOD([], HRESULT, 'Progress',
              ( ['in'], c_int, 'iProgress' )),
]
################################################################
## code template for IAMCopyCaptureFileProgress implementation
##class IAMCopyCaptureFileProgress_Impl(object):
##    def Progress(self, iProgress):
##        '-no docstring-'
##        #return 
##

class IAMTimecodeGenerator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9B496CE0-811B-11CF-8C77-00AA006B6814}')
    _idlflags_ = []
IAMTimecodeGenerator._methods_ = [
    COMMETHOD([], HRESULT, 'GetTCGMode',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTCGMode',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
    COMMETHOD([], HRESULT, 'put_VITCLine',
              ( ['in'], c_int, 'Line' )),
    COMMETHOD([], HRESULT, 'get_VITCLine',
              ( ['out'], POINTER(c_int), 'pLine' )),
    COMMETHOD([], HRESULT, 'SetTimecode',
              ( ['in'], POINTER(tagTIMECODE_SAMPLE), 'pTimecodeSample' )),
    COMMETHOD([], HRESULT, 'GetTimecode',
              ( ['out'], POINTER(tagTIMECODE_SAMPLE), 'pTimecodeSample' )),
]
################################################################
## code template for IAMTimecodeGenerator implementation
##class IAMTimecodeGenerator_Impl(object):
##    def get_VITCLine(self):
##        '-no docstring-'
##        #return pLine
##
##    def SetTCGMode(self, Param, Value):
##        '-no docstring-'
##        #return 
##
##    def GetTimecode(self):
##        '-no docstring-'
##        #return pTimecodeSample
##
##    def put_VITCLine(self, Line):
##        '-no docstring-'
##        #return 
##
##    def GetTCGMode(self, Param):
##        '-no docstring-'
##        #return pValue
##
##    def SetTimecode(self, pTimecodeSample):
##        '-no docstring-'
##        #return 
##

class IAMCrossbar(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13380-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMCrossbar._methods_ = [
    COMMETHOD([], HRESULT, 'get_PinCounts',
              ( ['out'], POINTER(c_int), 'OutputPinCount' ),
              ( ['out'], POINTER(c_int), 'InputPinCount' )),
    COMMETHOD([], HRESULT, 'CanRoute',
              ( ['in'], c_int, 'OutputPinIndex' ),
              ( ['in'], c_int, 'InputPinIndex' )),
    COMMETHOD([], HRESULT, 'Route',
              ( ['in'], c_int, 'OutputPinIndex' ),
              ( ['in'], c_int, 'InputPinIndex' )),
    COMMETHOD([], HRESULT, 'get_IsRoutedTo',
              ( ['in'], c_int, 'OutputPinIndex' ),
              ( ['out'], POINTER(c_int), 'InputPinIndex' )),
    COMMETHOD([], HRESULT, 'get_CrossbarPinInfo',
              ( ['in'], c_int, 'IsInputPin' ),
              ( ['in'], c_int, 'PinIndex' ),
              ( ['out'], POINTER(c_int), 'PinIndexRelated' ),
              ( ['out'], POINTER(c_int), 'PhysicalType' )),
]
################################################################
## code template for IAMCrossbar implementation
##class IAMCrossbar_Impl(object):
##    def get_PinCounts(self):
##        '-no docstring-'
##        #return OutputPinCount, InputPinCount
##
##    def Route(self, OutputPinIndex, InputPinIndex):
##        '-no docstring-'
##        #return 
##
##    def get_IsRoutedTo(self, OutputPinIndex):
##        '-no docstring-'
##        #return InputPinIndex
##
##    def get_CrossbarPinInfo(self, IsInputPin, PinIndex):
##        '-no docstring-'
##        #return PinIndexRelated, PhysicalType
##
##    def CanRoute(self, OutputPinIndex, InputPinIndex):
##        '-no docstring-'
##        #return 
##

class IQualityControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A5-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class tagQuality(Structure):
    pass

# values for enumeration 'tagQualityMessageType'
Famine = 0
Flood = 1
tagQualityMessageType = c_int # enum
tagQuality._fields_ = [
    ('type', tagQualityMessageType),
    ('Proportion', c_int),
    ('Late', c_longlong),
    ('TimeStamp', c_longlong),
]
assert sizeof(tagQuality) == 24, sizeof(tagQuality)
assert alignment(tagQuality) == 8, alignment(tagQuality)
IQualityControl._methods_ = [
    COMMETHOD([], HRESULT, 'Notify',
              ( ['in'], POINTER(IBaseFilter), 'pSelf' ),
              ( ['in'], tagQuality, 'q' )),
    COMMETHOD([], HRESULT, 'SetSink',
              ( ['in'], POINTER(IQualityControl), 'piqc' )),
]
################################################################
## code template for IQualityControl implementation
##class IQualityControl_Impl(object):
##    def Notify(self, pSelf, q):
##        '-no docstring-'
##        #return 
##
##    def SetSink(self, piqc):
##        '-no docstring-'
##        #return 
##

class IGetCapabilitiesKey(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A8809222-07BB-48EA-951C-33158100625B}')
    _idlflags_ = []
IGetCapabilitiesKey._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapabilitiesKey',
              ( ['out'], POINTER(c_void_p), 'pHKey' )),
]
################################################################
## code template for IGetCapabilitiesKey implementation
##class IGetCapabilitiesKey_Impl(object):
##    def GetCapabilitiesKey(self):
##        '-no docstring-'
##        #return pHKey
##

class IMemAllocatorNotifyCallbackTemp(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{92980B30-C1DE-11D2-ABF5-00A0C905F375}')
    _idlflags_ = []
IMemAllocatorNotifyCallbackTemp._methods_ = [
    COMMETHOD([], HRESULT, 'NotifyRelease'),
]
################################################################
## code template for IMemAllocatorNotifyCallbackTemp implementation
##class IMemAllocatorNotifyCallbackTemp_Impl(object):
##    def NotifyRelease(self):
##        '-no docstring-'
##        #return 
##

class IAMTunerNotification(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8760-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []

# values for enumeration 'tagAMTunerEventType'
AMTUNER_EVENT_CHANGED = 1
tagAMTunerEventType = c_int # enum
IAMTunerNotification._methods_ = [
    COMMETHOD([], HRESULT, 'OnEvent',
              ( ['in'], tagAMTunerEventType, 'Event' )),
]
################################################################
## code template for IAMTunerNotification implementation
##class IAMTunerNotification_Impl(object):
##    def OnEvent(self, Event):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'tagVideoControlFlags'
VideoControlFlag_FlipHorizontal = 1
VideoControlFlag_FlipVertical = 2
VideoControlFlag_ExternalTriggerEnable = 4
VideoControlFlag_Trigger = 8
tagVideoControlFlags = c_int # enum
class IAMOverlayFX(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{62FAE250-7E65-4460-BFC9-6398B322073C}')
    _idlflags_ = []
IAMOverlayFX._methods_ = [
    COMMETHOD([], HRESULT, 'QueryOverlayFXCaps',
              ( ['out'], POINTER(c_ulong), 'lpdwOverlayFXCaps' )),
    COMMETHOD([], HRESULT, 'SetOverlayFX',
              ( ['in'], c_ulong, 'dwOverlayFX' )),
    COMMETHOD([], HRESULT, 'GetOverlayFX',
              ( ['out'], POINTER(c_ulong), 'lpdwOverlayFX' )),
]
################################################################
## code template for IAMOverlayFX implementation
##class IAMOverlayFX_Impl(object):
##    def GetOverlayFX(self):
##        '-no docstring-'
##        #return lpdwOverlayFX
##
##    def QueryOverlayFXCaps(self):
##        '-no docstring-'
##        #return lpdwOverlayFXCaps
##
##    def SetOverlayFX(self, dwOverlayFX):
##        '-no docstring-'
##        #return 
##

IEnumMoniker._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(POINTER(IMoniker)), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenum' )),
]
################################################################
## code template for IEnumMoniker implementation
##class IEnumMoniker_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class IResourceManager(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AC-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IResourceConsumer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AD-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IResourceManager._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], WSTRING, 'pName' ),
              ( ['in'], c_int, 'cResource' ),
              ( ['out'], POINTER(c_int), 'plToken' )),
    COMMETHOD([], HRESULT, 'RegisterGroup',
              ( ['in'], WSTRING, 'pName' ),
              ( ['in'], c_int, 'cResource' ),
              ( ['in'], POINTER(c_int), 'palTokens' ),
              ( ['out'], POINTER(c_int), 'plToken' )),
    COMMETHOD([], HRESULT, 'RequestResource',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IUnknown), 'pFocusObject' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' )),
    COMMETHOD([], HRESULT, 'NotifyAcquire',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' ),
              ( ['in'], HRESULT, 'hr' )),
    COMMETHOD([], HRESULT, 'NotifyRelease',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' ),
              ( ['in'], c_int, 'bStillWant' )),
    COMMETHOD([], HRESULT, 'CancelRequest',
              ( ['in'], c_int, 'idResource' ),
              ( ['in'], POINTER(IResourceConsumer), 'pConsumer' )),
    COMMETHOD([], HRESULT, 'SetFocus',
              ( ['in'], POINTER(IUnknown), 'pFocusObject' )),
    COMMETHOD([], HRESULT, 'ReleaseFocus',
              ( ['in'], POINTER(IUnknown), 'pFocusObject' )),
]
################################################################
## code template for IResourceManager implementation
##class IResourceManager_Impl(object):
##    def SetFocus(self, pFocusObject):
##        '-no docstring-'
##        #return 
##
##    def NotifyRelease(self, idResource, pConsumer, bStillWant):
##        '-no docstring-'
##        #return 
##
##    def ReleaseFocus(self, pFocusObject):
##        '-no docstring-'
##        #return 
##
##    def NotifyAcquire(self, idResource, pConsumer, hr):
##        '-no docstring-'
##        #return 
##
##    def Register(self, pName, cResource):
##        '-no docstring-'
##        #return plToken
##
##    def CancelRequest(self, idResource, pConsumer):
##        '-no docstring-'
##        #return 
##
##    def RequestResource(self, idResource, pFocusObject, pConsumer):
##        '-no docstring-'
##        #return 
##
##    def RegisterGroup(self, pName, cResource, palTokens):
##        '-no docstring-'
##        #return plToken
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0373_0001'
VMR_ARMODE_NONE = 0
VMR_ARMODE_LETTER_BOX = 1
__MIDL___MIDL_itf_DirectShow_0373_0001 = c_int # enum
VMR_ASPECT_RATIO_MODE = __MIDL___MIDL_itf_DirectShow_0373_0001
IFileSourceFilter._methods_ = [
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], WSTRING, 'pszFileName' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'GetCurFile',
              ( ['out'], POINTER(WSTRING), 'ppszFileName' ),
              ( ['out'], POINTER(_AMMediaType), 'pmt' )),
]
################################################################
## code template for IFileSourceFilter implementation
##class IFileSourceFilter_Impl(object):
##    def Load(self, pszFileName, pmt):
##        '-no docstring-'
##        #return 
##
##    def GetCurFile(self):
##        '-no docstring-'
##        #return ppszFileName, pmt
##

class __MIDL___MIDL_itf_DirectShow_0130_0001(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0130_0001._fields_ = [
    ('clsid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('Name', WSTRING),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0130_0001) == 24, sizeof(__MIDL___MIDL_itf_DirectShow_0130_0001)
assert alignment(__MIDL___MIDL_itf_DirectShow_0130_0001) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0130_0001)
class IEncoderAPI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{70423839-6ACC-4B23-B079-21DBF08156A5}')
    _idlflags_ = []
IEncoderAPI._methods_ = [
    COMMETHOD([], HRESULT, 'IsSupported',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'IsAvailable',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'GetParameterRange',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'ValueMin' ),
              ( ['out'], POINTER(VARIANT), 'ValueMax' ),
              ( ['out'], POINTER(VARIANT), 'SteppingDelta' )),
    COMMETHOD([], HRESULT, 'GetParameterValues',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(POINTER(VARIANT)), 'Values' ),
              ( ['out'], POINTER(c_ulong), 'ValuesCount' )),
    COMMETHOD([], HRESULT, 'GetDefaultValue',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['in'], POINTER(VARIANT), 'Value' )),
]
################################################################
## code template for IEncoderAPI implementation
##class IEncoderAPI_Impl(object):
##    def IsSupported(self, Api):
##        '-no docstring-'
##        #return 
##
##    def SetValue(self, Api, Value):
##        '-no docstring-'
##        #return 
##
##    def GetDefaultValue(self, Api):
##        '-no docstring-'
##        #return Value
##
##    def GetParameterValues(self, Api):
##        '-no docstring-'
##        #return Values, ValuesCount
##
##    def GetValue(self, Api):
##        '-no docstring-'
##        #return Value
##
##    def GetParameterRange(self, Api):
##        '-no docstring-'
##        #return ValueMin, ValueMax, SteppingDelta
##
##    def IsAvailable(self, Api):
##        '-no docstring-'
##        #return 
##

class IVideoEncoder(IEncoderAPI):
    _case_insensitive_ = True
    _iid_ = GUID('{02997C3B-8E1B-460E-9270-545E0DE9563E}')
    _idlflags_ = []
IVideoEncoder._methods_ = [
]
################################################################
## code template for IVideoEncoder implementation
##class IVideoEncoder_Impl(object):

class IAMTVAudio(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{83EC1C30-23D1-11D1-99E6-00A0C9560266}')
    _idlflags_ = []
IAMTVAudio._methods_ = [
    COMMETHOD([], HRESULT, 'GetHardwareSupportedTVAudioModes',
              ( ['out'], POINTER(c_int), 'plModes' )),
    COMMETHOD([], HRESULT, 'GetAvailableTVAudioModes',
              ( ['out'], POINTER(c_int), 'plModes' )),
    COMMETHOD([], HRESULT, 'get_TVAudioMode',
              ( ['out'], POINTER(c_int), 'plMode' )),
    COMMETHOD([], HRESULT, 'put_TVAudioMode',
              ( ['in'], c_int, 'lMode' )),
    COMMETHOD([], HRESULT, 'RegisterNotificationCallBack',
              ( ['in'], POINTER(IAMTunerNotification), 'pNotify' ),
              ( ['in'], c_int, 'lEvents' )),
    COMMETHOD([], HRESULT, 'UnRegisterNotificationCallBack',
              ( [], POINTER(IAMTunerNotification), 'pNotify' )),
]
################################################################
## code template for IAMTVAudio implementation
##class IAMTVAudio_Impl(object):
##    def GetAvailableTVAudioModes(self):
##        '-no docstring-'
##        #return plModes
##
##    def GetHardwareSupportedTVAudioModes(self):
##        '-no docstring-'
##        #return plModes
##
##    def UnRegisterNotificationCallBack(self, pNotify):
##        '-no docstring-'
##        #return 
##
##    def get_TVAudioMode(self):
##        '-no docstring-'
##        #return plMode
##
##    def put_TVAudioMode(self, lMode):
##        '-no docstring-'
##        #return 
##
##    def RegisterNotificationCallBack(self, pNotify, lEvents):
##        '-no docstring-'
##        #return 
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0181_0001'
AMPROPERTY_PIN_CATEGORY = 0
AMPROPERTY_PIN_MEDIUM = 1
__MIDL___MIDL_itf_DirectShow_0181_0001 = c_int # enum

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0374_0001'
MixerPref_NoDecimation = 1
MixerPref_DecimateOutput = 2
MixerPref_DecimateMask = 15
MixerPref_BiLinearFiltering = 16
MixerPref_PointFiltering = 32
MixerPref_FilteringMask = 240
MixerPref_RenderTargetRGB = 256
MixerPref_RenderTargetYUV420 = 512
MixerPref_RenderTargetYUV422 = 1024
MixerPref_RenderTargetYUV444 = 2048
MixerPref_RenderTargetReserved = 61440
MixerPref_RenderTargetMask = 65280
__MIDL___MIDL_itf_DirectShow_0374_0001 = c_int # enum

# values for enumeration '_DVENCODERVIDEOFORMAT'
DVENCODERVIDEOFORMAT_NTSC = 2000
DVENCODERVIDEOFORMAT_PAL = 2001
_DVENCODERVIDEOFORMAT = c_int # enum

# values for enumeration 'tagVideoProcAmpProperty'
VideoProcAmp_Brightness = 0
VideoProcAmp_Contrast = 1
VideoProcAmp_Hue = 2
VideoProcAmp_Saturation = 3
VideoProcAmp_Sharpness = 4
VideoProcAmp_Gamma = 5
VideoProcAmp_ColorEnable = 6
VideoProcAmp_WhiteBalance = 7
VideoProcAmp_BacklightCompensation = 8
VideoProcAmp_Gain = 9
tagVideoProcAmpProperty = c_int # enum
class IPinFlowControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C56E9858-DBF3-4F6B-8119-384AF2060DEB}')
    _idlflags_ = []
IPinFlowControl._methods_ = [
    COMMETHOD([], HRESULT, 'Block',
              ( ['in'], c_ulong, 'dwBlockFlags' ),
              ( ['in'], c_void_p, 'hEvent' )),
]
################################################################
## code template for IPinFlowControl implementation
##class IPinFlowControl_Impl(object):
##    def Block(self, dwBlockFlags, hEvent):
##        '-no docstring-'
##        #return 
##

class IVMRImageCompositor(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRImageCompositor Interface'
    _iid_ = GUID('{7A4FB5AF-479F-4074-BB40-CE6722E43C82}')
    _idlflags_ = []
class _VMRVIDEOSTREAMINFO(Structure):
    pass
IVMRImageCompositor._methods_ = [
    COMMETHOD([], HRESULT, 'InitCompositionTarget',
              ( ['in'], POINTER(IUnknown), 'pD3DDevice' ),
              ( ['in'], POINTER(c_ulong), 'pddsRenderTarget' )),
    COMMETHOD([], HRESULT, 'TermCompositionTarget',
              ( ['in'], POINTER(IUnknown), 'pD3DDevice' ),
              ( ['in'], POINTER(c_ulong), 'pddsRenderTarget' )),
    COMMETHOD([], HRESULT, 'SetStreamMediaType',
              ( ['in'], c_ulong, 'dwStrmID' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' ),
              ( ['in'], c_int, 'fTexture' )),
    COMMETHOD([], HRESULT, 'CompositeImage',
              ( ['in'], POINTER(IUnknown), 'pD3DDevice' ),
              ( ['in'], POINTER(c_ulong), 'pddsRenderTarget' ),
              ( ['in'], POINTER(_AMMediaType), 'pmtRenderTarget' ),
              ( ['in'], c_longlong, 'rtStart' ),
              ( ['in'], c_longlong, 'rtEnd' ),
              ( ['in'], c_ulong, 'dwClrBkGnd' ),
              ( ['in'], POINTER(_VMRVIDEOSTREAMINFO), 'pVideoStreamInfo' ),
              ( ['in'], c_uint, 'cStreams' )),
]
################################################################
## code template for IVMRImageCompositor implementation
##class IVMRImageCompositor_Impl(object):
##    def CompositeImage(self, pD3DDevice, pddsRenderTarget, pmtRenderTarget, rtStart, rtEnd, dwClrBkGnd, pVideoStreamInfo, cStreams):
##        '-no docstring-'
##        #return 
##
##    def SetStreamMediaType(self, dwStrmID, pmt, fTexture):
##        '-no docstring-'
##        #return 
##
##    def TermCompositionTarget(self, pD3DDevice, pddsRenderTarget):
##        '-no docstring-'
##        #return 
##
##    def InitCompositionTarget(self, pD3DDevice, pddsRenderTarget):
##        '-no docstring-'
##        #return 
##

class IMemInputPin(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A8689D-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMemInputPin._methods_ = [
    COMMETHOD([], HRESULT, 'GetAllocator',
              ( ['out'], POINTER(POINTER(IMemAllocator)), 'ppAllocator' )),
    COMMETHOD([], HRESULT, 'NotifyAllocator',
              ( ['in'], POINTER(IMemAllocator), 'pAllocator' ),
              ( ['in'], c_int, 'bReadOnly' )),
    COMMETHOD([], HRESULT, 'GetAllocatorRequirements',
              ( ['out'], POINTER(_AllocatorProperties), 'pProps' )),
    COMMETHOD([], HRESULT, 'Receive',
              ( ['in'], POINTER(IMediaSample), 'pSample' )),
    COMMETHOD([], HRESULT, 'ReceiveMultiple',
              ( ['in'], POINTER(POINTER(IMediaSample)), 'pSamples' ),
              ( ['in'], c_int, 'nSamples' ),
              ( ['out'], POINTER(c_int), 'nSamplesProcessed' )),
    COMMETHOD([], HRESULT, 'ReceiveCanBlock'),
]
################################################################
## code template for IMemInputPin implementation
##class IMemInputPin_Impl(object):
##    def Receive(self, pSample):
##        '-no docstring-'
##        #return 
##
##    def ReceiveMultiple(self, pSamples, nSamples):
##        '-no docstring-'
##        #return nSamplesProcessed
##
##    def NotifyAllocator(self, pAllocator, bReadOnly):
##        '-no docstring-'
##        #return 
##
##    def GetAllocatorRequirements(self):
##        '-no docstring-'
##        #return pProps
##
##    def ReceiveCanBlock(self):
##        '-no docstring-'
##        #return 
##
##    def GetAllocator(self):
##        '-no docstring-'
##        #return ppAllocator
##

class IPinConnection(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4A9A62D3-27D4-403D-91E9-89F540E55534}')
    _idlflags_ = []
IPinConnection._methods_ = [
    COMMETHOD([], HRESULT, 'DynamicQueryAccept',
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'NotifyEndOfStream',
              ( ['in'], c_void_p, 'hNotifyEvent' )),
    COMMETHOD([], HRESULT, 'IsEndPin'),
    COMMETHOD([], HRESULT, 'DynamicDisconnect'),
]
################################################################
## code template for IPinConnection implementation
##class IPinConnection_Impl(object):
##    def DynamicDisconnect(self):
##        '-no docstring-'
##        #return 
##
##    def IsEndPin(self):
##        '-no docstring-'
##        #return 
##
##    def DynamicQueryAccept(self, pmt):
##        '-no docstring-'
##        #return 
##
##    def NotifyEndOfStream(self, hNotifyEvent):
##        '-no docstring-'
##        #return 
##

class IVMRAspectRatioControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRAspectRatioControl Interface'
    _iid_ = GUID('{EDE80B5C-BAD6-4623-B537-65586C9F8DFD}')
    _idlflags_ = []
IVMRAspectRatioControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetAspectRatioMode',
              ( ['out'], POINTER(c_ulong), 'lpdwARMode' )),
    COMMETHOD([], HRESULT, 'SetAspectRatioMode',
              ( ['in'], c_ulong, 'dwARMode' )),
]
################################################################
## code template for IVMRAspectRatioControl implementation
##class IVMRAspectRatioControl_Impl(object):
##    def GetAspectRatioMode(self):
##        '-no docstring-'
##        #return lpdwARMode
##
##    def SetAspectRatioMode(self, dwARMode):
##        '-no docstring-'
##        #return 
##

class __MIDL___MIDL_itf_DirectShow_0134_0001(Structure):
    pass
REGPINTYPES = __MIDL___MIDL_itf_DirectShow_0134_0001
__MIDL___MIDL_itf_DirectShow_0134_0005._fields_ = [
    ('dwFlags', c_ulong),
    ('cInstances', c_uint),
    ('nMediaTypes', c_uint),
    ('lpMediaType', POINTER(REGPINTYPES)),
    ('nMediums', c_uint),
    ('lpMedium', POINTER(REGPINMEDIUM)),
    ('clsPinCategory', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0005) == 48, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0005)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0005) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0005)

# values for enumeration '_AM_AUDIO_RENDERER_STAT_PARAM'
AM_AUDREND_STAT_PARAM_BREAK_COUNT = 1
AM_AUDREND_STAT_PARAM_SLAVE_MODE = 2
AM_AUDREND_STAT_PARAM_SILENCE_DUR = 3
AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR = 4
AM_AUDREND_STAT_PARAM_DISCONTINUITIES = 5
AM_AUDREND_STAT_PARAM_SLAVE_RATE = 6
AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR = 7
AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR = 8
AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR = 9
AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR = 10
AM_AUDREND_STAT_PARAM_BUFFERFULLNESS = 11
AM_AUDREND_STAT_PARAM_JITTER = 12
_AM_AUDIO_RENDERER_STAT_PARAM = c_int # enum
DVINFO = __MIDL___MIDL_itf_DirectShow_0345_0001
class IAMTuner(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8761-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []
class IBPCSatelliteTuner(IAMTuner):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8765-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []
IAMTuner._methods_ = [
    COMMETHOD([], HRESULT, 'put_Channel',
              ( ['in'], c_int, 'lChannel' ),
              ( ['in'], c_int, 'lVideoSubChannel' ),
              ( ['in'], c_int, 'lAudioSubChannel' )),
    COMMETHOD([], HRESULT, 'get_Channel',
              ( ['out'], POINTER(c_int), 'plChannel' ),
              ( ['out'], POINTER(c_int), 'plVideoSubChannel' ),
              ( ['out'], POINTER(c_int), 'plAudioSubChannel' )),
    COMMETHOD([], HRESULT, 'ChannelMinMax',
              ( ['out'], POINTER(c_int), 'lChannelMin' ),
              ( ['out'], POINTER(c_int), 'lChannelMax' )),
    COMMETHOD([], HRESULT, 'put_CountryCode',
              ( ['in'], c_int, 'lCountryCode' )),
    COMMETHOD([], HRESULT, 'get_CountryCode',
              ( ['out'], POINTER(c_int), 'plCountryCode' )),
    COMMETHOD([], HRESULT, 'put_TuningSpace',
              ( ['in'], c_int, 'lTuningSpace' )),
    COMMETHOD([], HRESULT, 'get_TuningSpace',
              ( ['out'], POINTER(c_int), 'plTuningSpace' )),
    COMMETHOD([], HRESULT, 'Logon',
              ( ['in'], c_void_p, 'hCurrentUser' )),
    COMMETHOD([], HRESULT, 'Logout'),
    COMMETHOD([], HRESULT, 'SignalPresent',
              ( ['out'], POINTER(c_int), 'plSignalStrength' )),
    COMMETHOD([], HRESULT, 'put_Mode',
              ( ['in'], tagAMTunerModeType, 'lMode' )),
    COMMETHOD([], HRESULT, 'get_Mode',
              ( ['out'], POINTER(tagAMTunerModeType), 'plMode' )),
    COMMETHOD([], HRESULT, 'GetAvailableModes',
              ( ['out'], POINTER(c_int), 'plModes' )),
    COMMETHOD([], HRESULT, 'RegisterNotificationCallBack',
              ( ['in'], POINTER(IAMTunerNotification), 'pNotify' ),
              ( ['in'], c_int, 'lEvents' )),
    COMMETHOD([], HRESULT, 'UnRegisterNotificationCallBack',
              ( ['in'], POINTER(IAMTunerNotification), 'pNotify' )),
]
################################################################
## code template for IAMTuner implementation
##class IAMTuner_Impl(object):
##    def SignalPresent(self):
##        '-no docstring-'
##        #return plSignalStrength
##
##    def RegisterNotificationCallBack(self, pNotify, lEvents):
##        '-no docstring-'
##        #return 
##
##    def ChannelMinMax(self):
##        '-no docstring-'
##        #return lChannelMin, lChannelMax
##
##    def put_CountryCode(self, lCountryCode):
##        '-no docstring-'
##        #return 
##
##    def get_Channel(self):
##        '-no docstring-'
##        #return plChannel, plVideoSubChannel, plAudioSubChannel
##
##    def UnRegisterNotificationCallBack(self, pNotify):
##        '-no docstring-'
##        #return 
##
##    def get_TuningSpace(self):
##        '-no docstring-'
##        #return plTuningSpace
##
##    def put_TuningSpace(self, lTuningSpace):
##        '-no docstring-'
##        #return 
##
##    def put_Mode(self, lMode):
##        '-no docstring-'
##        #return 
##
##    def put_Channel(self, lChannel, lVideoSubChannel, lAudioSubChannel):
##        '-no docstring-'
##        #return 
##
##    def Logout(self):
##        '-no docstring-'
##        #return 
##
##    def get_Mode(self):
##        '-no docstring-'
##        #return plMode
##
##    def get_CountryCode(self):
##        '-no docstring-'
##        #return plCountryCode
##
##    def Logon(self, hCurrentUser):
##        '-no docstring-'
##        #return 
##
##    def GetAvailableModes(self):
##        '-no docstring-'
##        #return plModes
##

IBPCSatelliteTuner._methods_ = [
    COMMETHOD([], HRESULT, 'get_DefaultSubChannelTypes',
              ( ['out'], POINTER(c_int), 'plDefaultVideoType' ),
              ( ['out'], POINTER(c_int), 'plDefaultAudioType' )),
    COMMETHOD([], HRESULT, 'put_DefaultSubChannelTypes',
              ( ['in'], c_int, 'lDefaultVideoType' ),
              ( ['in'], c_int, 'lDefaultAudioType' )),
    COMMETHOD([], HRESULT, 'IsTapingPermitted'),
]
################################################################
## code template for IBPCSatelliteTuner implementation
##class IBPCSatelliteTuner_Impl(object):
##    def get_DefaultSubChannelTypes(self):
##        '-no docstring-'
##        #return plDefaultVideoType, plDefaultAudioType
##
##    def put_DefaultSubChannelTypes(self, lDefaultVideoType, lDefaultAudioType):
##        '-no docstring-'
##        #return 
##
##    def IsTapingPermitted(self):
##        '-no docstring-'
##        #return 
##

class IAsyncReader(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AA-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IAsyncReader._methods_ = [
    COMMETHOD([], HRESULT, 'RequestAllocator',
              ( ['in'], POINTER(IMemAllocator), 'pPreferred' ),
              ( ['in'], POINTER(_AllocatorProperties), 'pProps' ),
              ( ['out'], POINTER(POINTER(IMemAllocator)), 'ppActual' )),
    COMMETHOD([], HRESULT, 'Request',
              ( ['in'], POINTER(IMediaSample), 'pSample' ),
              ( ['in'], ULONG_PTR, 'dwUser' )),
    COMMETHOD([], HRESULT, 'WaitForNext',
              ( ['in'], c_ulong, 'dwTimeout' ),
              ( ['out'], POINTER(POINTER(IMediaSample)), 'ppSample' ),
              ( ['out'], POINTER(ULONG_PTR), 'pdwUser' )),
    COMMETHOD([], HRESULT, 'SyncReadAligned',
              ( ['in'], POINTER(IMediaSample), 'pSample' )),
    COMMETHOD([], HRESULT, 'SyncRead',
              ( ['in'], c_longlong, 'llPosition' ),
              ( ['in'], c_int, 'lLength' ),
              ( ['out'], POINTER(c_ubyte), 'pBuffer' )),
    COMMETHOD([], HRESULT, 'Length',
              ( ['out'], POINTER(c_longlong), 'pTotal' ),
              ( ['out'], POINTER(c_longlong), 'pAvailable' )),
    COMMETHOD([], HRESULT, 'BeginFlush'),
    COMMETHOD([], HRESULT, 'EndFlush'),
]
################################################################
## code template for IAsyncReader implementation
##class IAsyncReader_Impl(object):
##    def WaitForNext(self, dwTimeout):
##        '-no docstring-'
##        #return ppSample, pdwUser
##
##    def BeginFlush(self):
##        '-no docstring-'
##        #return 
##
##    def EndFlush(self):
##        '-no docstring-'
##        #return 
##
##    def Request(self, pSample, dwUser):
##        '-no docstring-'
##        #return 
##
##    def Length(self):
##        '-no docstring-'
##        #return pTotal, pAvailable
##
##    def SyncReadAligned(self, pSample):
##        '-no docstring-'
##        #return 
##
##    def RequestAllocator(self, pPreferred, pProps):
##        '-no docstring-'
##        #return ppActual
##
##    def SyncRead(self, llPosition, lLength):
##        '-no docstring-'
##        #return pBuffer
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0364_0001'
ConstantBitRate = 0
VariableBitRateAverage = 1
VariableBitRatePeak = 2
__MIDL___MIDL_itf_DirectShow_0364_0001 = c_int # enum
VIDEOENCODER_BITRATE_MODE = __MIDL___MIDL_itf_DirectShow_0364_0001
tagTIMECODE_SAMPLE._fields_ = [
    ('qwTick', c_longlong),
    ('timecode', tagTIMECODE),
    ('dwUser', c_ulong),
    ('dwFlags', c_ulong),
]
assert sizeof(tagTIMECODE_SAMPLE) == 24, sizeof(tagTIMECODE_SAMPLE)
assert alignment(tagTIMECODE_SAMPLE) == 8, alignment(tagTIMECODE_SAMPLE)
class IAMVideoDecimationProperties(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{60D32930-13DA-11D3-9EC6-C4FCAEF5C7BE}')
    _idlflags_ = []

# values for enumeration '_DECIMATION_USAGE'
DECIMATION_LEGACY = 0
DECIMATION_USE_DECODER_ONLY = 1
DECIMATION_USE_VIDEOPORT_ONLY = 2
DECIMATION_USE_OVERLAY_ONLY = 3
DECIMATION_DEFAULT = 4
_DECIMATION_USAGE = c_int # enum
IAMVideoDecimationProperties._methods_ = [
    COMMETHOD([], HRESULT, 'QueryDecimationUsage',
              ( ['out'], POINTER(_DECIMATION_USAGE), 'lpUsage' )),
    COMMETHOD([], HRESULT, 'SetDecimationUsage',
              ( ['in'], _DECIMATION_USAGE, 'Usage' )),
]
################################################################
## code template for IAMVideoDecimationProperties implementation
##class IAMVideoDecimationProperties_Impl(object):
##    def SetDecimationUsage(self, Usage):
##        '-no docstring-'
##        #return 
##
##    def QueryDecimationUsage(self):
##        '-no docstring-'
##        #return lpUsage
##

CompressionCaps = __MIDL___MIDL_itf_DirectShow_0163_0001

# values for enumeration '_FilterState'
State_Stopped = 0
State_Paused = 1
State_Running = 2
_FilterState = c_int # enum
IMediaFilter._methods_ = [
    COMMETHOD([], HRESULT, 'Stop'),
    COMMETHOD([], HRESULT, 'Pause'),
    COMMETHOD([], HRESULT, 'Run',
              ( [], c_longlong, 'tStart' )),
    COMMETHOD([], HRESULT, 'GetState',
              ( ['in'], c_ulong, 'dwMilliSecsTimeout' ),
              ( ['out'], POINTER(_FilterState), 'State' )),
    COMMETHOD([], HRESULT, 'SetSyncSource',
              ( ['in'], POINTER(IReferenceClock), 'pClock' )),
    COMMETHOD([], HRESULT, 'GetSyncSource',
              ( ['out'], POINTER(POINTER(IReferenceClock)), 'pClock' )),
]
################################################################
## code template for IMediaFilter implementation
##class IMediaFilter_Impl(object):
##    def GetSyncSource(self):
##        '-no docstring-'
##        #return pClock
##
##    def Run(self, tStart):
##        '-no docstring-'
##        #return 
##
##    def SetSyncSource(self, pClock):
##        '-no docstring-'
##        #return 
##
##    def Stop(self):
##        '-no docstring-'
##        #return 
##
##    def Pause(self):
##        '-no docstring-'
##        #return 
##
##    def GetState(self, dwMilliSecsTimeout):
##        '-no docstring-'
##        #return State
##


# values for enumeration 'tagAMTunerSubChannel'
AMTUNER_SUBCHAN_NO_TUNE = -2
AMTUNER_SUBCHAN_DEFAULT = -1
tagAMTunerSubChannel = c_int # enum
class IFilterChain(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{DCFBDCF6-0DC2-45F5-9AB2-7C330EA09C29}')
    _idlflags_ = []
IFilterChain._methods_ = [
    COMMETHOD([], HRESULT, 'StartChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
    COMMETHOD([], HRESULT, 'PauseChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
    COMMETHOD([], HRESULT, 'StopChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
    COMMETHOD([], HRESULT, 'RemoveChain',
              ( ['in'], POINTER(IBaseFilter), 'pStartFilter' ),
              ( ['in'], POINTER(IBaseFilter), 'pEndFilter' )),
]
################################################################
## code template for IFilterChain implementation
##class IFilterChain_Impl(object):
##    def RemoveChain(self, pStartFilter, pEndFilter):
##        '-no docstring-'
##        #return 
##
##    def StopChain(self, pStartFilter, pEndFilter):
##        '-no docstring-'
##        #return 
##
##    def StartChain(self, pStartFilter, pEndFilter):
##        '-no docstring-'
##        #return 
##
##    def PauseChain(self, pStartFilter, pEndFilter):
##        '-no docstring-'
##        #return 
##

VfwCaptureDialogs = __MIDL___MIDL_itf_DirectShow_0164_0001

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0134_0004'
REG_PINFLAG_B_ZERO = 1
REG_PINFLAG_B_RENDERER = 2
REG_PINFLAG_B_MANY = 4
REG_PINFLAG_B_OUTPUT = 8
__MIDL___MIDL_itf_DirectShow_0134_0004 = c_int # enum
class IStreamBuilder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868BF-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IStreamBuilder._methods_ = [
    COMMETHOD([], HRESULT, 'Render',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IGraphBuilder), 'pGraph' )),
    COMMETHOD([], HRESULT, 'Backout',
              ( ['in'], POINTER(IPin), 'ppinOut' ),
              ( ['in'], POINTER(IGraphBuilder), 'pGraph' )),
]
################################################################
## code template for IStreamBuilder implementation
##class IStreamBuilder_Impl(object):
##    def Backout(self, ppinOut, pGraph):
##        '-no docstring-'
##        #return 
##
##    def Render(self, ppinOut, pGraph):
##        '-no docstring-'
##        #return 
##

class IGraphVersion(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AB-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IGraphVersion._methods_ = [
    COMMETHOD([], HRESULT, 'QueryVersion',
              ( [], POINTER(c_int), 'pVersion' )),
]
################################################################
## code template for IGraphVersion implementation
##class IGraphVersion_Impl(object):
##    def QueryVersion(self, pVersion):
##        '-no docstring-'
##        #return 
##

class IReferenceClock2(IReferenceClock):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73885-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IReferenceClock2._methods_ = [
]
################################################################
## code template for IReferenceClock2 implementation
##class IReferenceClock2_Impl(object):


# values for enumeration '_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS'
AM_PIN_FLOW_CONTROL_BLOCK = 1
_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS = c_int # enum
class IAMBufferNegotiation(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56ED71A0-AF5F-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMBufferNegotiation._methods_ = [
    COMMETHOD([], HRESULT, 'SuggestAllocatorProperties',
              ( ['in'], POINTER(_AllocatorProperties), 'pprop' )),
    COMMETHOD([], HRESULT, 'GetAllocatorProperties',
              ( ['out'], POINTER(_AllocatorProperties), 'pprop' )),
]
################################################################
## code template for IAMBufferNegotiation implementation
##class IAMBufferNegotiation_Impl(object):
##    def SuggestAllocatorProperties(self, pprop):
##        '-no docstring-'
##        #return 
##
##    def GetAllocatorProperties(self):
##        '-no docstring-'
##        #return pprop
##


# values for enumeration '_AMSTREAMSELECTENABLEFLAGS'
AMSTREAMSELECTENABLE_ENABLE = 1
AMSTREAMSELECTENABLE_ENABLEALL = 2
_AMSTREAMSELECTENABLEFLAGS = c_int # enum
__MIDL___MIDL_itf_DirectShow_0134_0001._fields_ = [
    ('clsMajorType', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
    ('clsMinorType', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0001) == 16, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0001)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0001) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0001)
class IAMClockSlave(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9FD52741-176D-4B36-8F51-CA8F933223BE}')
    _idlflags_ = []
IAMClockSlave._methods_ = [
    COMMETHOD([], HRESULT, 'SetErrorTolerance',
              ( ['in'], c_ulong, 'dwTolerance' )),
    COMMETHOD([], HRESULT, 'GetErrorTolerance',
              ( ['out'], POINTER(c_ulong), 'pdwTolerance' )),
]
################################################################
## code template for IAMClockSlave implementation
##class IAMClockSlave_Impl(object):
##    def SetErrorTolerance(self, dwTolerance):
##        '-no docstring-'
##        #return 
##
##    def GetErrorTolerance(self):
##        '-no docstring-'
##        #return pdwTolerance
##

class IAMAnalogVideoEncoder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E133B0-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMAnalogVideoEncoder._methods_ = [
    COMMETHOD([], HRESULT, 'get_AvailableTVFormats',
              ( ['out'], POINTER(c_int), 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'put_TVFormat',
              ( ['in'], c_int, 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_TVFormat',
              ( ['out'], POINTER(c_int), 'plAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'put_CopyProtection',
              ( ['in'], c_int, 'lVideoCopyProtection' )),
    COMMETHOD([], HRESULT, 'get_CopyProtection',
              ( ['out'], POINTER(c_int), 'lVideoCopyProtection' )),
    COMMETHOD([], HRESULT, 'put_CCEnable',
              ( ['in'], c_int, 'lCCEnable' )),
    COMMETHOD([], HRESULT, 'get_CCEnable',
              ( ['out'], POINTER(c_int), 'lCCEnable' )),
]
################################################################
## code template for IAMAnalogVideoEncoder implementation
##class IAMAnalogVideoEncoder_Impl(object):
##    def put_CCEnable(self, lCCEnable):
##        '-no docstring-'
##        #return 
##
##    def put_CopyProtection(self, lVideoCopyProtection):
##        '-no docstring-'
##        #return 
##
##    def get_CopyProtection(self):
##        '-no docstring-'
##        #return lVideoCopyProtection
##
##    def get_CCEnable(self):
##        '-no docstring-'
##        #return lCCEnable
##
##    def put_TVFormat(self, lAnalogVideoStandard):
##        '-no docstring-'
##        #return 
##
##    def get_AvailableTVFormats(self):
##        '-no docstring-'
##        #return lAnalogVideoStandard
##
##    def get_TVFormat(self):
##        '-no docstring-'
##        #return plAnalogVideoStandard
##

class FilterGraph(CoClass):
    _reg_clsid_ = GUID('{E436EBB3-524F-11CE-9F53-0020AF0BA770}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
FilterGraph._com_interfaces_ = [IGraphBuilder]


# values for enumeration 'tagTVAudioMode'
AMTVAUDIO_MODE_MONO = 1
AMTVAUDIO_MODE_STEREO = 2
AMTVAUDIO_MODE_LANG_A = 16
AMTVAUDIO_MODE_LANG_B = 32
AMTVAUDIO_MODE_LANG_C = 64
tagTVAudioMode = c_int # enum

# values for enumeration '_AM_INTF_SEARCH_FLAGS'
AM_INTF_SEARCH_INPUT_PIN = 1
AM_INTF_SEARCH_OUTPUT_PIN = 2
AM_INTF_SEARCH_FILTER = 4
_AM_INTF_SEARCH_FLAGS = c_int # enum
class __MIDL___MIDL_itf_DirectShow_0134_0008(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0134_0008._fields_ = [
    ('cPins', c_ulong),
    ('rgPins', POINTER(REGFILTERPINS)),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0008) == 16, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0008)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0008) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0008)

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0169_0001'
VideoCopyProtectionMacrovisionBasic = 0
VideoCopyProtectionMacrovisionCBI = 1
__MIDL___MIDL_itf_DirectShow_0169_0001 = c_int # enum
class IAMVideoControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{6A2E0670-28E4-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMVideoControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetCaps',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['out'], POINTER(c_int), 'pCapsFlags' )),
    COMMETHOD([], HRESULT, 'SetMode',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], c_int, 'mode' )),
    COMMETHOD([], HRESULT, 'GetMode',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['out'], POINTER(c_int), 'mode' )),
    COMMETHOD([], HRESULT, 'GetCurrentActualFrameRate',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['out'], POINTER(c_longlong), 'ActualFrameRate' )),
    COMMETHOD([], HRESULT, 'GetMaxAvailableFrameRate',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], c_int, 'iIndex' ),
              ( ['in'], tagSIZE, 'Dimensions' ),
              ( ['out'], POINTER(c_longlong), 'MaxAvailableFrameRate' )),
    COMMETHOD([], HRESULT, 'GetFrameRateList',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], c_int, 'iIndex' ),
              ( ['in'], tagSIZE, 'Dimensions' ),
              ( ['out'], POINTER(c_int), 'ListSize' ),
              ( ['out'], POINTER(POINTER(c_longlong)), 'FrameRates' )),
]
################################################################
## code template for IAMVideoControl implementation
##class IAMVideoControl_Impl(object):
##    def GetMaxAvailableFrameRate(self, pPin, iIndex, Dimensions):
##        '-no docstring-'
##        #return MaxAvailableFrameRate
##
##    def GetFrameRateList(self, pPin, iIndex, Dimensions):
##        '-no docstring-'
##        #return ListSize, FrameRates
##
##    def GetMode(self, pPin):
##        '-no docstring-'
##        #return mode
##
##    def GetCurrentActualFrameRate(self, pPin):
##        '-no docstring-'
##        #return ActualFrameRate
##
##    def GetCaps(self, pPin):
##        '-no docstring-'
##        #return pCapsFlags
##
##    def SetMode(self, pPin, mode):
##        '-no docstring-'
##        #return 
##

class IRegisterServiceProvider(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{7B3A2F01-0751-48DD-B556-004785171C54}')
    _idlflags_ = []
IRegisterServiceProvider._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterService',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'guidService' ),
              ( ['in'], POINTER(IUnknown), 'punkObject' )),
]
################################################################
## code template for IRegisterServiceProvider implementation
##class IRegisterServiceProvider_Impl(object):
##    def RegisterService(self, guidService, punkObject):
##        '-no docstring-'
##        #return 
##


# values for enumeration '__MIDL___MIDL_itf_DirectShow_0378_0001'
DeinterlacePref_NextBest = 1
DeinterlacePref_BOB = 2
DeinterlacePref_Weave = 4
DeinterlacePref_Mask = 7
__MIDL___MIDL_itf_DirectShow_0378_0001 = c_int # enum
ISequentialStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteRead',
              ( ['out'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbRead' )),
    COMMETHOD([], HRESULT, 'RemoteWrite',
              ( ['in'], POINTER(c_ubyte), 'pv' ),
              ( ['in'], c_ulong, 'cb' ),
              ( ['out'], POINTER(c_ulong), 'pcbWritten' )),
]
################################################################
## code template for ISequentialStream implementation
##class ISequentialStream_Impl(object):
##    def RemoteRead(self, cb):
##        '-no docstring-'
##        #return pv, pcbRead
##
##    def RemoteWrite(self, pv, cb):
##        '-no docstring-'
##        #return pcbWritten
##

IStream._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSeek',
              ( ['in'], _LARGE_INTEGER, 'dlibMove' ),
              ( ['in'], c_ulong, 'dwOrigin' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'plibNewPosition' )),
    COMMETHOD([], HRESULT, 'SetSize',
              ( ['in'], _ULARGE_INTEGER, 'libNewSize' )),
    COMMETHOD([], HRESULT, 'RemoteCopyTo',
              ( ['in'], POINTER(IStream), 'pstm' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbRead' ),
              ( ['out'], POINTER(_ULARGE_INTEGER), 'pcbWritten' )),
    COMMETHOD([], HRESULT, 'Commit',
              ( ['in'], c_ulong, 'grfCommitFlags' )),
    COMMETHOD([], HRESULT, 'Revert'),
    COMMETHOD([], HRESULT, 'LockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'UnlockRegion',
              ( ['in'], _ULARGE_INTEGER, 'libOffset' ),
              ( ['in'], _ULARGE_INTEGER, 'cb' ),
              ( ['in'], c_ulong, 'dwLockType' )),
    COMMETHOD([], HRESULT, 'Stat',
              ( ['out'], POINTER(tagSTATSTG), 'pstatstg' ),
              ( ['in'], c_ulong, 'grfStatFlag' )),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IStream)), 'ppstm' )),
]
################################################################
## code template for IStream implementation
##class IStream_Impl(object):
##    def RemoteSeek(self, dlibMove, dwOrigin):
##        '-no docstring-'
##        #return plibNewPosition
##
##    def Stat(self, grfStatFlag):
##        '-no docstring-'
##        #return pstatstg
##
##    def UnlockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppstm
##
##    def Revert(self):
##        '-no docstring-'
##        #return 
##
##    def RemoteCopyTo(self, pstm, cb):
##        '-no docstring-'
##        #return pcbRead, pcbWritten
##
##    def LockRegion(self, libOffset, cb, dwLockType):
##        '-no docstring-'
##        #return 
##
##    def Commit(self, grfCommitFlags):
##        '-no docstring-'
##        #return 
##
##    def SetSize(self, libNewSize):
##        '-no docstring-'
##        #return 
##

VideoCopyProtectionType = __MIDL___MIDL_itf_DirectShow_0169_0001
class IAMPhysicalPinInfo(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F938C991-3029-11CF-8C44-00AA006B6814}')
    _idlflags_ = []
IAMPhysicalPinInfo._methods_ = [
    COMMETHOD([], HRESULT, 'GetPhysicalType',
              ( ['out'], POINTER(c_int), 'pType' ),
              ( ['out'], POINTER(WSTRING), 'ppszType' )),
]
################################################################
## code template for IAMPhysicalPinInfo implementation
##class IAMPhysicalPinInfo_Impl(object):
##    def GetPhysicalType(self):
##        '-no docstring-'
##        #return pType, ppszType
##


# values for enumeration '_AM_GRAPH_CONFIG_RECONNECT_FLAGS'
AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT = 1
AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS = 2
AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS = 4
_AM_GRAPH_CONFIG_RECONNECT_FLAGS = c_int # enum
class ICaptureGraphBuilder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{BF87B6E0-8C27-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
ICaptureGraphBuilder._methods_ = [
    COMMETHOD([], HRESULT, 'SetFiltergraph',
              ( ['in'], POINTER(IGraphBuilder), 'pfg' )),
    COMMETHOD([], HRESULT, 'GetFiltergraph',
              ( ['out'], POINTER(POINTER(IGraphBuilder)), 'ppfg' )),
    COMMETHOD([], HRESULT, 'SetOutputFileName',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pType' ),
              ( ['in'], WSTRING, 'lpstrFile' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppf' ),
              ( ['out'], POINTER(POINTER(IFileSinkFilter)), 'ppSink' )),
    COMMETHOD([], HRESULT, 'RemoteFindInterface',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(IBaseFilter), 'pf' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppint' )),
    COMMETHOD([], HRESULT, 'RenderStream',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(IUnknown), 'pSource' ),
              ( ['in'], POINTER(IBaseFilter), 'pfCompressor' ),
              ( ['in'], POINTER(IBaseFilter), 'pfRenderer' )),
    COMMETHOD([], HRESULT, 'ControlStream',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pCategory' ),
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], POINTER(c_longlong), 'pstart' ),
              ( ['in'], POINTER(c_longlong), 'pStop' ),
              ( ['in'], c_ushort, 'wStartCookie' ),
              ( ['in'], c_ushort, 'wStopCookie' )),
    COMMETHOD([], HRESULT, 'AllocCapFile',
              ( ['in'], WSTRING, 'lpstr' ),
              ( ['in'], c_ulonglong, 'dwlSize' )),
    COMMETHOD([], HRESULT, 'CopyCaptureFile',
              ( ['in'], WSTRING, 'lpwstrOld' ),
              ( ['in'], WSTRING, 'lpwstrNew' ),
              ( ['in'], c_int, 'fAllowEscAbort' ),
              ( ['in'], POINTER(IAMCopyCaptureFileProgress), 'pCallback' )),
]
################################################################
## code template for ICaptureGraphBuilder implementation
##class ICaptureGraphBuilder_Impl(object):
##    def RemoteFindInterface(self, pCategory, pf, riid):
##        '-no docstring-'
##        #return ppint
##
##    def RenderStream(self, pCategory, pSource, pfCompressor, pfRenderer):
##        '-no docstring-'
##        #return 
##
##    def ControlStream(self, pCategory, pFilter, pstart, pStop, wStartCookie, wStopCookie):
##        '-no docstring-'
##        #return 
##
##    def GetFiltergraph(self):
##        '-no docstring-'
##        #return ppfg
##
##    def SetFiltergraph(self, pfg):
##        '-no docstring-'
##        #return 
##
##    def SetOutputFileName(self, pType, lpstrFile):
##        '-no docstring-'
##        #return ppf, ppSink
##
##    def AllocCapFile(self, lpstr, dwlSize):
##        '-no docstring-'
##        #return 
##
##    def CopyCaptureFile(self, lpwstrOld, lpwstrNew, fAllowEscAbort, pCallback):
##        '-no docstring-'
##        #return 
##

class IFilterMapper(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A3-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IEnumRegFilters(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A4-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IFilterMapper._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterFilter',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsid' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['in'], c_ulong, 'dwMerit' )),
    COMMETHOD([], HRESULT, 'RegisterFilterInstance',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsid' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'MRId' )),
    COMMETHOD([], HRESULT, 'RegisterPin',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'Filter' ),
              ( ['in'], WSTRING, 'Name' ),
              ( ['in'], c_int, 'bRendered' ),
              ( ['in'], c_int, 'bOutput' ),
              ( ['in'], c_int, 'bZero' ),
              ( ['in'], c_int, 'bMany' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'ConnectsToFilter' ),
              ( ['in'], WSTRING, 'ConnectsToPin' )),
    COMMETHOD([], HRESULT, 'RegisterPinType',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsFilter' ),
              ( ['in'], WSTRING, 'strName' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsMajorType' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsSubType' )),
    COMMETHOD([], HRESULT, 'UnregisterFilter',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'Filter' )),
    COMMETHOD([], HRESULT, 'UnregisterFilterInstance',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'MRId' )),
    COMMETHOD([], HRESULT, 'UnregisterPin',
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'Filter' ),
              ( ['in'], WSTRING, 'Name' )),
    COMMETHOD([], HRESULT, 'EnumMatchingFilters',
              ( ['out'], POINTER(POINTER(IEnumRegFilters)), 'ppenum' ),
              ( ['in'], c_ulong, 'dwMerit' ),
              ( ['in'], c_int, 'bInputNeeded' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsInMaj' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsInSub' ),
              ( ['in'], c_int, 'bRender' ),
              ( ['in'], c_int, 'bOututNeeded' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsOutMaj' ),
              ( ['in'], comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID, 'clsOutSub' )),
]
################################################################
## code template for IFilterMapper implementation
##class IFilterMapper_Impl(object):
##    def UnregisterFilter(self, Filter):
##        '-no docstring-'
##        #return 
##
##    def UnregisterPin(self, Filter, Name):
##        '-no docstring-'
##        #return 
##
##    def RegisterPin(self, Filter, Name, bRendered, bOutput, bZero, bMany, ConnectsToFilter, ConnectsToPin):
##        '-no docstring-'
##        #return 
##
##    def EnumMatchingFilters(self, dwMerit, bInputNeeded, clsInMaj, clsInSub, bRender, bOututNeeded, clsOutMaj, clsOutSub):
##        '-no docstring-'
##        #return ppenum
##
##    def RegisterFilterInstance(self, clsid, Name):
##        '-no docstring-'
##        #return MRId
##
##    def UnregisterFilterInstance(self, MRId):
##        '-no docstring-'
##        #return 
##
##    def RegisterFilter(self, clsid, Name, dwMerit):
##        '-no docstring-'
##        #return 
##
##    def RegisterPinType(self, clsFilter, strName, clsMajorType, clsSubType):
##        '-no docstring-'
##        #return 
##

class ICodecAPI(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{901DB4C7-31CE-41A2-85DC-8FA0BF41B8DA}')
    _idlflags_ = []
ICodecAPI._methods_ = [
    COMMETHOD([], HRESULT, 'IsSupported',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'IsModifiable',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'GetParameterRange',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'ValueMin' ),
              ( ['out'], POINTER(VARIANT), 'ValueMax' ),
              ( ['out'], POINTER(VARIANT), 'SteppingDelta' )),
    COMMETHOD([], HRESULT, 'GetParameterValues',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(POINTER(VARIANT)), 'Values' ),
              ( ['out'], POINTER(c_ulong), 'ValuesCount' )),
    COMMETHOD([], HRESULT, 'GetDefaultValue',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'GetValue',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['out'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'SetValue',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['in'], POINTER(VARIANT), 'Value' )),
    COMMETHOD([], HRESULT, 'RegisterForEvent',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['in'], LONG_PTR, 'userData' )),
    COMMETHOD([], HRESULT, 'UnregisterForEvent',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' )),
    COMMETHOD([], HRESULT, 'SetAllDefaults'),
    COMMETHOD([], HRESULT, 'SetValueWithNotify',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'Api' ),
              ( ['in'], POINTER(VARIANT), 'Value' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)), 'ChangedParam' ),
              ( ['out'], POINTER(c_ulong), 'ChangedParamCount' )),
    COMMETHOD([], HRESULT, 'SetAllDefaultsWithNotify',
              ( ['out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)), 'ChangedParam' ),
              ( ['out'], POINTER(c_ulong), 'ChangedParamCount' )),
    COMMETHOD([], HRESULT, 'GetAllSettings',
              ( ['in'], POINTER(IStream), '__MIDL_0016' )),
    COMMETHOD([], HRESULT, 'SetAllSettings',
              ( ['in'], POINTER(IStream), '__MIDL_0017' )),
    COMMETHOD([], HRESULT, 'SetAllSettingsWithNotify',
              ( [], POINTER(IStream), '__MIDL_0018' ),
              ( ['out'], POINTER(POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)), 'ChangedParam' ),
              ( ['out'], POINTER(c_ulong), 'ChangedParamCount' )),
]
################################################################
## code template for ICodecAPI implementation
##class ICodecAPI_Impl(object):
##    def SetAllSettingsWithNotify(self, __MIDL_0018):
##        '-no docstring-'
##        #return ChangedParam, ChangedParamCount
##
##    def IsSupported(self, Api):
##        '-no docstring-'
##        #return 
##
##    def SetValue(self, Api, Value):
##        '-no docstring-'
##        #return 
##
##    def GetDefaultValue(self, Api):
##        '-no docstring-'
##        #return Value
##
##    def GetParameterValues(self, Api):
##        '-no docstring-'
##        #return Values, ValuesCount
##
##    def SetAllDefaults(self):
##        '-no docstring-'
##        #return 
##
##    def RegisterForEvent(self, Api, userData):
##        '-no docstring-'
##        #return 
##
##    def GetValue(self, Api):
##        '-no docstring-'
##        #return Value
##
##    def GetAllSettings(self, __MIDL_0016):
##        '-no docstring-'
##        #return 
##
##    def IsModifiable(self, Api):
##        '-no docstring-'
##        #return 
##
##    def SetAllSettings(self, __MIDL_0017):
##        '-no docstring-'
##        #return 
##
##    def SetValueWithNotify(self, Api, Value):
##        '-no docstring-'
##        #return ChangedParam, ChangedParamCount
##
##    def SetAllDefaultsWithNotify(self):
##        '-no docstring-'
##        #return ChangedParam, ChangedParamCount
##
##    def GetParameterRange(self, Api):
##        '-no docstring-'
##        #return ValueMin, ValueMax, SteppingDelta
##
##    def UnregisterForEvent(self, Api):
##        '-no docstring-'
##        #return 
##

class IMediaSample2(IMediaSample):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73884-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
IMediaSample2._methods_ = [
    COMMETHOD([], HRESULT, 'GetProperties',
              ( ['in'], c_ulong, 'cbProperties' ),
              ( ['out'], POINTER(c_ubyte), 'pbProperties' )),
    COMMETHOD([], HRESULT, 'SetProperties',
              ( ['in'], c_ulong, 'cbProperties' ),
              ( ['in'], POINTER(c_ubyte), 'pbProperties' )),
]
################################################################
## code template for IMediaSample2 implementation
##class IMediaSample2_Impl(object):
##    def SetProperties(self, cbProperties, pbProperties):
##        '-no docstring-'
##        #return 
##
##    def GetProperties(self, cbProperties):
##        '-no docstring-'
##        #return pbProperties
##

class __MIDL_IWinTypes_0009(Union):
    pass
__MIDL_IWinTypes_0009._fields_ = [
    ('hInproc', c_int),
    ('hRemote', c_int),
]
assert sizeof(__MIDL_IWinTypes_0009) == 4, sizeof(__MIDL_IWinTypes_0009)
assert alignment(__MIDL_IWinTypes_0009) == 4, alignment(__MIDL_IWinTypes_0009)
_RemotableHandle._fields_ = [
    ('fContext', c_int),
    ('u', __MIDL_IWinTypes_0009),
]
assert sizeof(_RemotableHandle) == 8, sizeof(_RemotableHandle)
assert alignment(_RemotableHandle) == 4, alignment(_RemotableHandle)

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0138_0002'
ADVISE_NONE = 0
ADVISE_CLIPPING = 1
ADVISE_PALETTE = 2
ADVISE_COLORKEY = 4
ADVISE_POSITION = 8
ADVISE_DISPLAY_CHANGE = 16
__MIDL___MIDL_itf_DirectShow_0138_0002 = c_int # enum
class tagCOLORKEY(Structure):
    pass
tagCOLORKEY._fields_ = [
    ('KeyType', c_ulong),
    ('PaletteIndex', c_ulong),
    ('LowColorValue', c_ulong),
    ('HighColorValue', c_ulong),
]
assert sizeof(tagCOLORKEY) == 16, sizeof(tagCOLORKEY)
assert alignment(tagCOLORKEY) == 4, alignment(tagCOLORKEY)
class tagVMRGUID(Structure):
    pass
tagVMRGUID._fields_ = [
    ('pGUID', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
    ('guid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
]
assert sizeof(tagVMRGUID) == 24, sizeof(tagVMRGUID)
assert alignment(tagVMRGUID) == 8, alignment(tagVMRGUID)
class IAMVideoCompression(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13343-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMVideoCompression._methods_ = [
    COMMETHOD([], HRESULT, 'put_KeyFrameRate',
              ( ['in'], c_int, 'KeyFrameRate' )),
    COMMETHOD([], HRESULT, 'get_KeyFrameRate',
              ( ['out'], POINTER(c_int), 'pKeyFrameRate' )),
    COMMETHOD([], HRESULT, 'put_PFramesPerKeyFrame',
              ( ['in'], c_int, 'PFramesPerKeyFrame' )),
    COMMETHOD([], HRESULT, 'get_PFramesPerKeyFrame',
              ( ['out'], POINTER(c_int), 'pPFramesPerKeyFrame' )),
    COMMETHOD([], HRESULT, 'put_Quality',
              ( ['in'], c_double, 'Quality' )),
    COMMETHOD([], HRESULT, 'get_Quality',
              ( ['out'], POINTER(c_double), 'pQuality' )),
    COMMETHOD([], HRESULT, 'put_WindowSize',
              ( ['in'], c_ulonglong, 'WindowSize' )),
    COMMETHOD([], HRESULT, 'get_WindowSize',
              ( ['out'], POINTER(c_ulonglong), 'pWindowSize' )),
    COMMETHOD([], HRESULT, 'GetInfo',
              ( ['out'], POINTER(c_ushort), 'pszVersion' ),
              ( ['in', 'out'], POINTER(c_int), 'pcbVersion' ),
              ( ['out'], WSTRING, 'pszDescription' ),
              ( ['in', 'out'], POINTER(c_int), 'pcbDescription' ),
              ( ['out'], POINTER(c_int), 'pDefaultKeyFrameRate' ),
              ( ['out'], POINTER(c_int), 'pDefaultPFramesPerKey' ),
              ( ['out'], POINTER(c_double), 'pDefaultQuality' ),
              ( ['out'], POINTER(c_int), 'pCapabilities' )),
    COMMETHOD([], HRESULT, 'OverrideKeyFrame',
              ( ['in'], c_int, 'FrameNumber' )),
    COMMETHOD([], HRESULT, 'OverrideFrameSize',
              ( ['in'], c_int, 'FrameNumber' ),
              ( ['in'], c_int, 'Size' )),
]
################################################################
## code template for IAMVideoCompression implementation
##class IAMVideoCompression_Impl(object):
##    def put_KeyFrameRate(self, KeyFrameRate):
##        '-no docstring-'
##        #return 
##
##    def put_WindowSize(self, WindowSize):
##        '-no docstring-'
##        #return 
##
##    def get_WindowSize(self):
##        '-no docstring-'
##        #return pWindowSize
##
##    def put_PFramesPerKeyFrame(self, PFramesPerKeyFrame):
##        '-no docstring-'
##        #return 
##
##    def GetInfo(self):
##        '-no docstring-'
##        #return pszVersion, pcbVersion, pszDescription, pcbDescription, pDefaultKeyFrameRate, pDefaultPFramesPerKey, pDefaultQuality, pCapabilities
##
##    def OverrideFrameSize(self, FrameNumber, Size):
##        '-no docstring-'
##        #return 
##
##    def get_PFramesPerKeyFrame(self):
##        '-no docstring-'
##        #return pPFramesPerKeyFrame
##
##    def get_Quality(self):
##        '-no docstring-'
##        #return pQuality
##
##    def put_Quality(self, Quality):
##        '-no docstring-'
##        #return 
##
##    def OverrideKeyFrame(self, FrameNumber):
##        '-no docstring-'
##        #return 
##
##    def get_KeyFrameRate(self):
##        '-no docstring-'
##        #return pKeyFrameRate
##

class tagVMRALLOCATIONINFO(Structure):
    pass
tagVMRALLOCATIONINFO._fields_ = [
    ('dwFlags', c_ulong),
    ('lpHdr', POINTER(c_ulong)),
    ('lpPixFmt', POINTER(c_ulong)),
    ('szAspectRatio', tagSIZE),
    ('dwMinBuffers', c_ulong),
    ('dwMaxBuffers', c_ulong),
    ('dwInterlaceFlags', c_ulong),
    ('szNativeSize', tagSIZE),
]
assert sizeof(tagVMRALLOCATIONINFO) == 56, sizeof(tagVMRALLOCATIONINFO)
assert alignment(tagVMRALLOCATIONINFO) == 8, alignment(tagVMRALLOCATIONINFO)

# values for enumeration '_DVDECODERRESOLUTION'
DVDECODERRESOLUTION_720x480 = 1000
DVDECODERRESOLUTION_360x240 = 1001
DVDECODERRESOLUTION_180x120 = 1002
DVDECODERRESOLUTION_88x60 = 1003
_DVDECODERRESOLUTION = c_int # enum
AM_FILESINK_FLAGS = __MIDL___MIDL_itf_DirectShow_0145_0001

# values for enumeration '_DVENCODERFORMAT'
DVENCODERFORMAT_DVSD = 2007
DVENCODERFORMAT_DVHD = 2008
DVENCODERFORMAT_DVSL = 2009
_DVENCODERFORMAT = c_int # enum
class IDVEnc(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D18E17A0-AACB-11D0-AFB0-00AA00B67A42}')
    _idlflags_ = []
IDVEnc._methods_ = [
    COMMETHOD([], HRESULT, 'get_IFormatResolution',
              ( ['out'], POINTER(c_int), 'VideoFormat' ),
              ( ['out'], POINTER(c_int), 'DVFormat' ),
              ( ['out'], POINTER(c_int), 'Resolution' ),
              ( ['in'], c_ubyte, 'fDVInfo' ),
              ( ['out'], POINTER(DVINFO), 'sDVInfo' )),
    COMMETHOD([], HRESULT, 'put_IFormatResolution',
              ( ['in'], c_int, 'VideoFormat' ),
              ( ['in'], c_int, 'DVFormat' ),
              ( ['in'], c_int, 'Resolution' ),
              ( ['in'], c_ubyte, 'fDVInfo' ),
              ( ['in'], POINTER(DVINFO), 'sDVInfo' )),
]
################################################################
## code template for IDVEnc implementation
##class IDVEnc_Impl(object):
##    def put_IFormatResolution(self, VideoFormat, DVFormat, Resolution, fDVInfo, sDVInfo):
##        '-no docstring-'
##        #return 
##
##    def get_IFormatResolution(self, fDVInfo):
##        '-no docstring-'
##        #return VideoFormat, DVFormat, Resolution, sDVInfo
##


# values for enumeration '_AM_RENSDEREXFLAGS'
AM_RENDEREX_RENDERTOEXISTINGRENDERERS = 1
_AM_RENSDEREXFLAGS = c_int # enum
AMPROPERTY_PIN = __MIDL___MIDL_itf_DirectShow_0181_0001
class __MIDL___MIDL_itf_DirectShow_0370_0001(Structure):
    pass
__MIDL___MIDL_itf_DirectShow_0370_0001._fields_ = [
    ('dw1', c_ulong),
    ('dw2', c_ulong),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0370_0001) == 8, sizeof(__MIDL___MIDL_itf_DirectShow_0370_0001)
assert alignment(__MIDL___MIDL_itf_DirectShow_0370_0001) == 4, alignment(__MIDL___MIDL_itf_DirectShow_0370_0001)
VMRMixerPrefs = __MIDL___MIDL_itf_DirectShow_0374_0001

# values for enumeration 'tagAnalogVideoStandard'
AnalogVideo_None = 0
AnalogVideo_NTSC_M = 1
AnalogVideo_NTSC_M_J = 2
AnalogVideo_NTSC_433 = 4
AnalogVideo_PAL_B = 16
AnalogVideo_PAL_D = 32
AnalogVideo_PAL_G = 64
AnalogVideo_PAL_H = 128
AnalogVideo_PAL_I = 256
AnalogVideo_PAL_M = 512
AnalogVideo_PAL_N = 1024
AnalogVideo_PAL_60 = 2048
AnalogVideo_SECAM_B = 4096
AnalogVideo_SECAM_D = 8192
AnalogVideo_SECAM_G = 16384
AnalogVideo_SECAM_H = 32768
AnalogVideo_SECAM_K = 65536
AnalogVideo_SECAM_K1 = 131072
AnalogVideo_SECAM_L = 262144
AnalogVideo_SECAM_L1 = 524288
AnalogVideo_PAL_N_COMBO = 1048576
tagAnalogVideoStandard = c_int # enum
__MIDL___MIDL_itf_DirectShow_0134_0003._fields_ = [
    ('clsMedium', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('dw1', c_ulong),
    ('dw2', c_ulong),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0003) == 24, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0003)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0003) == 4, alignment(__MIDL___MIDL_itf_DirectShow_0134_0003)
class IOverlayNotify(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A0-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
class IOverlayNotify2(IOverlayNotify):
    _case_insensitive_ = True
    _iid_ = GUID('{680EFA10-D535-11D1-87C8-00A0C9223196}')
    _idlflags_ = []
class tagPALETTEENTRY(Structure):
    pass
IOverlayNotify._methods_ = [
    COMMETHOD([], HRESULT, 'OnPaletteChange',
              ( ['in'], c_ulong, 'dwColors' ),
              ( ['in'], POINTER(tagPALETTEENTRY), 'pPalette' )),
    COMMETHOD([], HRESULT, 'OnClipChange',
              ( ['in'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['in'], POINTER(tagRECT), 'pDestinationRect' ),
              ( ['in'], POINTER(_RGNDATA), 'pRgnData' )),
    COMMETHOD([], HRESULT, 'OnColorKeyChange',
              ( ['in'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'OnPositionChange',
              ( ['in'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['in'], POINTER(tagRECT), 'pDestinationRect' )),
]
################################################################
## code template for IOverlayNotify implementation
##class IOverlayNotify_Impl(object):
##    def OnPaletteChange(self, dwColors, pPalette):
##        '-no docstring-'
##        #return 
##
##    def OnClipChange(self, pSourceRect, pDestinationRect, pRgnData):
##        '-no docstring-'
##        #return 
##
##    def OnPositionChange(self, pSourceRect, pDestinationRect):
##        '-no docstring-'
##        #return 
##
##    def OnColorKeyChange(self, pColorKey):
##        '-no docstring-'
##        #return 
##

IOverlayNotify2._methods_ = [
    COMMETHOD([], HRESULT, 'OnDisplayChange',
              ( [], c_void_p, 'hMonitor' )),
]
################################################################
## code template for IOverlayNotify2 implementation
##class IOverlayNotify2_Impl(object):
##    def OnDisplayChange(self, hMonitor):
##        '-no docstring-'
##        #return 
##

__MIDL___MIDL_itf_DirectShow_0134_0002._fields_ = [
    ('strName', WSTRING),
    ('bRendered', c_int),
    ('bOutput', c_int),
    ('bZero', c_int),
    ('bMany', c_int),
    ('clsConnectsToFilter', POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID)),
    ('strConnectsToPin', POINTER(c_ushort)),
    ('nMediaTypes', c_uint),
    ('lpMediaType', POINTER(REGPINTYPES)),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0002) == 56, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0002)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0002) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0002)
class IVMRFilterConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRFilterConfig Interface'
    _iid_ = GUID('{9E5530C5-7034-48B4-BB46-0B8A6EFC8E36}')
    _idlflags_ = []
IVMRFilterConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetImageCompositor',
              ( ['in'], POINTER(IVMRImageCompositor), 'lpVMRImgCompositor' )),
    COMMETHOD([], HRESULT, 'SetNumberOfStreams',
              ( ['in'], c_ulong, 'dwMaxStreams' )),
    COMMETHOD([], HRESULT, 'GetNumberOfStreams',
              ( ['out'], POINTER(c_ulong), 'pdwMaxStreams' )),
    COMMETHOD([], HRESULT, 'SetRenderingPrefs',
              ( ['in'], c_ulong, 'dwRenderFlags' )),
    COMMETHOD([], HRESULT, 'GetRenderingPrefs',
              ( ['out'], POINTER(c_ulong), 'pdwRenderFlags' )),
    COMMETHOD([], HRESULT, 'SetRenderingMode',
              ( ['in'], c_ulong, 'mode' )),
    COMMETHOD([], HRESULT, 'GetRenderingMode',
              ( ['out'], POINTER(c_ulong), 'pMode' )),
]
################################################################
## code template for IVMRFilterConfig implementation
##class IVMRFilterConfig_Impl(object):
##    def GetNumberOfStreams(self):
##        '-no docstring-'
##        #return pdwMaxStreams
##
##    def SetImageCompositor(self, lpVMRImgCompositor):
##        '-no docstring-'
##        #return 
##
##    def GetRenderingPrefs(self):
##        '-no docstring-'
##        #return pdwRenderFlags
##
##    def GetRenderingMode(self):
##        '-no docstring-'
##        #return pMode
##
##    def SetRenderingPrefs(self, dwRenderFlags):
##        '-no docstring-'
##        #return 
##
##    def SetRenderingMode(self, mode):
##        '-no docstring-'
##        #return 
##
##    def SetNumberOfStreams(self, dwMaxStreams):
##        '-no docstring-'
##        #return 
##


# values for enumeration '_AM_FILTER_MISC_FLAGS'
AM_FILTER_MISC_FLAGS_IS_RENDERER = 1
AM_FILTER_MISC_FLAGS_IS_SOURCE = 2
_AM_FILTER_MISC_FLAGS = c_int # enum
class IDistributorNotify(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868AF-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IDistributorNotify._methods_ = [
    COMMETHOD([], HRESULT, 'Stop'),
    COMMETHOD([], HRESULT, 'Pause'),
    COMMETHOD([], HRESULT, 'Run',
              ( [], c_longlong, 'tStart' )),
    COMMETHOD([], HRESULT, 'SetSyncSource',
              ( ['in'], POINTER(IReferenceClock), 'pClock' )),
    COMMETHOD([], HRESULT, 'NotifyGraphChange'),
]
################################################################
## code template for IDistributorNotify implementation
##class IDistributorNotify_Impl(object):
##    def Run(self, tStart):
##        '-no docstring-'
##        #return 
##
##    def NotifyGraphChange(self):
##        '-no docstring-'
##        #return 
##
##    def Pause(self):
##        '-no docstring-'
##        #return 
##
##    def Stop(self):
##        '-no docstring-'
##        #return 
##
##    def SetSyncSource(self, pClock):
##        '-no docstring-'
##        #return 
##

class IVMRImagePresenter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRImagePresenter Interface'
    _iid_ = GUID('{CE704FE7-E71E-41FB-BAA2-C4403E1182F5}')
    _idlflags_ = []
IVMRImagePresenter._methods_ = [
    COMMETHOD([], HRESULT, 'StartPresenting',
              ( ['in'], ULONG_PTR, 'dwUserID' )),
    COMMETHOD([], HRESULT, 'StopPresenting',
              ( ['in'], ULONG_PTR, 'dwUserID' )),
    COMMETHOD([], HRESULT, 'PresentImage',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(tagVMRPRESENTATIONINFO), 'lpPresInfo' )),
]
################################################################
## code template for IVMRImagePresenter implementation
##class IVMRImagePresenter_Impl(object):
##    def StopPresenting(self, dwUserID):
##        '-no docstring-'
##        #return 
##
##    def StartPresenting(self, dwUserID):
##        '-no docstring-'
##        #return 
##
##    def PresentImage(self, dwUserID, lpPresInfo):
##        '-no docstring-'
##        #return 
##

class _FilterInfo(Structure):
    pass
IBaseFilter._methods_ = [
    COMMETHOD([], HRESULT, 'EnumPins',
              ( ['retval', 'out'], POINTER(POINTER(IEnumPins)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'FindPin',
              ( ['in'], WSTRING, 'Id' ),
              ( ['retval', 'out'], POINTER(POINTER(IPin)), 'ppPin' )),
    COMMETHOD([], HRESULT, 'QueryFilterInfo',
              ( ['retval', 'out'], POINTER(_FilterInfo), 'pInfo' )),
    COMMETHOD([], HRESULT, 'JoinFilterGraph',
              ( ['in'], POINTER(IFilterGraph), 'pGraph' ),
              ( ['in'], WSTRING, 'pName' )),
    COMMETHOD([], HRESULT, 'QueryVendorInfo',
              ( ['retval', 'out'], POINTER(WSTRING), 'pVendorInfo' )),
]
################################################################
## code template for IBaseFilter implementation
##class IBaseFilter_Impl(object):
##    def QueryVendorInfo(self):
##        '-no docstring-'
##        #return pVendorInfo
##
##    def FindPin(self, Id):
##        '-no docstring-'
##        #return ppPin
##
##    def JoinFilterGraph(self, pGraph, pName):
##        '-no docstring-'
##        #return 
##
##    def QueryFilterInfo(self):
##        '-no docstring-'
##        #return pInfo
##
##    def EnumPins(self):
##        '-no docstring-'
##        #return ppenum
##

class IOverlay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A1-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IOverlay._methods_ = [
    COMMETHOD([], HRESULT, 'GetPalette',
              ( ['out'], POINTER(c_ulong), 'pdwColors' ),
              ( ['out'], POINTER(POINTER(tagPALETTEENTRY)), 'ppPalette' )),
    COMMETHOD([], HRESULT, 'SetPalette',
              ( ['in'], c_ulong, 'dwColors' ),
              ( ['in'], POINTER(tagPALETTEENTRY), 'pPalette' )),
    COMMETHOD([], HRESULT, 'GetDefaultColorKey',
              ( ['out'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'GetColorKey',
              ( ['out'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'SetColorKey',
              ( ['in', 'out'], POINTER(tagCOLORKEY), 'pColorKey' )),
    COMMETHOD([], HRESULT, 'GetWindowHandle',
              ( ['out'], POINTER(wireHWND), 'pHwnd' )),
    COMMETHOD([], HRESULT, 'GetClipList',
              ( ['out'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['out'], POINTER(tagRECT), 'pDestinationRect' ),
              ( ['out'], POINTER(POINTER(_RGNDATA)), 'ppRgnData' )),
    COMMETHOD([], HRESULT, 'GetVideoPosition',
              ( ['out'], POINTER(tagRECT), 'pSourceRect' ),
              ( ['out'], POINTER(tagRECT), 'pDestinationRect' )),
    COMMETHOD([], HRESULT, 'Advise',
              ( ['in'], POINTER(IOverlayNotify), 'pOverlayNotify' ),
              ( ['in'], c_ulong, 'dwInterests' )),
    COMMETHOD([], HRESULT, 'Unadvise'),
]
################################################################
## code template for IOverlay implementation
##class IOverlay_Impl(object):
##    def GetDefaultColorKey(self):
##        '-no docstring-'
##        #return pColorKey
##
##    def GetColorKey(self):
##        '-no docstring-'
##        #return pColorKey
##
##    def SetPalette(self, dwColors, pPalette):
##        '-no docstring-'
##        #return 
##
##    def SetColorKey(self):
##        '-no docstring-'
##        #return pColorKey
##
##    def GetPalette(self):
##        '-no docstring-'
##        #return pdwColors, ppPalette
##
##    def Unadvise(self):
##        '-no docstring-'
##        #return 
##
##    def GetClipList(self):
##        '-no docstring-'
##        #return pSourceRect, pDestinationRect, ppRgnData
##
##    def Advise(self, pOverlayNotify, dwInterests):
##        '-no docstring-'
##        #return 
##
##    def GetVideoPosition(self):
##        '-no docstring-'
##        #return pSourceRect, pDestinationRect
##
##    def GetWindowHandle(self):
##        '-no docstring-'
##        #return pHwnd
##

class IAMExtDevice(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{B5730A90-1A2C-11CF-8C23-00AA006B6814}')
    _idlflags_ = []
IAMExtDevice._methods_ = [
    COMMETHOD([], HRESULT, 'GetCapability',
              ( ['in'], c_int, 'Capability' ),
              ( ['out'], POINTER(c_int), 'pValue' ),
              ( ['out'], POINTER(c_double), 'pdblValue' )),
    COMMETHOD([], HRESULT, 'get_ExternalDeviceID',
              ( ['out'], POINTER(WSTRING), 'ppszData' )),
    COMMETHOD([], HRESULT, 'get_ExternalDeviceVersion',
              ( ['out'], POINTER(WSTRING), 'ppszData' )),
    COMMETHOD([], HRESULT, 'put_DevicePower',
              ( ['in'], c_int, 'PowerMode' )),
    COMMETHOD([], HRESULT, 'get_DevicePower',
              ( ['out'], POINTER(c_int), 'pPowerMode' )),
    COMMETHOD([], HRESULT, 'Calibrate',
              ( ['in'], ULONG_PTR, 'hEvent' ),
              ( ['in'], c_int, 'mode' ),
              ( ['out'], POINTER(c_int), 'pStatus' )),
    COMMETHOD([], HRESULT, 'put_DevicePort',
              ( ['in'], c_int, 'DevicePort' )),
    COMMETHOD([], HRESULT, 'get_DevicePort',
              ( ['out'], POINTER(c_int), 'pDevicePort' )),
]
################################################################
## code template for IAMExtDevice implementation
##class IAMExtDevice_Impl(object):
##    def put_DevicePort(self, DevicePort):
##        '-no docstring-'
##        #return 
##
##    def GetCapability(self, Capability):
##        '-no docstring-'
##        #return pValue, pdblValue
##
##    def get_DevicePower(self):
##        '-no docstring-'
##        #return pPowerMode
##
##    def get_ExternalDeviceID(self):
##        '-no docstring-'
##        #return ppszData
##
##    def get_ExternalDeviceVersion(self):
##        '-no docstring-'
##        #return ppszData
##
##    def Calibrate(self, hEvent, mode):
##        '-no docstring-'
##        #return pStatus
##
##    def put_DevicePower(self, PowerMode):
##        '-no docstring-'
##        #return 
##
##    def get_DevicePort(self):
##        '-no docstring-'
##        #return pDevicePort
##


# values for enumeration 'tagAMTVAudioEventType'
AMTVAUDIO_EVENT_CHANGED = 1
tagAMTVAudioEventType = c_int # enum
class IVMRWindowlessControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRWindowlessControl Interface'
    _iid_ = GUID('{0EB1088C-4DCD-46F0-878F-39DAE86A51B7}')
    _idlflags_ = []
IVMRWindowlessControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetNativeVideoSize',
              ( ['out'], POINTER(c_int), 'lpWidth' ),
              ( ['out'], POINTER(c_int), 'lpHeight' ),
              ( ['out'], POINTER(c_int), 'lpARWidth' ),
              ( ['out'], POINTER(c_int), 'lpARHeight' )),
    COMMETHOD([], HRESULT, 'GetMinIdealVideoSize',
              ( ['out'], POINTER(c_int), 'lpWidth' ),
              ( ['out'], POINTER(c_int), 'lpHeight' )),
    COMMETHOD([], HRESULT, 'GetMaxIdealVideoSize',
              ( ['out'], POINTER(c_int), 'lpWidth' ),
              ( ['out'], POINTER(c_int), 'lpHeight' )),
    COMMETHOD([], HRESULT, 'SetVideoPosition',
              ( ['in'], POINTER(tagRECT), 'lpSRCRect' ),
              ( ['in'], POINTER(tagRECT), 'lpDSTRect' )),
    COMMETHOD([], HRESULT, 'GetVideoPosition',
              ( ['out'], POINTER(tagRECT), 'lpSRCRect' ),
              ( ['out'], POINTER(tagRECT), 'lpDSTRect' )),
    COMMETHOD([], HRESULT, 'GetAspectRatioMode',
              ( ['out'], POINTER(c_ulong), 'lpAspectRatioMode' )),
    COMMETHOD([], HRESULT, 'SetAspectRatioMode',
              ( ['in'], c_ulong, 'AspectRatioMode' )),
    COMMETHOD([], HRESULT, 'SetVideoClippingWindow',
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'RepaintVideo',
              ( ['in'], wireHWND, 'hwnd' ),
              ( ['in'], wireHDC, 'hdc' )),
    COMMETHOD([], HRESULT, 'DisplayModeChanged'),
    COMMETHOD([], HRESULT, 'GetCurrentImage',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'lpDib' )),
    COMMETHOD([], HRESULT, 'SetBorderColor',
              ( ['in'], c_ulong, 'Clr' )),
    COMMETHOD([], HRESULT, 'GetBorderColor',
              ( ['out'], POINTER(c_ulong), 'lpClr' )),
    COMMETHOD([], HRESULT, 'SetColorKey',
              ( ['in'], c_ulong, 'Clr' )),
    COMMETHOD([], HRESULT, 'GetColorKey',
              ( ['out'], POINTER(c_ulong), 'lpClr' )),
]
################################################################
## code template for IVMRWindowlessControl implementation
##class IVMRWindowlessControl_Impl(object):
##    def SetVideoPosition(self, lpSRCRect, lpDSTRect):
##        '-no docstring-'
##        #return 
##
##    def GetNativeVideoSize(self):
##        '-no docstring-'
##        #return lpWidth, lpHeight, lpARWidth, lpARHeight
##
##    def SetBorderColor(self, Clr):
##        '-no docstring-'
##        #return 
##
##    def SetAspectRatioMode(self, AspectRatioMode):
##        '-no docstring-'
##        #return 
##
##    def GetBorderColor(self):
##        '-no docstring-'
##        #return lpClr
##
##    def RepaintVideo(self, hwnd, hdc):
##        '-no docstring-'
##        #return 
##
##    def DisplayModeChanged(self):
##        '-no docstring-'
##        #return 
##
##    def SetColorKey(self, Clr):
##        '-no docstring-'
##        #return 
##
##    def GetAspectRatioMode(self):
##        '-no docstring-'
##        #return lpAspectRatioMode
##
##    def GetMinIdealVideoSize(self):
##        '-no docstring-'
##        #return lpWidth, lpHeight
##
##    def SetVideoClippingWindow(self, hwnd):
##        '-no docstring-'
##        #return 
##
##    def GetColorKey(self):
##        '-no docstring-'
##        #return lpClr
##
##    def GetMaxIdealVideoSize(self):
##        '-no docstring-'
##        #return lpWidth, lpHeight
##
##    def GetVideoPosition(self):
##        '-no docstring-'
##        #return lpSRCRect, lpDSTRect
##
##    def GetCurrentImage(self):
##        '-no docstring-'
##        #return lpDib
##

class IAMDroppedFrames(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13344-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMDroppedFrames._methods_ = [
    COMMETHOD([], HRESULT, 'GetNumDropped',
              ( ['out'], POINTER(c_int), 'plDropped' )),
    COMMETHOD([], HRESULT, 'GetNumNotDropped',
              ( ['out'], POINTER(c_int), 'plNotDropped' )),
    COMMETHOD([], HRESULT, 'GetDroppedInfo',
              ( ['in'], c_int, 'lSize' ),
              ( ['out'], POINTER(c_int), 'plArray' ),
              ( ['out'], POINTER(c_int), 'plNumCopied' )),
    COMMETHOD([], HRESULT, 'GetAverageFrameSize',
              ( ['out'], POINTER(c_int), 'plAverageSize' )),
]
################################################################
## code template for IAMDroppedFrames implementation
##class IAMDroppedFrames_Impl(object):
##    def GetDroppedInfo(self, lSize):
##        '-no docstring-'
##        #return plArray, plNumCopied
##
##    def GetAverageFrameSize(self):
##        '-no docstring-'
##        #return plAverageSize
##
##    def GetNumDropped(self):
##        '-no docstring-'
##        #return plDropped
##
##    def GetNumNotDropped(self):
##        '-no docstring-'
##        #return plNotDropped
##

_AMMediaType._fields_ = [
    ('majortype', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('subtype', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('bFixedSizeSamples', c_int),
    ('bTemporalCompression', c_int),
    ('lSampleSize', c_ulong),
    ('formattype', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('punk', POINTER(IUnknown)),
    ('cbFormat', c_ulong),
    ('pbFormat', POINTER(c_ubyte)),
]
assert sizeof(_AMMediaType) == 88, sizeof(_AMMediaType)
assert alignment(_AMMediaType) == 8, alignment(_AMMediaType)
DDCOLORKEY = __MIDL___MIDL_itf_DirectShow_0370_0001
class ISeekingPassThru(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{36B73883-C2C8-11CF-8B46-00805F6CEF60}')
    _idlflags_ = []
ISeekingPassThru._methods_ = [
    COMMETHOD([], HRESULT, 'Init',
              ( ['in'], c_int, 'bSupportRendering' ),
              ( ['in'], POINTER(IPin), 'pPin' )),
]
################################################################
## code template for ISeekingPassThru implementation
##class ISeekingPassThru_Impl(object):
##    def Init(self, bSupportRendering, pPin):
##        '-no docstring-'
##        #return 
##

class IAMCameraControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13370-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMCameraControl._methods_ = [
    COMMETHOD([], HRESULT, 'GetRange',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'pMin' ),
              ( ['out'], POINTER(c_int), 'pMax' ),
              ( ['out'], POINTER(c_int), 'pSteppingDelta' ),
              ( ['out'], POINTER(c_int), 'pDefault' ),
              ( ['out'], POINTER(c_int), 'pCapsFlags' )),
    COMMETHOD([], HRESULT, 'Set',
              ( ['in'], c_int, 'Property' ),
              ( ['in'], c_int, 'lValue' ),
              ( ['in'], c_int, 'Flags' )),
    COMMETHOD([], HRESULT, 'Get',
              ( ['in'], c_int, 'Property' ),
              ( ['out'], POINTER(c_int), 'lValue' ),
              ( ['out'], POINTER(c_int), 'Flags' )),
]
################################################################
## code template for IAMCameraControl implementation
##class IAMCameraControl_Impl(object):
##    def Set(self, Property, lValue, Flags):
##        '-no docstring-'
##        #return 
##
##    def GetRange(self, Property):
##        '-no docstring-'
##        #return pMin, pMax, pSteppingDelta, pDefault, pCapsFlags
##
##    def Get(self, Property):
##        '-no docstring-'
##        #return lValue, Flags
##

class IAMDecoderCaps(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C0DFF467-D499-4986-972B-E1D9090FA941}')
    _idlflags_ = []
IAMDecoderCaps._methods_ = [
    COMMETHOD([], HRESULT, 'GetDecoderCaps',
              ( ['in'], c_ulong, 'dwCapIndex' ),
              ( ['out'], POINTER(c_ulong), 'lpdwCap' )),
]
################################################################
## code template for IAMDecoderCaps implementation
##class IAMDecoderCaps_Impl(object):
##    def GetDecoderCaps(self, dwCapIndex):
##        '-no docstring-'
##        #return lpdwCap
##

IVMRSurfaceAllocator._methods_ = [
    COMMETHOD([], HRESULT, 'AllocateSurface',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(tagVMRALLOCATIONINFO), 'lpAllocInfo' ),
              ( ['in', 'out'], POINTER(c_ulong), 'lpdwActualBuffers' ),
              ( ['out'], POINTER(POINTER(c_ulong)), 'lplpSurface' )),
    COMMETHOD([], HRESULT, 'FreeSurface',
              ( ['in'], ULONG_PTR, 'dwID' )),
    COMMETHOD([], HRESULT, 'PrepareSurface',
              ( ['in'], ULONG_PTR, 'dwUserID' ),
              ( ['in'], POINTER(c_ulong), 'lpSurface' ),
              ( ['in'], c_ulong, 'dwSurfaceFlags' )),
    COMMETHOD([], HRESULT, 'AdviseNotify',
              ( ['in'], POINTER(IVMRSurfaceAllocatorNotify), 'lpIVMRSurfAllocNotify' )),
]
################################################################
## code template for IVMRSurfaceAllocator implementation
##class IVMRSurfaceAllocator_Impl(object):
##    def AllocateSurface(self, dwUserID, lpAllocInfo):
##        '-no docstring-'
##        #return lpdwActualBuffers, lplpSurface
##
##    def PrepareSurface(self, dwUserID, lpSurface, dwSurfaceFlags):
##        '-no docstring-'
##        #return 
##
##    def AdviseNotify(self, lpIVMRSurfAllocNotify):
##        '-no docstring-'
##        #return 
##
##    def FreeSurface(self, dwID):
##        '-no docstring-'
##        #return 
##

class IAMTimecodeDisplay(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{9B496CE2-811B-11CF-8C77-00AA006B6814}')
    _idlflags_ = []
IAMTimecodeDisplay._methods_ = [
    COMMETHOD([], HRESULT, 'GetTCDisplayEnable',
              ( ['out'], POINTER(c_int), 'pState' )),
    COMMETHOD([], HRESULT, 'SetTCDisplayEnable',
              ( ['in'], c_int, 'State' )),
    COMMETHOD([], HRESULT, 'GetTCDisplay',
              ( ['in'], c_int, 'Param' ),
              ( ['out'], POINTER(c_int), 'pValue' )),
    COMMETHOD([], HRESULT, 'SetTCDisplay',
              ( ['in'], c_int, 'Param' ),
              ( ['in'], c_int, 'Value' )),
]
################################################################
## code template for IAMTimecodeDisplay implementation
##class IAMTimecodeDisplay_Impl(object):
##    def SetTCDisplayEnable(self, State):
##        '-no docstring-'
##        #return 
##
##    def SetTCDisplay(self, Param, Value):
##        '-no docstring-'
##        #return 
##
##    def GetTCDisplayEnable(self):
##        '-no docstring-'
##        #return pState
##
##    def GetTCDisplay(self, Param):
##        '-no docstring-'
##        #return pValue
##

AM_STREAM_INFO_FLAGS = __MIDL___MIDL_itf_DirectShow_0156_0001
class IMemAllocatorCallbackTemp(IMemAllocator):
    _case_insensitive_ = True
    _iid_ = GUID('{379A0CF0-C1DE-11D2-ABF5-00A0C905F375}')
    _idlflags_ = []
IMemAllocatorCallbackTemp._methods_ = [
    COMMETHOD([], HRESULT, 'SetNotify',
              ( ['in'], POINTER(IMemAllocatorNotifyCallbackTemp), 'pNotify' )),
    COMMETHOD([], HRESULT, 'GetFreeCount',
              ( ['out'], POINTER(c_int), 'plBuffersFree' )),
]
################################################################
## code template for IMemAllocatorCallbackTemp implementation
##class IMemAllocatorCallbackTemp_Impl(object):
##    def SetNotify(self, pNotify):
##        '-no docstring-'
##        #return 
##
##    def GetFreeCount(self):
##        '-no docstring-'
##        #return plBuffersFree
##


# values for enumeration '_DVENCODERRESOLUTION'
DVENCODERRESOLUTION_720x480 = 2012
DVENCODERRESOLUTION_360x240 = 2013
DVENCODERRESOLUTION_180x120 = 2014
DVENCODERRESOLUTION_88x60 = 2015
_DVENCODERRESOLUTION = c_int # enum
class IAMDeviceRemoval(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{F90A6130-B658-11D2-AE49-0000F8754B99}')
    _idlflags_ = []
IAMDeviceRemoval._methods_ = [
    COMMETHOD([], HRESULT, 'DeviceInfo',
              ( ['out'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'pclsidInterfaceClass' ),
              ( ['out'], POINTER(POINTER(c_ushort)), 'pwszSymbolicLink' )),
    COMMETHOD([], HRESULT, 'Reassociate'),
    COMMETHOD([], HRESULT, 'Disassociate'),
]
################################################################
## code template for IAMDeviceRemoval implementation
##class IAMDeviceRemoval_Impl(object):
##    def Reassociate(self):
##        '-no docstring-'
##        #return 
##
##    def DeviceInfo(self):
##        '-no docstring-'
##        #return pclsidInterfaceClass, pwszSymbolicLink
##
##    def Disassociate(self):
##        '-no docstring-'
##        #return 
##

class IRunningObjectTable(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000010-0000-0000-C000-000000000046}')
    _idlflags_ = []
IRunningObjectTable._methods_ = [
    COMMETHOD([], HRESULT, 'Register',
              ( ['in'], c_ulong, 'grfFlags' ),
              ( ['in'], POINTER(IUnknown), 'punkObject' ),
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(c_ulong), 'pdwRegister' )),
    COMMETHOD([], HRESULT, 'Revoke',
              ( ['in'], c_ulong, 'dwRegister' )),
    COMMETHOD([], HRESULT, 'IsRunning',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' )),
    COMMETHOD([], HRESULT, 'GetObject',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunkObject' )),
    COMMETHOD([], HRESULT, 'NoteChangeTime',
              ( ['in'], c_ulong, 'dwRegister' ),
              ( ['in'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'GetTimeOfLastChange',
              ( ['in'], POINTER(IMoniker), 'pmkObjectName' ),
              ( ['out'], POINTER(_FILETIME), 'pfiletime' )),
    COMMETHOD([], HRESULT, 'EnumRunning',
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' )),
]
################################################################
## code template for IRunningObjectTable implementation
##class IRunningObjectTable_Impl(object):
##    def Register(self, grfFlags, punkObject, pmkObjectName):
##        '-no docstring-'
##        #return pdwRegister
##
##    def IsRunning(self, pmkObjectName):
##        '-no docstring-'
##        #return 
##
##    def GetTimeOfLastChange(self, pmkObjectName):
##        '-no docstring-'
##        #return pfiletime
##
##    def GetObject(self, pmkObjectName):
##        '-no docstring-'
##        #return ppunkObject
##
##    def NoteChangeTime(self, dwRegister, pfiletime):
##        '-no docstring-'
##        #return 
##
##    def EnumRunning(self):
##        '-no docstring-'
##        #return ppenumMoniker
##
##    def Revoke(self, dwRegister):
##        '-no docstring-'
##        #return 
##

class IEnumMediaTypes(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{89C31040-846B-11CE-97D3-00AA0055595A}')
    _idlflags_ = []
    def __iter__(self):
        return self

    def next(self):
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise StopIteration

    def __getitem__(self, index):
        self.Reset()
        self.Skip(index)
        item, fetched = self.Next(1)
        if fetched:
            return item
        raise IndexError(index)

IPin._methods_ = [
    COMMETHOD([], HRESULT, 'Connect',
              ( ['in'], POINTER(IPin), 'pReceivePin' ),
              ( ['in'], c_ulong, 'pmt' )),
    COMMETHOD([], HRESULT, 'ReceiveConnection',
              ( ['in'], POINTER(IPin), 'pConnector' ),
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'Disconnect'),
    COMMETHOD([], HRESULT, 'ConnectedTo',
              ( ['retval', 'out'], POINTER(POINTER(IPin)), 'pPin' )),
    COMMETHOD([], HRESULT, 'ConnectionMediaType',
              ( ['out'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'QueryPinInfo',
              ( ['retval', 'out'], POINTER(_PinInfo), 'pInfo' )),
    COMMETHOD([], HRESULT, 'QueryDirection',
              ( ['retval', 'out'], POINTER(_PinDirection), 'pPinDir' )),
    COMMETHOD([], HRESULT, 'QueryId',
              ( ['retval', 'out'], POINTER(WSTRING), 'Id' )),
    COMMETHOD([], HRESULT, 'QueryAccept',
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'EnumMediaTypes',
              ( ['retval', 'out'], POINTER(POINTER(IEnumMediaTypes)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'QueryInternalConnections',
              ( ['out'], POINTER(POINTER(IPin)), 'apPin' ),
              ( ['in', 'out'], POINTER(c_ulong), 'nPin' )),
    COMMETHOD([], HRESULT, 'EndOfStream'),
    COMMETHOD([], HRESULT, 'BeginFlush'),
    COMMETHOD([], HRESULT, 'EndFlush'),
    COMMETHOD([], HRESULT, 'NewSegment',
              ( ['in'], c_longlong, 'tStart' ),
              ( ['in'], c_longlong, 'tStop' ),
              ( ['in'], c_double, 'dRate' )),
]
################################################################
## code template for IPin implementation
##class IPin_Impl(object):
##    def QueryPinInfo(self):
##        '-no docstring-'
##        #return pInfo
##
##    def Disconnect(self):
##        '-no docstring-'
##        #return 
##
##    def BeginFlush(self):
##        '-no docstring-'
##        #return 
##
##    def EndFlush(self):
##        '-no docstring-'
##        #return 
##
##    def QueryDirection(self):
##        '-no docstring-'
##        #return pPinDir
##
##    def ReceiveConnection(self, pConnector, pmt):
##        '-no docstring-'
##        #return 
##
##    def NewSegment(self, tStart, tStop, dRate):
##        '-no docstring-'
##        #return 
##
##    def ConnectedTo(self):
##        '-no docstring-'
##        #return pPin
##
##    def EnumMediaTypes(self):
##        '-no docstring-'
##        #return ppenum
##
##    def ConnectionMediaType(self):
##        '-no docstring-'
##        #return pmt
##
##    def EndOfStream(self):
##        '-no docstring-'
##        #return 
##
##    def QueryId(self):
##        '-no docstring-'
##        #return Id
##
##    def Connect(self, pReceivePin, pmt):
##        '-no docstring-'
##        #return 
##
##    def QueryInternalConnections(self):
##        '-no docstring-'
##        #return apPin, nPin
##
##    def QueryAccept(self, pmt):
##        '-no docstring-'
##        #return 
##

class AviSplitter(CoClass):
    u'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/avisplitterfilter.asp'
    _reg_clsid_ = GUID('{1B544C20-FD0B-11CE-8C63-00AA0044B51E}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IPersistMediaPropertyBag(IPersist):
    _case_insensitive_ = True
    _iid_ = GUID('{5738E040-B67F-11D0-BD4D-00A0C911CE86}')
    _idlflags_ = []
AviSplitter._com_interfaces_ = [IBaseFilter, IPersistMediaPropertyBag]

class IAMTVAudioNotification(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{83EC1C33-23D1-11D1-99E6-00A0C9560266}')
    _idlflags_ = []
IAMTVAudioNotification._methods_ = [
    COMMETHOD([], HRESULT, 'OnEvent',
              ( ['in'], tagAMTVAudioEventType, 'Event' )),
]
################################################################
## code template for IAMTVAudioNotification implementation
##class IAMTVAudioNotification_Impl(object):
##    def OnEvent(self, Event):
##        '-no docstring-'
##        #return 
##


# values for enumeration 'AMOVERLAYFX'
AMOVERFX_NOFX = 0
AMOVERFX_MIRRORLEFTRIGHT = 2
AMOVERFX_MIRRORUPDOWN = 4
AMOVERFX_DEINTERLACE = 8
AMOVERLAYFX = c_int # enum
class tagAM_SAMPLE2_PROPERTIES(Structure):
    pass
tagAM_SAMPLE2_PROPERTIES._fields_ = [
    ('cbData', c_ulong),
    ('dwTypeSpecificFlags', c_ulong),
    ('dwSampleFlags', c_ulong),
    ('lActual', c_int),
    ('tStart', c_longlong),
    ('tStop', c_longlong),
    ('dwStreamId', c_ulong),
    ('pMediaType', POINTER(_AMMediaType)),
    ('pbBuffer', POINTER(c_ubyte)),
    ('cbBuffer', c_int),
]
assert sizeof(tagAM_SAMPLE2_PROPERTIES) == 64, sizeof(tagAM_SAMPLE2_PROPERTIES)
assert alignment(tagAM_SAMPLE2_PROPERTIES) == 8, alignment(tagAM_SAMPLE2_PROPERTIES)
class DvSplitter(CoClass):
    u'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/dvsplitterfilter.asp'
    _reg_clsid_ = GUID('{4EB31670-9FC6-11CF-AF6E-00AA00B67A42}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
class IDVSplitter(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{92A3A302-DA7C-4A1F-BA7E-1802BB5D2D02}')
    _idlflags_ = []
DvSplitter._com_interfaces_ = [IDVSplitter, IBaseFilter]


# values for enumeration '_AMRESCTL_RESERVEFLAGS'
AMRESCTL_RESERVEFLAGS_RESERVE = 0
AMRESCTL_RESERVEFLAGS_UNRESERVE = 1
_AMRESCTL_RESERVEFLAGS = c_int # enum

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0376_0003'
MAX_NUMBER_OF_STREAMS = 16
__MIDL___MIDL_itf_DirectShow_0376_0003 = c_int # enum

# values for enumeration '_AM_PUSHSOURCE_FLAGS'
AM_PUSHSOURCECAPS_INTERNAL_RM = 1
AM_PUSHSOURCECAPS_NOT_LIVE = 2
AM_PUSHSOURCECAPS_PRIVATE_CLOCK = 4
AM_PUSHSOURCEREQS_USE_STREAM_CLOCK = 65536
_AM_PUSHSOURCE_FLAGS = c_int # enum
VMRDeinterlacePrefs = __MIDL___MIDL_itf_DirectShow_0378_0001
class IEnumString(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{00000101-0000-0000-C000-000000000046}')
    _idlflags_ = []
IEnumString._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteNext',
              ( ['in'], c_ulong, 'celt' ),
              ( ['out'], POINTER(WSTRING), 'rgelt' ),
              ( ['out'], POINTER(c_ulong), 'pceltFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'celt' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
]
################################################################
## code template for IEnumString implementation
##class IEnumString_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, celt):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def RemoteNext(self, celt):
##        '-no docstring-'
##        #return rgelt, pceltFetched
##

class IAMGraphBuilderCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4995F511-9DDB-4F12-BD3B-F04611807B79}')
    _idlflags_ = []
IAMGraphBuilderCallback._methods_ = [
    COMMETHOD([], HRESULT, 'SelectedFilter',
              ( ['in'], POINTER(IMoniker), 'pMon' )),
    COMMETHOD([], HRESULT, 'CreatedFilter',
              ( ['in'], POINTER(IBaseFilter), 'pFil' )),
]
################################################################
## code template for IAMGraphBuilderCallback implementation
##class IAMGraphBuilderCallback_Impl(object):
##    def CreatedFilter(self, pFil):
##        '-no docstring-'
##        #return 
##
##    def SelectedFilter(self, pMon):
##        '-no docstring-'
##        #return 
##

class IAMStreamConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13340-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMStreamConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetFormat',
              ( ['in'], POINTER(_AMMediaType), 'pmt' )),
    COMMETHOD([], HRESULT, 'GetFormat',
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppmt' )),
    COMMETHOD([], HRESULT, 'GetNumberOfCapabilities',
              ( ['out'], POINTER(c_int), 'piCount' ),
              ( ['out'], POINTER(c_int), 'piSize' )),
    COMMETHOD([], HRESULT, 'GetStreamCaps',
              ( ['in'], c_int, 'iIndex' ),
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppmt' ),
              ( ['out'], POINTER(c_ubyte), 'pSCC' )),
]
################################################################
## code template for IAMStreamConfig implementation
##class IAMStreamConfig_Impl(object):
##    def SetFormat(self, pmt):
##        '-no docstring-'
##        #return 
##
##    def GetStreamCaps(self, iIndex):
##        '-no docstring-'
##        #return ppmt, pSCC
##
##    def GetFormat(self):
##        '-no docstring-'
##        #return ppmt
##
##    def GetNumberOfCapabilities(self):
##        '-no docstring-'
##        #return piCount, piSize
##


# values for enumeration 'tagPhysicalConnectorType'
PhysConn_Video_Tuner = 1
PhysConn_Video_Composite = 2
PhysConn_Video_SVideo = 3
PhysConn_Video_RGB = 4
PhysConn_Video_YRYBY = 5
PhysConn_Video_SerialDigital = 6
PhysConn_Video_ParallelDigital = 7
PhysConn_Video_SCSI = 8
PhysConn_Video_AUX = 9
PhysConn_Video_1394 = 10
PhysConn_Video_USB = 11
PhysConn_Video_VideoDecoder = 12
PhysConn_Video_VideoEncoder = 13
PhysConn_Video_SCART = 14
PhysConn_Video_Black = 15
PhysConn_Audio_Tuner = 4096
PhysConn_Audio_Line = 4097
PhysConn_Audio_Mic = 4098
PhysConn_Audio_AESDigital = 4099
PhysConn_Audio_SPDIFDigital = 4100
PhysConn_Audio_SCSI = 4101
PhysConn_Audio_AUX = 4102
PhysConn_Audio_1394 = 4103
PhysConn_Audio_USB = 4104
PhysConn_Audio_AudioDecoder = 4105
tagPhysicalConnectorType = c_int # enum
class IVMRMonitorConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRMonitorConfig Interface'
    _iid_ = GUID('{9CF0B1B6-FBAA-4B7F-88CF-CF1F130A0DCE}')
    _idlflags_ = []
class tagVMRMONITORINFO(Structure):
    pass
IVMRMonitorConfig._methods_ = [
    COMMETHOD([], HRESULT, 'SetMonitor',
              ( ['in'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'GetMonitor',
              ( ['out'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'SetDefaultMonitor',
              ( ['in'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'GetDefaultMonitor',
              ( ['out'], POINTER(tagVMRGUID), 'pGUID' )),
    COMMETHOD([], HRESULT, 'GetAvailableMonitors',
              ( ['out'], POINTER(tagVMRMONITORINFO), 'pInfo' ),
              ( ['in'], c_ulong, 'dwMaxInfoArraySize' ),
              ( ['out'], POINTER(c_ulong), 'pdwNumDevices' )),
]
################################################################
## code template for IVMRMonitorConfig implementation
##class IVMRMonitorConfig_Impl(object):
##    def SetMonitor(self, pGUID):
##        '-no docstring-'
##        #return 
##
##    def GetAvailableMonitors(self, dwMaxInfoArraySize):
##        '-no docstring-'
##        #return pInfo, pdwNumDevices
##
##    def SetDefaultMonitor(self, pGUID):
##        '-no docstring-'
##        #return 
##
##    def GetMonitor(self):
##        '-no docstring-'
##        #return pGUID
##
##    def GetDefaultMonitor(self):
##        '-no docstring-'
##        #return pGUID
##

class IDecimateVideoImage(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{2E5EA3E0-E924-11D2-B6DA-00A0C995E8DF}')
    _idlflags_ = []
IDecimateVideoImage._methods_ = [
    COMMETHOD([], HRESULT, 'SetDecimationImageSize',
              ( ['in'], c_int, 'lWidth' ),
              ( ['in'], c_int, 'lHeight' )),
    COMMETHOD([], HRESULT, 'ResetDecimationImageSize'),
]
################################################################
## code template for IDecimateVideoImage implementation
##class IDecimateVideoImage_Impl(object):
##    def ResetDecimationImageSize(self):
##        '-no docstring-'
##        #return 
##
##    def SetDecimationImageSize(self, lWidth, lHeight):
##        '-no docstring-'
##        #return 
##

IResourceConsumer._methods_ = [
    COMMETHOD([], HRESULT, 'AcquireResource',
              ( ['in'], c_int, 'idResource' )),
    COMMETHOD([], HRESULT, 'ReleaseResource',
              ( ['in'], c_int, 'idResource' )),
]
################################################################
## code template for IResourceConsumer implementation
##class IResourceConsumer_Impl(object):
##    def ReleaseResource(self, idResource):
##        '-no docstring-'
##        #return 
##
##    def AcquireResource(self, idResource):
##        '-no docstring-'
##        #return 
##

class DvVideoDecoder(CoClass):
    u'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/dvvideodecoderfilter.asp'
    _reg_clsid_ = GUID('{B1B77C00-C3E4-11CF-AF79-00AA00B67A42}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
DvVideoDecoder._com_interfaces_ = [IIPDVDec, IDVRGB219, IBaseFilter]


# values for enumeration '_DVRESOLUTION'
DVRESOLUTION_FULL = 1000
DVRESOLUTION_HALF = 1001
DVRESOLUTION_QUARTER = 1002
DVRESOLUTION_DC = 1003
_DVRESOLUTION = c_int # enum
class IMediaEventSink(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{56A868A2-0AD4-11CE-B03A-0020AF0BA770}')
    _idlflags_ = []
IMediaEventSink._methods_ = [
    COMMETHOD([], HRESULT, 'Notify',
              ( ['in'], c_int, 'EventCode' ),
              ( ['in'], LONG_PTR, 'EventParam1' ),
              ( ['in'], LONG_PTR, 'EventParam2' )),
]
################################################################
## code template for IMediaEventSink implementation
##class IMediaEventSink_Impl(object):
##    def Notify(self, EventCode, EventParam1, EventParam2):
##        '-no docstring-'
##        #return 
##

class IAMVfwCaptureDialogs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D8D715A0-6E5E-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMVfwCaptureDialogs._methods_ = [
    COMMETHOD([], HRESULT, 'HasDialog',
              ( ['in'], c_int, 'iDialog' )),
    COMMETHOD([], HRESULT, 'ShowDialog',
              ( ['in'], c_int, 'iDialog' ),
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'SendDriverMessage',
              ( ['in'], c_int, 'iDialog' ),
              ( ['in'], c_int, 'uMsg' ),
              ( ['in'], c_int, 'dw1' ),
              ( ['in'], c_int, 'dw2' )),
]
################################################################
## code template for IAMVfwCaptureDialogs implementation
##class IAMVfwCaptureDialogs_Impl(object):
##    def HasDialog(self, iDialog):
##        '-no docstring-'
##        #return 
##
##    def SendDriverMessage(self, iDialog, uMsg, dw1, dw2):
##        '-no docstring-'
##        #return 
##
##    def ShowDialog(self, iDialog, hwnd):
##        '-no docstring-'
##        #return 
##

IEnumFilters._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cFilters' ),
              ( ['out'], POINTER(POINTER(IBaseFilter)), 'ppFilter' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cFilters' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumFilters)), 'ppenum' )),
]
################################################################
## code template for IEnumFilters implementation
##class IEnumFilters_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cFilters):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, cFilters):
##        '-no docstring-'
##        #return ppFilter, pcFetched
##

class IGraphConfig(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{03A1EB8E-32BF-4245-8502-114D08A9CB88}')
    _idlflags_ = []
class IGraphConfigCallback(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{ADE0FD60-D19D-11D2-ABF6-00A0C905F375}')
    _idlflags_ = []
IGraphConfig._methods_ = [
    COMMETHOD([], HRESULT, 'Reconnect',
              ( ['in'], POINTER(IPin), 'pOutputPin' ),
              ( ['in'], POINTER(IPin), 'pInputPin' ),
              ( ['in'], POINTER(_AMMediaType), 'pmtFirstConnection' ),
              ( ['in'], POINTER(IBaseFilter), 'pUsingFilter' ),
              ( ['in'], c_void_p, 'hAbortEvent' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'Reconfigure',
              ( ['in'], POINTER(IGraphConfigCallback), 'pCallback' ),
              ( ['in'], c_void_p, 'pvContext' ),
              ( ['in'], c_ulong, 'dwFlags' ),
              ( ['in'], c_void_p, 'hAbortEvent' )),
    COMMETHOD([], HRESULT, 'AddFilterToCache',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' )),
    COMMETHOD([], HRESULT, 'EnumCacheFilter',
              ( ['out'], POINTER(POINTER(IEnumFilters)), 'pEnum' )),
    COMMETHOD([], HRESULT, 'RemoveFilterFromCache',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' )),
    COMMETHOD([], HRESULT, 'GetStartTime',
              ( ['out'], POINTER(c_longlong), 'prtStart' )),
    COMMETHOD([], HRESULT, 'PushThroughData',
              ( ['in'], POINTER(IPin), 'pOutputPin' ),
              ( ['in'], POINTER(IPinConnection), 'pConnection' ),
              ( ['in'], c_void_p, 'hEventAbort' )),
    COMMETHOD([], HRESULT, 'SetFilterFlags',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'GetFilterFlags',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( ['out'], POINTER(c_ulong), 'pdwFlags' )),
    COMMETHOD([], HRESULT, 'RemoveFilterEx',
              ( ['in'], POINTER(IBaseFilter), 'pFilter' ),
              ( [], c_ulong, 'Flags' )),
]
################################################################
## code template for IGraphConfig implementation
##class IGraphConfig_Impl(object):
##    def RemoveFilterFromCache(self, pFilter):
##        '-no docstring-'
##        #return 
##
##    def AddFilterToCache(self, pFilter):
##        '-no docstring-'
##        #return 
##
##    def Reconnect(self, pOutputPin, pInputPin, pmtFirstConnection, pUsingFilter, hAbortEvent, dwFlags):
##        '-no docstring-'
##        #return 
##
##    def EnumCacheFilter(self):
##        '-no docstring-'
##        #return pEnum
##
##    def RemoveFilterEx(self, pFilter, Flags):
##        '-no docstring-'
##        #return 
##
##    def SetFilterFlags(self, pFilter, dwFlags):
##        '-no docstring-'
##        #return 
##
##    def Reconfigure(self, pCallback, pvContext, dwFlags, hAbortEvent):
##        '-no docstring-'
##        #return 
##
##    def PushThroughData(self, pOutputPin, pConnection, hEventAbort):
##        '-no docstring-'
##        #return 
##
##    def GetFilterFlags(self, pFilter):
##        '-no docstring-'
##        #return pdwFlags
##
##    def GetStartTime(self):
##        '-no docstring-'
##        #return prtStart
##

VMRRenderPrefs = __MIDL___MIDL_itf_DirectShow_0376_0001

# values for enumeration '__MIDL___MIDL_itf_DirectShow_0138_0001'
CK_NOCOLORKEY = 0
CK_INDEX = 1
CK_RGB = 2
__MIDL___MIDL_itf_DirectShow_0138_0001 = c_int # enum

# values for enumeration 'tagAMTunerSignalStrength'
AMTUNER_HASNOSIGNALSTRENGTH = -1
AMTUNER_NOSIGNAL = 0
AMTUNER_SIGNALPRESENT = 1
tagAMTunerSignalStrength = c_int # enum
REGFILTER = __MIDL___MIDL_itf_DirectShow_0130_0001
IEnumRegFilters._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cFilters' ),
              ( ['out'], POINTER(POINTER(REGFILTER)), 'apRegFilter' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cFilters' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumRegFilters)), 'ppenum' )),
]
################################################################
## code template for IEnumRegFilters implementation
##class IEnumRegFilters_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cFilters):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, cFilters):
##        '-no docstring-'
##        #return apRegFilter, pcFetched
##

IConfigAviMux._methods_ = [
    COMMETHOD([], HRESULT, 'SetMasterStream',
              ( ['in'], c_int, 'IStream' )),
    COMMETHOD([], HRESULT, 'GetMasterStream',
              ( ['out'], POINTER(c_int), 'pStream' )),
    COMMETHOD([], HRESULT, 'SetOutputCompatibilityIndex',
              ( ['in'], c_int, 'fOldIndex' )),
    COMMETHOD([], HRESULT, 'GetOutputCompatibilityIndex',
              ( ['out'], POINTER(c_int), 'pfOldIndex' )),
]
################################################################
## code template for IConfigAviMux implementation
##class IConfigAviMux_Impl(object):
##    def SetOutputCompatibilityIndex(self, fOldIndex):
##        '-no docstring-'
##        #return 
##
##    def GetMasterStream(self):
##        '-no docstring-'
##        #return pStream
##
##    def GetOutputCompatibilityIndex(self):
##        '-no docstring-'
##        #return pfOldIndex
##
##    def SetMasterStream(self, IStream):
##        '-no docstring-'
##        #return 
##

class IAMovieSetup(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{A3D8CEC0-7E5A-11CF-BBC5-00805F6CEF20}')
    _idlflags_ = []
IAMovieSetup._methods_ = [
    COMMETHOD([], HRESULT, 'Register'),
    COMMETHOD([], HRESULT, 'Unregister'),
]
################################################################
## code template for IAMovieSetup implementation
##class IAMovieSetup_Impl(object):
##    def Unregister(self):
##        '-no docstring-'
##        #return 
##
##    def Register(self):
##        '-no docstring-'
##        #return 
##

class Library(object):
    u'DirectShow type library (Kohsuke private build)'
    name = u'DirectShowLib'
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)

IBindCtx._methods_ = [
    COMMETHOD([], HRESULT, 'RegisterObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'RevokeObjectBound',
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'ReleaseBoundObjects'),
    COMMETHOD([], HRESULT, 'RemoteSetBindOptions',
              ( ['in'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'RemoteGetBindOptions',
              ( ['in', 'out'], POINTER(tagBIND_OPTS2), 'pbindopts' )),
    COMMETHOD([], HRESULT, 'GetRunningObjectTable',
              ( ['out'], POINTER(POINTER(IRunningObjectTable)), 'pprot' )),
    COMMETHOD([], HRESULT, 'RegisterObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['in'], POINTER(IUnknown), 'punk' )),
    COMMETHOD([], HRESULT, 'GetObjectParam',
              ( ['in'], WSTRING, 'pszKey' ),
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppunk' )),
    COMMETHOD([], HRESULT, 'EnumObjectParam',
              ( ['out'], POINTER(POINTER(IEnumString)), 'ppenum' )),
    COMMETHOD([], HRESULT, 'RevokeObjectParam',
              ( ['in'], WSTRING, 'pszKey' )),
]
################################################################
## code template for IBindCtx implementation
##class IBindCtx_Impl(object):
##    def RemoteGetBindOptions(self):
##        '-no docstring-'
##        #return pbindopts
##
##    def RegisterObjectBound(self, punk):
##        '-no docstring-'
##        #return 
##
##    def RevokeObjectParam(self, pszKey):
##        '-no docstring-'
##        #return 
##
##    def ReleaseBoundObjects(self):
##        '-no docstring-'
##        #return 
##
##    def EnumObjectParam(self):
##        '-no docstring-'
##        #return ppenum
##
##    def GetObjectParam(self, pszKey):
##        '-no docstring-'
##        #return ppunk
##
##    def GetRunningObjectTable(self):
##        '-no docstring-'
##        #return pprot
##
##    def RevokeObjectBound(self, punk):
##        '-no docstring-'
##        #return 
##
##    def RemoteSetBindOptions(self, pbindopts):
##        '-no docstring-'
##        #return 
##
##    def RegisterObjectParam(self, pszKey, punk):
##        '-no docstring-'
##        #return 
##

_VMRVIDEOSTREAMINFO._fields_ = [
    ('pddsVideoSurface', POINTER(c_ulong)),
    ('dwWidth', c_ulong),
    ('dwHeight', c_ulong),
    ('dwStrmID', c_ulong),
    ('fAlpha', c_float),
    ('ddClrKey', DDCOLORKEY),
    ('rNormal', _NORMALIZEDRECT),
]
assert sizeof(_VMRVIDEOSTREAMINFO) == 48, sizeof(_VMRVIDEOSTREAMINFO)
assert alignment(_VMRVIDEOSTREAMINFO) == 8, alignment(_VMRVIDEOSTREAMINFO)
class IAMGraphStreams(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{632105FA-072E-11D3-8AF9-00C04FB6BD3D}')
    _idlflags_ = []
IAMGraphStreams._methods_ = [
    COMMETHOD([], HRESULT, 'FindUpstreamInterface',
              ( ['in'], POINTER(IPin), 'pPin' ),
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'riid' ),
              ( ['out'], POINTER(c_void_p), 'ppvInterface' ),
              ( ['in'], c_ulong, 'dwFlags' )),
    COMMETHOD([], HRESULT, 'SyncUsingStreamOffset',
              ( ['in'], c_int, 'bUseStreamOffset' )),
    COMMETHOD([], HRESULT, 'SetMaxGraphLatency',
              ( ['in'], c_longlong, 'rtMaxGraphLatency' )),
]
################################################################
## code template for IAMGraphStreams implementation
##class IAMGraphStreams_Impl(object):
##    def FindUpstreamInterface(self, pPin, riid, dwFlags):
##        '-no docstring-'
##        #return ppvInterface
##
##    def SyncUsingStreamOffset(self, bUseStreamOffset):
##        '-no docstring-'
##        #return 
##
##    def SetMaxGraphLatency(self, rtMaxGraphLatency):
##        '-no docstring-'
##        #return 
##

class IAMClockAdjust(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{4D5466B0-A49C-11D1-ABE8-00A0C905F375}')
    _idlflags_ = []
IAMClockAdjust._methods_ = [
    COMMETHOD([], HRESULT, 'SetClockDelta',
              ( ['in'], c_longlong, 'rtDelta' )),
]
################################################################
## code template for IAMClockAdjust implementation
##class IAMClockAdjust_Impl(object):
##    def SetClockDelta(self, rtDelta):
##        '-no docstring-'
##        #return 
##

class IKsPropertySet(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{31EFAC30-515C-11D0-A9AA-00AA0061BE93}')
    _idlflags_ = []
IKsPropertySet._methods_ = [
    COMMETHOD([], HRESULT, 'RemoteSet',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'guidPropSet' ),
              ( ['in'], c_ulong, 'dwPropID' ),
              ( ['in'], POINTER(c_ubyte), 'pInstanceData' ),
              ( ['in'], c_ulong, 'cbInstanceData' ),
              ( ['in'], POINTER(c_ubyte), 'pPropData' ),
              ( ['in'], c_ulong, 'cbPropData' )),
    COMMETHOD([], HRESULT, 'RemoteGet',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'guidPropSet' ),
              ( ['in'], c_ulong, 'dwPropID' ),
              ( ['in'], POINTER(c_ubyte), 'pInstanceData' ),
              ( ['in'], c_ulong, 'cbInstanceData' ),
              ( ['out'], POINTER(c_ubyte), 'pPropData' ),
              ( ['in'], c_ulong, 'cbPropData' ),
              ( ['out'], POINTER(c_ulong), 'pcbReturned' )),
    COMMETHOD([], HRESULT, 'QuerySupported',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'guidPropSet' ),
              ( ['in'], c_ulong, 'dwPropID' ),
              ( ['out'], POINTER(c_ulong), 'pTypeSupport' )),
]
################################################################
## code template for IKsPropertySet implementation
##class IKsPropertySet_Impl(object):
##    def QuerySupported(self, guidPropSet, dwPropID):
##        '-no docstring-'
##        #return pTypeSupport
##
##    def RemoteSet(self, guidPropSet, dwPropID, pInstanceData, cbInstanceData, pPropData, cbPropData):
##        '-no docstring-'
##        #return 
##
##    def RemoteGet(self, guidPropSet, dwPropID, pInstanceData, cbInstanceData, cbPropData):
##        '-no docstring-'
##        #return pPropData, pcbReturned
##

class IAMAnalogVideoDecoder(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6E13350-30AC-11D0-A18C-00A0C9118956}')
    _idlflags_ = []
IAMAnalogVideoDecoder._methods_ = [
    COMMETHOD([], HRESULT, 'get_AvailableTVFormats',
              ( ['out'], POINTER(c_int), 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'put_TVFormat',
              ( ['in'], c_int, 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_TVFormat',
              ( ['out'], POINTER(c_int), 'plAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_HorizontalLocked',
              ( ['out'], POINTER(c_int), 'plLocked' )),
    COMMETHOD([], HRESULT, 'put_VCRHorizontalLocking',
              ( ['in'], c_int, 'lVCRHorizontalLocking' )),
    COMMETHOD([], HRESULT, 'get_VCRHorizontalLocking',
              ( ['out'], POINTER(c_int), 'plVCRHorizontalLocking' )),
    COMMETHOD([], HRESULT, 'get_NumberOfLines',
              ( ['out'], POINTER(c_int), 'plNumberOfLines' )),
    COMMETHOD([], HRESULT, 'put_OutputEnable',
              ( ['in'], c_int, 'lOutputEnable' )),
    COMMETHOD([], HRESULT, 'get_OutputEnable',
              ( ['out'], POINTER(c_int), 'plOutputEnable' )),
]
################################################################
## code template for IAMAnalogVideoDecoder implementation
##class IAMAnalogVideoDecoder_Impl(object):
##    def get_HorizontalLocked(self):
##        '-no docstring-'
##        #return plLocked
##
##    def put_VCRHorizontalLocking(self, lVCRHorizontalLocking):
##        '-no docstring-'
##        #return 
##
##    def put_TVFormat(self, lAnalogVideoStandard):
##        '-no docstring-'
##        #return 
##
##    def get_AvailableTVFormats(self):
##        '-no docstring-'
##        #return lAnalogVideoStandard
##
##    def get_OutputEnable(self):
##        '-no docstring-'
##        #return plOutputEnable
##
##    def get_TVFormat(self):
##        '-no docstring-'
##        #return plAnalogVideoStandard
##
##    def get_VCRHorizontalLocking(self):
##        '-no docstring-'
##        #return plVCRHorizontalLocking
##
##    def put_OutputEnable(self, lOutputEnable):
##        '-no docstring-'
##        #return 
##
##    def get_NumberOfLines(self):
##        '-no docstring-'
##        #return plNumberOfLines
##

ICreateDevEnum._methods_ = [
    COMMETHOD([], HRESULT, 'CreateClassEnumerator',
              ( ['in'], POINTER(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID), 'clsidDeviceClass' ),
              ( ['out'], POINTER(POINTER(IEnumMoniker)), 'ppenumMoniker' ),
              ( ['in'], c_ulong, 'dwFlags' )),
]
################################################################
## code template for ICreateDevEnum implementation
##class ICreateDevEnum_Impl(object):
##    def CreateClassEnumerator(self, clsidDeviceClass, dwFlags):
##        '-no docstring-'
##        #return ppenumMoniker
##

IEnumMediaTypes._methods_ = [
    COMMETHOD([], HRESULT, 'Next',
              ( ['in'], c_ulong, 'cMediaTypes' ),
              ( ['out'], POINTER(POINTER(_AMMediaType)), 'ppMediaTypes' ),
              ( ['out'], POINTER(c_ulong), 'pcFetched' )),
    COMMETHOD([], HRESULT, 'Skip',
              ( ['in'], c_ulong, 'cMediaTypes' )),
    COMMETHOD([], HRESULT, 'Reset'),
    COMMETHOD([], HRESULT, 'Clone',
              ( ['out'], POINTER(POINTER(IEnumMediaTypes)), 'ppenum' )),
]
################################################################
## code template for IEnumMediaTypes implementation
##class IEnumMediaTypes_Impl(object):
##    def Reset(self):
##        '-no docstring-'
##        #return 
##
##    def Skip(self, cMediaTypes):
##        '-no docstring-'
##        #return 
##
##    def Clone(self):
##        '-no docstring-'
##        #return ppenum
##
##    def Next(self, cMediaTypes):
##        '-no docstring-'
##        #return ppMediaTypes, pcFetched
##

class CaptureGraphBuilder2(CoClass):
    _reg_clsid_ = GUID('{BF87B6E1-8C27-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
CaptureGraphBuilder2._com_interfaces_ = [ICaptureGraphBuilder2]

class FileWriter(CoClass):
    u'http://msdn.microsoft.com/library/default.asp?url=/library/en-us/directshow/htm/filewriterfilter.asp'
    _reg_clsid_ = GUID('{8596E5F0-0DA5-11D0-BD21-00A0C911CE86}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{24BC6711-3881-420F-8299-34DA1026D31E}', 1, 0)
FileWriter._com_interfaces_ = [IFileSinkFilter2, IBaseFilter]

class IMediaPropertyBag(IPropertyBag):
    _case_insensitive_ = True
    _iid_ = GUID('{6025A880-C0D5-11D0-BD4E-00A0C911CE86}')
    _idlflags_ = []
IMediaPropertyBag._methods_ = [
    COMMETHOD([], HRESULT, 'EnumProperty',
              ( ['in'], c_ulong, 'iProperty' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarPropertyName' ),
              ( ['in', 'out'], POINTER(VARIANT), 'pvarPropertyValue' )),
]
################################################################
## code template for IMediaPropertyBag implementation
##class IMediaPropertyBag_Impl(object):
##    def EnumProperty(self, iProperty):
##        '-no docstring-'
##        #return pvarPropertyName, pvarPropertyValue
##

class IAMDevMemoryControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6545BF1-E76B-11D0-BD52-00A0C911CE86}')
    _idlflags_ = []
IAMDevMemoryControl._methods_ = [
    COMMETHOD([], HRESULT, 'QueryWriteSync'),
    COMMETHOD([], HRESULT, 'WriteSync'),
    COMMETHOD([], HRESULT, 'GetDevId',
              ( ['out'], POINTER(c_ulong), 'pdwDevId' )),
]
################################################################
## code template for IAMDevMemoryControl implementation
##class IAMDevMemoryControl_Impl(object):
##    def WriteSync(self):
##        '-no docstring-'
##        #return 
##
##    def QueryWriteSync(self):
##        '-no docstring-'
##        #return 
##
##    def GetDevId(self):
##        '-no docstring-'
##        #return pdwDevId
##


# values for enumeration 'AM_SEEKING_SeekingCapabilities'
AM_SEEKING_CanSeekAbsolute = 1
AM_SEEKING_CanSeekForwards = 2
AM_SEEKING_CanSeekBackwards = 4
AM_SEEKING_CanGetCurrentPos = 8
AM_SEEKING_CanGetStopPos = 16
AM_SEEKING_CanGetDuration = 32
AM_SEEKING_CanPlayBackwards = 64
AM_SEEKING_CanDoSegments = 128
AM_SEEKING_Source = 256
AM_SEEKING_SeekingCapabilities = c_int # enum
class IAMDevMemoryAllocator(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{C6545BF0-E76B-11D0-BD52-00A0C911CE86}')
    _idlflags_ = []
IAMDevMemoryAllocator._methods_ = [
    COMMETHOD([], HRESULT, 'GetInfo',
              ( ['out'], POINTER(c_ulong), 'pdwcbTotalFree' ),
              ( ['out'], POINTER(c_ulong), 'pdwcbLargestFree' ),
              ( ['out'], POINTER(c_ulong), 'pdwcbTotalMemory' ),
              ( ['out'], POINTER(c_ulong), 'pdwcbMinimumChunk' )),
    COMMETHOD([], HRESULT, 'CheckMemory',
              ( ['in'], POINTER(c_ubyte), 'pBuffer' )),
    COMMETHOD([], HRESULT, 'Alloc',
              ( ['out'], POINTER(POINTER(c_ubyte)), 'ppBuffer' ),
              ( ['in', 'out'], POINTER(c_ulong), 'pdwcbBuffer' )),
    COMMETHOD([], HRESULT, 'Free',
              ( ['in'], POINTER(c_ubyte), 'pBuffer' )),
    COMMETHOD([], HRESULT, 'GetDevMemoryObject',
              ( ['out'], POINTER(POINTER(IUnknown)), 'ppUnkInnner' ),
              ( ['in'], POINTER(IUnknown), 'pUnkOuter' )),
]
################################################################
## code template for IAMDevMemoryAllocator implementation
##class IAMDevMemoryAllocator_Impl(object):
##    def CheckMemory(self, pBuffer):
##        '-no docstring-'
##        #return 
##
##    def GetDevMemoryObject(self, pUnkOuter):
##        '-no docstring-'
##        #return ppUnkInnner
##
##    def Alloc(self):
##        '-no docstring-'
##        #return ppBuffer, pdwcbBuffer
##
##    def Free(self, pBuffer):
##        '-no docstring-'
##        #return 
##
##    def GetInfo(self):
##        '-no docstring-'
##        #return pdwcbTotalFree, pdwcbLargestFree, pdwcbTotalMemory, pdwcbMinimumChunk
##

class IVMRVideoStreamControl(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    u'IVMRMixerStreamConfig Interface'
    _iid_ = GUID('{058D1F11-2A54-4BEF-BD54-DF706626B727}')
    _idlflags_ = []
IVMRVideoStreamControl._methods_ = [
    COMMETHOD([], HRESULT, 'SetColorKey',
              ( ['in'], POINTER(DDCOLORKEY), 'lpClrKey' )),
    COMMETHOD([], HRESULT, 'GetColorKey',
              ( ['out'], POINTER(DDCOLORKEY), 'lpClrKey' )),
    COMMETHOD([], HRESULT, 'SetStreamActiveState',
              ( ['in'], c_int, 'fActive' )),
    COMMETHOD([], HRESULT, 'GetStreamActiveState',
              ( ['out'], POINTER(c_int), 'lpfActive' )),
]
################################################################
## code template for IVMRVideoStreamControl implementation
##class IVMRVideoStreamControl_Impl(object):
##    def SetColorKey(self, lpClrKey):
##        '-no docstring-'
##        #return 
##
##    def GetStreamActiveState(self):
##        '-no docstring-'
##        #return lpfActive
##
##    def GetColorKey(self):
##        '-no docstring-'
##        #return lpClrKey
##
##    def SetStreamActiveState(self, fActive):
##        '-no docstring-'
##        #return 
##

IPersistMediaPropertyBag._methods_ = [
    COMMETHOD([], HRESULT, 'InitNew'),
    COMMETHOD([], HRESULT, 'Load',
              ( ['in'], POINTER(IMediaPropertyBag), 'pPropBag' ),
              ( ['in'], POINTER(IErrorLog), 'pErrorLog' )),
    COMMETHOD([], HRESULT, 'Save',
              ( ['in'], POINTER(IMediaPropertyBag), 'pPropBag' ),
              ( ['in'], c_int, 'fClearDirty' ),
              ( ['in'], c_int, 'fSaveAllProperties' )),
]
################################################################
## code template for IPersistMediaPropertyBag implementation
##class IPersistMediaPropertyBag_Impl(object):
##    def Load(self, pPropBag, pErrorLog):
##        '-no docstring-'
##        #return 
##
##    def InitNew(self):
##        '-no docstring-'
##        #return 
##
##    def Save(self, pPropBag, fClearDirty, fSaveAllProperties):
##        '-no docstring-'
##        #return 
##

class IMpeg2Demultiplexer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{436EEE9C-264F-4242-90E1-4E330C107512}')
    _idlflags_ = []
IMpeg2Demultiplexer._methods_ = [
    COMMETHOD([], HRESULT, 'CreateOutputPin',
              ( ['in'], POINTER(_AMMediaType), 'pMediaType' ),
              ( ['in'], WSTRING, 'pszPinName' ),
              ( ['out'], POINTER(POINTER(IPin)), 'ppIPin' )),
    COMMETHOD([], HRESULT, 'SetOutputPinMediaType',
              ( ['in'], WSTRING, 'pszPinName' ),
              ( ['in'], POINTER(_AMMediaType), 'pMediaType' )),
    COMMETHOD([], HRESULT, 'DeleteOutputPin',
              ( ['in'], WSTRING, 'pszPinName' )),
]
################################################################
## code template for IMpeg2Demultiplexer implementation
##class IMpeg2Demultiplexer_Impl(object):
##    def DeleteOutputPin(self, pszPinName):
##        '-no docstring-'
##        #return 
##
##    def SetOutputPinMediaType(self, pszPinName, pMediaType):
##        '-no docstring-'
##        #return 
##
##    def CreateOutputPin(self, pMediaType, pszPinName):
##        '-no docstring-'
##        #return ppIPin
##

class __MIDL___MIDL_itf_DirectShow_0134_0007(Union):
    pass
__MIDL___MIDL_itf_DirectShow_0134_0007._fields_ = [
    ('__MIDL_0011', __MIDL___MIDL_itf_DirectShow_0134_0008),
    ('__MIDL_0012', __MIDL___MIDL_itf_DirectShow_0134_0009),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0007) == 16, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0007)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0007) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0007)
IGraphConfigCallback._methods_ = [
    COMMETHOD([], HRESULT, 'Reconfigure',
              ( [], c_void_p, 'pvContext' ),
              ( [], c_ulong, 'dwFlags' )),
]
################################################################
## code template for IGraphConfigCallback implementation
##class IGraphConfigCallback_Impl(object):
##    def Reconfigure(self, pvContext, dwFlags):
##        '-no docstring-'
##        #return 
##

class IAMVfwCompressDialogs(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{D8D715A3-6E5E-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMVfwCompressDialogs._methods_ = [
    COMMETHOD([], HRESULT, 'ShowDialog',
              ( ['in'], c_int, 'iDialog' ),
              ( ['in'], wireHWND, 'hwnd' )),
    COMMETHOD([], HRESULT, 'GetState',
              ( ['out'], c_void_p, 'pState' ),
              ( ['in', 'out'], POINTER(c_int), 'pcbState' )),
    COMMETHOD([], HRESULT, 'SetState',
              ( ['in'], c_void_p, 'pState' ),
              ( ['in'], c_int, 'cbState' )),
    COMMETHOD([], HRESULT, 'SendDriverMessage',
              ( ['in'], c_int, 'uMsg' ),
              ( ['in'], c_int, 'dw1' ),
              ( ['in'], c_int, 'dw2' )),
]
################################################################
## code template for IAMVfwCompressDialogs implementation
##class IAMVfwCompressDialogs_Impl(object):
##    def GetState(self):
##        '-no docstring-'
##        #return pState, pcbState
##
##    def SendDriverMessage(self, uMsg, dw1, dw2):
##        '-no docstring-'
##        #return 
##
##    def ShowDialog(self, iDialog, hwnd):
##        '-no docstring-'
##        #return 
##
##    def SetState(self, pState, cbState):
##        '-no docstring-'
##        #return 
##

_FilterInfo._fields_ = [
    ('achName', c_ushort * 128),
    ('pGraph', POINTER(IFilterGraph)),
]
assert sizeof(_FilterInfo) == 264, sizeof(_FilterInfo)
assert alignment(_FilterInfo) == 8, alignment(_FilterInfo)
__MIDL___MIDL_itf_DirectShow_0134_0006._fields_ = [
    ('dwVersion', c_ulong),
    ('dwMerit', c_ulong),
    ('__MIDL_0014', __MIDL___MIDL_itf_DirectShow_0134_0007),
]
assert sizeof(__MIDL___MIDL_itf_DirectShow_0134_0006) == 24, sizeof(__MIDL___MIDL_itf_DirectShow_0134_0006)
assert alignment(__MIDL___MIDL_itf_DirectShow_0134_0006) == 8, alignment(__MIDL___MIDL_itf_DirectShow_0134_0006)
class CodecAPIEventData(Structure):
    pass
CodecAPIEventData._fields_ = [
    ('guid', comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.GUID),
    ('dataLength', c_ulong),
    ('reserved', c_ulong * 3),
]
assert sizeof(CodecAPIEventData) == 32, sizeof(CodecAPIEventData)
assert alignment(CodecAPIEventData) == 4, alignment(CodecAPIEventData)
tagPALETTEENTRY._fields_ = [
    ('peRed', c_ubyte),
    ('peGreen', c_ubyte),
    ('peBlue', c_ubyte),
    ('peFlags', c_ubyte),
]
assert sizeof(tagPALETTEENTRY) == 4, sizeof(tagPALETTEENTRY)
assert alignment(tagPALETTEENTRY) == 1, alignment(tagPALETTEENTRY)
class IAMTVTuner(IAMTuner):
    _case_insensitive_ = True
    _iid_ = GUID('{211A8766-03AC-11D1-8D13-00AA00BD8339}')
    _idlflags_ = []
IAMTVTuner._methods_ = [
    COMMETHOD([], HRESULT, 'get_AvailableTVFormats',
              ( ['out'], POINTER(c_int), 'lAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'get_TVFormat',
              ( ['out'], POINTER(c_int), 'plAnalogVideoStandard' )),
    COMMETHOD([], HRESULT, 'AutoTune',
              ( ['in'], c_int, 'lChannel' ),
              ( ['out'], POINTER(c_int), 'plFoundSignal' )),
    COMMETHOD([], HRESULT, 'StoreAutoTune'),
    COMMETHOD([], HRESULT, 'get_NumInputConnections',
              ( ['out'], POINTER(c_int), 'plNumInputConnections' )),
    COMMETHOD([], HRESULT, 'put_InputType',
              ( ['in'], c_int, 'lIndex' ),
              ( ['in'], tagTunerInputType, 'InputType' )),
    COMMETHOD([], HRESULT, 'get_InputType',
              ( ['in'], c_int, 'lIndex' ),
              ( ['out'], POINTER(tagTunerInputType), 'pInputType' )),
    COMMETHOD([], HRESULT, 'put_ConnectInput',
              ( ['in'], c_int, 'lIndex' )),
    COMMETHOD([], HRESULT, 'get_ConnectInput',
              ( ['out'], POINTER(c_int), 'plIndex' )),
    COMMETHOD([], HRESULT, 'get_VideoFrequency',
              ( ['out'], POINTER(c_int), 'lFreq' )),
    COMMETHOD([], HRESULT, 'get_AudioFrequency',
              ( ['out'], POINTER(c_int), 'lFreq' )),
]
################################################################
## code template for IAMTVTuner implementation
##class IAMTVTuner_Impl(object):
##    def get_InputType(self, lIndex):
##        '-no docstring-'
##        #return pInputType
##
##    def get_ConnectInput(self):
##        '-no docstring-'
##        #return plIndex
##
##    def get_AudioFrequency(self):
##        '-no docstring-'
##        #return lFreq
##
##    def get_VideoFrequency(self):
##        '-no docstring-'
##        #return lFreq
##
##    def StoreAutoTune(self):
##        '-no docstring-'
##        #return 
##
##    def AutoTune(self, lChannel):
##        '-no docstring-'
##        #return plFoundSignal
##
##    def get_AvailableTVFormats(self):
##        '-no docstring-'
##        #return lAnalogVideoStandard
##
##    def put_InputType(self, lIndex, InputType):
##        '-no docstring-'
##        #return 
##
##    def get_TVFormat(self):
##        '-no docstring-'
##        #return plAnalogVideoStandard
##
##    def put_ConnectInput(self, lIndex):
##        '-no docstring-'
##        #return 
##
##    def get_NumInputConnections(self):
##        '-no docstring-'
##        #return plNumInputConnections
##

tagVMRMONITORINFO._fields_ = [
    ('guid', tagVMRGUID),
    ('rcMonitor', tagRECT),
    ('hMon', c_void_p),
    ('dwFlags', c_ulong),
    ('szDevice', c_ushort * 32),
    ('szDescription', c_ushort * 256),
    ('liDriverVersion', _LARGE_INTEGER),
    ('dwVendorId', c_ulong),
    ('dwDeviceId', c_ulong),
    ('dwSubSysId', c_ulong),
    ('dwRevision', c_ulong),
]
assert sizeof(tagVMRMONITORINFO) == 656, sizeof(tagVMRMONITORINFO)
assert alignment(tagVMRMONITORINFO) == 8, alignment(tagVMRMONITORINFO)
IDVSplitter._methods_ = [
    COMMETHOD([], HRESULT, 'DiscardAlternateVideoFrames',
              ( ['in'], c_int, 'nDiscard' )),
]
################################################################
## code template for IDVSplitter implementation
##class IDVSplitter_Impl(object):
##    def DiscardAlternateVideoFrames(self, nDiscard):
##        '-no docstring-'
##        #return 
##

class IAMAudioInputMixer(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IUnknown):
    _case_insensitive_ = True
    _iid_ = GUID('{54C39221-8380-11D0-B3F0-00AA003761C5}')
    _idlflags_ = []
IAMAudioInputMixer._methods_ = [
    COMMETHOD([], HRESULT, 'put_Enable',
              ( ['in'], c_int, 'fEnable' )),
    COMMETHOD([], HRESULT, 'get_Enable',
              ( ['out'], POINTER(c_int), 'pfEnable' )),
    COMMETHOD([], HRESULT, 'put_Mono',
              ( ['in'], c_int, 'fMono' )),
    COMMETHOD([], HRESULT, 'get_Mono',
              ( ['out'], POINTER(c_int), 'pfMono' )),
    COMMETHOD([], HRESULT, 'put_MixLevel',
              ( ['in'], c_double, 'Level' )),
    COMMETHOD([], HRESULT, 'get_MixLevel',
              ( ['out'], POINTER(c_double), 'pLevel' )),
    COMMETHOD([], HRESULT, 'put_Pan',
              ( ['in'], c_double, 'Pan' )),
    COMMETHOD([], HRESULT, 'get_Pan',
              ( ['out'], POINTER(c_double), 'pPan' )),
    COMMETHOD([], HRESULT, 'put_Loudness',
              ( ['in'], c_int, 'fLoudness' )),
    COMMETHOD([], HRESULT, 'get_Loudness',
              ( ['out'], POINTER(c_int), 'pfLoudness' )),
    COMMETHOD([], HRESULT, 'put_Treble',
              ( ['in'], c_double, 'Treble' )),
    COMMETHOD([], HRESULT, 'get_Treble',
              ( ['out'], POINTER(c_double), 'pTreble' )),
    COMMETHOD([], HRESULT, 'get_TrebleRange',
              ( ['out'], POINTER(c_double), 'pRange' )),
    COMMETHOD([], HRESULT, 'put_Bass',
              ( ['in'], c_double, 'Bass' )),
    COMMETHOD([], HRESULT, 'get_Bass',
              ( ['out'], POINTER(c_double), 'pBass' )),
    COMMETHOD([], HRESULT, 'get_BassRange',
              ( ['out'], POINTER(c_double), 'pRange' )),
]
################################################################
## code template for IAMAudioInputMixer implementation
##class IAMAudioInputMixer_Impl(object):
##    def put_Loudness(self, fLoudness):
##        '-no docstring-'
##        #return 
##
##    def get_Mono(self):
##        '-no docstring-'
##        #return pfMono
##
##    def get_TrebleRange(self):
##        '-no docstring-'
##        #return pRange
##
##    def put_Pan(self, Pan):
##        '-no docstring-'
##        #return 
##
##    def put_Mono(self, fMono):
##        '-no docstring-'
##        #return 
##
##    def put_Enable(self, fEnable):
##        '-no docstring-'
##        #return 
##
##    def get_Pan(self):
##        '-no docstring-'
##        #return pPan
##
##    def get_Enable(self):
##        '-no docstring-'
##        #return pfEnable
##
##    def get_Bass(self):
##        '-no docstring-'
##        #return pBass
##
##    def put_Bass(self, Bass):
##        '-no docstring-'
##        #return 
##
##    def put_MixLevel(self, Level):
##        '-no docstring-'
##        #return 
##
##    def get_MixLevel(self):
##        '-no docstring-'
##        #return pLevel
##
##    def get_BassRange(self):
##        '-no docstring-'
##        #return pRange
##
##    def put_Treble(self, Treble):
##        '-no docstring-'
##        #return 
##
##    def get_Treble(self):
##        '-no docstring-'
##        #return pTreble
##
##    def get_Loudness(self):
##        '-no docstring-'
##        #return pfLoudness
##

__all__ = ['IAMPushSource', 'REMFILTERF_LEAVECONNECTED',
           'VMRSurfaceAllocationFlags',
           'AM_STREAM_INFO_START_DEFINED', 'AMTUNER_NOSIGNAL',
           'PhysConn_Video_Tuner', 'IDVSplitter', 'IAMClockSlave',
           'VideoProcAmp_Flags_Manual', 'AM_SEEKING_CanSeekBackwards',
           'IAMAnalogVideoEncoder', '_AM_PUSHSOURCE_FLAGS',
           'IOverlayNotify', 'State_Paused',
           'VfwCaptureDialog_Source', 'CompressionCaps_CanQuality',
           'AM_SEEKING_IncrementalPositioning',
           'DVDECODERRESOLUTION_360x240', '_RemotableHandle',
           'IEnumString', 'PhysConn_Video_SerialDigital',
           'VMRDeinterlacePrefs', 'IAMClockAdjust',
           'PhysConn_Video_YRYBY', 'AviMux', 'State_Stopped',
           'AM_SEEKING_SeekToKeyFrame', 'AMOVERLAYFX',
           'AM_SEEKING_SeekingFlags',
           'RenderPrefs_PreferAGPMemWhenMixing', 'AMTUNER_MODE_TV',
           'DECIMATION_USE_OVERLAY_ONLY', 'MixerPref_FilteringMask',
           'IAMVideoProcAmp', 'AM_SEEKING_CanSeekAbsolute',
           'CameraControl_Flags_Manual', '_AMSTREAMSELECTINFOFLAGS',
           '__MIDL___MIDL_itf_DirectShow_0164_0001',
           '__MIDL___MIDL_itf_DirectShow_0164_0002',
           'AMTVAUDIO_MODE_LANG_C', 'AMTVAUDIO_MODE_LANG_B',
           'AMTVAUDIO_MODE_LANG_A', 'IAMFilterMiscFlags',
           '_AMRESCTL_RESERVEFLAGS', 'AMAP_3D_TARGET', 'IPin',
           'tagAM_SAMPLE2_PROPERTIES',
           '__MIDL___MIDL_itf_DirectShow_0355_0001',
           '_AMSTREAMSELECTENABLEFLAGS',
           'PhysConn_Video_ParallelDigital',
           '__MIDL___MIDL_itf_DirectShow_0364_0001',
           'CameraControl_Pan', 'IFilterGraph',
           'VideoCopyProtectionMacrovisionBasic', 'IAMOpenProgress',
           'IVMRSurface', 'AM_AUDREND_STAT_PARAM_LAST_BUFFER_DUR',
           'IVPManager', '__MIDL___MIDL_itf_DirectShow_0134_0008',
           '__MIDL___MIDL_itf_DirectShow_0134_0009', 'IBindCtx',
           'AMAP_PIXELFORMAT_VALID',
           '__MIDL___MIDL_itf_DirectShow_0134_0001',
           '__MIDL___MIDL_itf_DirectShow_0134_0002',
           '__MIDL___MIDL_itf_DirectShow_0134_0003',
           '__MIDL___MIDL_itf_DirectShow_0134_0004',
           '__MIDL___MIDL_itf_DirectShow_0134_0005',
           'DeinterlaceTech_PixelAdaptive',
           '__MIDL___MIDL_itf_DirectShow_0134_0007',
           'AM_STREAM_CONTROL', 'AnalogVideo_SECAM_K1',
           'MixerPref_NoDecimation', 'DVENCODERRESOLUTION_88x60',
           'PhysConn_Audio_Line', 'IAMTunerNotification',
           'IVMRAspectRatioControl', 'DVRESOLUTION_DC',
           'VfwCompressDialog_Config', 'IAMResourceControl',
           '__MIDL___MIDL_itf_DirectShow_0156_0001',
           'VideoProcAmp_Brightness', 'VideoProcAmp_WhiteBalance',
           'IAMAnalogVideoDecoder', 'IFilterGraph2',
           'IVMRVideoStreamControl', 'INTERLEAVE_CAPTURE',
           'IVMRMonitorConfig', '_FilterInfo', 'IDVEnc',
           'PhysConn_Audio_USB', 'CameraControl_Focus',
           'IAMDeviceRemoval', 'IDVRGB219', 'VMRSample_SyncPoint',
           'MixerPref_PointFiltering', 'VideoProcAmp_Sharpness',
           'IAMAudioRendererStats', 'AM_FILE_OVERWRITE', 'IAMTVAudio',
           'VMRMode_Renderless', 'IVMRDeinterlaceControl',
           'DECIMATION_USE_DECODER_ONLY', 'AM_SEEKING_CanDoSegments',
           'REGPINTYPES', 'IAMAudioInputMixer', 'INTERLEAVE_FULL',
           '_AM_RENSDEREXFLAGS',
           '__MIDL___MIDL_itf_DirectShow_0163_0001',
           'PhysConn_Audio_AESDigital',
           '__MIDL___MIDL_itf_DirectShow_0181_0001', 'CK_NOCOLORKEY',
           'IFileSinkFilter2', 'DeinterlaceTech_MotionVectorSteered',
           'DeinterlaceTech_MedianFiltering',
           'INTERLEAVE_NONE_BUFFERED',
           'AM_PUSHSOURCECAPS_INTERNAL_RM', 'TunerInputCable',
           '__MIDL___MIDL_itf_DirectShow_0378_0001', 'IConfigAviMux',
           'AM_AUDREND_STAT_PARAM_SLAVE_RATE', 'VMRSample_TimeValid',
           'IVMRMixerBitmap', 'tagQuality', 'DECIMATION_LEGACY',
           'MixerPref_RenderTargetMask', 'IOverlay',
           'INTERLEAVE_NONE', 'IAMVideoDecimationProperties',
           'MixerPref_BiLinearFiltering',
           'AM_AUDREND_STAT_PARAM_SLAVE_HIGHLOWERROR',
           'PhysConn_Audio_Mic', 'VariableBitRatePeak',
           'DeinterlaceTech_EdgeFiltering', 'AnalogVideo_NTSC_M',
           '_DVENCODERRESOLUTION', 'VMRSample_Preroll',
           'VfwCompressDialog_QueryAbout', 'DVENCODERFORMAT_DVHD',
           'AMTVAUDIO_EVENT_CHANGED', 'IAMStreamControl',
           'IAMDevMemoryAllocator', 'IMemInputPin',
           'PhysConn_Audio_AUX', 'IVMRImagePresenterConfig',
           '_RGNDATAHEADER', 'REG_PINFLAG_B_MANY',
           'tagCameraControlProperty', '_AM_FILTER_FLAGS',
           'IMpeg2Demultiplexer',
           'AM_AUDREND_STAT_PARAM_BUFFERFULLNESS',
           'PhysConn_Audio_Tuner', 'AMOVERFX_MIRRORUPDOWN',
           'IPinFlowControl', 'IAMVfwCaptureDialogs',
           'IAMGraphBuilderCallback', 'DeinterlaceTech_Unknown',
           'IPersistStream', 'IAMVideoControl', 'IAMExtTransport',
           'PhysConn_Video_AUX', 'AnalogVideo_PAL_H',
           'AM_SEEKING_SeekingCapabilities', 'IMoniker',
           '_DVDECODERRESOLUTION', 'IPersistMediaPropertyBag',
           'IEnumFilters', 'DDCOLORKEY', 'LONG_PTR',
           'IAMTimecodeReader', 'REG_PINFLAG_B_ZERO',
           'AnalogVideo_PAL_N_COMBO', 'tagAMTunerSubChannel',
           'AM_FILTER_MISC_FLAGS_IS_RENDERER', 'CameraControl_Roll',
           'DeinterlacePref_BOB', 'AMRESCTL_RESERVEFLAGS_RESERVE',
           'PhysConn_Video_SCSI', 'IVMRImagePresenter',
           'PhysConn_Video_RGB', 'IAMStreamConfig',
           'IResourceConsumer', 'AM_STREAM_INFO_DISCARDING',
           'tagVMRGUID', 'VMRMixerPrefs', 'PhysConn_Video_Black',
           'AMTUNER_SUBCHAN_NO_TUNE', 'VfwCompressDialog_About',
           'IVMRWindowlessControl', 'IAMTuner',
           'AM_AUDREND_STAT_PARAM_SLAVE_LASTHIGHLOWERROR',
           'VIDEOENCODER_BITRATE_MODE', 'REG_PINFLAG_B_OUTPUT',
           'ISequentialStream', 'AnalogVideo_PAL_60', 'IMediaSample2',
           'AviSplitter', 'IReferenceClock',
           'VMRSample_Discontinuity', '_VMRALPHABITMAP',
           'AM_RENDEREX_RENDERTOEXISTINGRENDERERS',
           'DeinterlaceTech_FieldAdaptive',
           'AM_PUSHSOURCECAPS_PRIVATE_CLOCK', 'VideoProcAmp_Gain',
           'AM_SEEKING_CanGetStopPos', 'IStreamBuilder',
           'IAMPhysicalPinInfo', 'RenderPrefs_AllowOffscreen',
           'RenderPrefs_ForceOverlays', 'AM_STREAM_MEDIA',
           'IAMTVTuner', 'AM_SAMPLE_TIMEDISCONTINUITY',
           'REG_PINFLAG_B_RENDERER',
           'AM_AUDREND_STAT_PARAM_SILENCE_DUR', 'FilterGraph',
           'DVRESOLUTION_HALF', 'CompressionCaps',
           'tagAMTunerSignalStrength', 'AM_SAMPLE_TIMEVALID',
           'PhysConn_Video_VideoDecoder', 'AMAP_DIRECTED_FLIP',
           'IGraphBuilder', 'IGraphConfigCallback',
           'AnalogVideo_SECAM_L1', 'CameraControl_Exposure',
           'IMediaSeeking', 'VideoControlFlag_FlipVertical',
           'CodecAPIEventData', 'IAMExtDevice', 'IConfigInterleaving',
           'IVideoFrameStep', 'FileWriter', 'IAMDevMemoryControl',
           'REGFILTERPINS2', 'IVMRFilterConfig',
           'AM_SAMPLE_DATADISCONTINUITY', 'CameraControl_Zoom',
           'AM_SEEKING_NoFlush', 'ADVISE_COLORKEY',
           'AM_SEEKING_CanSeekForwards', 'Flood',
           'AM_AUDREND_STAT_PARAM_BREAK_COUNT',
           '__MIDL___MIDL_itf_DirectShow_0376_0003',
           'AMSTREAMSELECTENABLE_ENABLEALL', 'PINDIR_OUTPUT',
           'VMR_ARMODE_LETTER_BOX', 'IVMRImageCompositor',
           'VideoProcAmp_Saturation', 'PhysConn_Video_SVideo',
           'IVMRSurfaceAllocatorNotify',
           'VfwCompressDialog_QueryConfig',
           'DVDECODERRESOLUTION_720x480', 'RenderPrefs_AllowOverlays',
           'MixerPref_DecimateOutput', 'PhysConn_Audio_SPDIFDigital',
           'VMRMode_Windowed', 'AMPROPERTY_PIN', 'tagPALETTEENTRY',
           'CameraControl_Flags_Auto', 'REGFILTERPINS',
           'AM_SAMPLE_PREROLL', 'AM_SEEKING_RelativePositioning',
           'tagAnalogVideoStandard', 'IBaseFilter',
           '_DVENCODERFORMAT', '_RGNDATA',
           'MixerPref_RenderTargetYUV422',
           'AM_STREAM_INFO_STOP_SEND_EXTRA',
           'MixerPref_RenderTargetYUV420', 'ConstantBitRate',
           '_AllocatorProperties', '_DVRESOLUTION',
           'AM_SEEKING_AbsolutePositioning',
           '__MIDL___MIDL_itf_DirectShow_0370_0002',
           'AM_SEEKING_ReturnTime',
           '__MIDL___MIDL_itf_DirectShow_0370_0001',
           'IDrawVideoImage', '_AM_AUDIO_RENDERER_STAT_PARAM',
           'DvVideoDecoder', 'AM_PUSHSOURCEREQS_USE_STREAM_CLOCK',
           'State_Running', 'ISeekingPassThru',
           'RenderPrefs_RestrictToInitialMonitor',
           'AM_GRAPH_CONFIG_RECONNECT_CACHE_REMOVED_FILTERS',
           'tagAMTunerModeType', 'IOverlayNotify2', '_PinDirection',
           'PhysConn_Video_USB', 'AM_STREAM_INFO_FLAGS', 'tagSTATSTG',
           'IEnumRegFilters',
           '__MIDL___MIDL_itf_DirectShow_0373_0001',
           '__MIDL___MIDL_itf_DirectShow_0138_0001',
           '__MIDL___MIDL_itf_DirectShow_0138_0002',
           'tagTIMECODE_SAMPLE', 'TunerInputAntenna',
           'IVMRMixerControl', 'DVENCODERRESOLUTION_180x120',
           'IDistributorNotify', 'REGPINMEDIUM', 'REGFILTER',
           'RenderPrefs_Reserved', '_AM_GRAPH_CONFIG_RECONNECT_FLAGS',
           'IAMStreamSelect', 'IEncoderAPI', 'ICaptureGraphBuilder2',
           'AM_SEEKING_CanPlayBackwards', '_NORMALIZEDRECT',
           'ICaptureGraphBuilder', 'IMediaFilter',
           'AM_PUSHSOURCECAPS_NOT_LIVE', '_AMMediaType',
           'DeinterlacePref_Weave', 'VideoProcAmp_Contrast',
           'IStream', 'AMTVAUDIO_MODE_MONO',
           'AMSTREAMSELECTINFO_EXCLUSIVE',
           'DVDECODERRESOLUTION_180x120', 'tagCOLORKEY',
           'PhysConn_Audio_AudioDecoder', 'AnalogVideo_SECAM_H',
           'REGFILTER2', 'DVENCODERRESOLUTION_360x240',
           'tagVideoProcAmpFlags', 'VfwCaptureDialogs',
           'AM_SEEKING_Segment', 'IMPEG2StreamIdMap', 'IFilterChain',
           'IAMVideoCompression', 'IMediaEventSink',
           'AnalogVideo_SECAM_L',
           '__MIDL___MIDL_itf_DirectShow_0169_0001',
           'VideoCopyProtectionMacrovisionCBI',
           'DeinterlacePref_NextBest', 'AMTUNER_MODE_DSS',
           'AM_INTF_SEARCH_OUTPUT_PIN', 'AnalogVideo_SECAM_K',
           'AM_SAMPLE_STOPVALID',
           'AM_AUDREND_STAT_PARAM_SLAVE_ACCUMERROR',
           'AnalogVideo_SECAM_B', 'VMR_ARMODE_NONE',
           'CompressionCaps_CanWindow', 'AnalogVideo_SECAM_G',
           'AM_SAMPLE_TYPECHANGED', 'VMRMode_Windowless',
           'IAMTimecodeDisplay', 'AnalogVideo_SECAM_D',
           'IMemAllocatorCallbackTemp', 'tagVideoProcAmpProperty',
           'CK_INDEX', 'IMediaSample', '_DECIMATION_USAGE',
           'IAMGraphStreams', 'Famine', 'tagAM_SAMPLE_PROPERTY_FLAGS',
           'IAMBufferNegotiation', '_REM_FILTER_FLAGS',
           'CompressionCaps_CanBFrame', 'IAMCrossbar',
           'IReferenceClock2', 'DECIMATION_DEFAULT',
           'AM_SEEKING_NoPositioning', 'PhysConn_Audio_SCSI',
           'MixerPref_RenderTargetReserved', 'ICodecAPI',
           'DVENCODERRESOLUTION_720x480',
           'AMRESCTL_RESERVEFLAGS_UNRESERVE', 'IQualityControl',
           'IAMCameraControl', 'ICreateDevEnum', 'IEnumMoniker',
           'PhysConn_Video_Composite', 'DVDECODERRESOLUTION_88x60',
           'DVRESOLUTION_FULL', 'tagTIMECODE', 'PINDIR_INPUT',
           'CompressionCaps_CanKeyFrame',
           'IMemAllocatorNotifyCallbackTemp', 'IFilterMapper3',
           'AM_AUDREND_STAT_PARAM_DISCONTINUITIES',
           'AMSTREAMSELECTENABLE_ENABLE', 'IAMovieSetup',
           'AMOVERFX_NOFX', 'wireHDC', 'VideoProcAmp_Hue',
           '__MIDL___MIDL_itf_DirectShow_0376_0001',
           'AMAP_DXVA_TARGET',
           '__MIDL___MIDL_itf_DirectShow_0376_0002', 'ADVISE_NONE',
           'ADVISE_DISPLAY_CHANGE', 'VMRRenderPrefs',
           'AMPROPERTY_PIN_CATEGORY', 'VariableBitRateAverage',
           'IFileSinkFilter', 'VfwCompressDialogs', 'IGraphConfig',
           '__MIDL___MIDL_itf_DirectShow_0378_0002',
           'ADVISE_POSITION', 'AM_SAMPLE_FLUSH_ON_PAUSE',
           'AM_SEEKING_CanGetDuration', 'AM_SEEKING_Source',
           'MAX_NUMBER_OF_STREAMS', 'IIPDVDec',
           'AMTUNER_MODE_FM_RADIO', 'IAMTimecodeGenerator',
           '_DVENCODERVIDEOFORMAT', 'IResourceManager',
           'IVMRSurfaceAllocator', '__MIDL_IConfigInterleaving_0001',
           'DeinterlaceTech_BOBVerticalStretch',
           'AMTUNER_SIGNALPRESENT', 'IVideoEncoder', 'IFilterMapper',
           '_VMRFrequency', 'AM_INTF_SEARCH_FILTER',
           'tagAMTVAudioEventType', 'AMTUNER_SUBCHAN_DEFAULT',
           'AMTUNER_MODE_AM_RADIO', 'tagVMRMONITORINFO',
           'AsyncFileReader', 'InterleavingMode',
           'RenderPrefs_DoNotRenderColorKeyAndBorder',
           '_VMRDeinterlaceCaps', 'DVINFO',
           'AMSTREAMSELECTINFO_ENABLED',
           'MixerPref_RenderTargetYUV444', 'AMTUNER_EVENT_CHANGED',
           'IBPCSatelliteTuner', 'AMTUNER_HASNOSIGNALSTRENGTH',
           'tagVMRPRESENTATIONINFO', 'DeinterlacePref_Mask',
           'IKsPropertySet', 'PhysConn_Video_1394',
           'AM_FILTER_MISC_FLAGS_IS_SOURCE', 'IAMDecoderCaps',
           'IAMVfwCompressDialogs', 'IAMTVAudioNotification',
           'AM_AUDREND_STAT_PARAM_JITTER', 'AMPROPERTY_PIN_MEDIUM',
           'IAMDroppedFrames', 'IEnumPins',
           '__MIDL___MIDL_itf_DirectShow_0134_0006',
           '__MIDL_IWinTypes_0009', 'tagVMRALLOCATIONINFO',
           'RenderPrefs_ForceOffscreen', 'MixerPref_RenderTargetRGB',
           'IRegisterServiceProvider', 'tagPhysicalConnectorType',
           'DvSplitter', '_AM_INTF_SEARCH_FLAGS', 'RenderPrefs_Mask',
           'IAMCopyCaptureFileProgress', 'CaptureGraphBuilder2',
           'tagQualityMessageType', 'tagCameraControlFlags',
           'ADVISE_PALETTE', 'MixerPref_DecimateMask',
           'PhysConn_Video_SCART', 'AMTUNER_MODE_DEFAULT',
           'CompressionCaps_CanCrunch', '_VMRVideoDesc',
           '__MIDL___MIDL_itf_DirectShow_0130_0001',
           'AM_FILESINK_FLAGS',
           'VideoControlFlag_ExternalTriggerEnable', 'IMemAllocator',
           'tagTVAudioMode', 'CameraControl_Iris', 'AnalogVideo_None',
           'AnalogVideo_NTSC_M_J', 'PhysConn_Audio_1394',
           'IAMLatency', 'CK_RGB', 'AMOVERFX_MIRRORLEFTRIGHT',
           'VMRMode_Mask', 'VideoControlFlag_Trigger',
           'DeinterlaceTech_BOBLineReplicate', 'CameraControl_Tilt',
           'VideoProcAmp_Flags_Auto',
           '_AM_PIN_FLOW_CONTROL_BLOCK_FLAGS', 'tagVideoControlFlags',
           'ADVISE_CLIPPING', '_VMRVIDEOSTREAMINFO',
           'AM_AUDREND_STAT_PARAM_SLAVE_MODE',
           'AM_AUDREND_STAT_PARAM_SLAVE_DROPWRITE_DUR',
           'AM_PIN_FLOW_CONTROL_BLOCK', 'AMTVAUDIO_MODE_STEREO',
           'VideoControlFlag_FlipHorizontal',
           'AM_INTF_SEARCH_INPUT_PIN',
           '__MIDL___MIDL_itf_DirectShow_0145_0001',
           'tagAMTunerEventType', 'VideoCopyProtectionType',
           'AnalogVideo_PAL_B',
           '__MIDL___MIDL_itf_DirectShow_0345_0001',
           'AnalogVideo_PAL_G', 'STREAM_ID_MAP', 'AnalogVideo_PAL_D',
           'VfwCaptureDialog_Format', 'AnalogVideo_PAL_I',
           '__MIDL___MIDL_itf_DirectShow_0374_0001',
           'AM_FILTER_FLAGS_REMOVABLE', 'AnalogVideo_PAL_N',
           'AnalogVideo_PAL_M', 'IAMOverlayFX',
           'AnalogVideo_NTSC_433',
           '__MIDL___MIDL_itf_DirectShow_0371_0001',
           'AM_SAMPLE_ENDOFSTREAM', '_AM_FILTER_MISC_FLAGS',
           'VMRPresentationFlags', 'AM_STREAM_INFO_STOP_DEFINED',
           'DVENCODERFORMAT_DVSL', 'AM_SEEKING_PositioningBitsMask',
           '_FilterState', 'DVENCODERFORMAT_DVSD',
           'IFileSourceFilter', 'tagTunerInputType',
           'VMR_ASPECT_RATIO_MODE', 'AMAP_ALLOW_SYSMEM',
           'AM_SEEKING_CanGetCurrentPos',
           'AM_GRAPH_CONFIG_RECONNECT_DIRECTCONNECT',
           'IGetCapabilitiesKey', 'AM_STREAM_INFO',
           'VideoProcAmp_ColorEnable', 'AM_SAMPLE_SPLICEPOINT',
           'DVRESOLUTION_QUARTER', 'DVENCODERVIDEOFORMAT_NTSC',
           'IMediaPropertyBag',
           '__MIDL___MIDL_itf_DirectShow_0156_0002',
           'AMOVERFX_DEINTERLACE', 'VfwCaptureDialog_Display',
           'IEnumStreamIdMap', 'VMRDeinterlaceTech',
           'PhysConn_Video_VideoEncoder', 'IFilterMapper2',
           'IRunningObjectTable', 'VideoProcAmp_Gamma',
           'DECIMATION_USE_VIDEOPORT_ONLY', 'IDecimateVideoImage',
           'IPinConnection', '_PinInfo', 'VMRMode', 'IGraphVersion',
           'IEnumMediaTypes', 'VideoProcAmp_BacklightCompensation',
           'IVMRImagePresenterExclModeConfig', 'IAsyncReader',
           'AM_GRAPH_CONFIG_RECONNECT_USE_ONLY_CACHED_FILTERS',
           'DVENCODERVIDEOFORMAT_PAL', 'AMAP_FORCE_SYSMEM']
from comtypes import _check_version; _check_version('482')
