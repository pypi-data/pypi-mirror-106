from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ForceMoCall:
	"""ForceMoCall commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("forceMoCall", core, parent)

	def set(self, force_codec_mo: bool, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:FORCemocall \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.forceMoCall.set(force_codec_mo = False, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Forces a specific codec type for mobile-originating calls. \n
			:param force_codec_mo: OFF | ON OFF The first codec type offered via SDP is used. ON The voice codec type configured for the virtual subscriber is used.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.bool_to_str(force_codec_mo)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:FORCemocall {param}')

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:FORCemocall \n
		Snippet: value: bool = driver.configure.data.control.ims.virtualSubscriber.forceMoCall.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Forces a specific codec type for mobile-originating calls. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: force_codec_mo: OFF | ON OFF The first codec type offered via SDP is used. ON The voice codec type configured for the virtual subscriber is used."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:FORCemocall?')
		return Conversions.str_to_bool(response)
