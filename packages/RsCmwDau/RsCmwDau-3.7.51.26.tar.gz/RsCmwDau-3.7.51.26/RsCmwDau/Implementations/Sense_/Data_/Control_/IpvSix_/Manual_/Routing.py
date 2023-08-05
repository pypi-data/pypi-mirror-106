from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Routing:
	"""Routing commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("routing", core, parent)

	# noinspection PyTypeChecker
	class CatalogStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Prefixes: List[str]: String specifying an IPv6 prefix
			- Routers: List[str]: IPv6 address of assigned router as string"""
		__meta_args_list = [
			ArgStruct('Prefixes', DataType.StringList, None, False, True, 1),
			ArgStruct('Routers', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Prefixes: List[str] = None
			self.Routers: List[str] = None

	def get_catalog(self) -> CatalogStruct:
		"""SCPI: SENSe:DATA:CONTrol:IPVSix:MANual:ROUTing:CATalog \n
		Snippet: value: CatalogStruct = driver.sense.data.control.ipvSix.manual.routing.get_catalog() \n
		Queries the pool of manual routes for IPv6. The two values listed below are returned for each route: {<Prefixes>,
		<Routers>}entry 0, {<Prefixes>, <Routers>}entry 1, ... \n
			:return: structure: for return value, see the help for CatalogStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:IPVSix:MANual:ROUTing:CATalog?', self.__class__.CatalogStruct())
