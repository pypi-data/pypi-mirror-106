from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Apn:
	"""Apn commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("apn", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Name: List[str]: Access point name (APN) as string
			- Ip_V_4: List[str]: IPv4 address as string
			- Ip_V_6: List[str]: IPv6 address as string"""
		__meta_args_list = [
			ArgStruct('Name', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_V_4', DataType.StringList, None, False, True, 1),
			ArgStruct('Ip_V_6', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Name: List[str] = None
			self.Ip_V_4: List[str] = None
			self.Ip_V_6: List[str] = None

	def get(self, imsi=repcap.Imsi.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:EPDG:CONNections:IMSI<Suffix>:APN \n
		Snippet: value: GetStruct = driver.sense.data.control.epdg.connections.imsi.apn.get(imsi = repcap.Imsi.Default) \n
		Queries the connection list for a selected IMSI. The list contains 15 connections. If there are fewer connections, the
		remaining entries are filled with INV. Three parameters are returned for each of the 15 connections: {<Name>, <IPv4>,
		<IPv6>}conn 1, {...}conn 2, ..., {...}conn 15 \n
			:param imsi: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Imsi')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		imsi_cmd_val = self._base.get_repcap_cmd_value(imsi, repcap.Imsi)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:EPDG:CONNections:IMSI{imsi_cmd_val}:APN?', self.__class__.GetStruct())
