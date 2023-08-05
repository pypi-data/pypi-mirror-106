from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("text", core, parent)

	def set(self, text: str, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTSMs:TEXT \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.mtSms.text.set(text = '1', ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Defines the text for messages to be sent by virtual subscriber number <v>. For generic SMS, it defines the contents of
		the RPDU via hexadecimal characters. \n
			:param text: Message text or RPDU contents as string
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.value_to_quoted_str(text)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTSMs:TEXT {param}')

	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:MTSMs:TEXT \n
		Snippet: value: str = driver.configure.data.control.ims.virtualSubscriber.mtSms.text.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Defines the text for messages to be sent by virtual subscriber number <v>. For generic SMS, it defines the contents of
		the RPDU via hexadecimal characters. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: text: Message text or RPDU contents as string"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:MTSMs:TEXT?')
		return trim_str_response(response)
