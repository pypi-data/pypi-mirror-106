from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.CallType, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTSMs:TYPE \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtSms.typePy.set(type_py = enums.CallType.ACK, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the type of messages to be sent by virtual subscriber number <v>. \n
			:param type_py: GPP | GPP2 | ACK | PAGer | LARGe | RCSChat | RCSGrpchat | GENeric GPP: 3GPP GPP2: 3GPP2 without delivery ACK ACK: 3GPP2 with delivery ACK PAGer: RCS pager mode LARGe: RCS large mode RCSChat: RCS 1 to 1 chat RCSGrpchat: RCS group chat GENeric: 3GPP generic SMS
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(type_py, enums.CallType)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTSMs:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.CallType:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTSMs:TYPE \n
		Snippet: value: enums.CallType = driver.configure.data.control.ims.virtualSubscriber.mtSms.typePy.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Selects the type of messages to be sent by virtual subscriber number <v>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: type_py: GPP | GPP2 | ACK | PAGer | LARGe | RCSChat | RCSGrpchat | GENeric GPP: 3GPP GPP2: 3GPP2 without delivery ACK ACK: 3GPP2 with delivery ACK PAGer: RCS pager mode LARGe: RCS large mode RCSChat: RCS 1 to 1 chat RCSGrpchat: RCS group chat GENeric: 3GPP generic SMS"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTSMs:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.CallType)
