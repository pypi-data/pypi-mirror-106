from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ginfo:
	"""Ginfo commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ginfo", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Timestamp: List[str]: Timestamp of the entry as string in the format 'hh:mm:ss'
			- Info_Type: List[enums.InfoType]: NONE | INFO | WARNing | ERRor Category of the entry NONE means that no category is assigned. If no entry at all is available, the answer is '',NONE,''.
			- Generic_Info: List[str]: Text string describing the event"""
		__meta_args_list = [
			ArgStruct('Timestamp', DataType.StringList, None, False, True, 1),
			ArgStruct('Info_Type', DataType.EnumList, enums.InfoType, False, True, 1),
			ArgStruct('Generic_Info', DataType.StringList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Timestamp: List[str] = None
			self.Info_Type: List[enums.InfoType] = None
			self.Generic_Info: List[str] = None

	def get(self, ims=repcap.Ims.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:GINFo \n
		Snippet: value: GetStruct = driver.sense.data.control.ims.ginfo.get(ims = repcap.Ims.Default) \n
		Queries all entries of the 'General IMS Info' area. For each entry, three parameters are returned, from oldest to latest
		entry: {<Timestamp>, <InfoType>, <GenericInfo>}entry 1, {<Timestamp>, <InfoType>, <GenericInfo>}entry 2, ... \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:GINFo?', self.__class__.GetStruct())
