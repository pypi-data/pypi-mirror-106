from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Local:
	"""Local commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("local", core, parent)

	# noinspection PyTypeChecker
	class CatalogStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Url: List[str]: String specifying the URL of a domain
			- Ip: List[str]: Assigned IPv4 address or IPv6 address as string"""
		__meta_args_list = [
			ArgStruct('Url', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Url: List[str] = None
			self.Ip: List[str] = None

	def get_catalog(self) -> CatalogStruct:
		"""SCPI: SENSe:DATA:CONTrol:DNS:LOCal:CATalog \n
		Snippet: value: CatalogStruct = driver.sense.data.control.dns.local.get_catalog() \n
		Queries the entries of the local DNS server database for type A or type AAAA DNS queries. The two values listed below are
		returned for each database entry: {<Url>, <IP>}entry 0, {<Url>, <IP>}entry 1, ... \n
			:return: structure: for return value, see the help for CatalogStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:DNS:LOCal:CATalog?', self.__class__.CatalogStruct())
