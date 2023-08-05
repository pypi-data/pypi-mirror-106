from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aservices:
	"""Aservices commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aservices", core, parent)

	# noinspection PyTypeChecker
	class CatalogStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Name: List[str]: String specifying the service name
			- Url: List[str]: String specifying the URL of the domain
			- Protocol: List[enums.Protocol]: UDP | TCP
			- Port: List[int]: Range: 0 to 65654"""
		__meta_args_list = [
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Url', DataType.StringList, None, False, True, 1),
			ArgStruct('Protocol', DataType.EnumList, enums.Protocol, False, True, 1),
			ArgStruct('Port', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name: List[str] = None
			self.Url: List[str] = None
			self.Protocol: List[enums.Protocol] = None
			self.Port: List[int] = None

	def get_catalog(self) -> CatalogStruct:
		"""SCPI: SENSe:DATA:CONTrol:DNS:ASERvices:CATalog \n
		Snippet: value: CatalogStruct = driver.sense.data.control.dns.aservices.get_catalog() \n
		Queries the entries of the local DNS server database for type SRV DNS queries. The four values listed below are returned
		for each database entry: {<Name>, <Url>, <Protocol>, <Port>}entry 0, {...}entry 1, ... \n
			:return: structure: for return value, see the help for CatalogStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:DNS:ASERvices:CATalog?', self.__class__.CatalogStruct())
