from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Last:
	"""Last commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("last", core, parent)

	# noinspection PyTypeChecker
	class GetStruct(StructBase):
		"""Response structure. Fields: \n
			- Idn: str: String identifying the event log entry Use this ID to query event details via [CMDLINK: SENSe:DATA:CONTrol:IMS2:HISTory CMDLINK]
			- Timestamps: str: Timestamp as string in the format 'hh:mm:ss'
			- Source: str: Originating party as string
			- Destination: str: Terminating party as string
			- Type_Py: enums.DataType: AUDio | VIDeo | SMS | INValid | CALL | RCSLmsg | FILetransfer | FTLMode AUDio: audio call VIDeo: video call SMS: sent or received short message CALL: call setup, released call or call on hold RCSLmsg: sent or received RCS large message FILetransfer: file transfer FTLMode: file transfer large mode
			- State: enums.SessionState: OK | NOK | PROGgres | RINGing | ESTablished | HOLD | RESumed | RELeased | MEDiaupdate | BUSY | DECLined | INITialmedia | FILetransfer | SRVCcrelease | TERMinated | CANCeled | REJected | CREated Status of the session or message transfer"""
		__meta_args_list = [
			ArgStruct.scalar_str('Idn'),
			ArgStruct.scalar_str('Timestamps'),
			ArgStruct.scalar_str('Source'),
			ArgStruct.scalar_str('Destination'),
			ArgStruct.scalar_enum('Type_Py', enums.DataType),
			ArgStruct.scalar_enum('State', enums.SessionState)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Idn: str = None
			self.Timestamps: str = None
			self.Source: str = None
			self.Destination: str = None
			self.Type_Py: enums.DataType = None
			self.State: enums.SessionState = None

	def get(self, ims=repcap.Ims.Default) -> GetStruct:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:EVENts:LAST \n
		Snippet: value: GetStruct = driver.sense.data.control.ims.events.last.get(ims = repcap.Ims.Default) \n
		Queries the last entry of the event log. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: structure: for return value, see the help for GetStruct structure arguments."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		return self._core.io.query_struct(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:EVENts:LAST?', self.__class__.GetStruct())
