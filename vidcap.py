
from comtypes import GUID, CLSCTX_INPROC
from comtypes.client import CreateObject
from DirectShowLib import (FilterGraph, CaptureGraphBuilder2,)

class error(Exception):
	pass



class Device(object):
	def __init__(self):
		self.filter_graph = CreateObject(FilterGraph)
		self.graph_builder = CreateObject(CaptureGraphBuilder2)
		self.graph_builder.SetFiltergraph(self.filter_graph)

def test():
	d = Device()

if __name__ == '__main__': test()