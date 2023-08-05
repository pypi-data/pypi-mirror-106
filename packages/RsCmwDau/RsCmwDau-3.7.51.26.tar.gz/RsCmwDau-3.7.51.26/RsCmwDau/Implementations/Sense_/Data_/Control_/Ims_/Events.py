from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Events:
	"""Events commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("events", core, parent)

	@property
	def last(self):
		"""last commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_last'):
			from .Events_.Last import Last
			self._last = Last(self._core, self._base)
		return self._last

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Idn: List[str]: String identifying the event log entry Use this ID to query event details via [CMDLINK: SENSe:DATA:CONTrol:IMS2:HISTory CMDLINK]
			- Timestamps: List[str]: Timestamp as string in the format 'hh:mm:ss'
			- Source: List[str]: Originating party as string
			- Destination: List[str]: Terminating party as string
			- Type_Py: List[enums.DataType]: AUDio | VIDeo | SMS | INValid | CALL | RCSLmsg | FILetransfer | FTLMode AUDio: audio call VIDeo: video call SMS: sent or received short message CALL: call setup, released call or call on hold RCSLmsg: sent or received RCS large message FILetransfer: file transfer FTLMode: file transfer large mode
			- State: List[enums.SessionState]: OK | NOK | PROGgres | RINGing | ESTablished | HOLD | RESumed | RELeased | MEDiaupdate | BUSY | DECLined | INITialmedia | FILetransfer | SRVCcrelease | TERMinated | CANCeled | REJected | CREated Status of the session or message transfer"""
		__meta_args_list = [
			ArgStruct('Idn', DataType.StringList, None, False, True, 1),
			ArgStruct('Timestamps', DataType.StringList, None, False, True, 1),
			ArgStruct('Source', DataType.StringList, None, False, True, 1),
			ArgStruct('Destination', DataType.StringList, None, False, True, 1),
			ArgStruct('Type_Py', DataType.EnumList, enums.DataType, False, True, 1),
			ArgStruct('State', DataType.EnumList, enums.SessionState, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: List[str] = None
			self.Timestamps: List[str] = None
			self.Source: List[str] = None
			self.Destination: List[str] = None
			self.Type_Py: List[enums.DataType] = None
			self.State: List[enums.SessionState] = None

	def get(self, ims=repcap.Ims.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:EVENts \n
		Snippet: value: GetStruct = driver.sense.data.control.ims.events.get(ims = repcap.Ims.Default) \n
		Queries all entries of the event log. For each entry, six parameters are returned: {<ID>, <Timestamps>, <Source>,
		<Destination>, <Type>, <State>}entry 1, {<ID>, ..., <State>}entry 2, ... \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:EVENts?', self.__class__.GetStruct())

	def clone(self) -> 'Events':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Events(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
