from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DtxRecv:
	"""DtxRecv commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dtxRecv", core, parent)

	def set(self, dtx_recv: enums.DtxRecv, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:DTXRecv \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.evs.dtxRecv.set(dtx_recv = enums.DtxRecv.DISable, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Specifies the SDP parameter 'dtx-recv' for the EVS codec. \n
			:param dtx_recv: DISable | ENABle | NP Disable, enable, not present
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(dtx_recv, enums.DtxRecv)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:DTXRecv {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.DtxRecv:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:EVS:DTXRecv \n
		Snippet: value: enums.DtxRecv = driver.configure.data.control.ims.virtualSubscriber.evs.dtxRecv.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Specifies the SDP parameter 'dtx-recv' for the EVS codec. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: dtx_recv: DISable | ENABle | NP Disable, enable, not present"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:EVS:DTXRecv?')
		return Conversions.str_to_scalar_enum(response, enums.DtxRecv)
