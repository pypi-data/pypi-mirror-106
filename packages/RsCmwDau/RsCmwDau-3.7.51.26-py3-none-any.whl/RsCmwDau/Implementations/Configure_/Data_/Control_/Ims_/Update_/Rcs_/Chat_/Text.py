from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("text", core, parent)

	def set(self, text: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:RCS:CHAT:TEXT \n
		Snippet: driver.configure.data.control.ims.update.rcs.chat.text.set(text = '1', ims = repcap.Ims.Default) \n
		Defines a message text to be sent to the DUT via an established chat session. Initiate the message transfer via method
		RsCmwDau.Configure.Data.Control.Ims.Update.Rcs.Chat.Perform.set. \n
			:param text: Message as string
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(text)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:RCS:CHAT:TEXT {param}')

	def get(self, ims=repcap.Ims.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:RCS:CHAT:TEXT \n
		Snippet: value: str = driver.configure.data.control.ims.update.rcs.chat.text.get(ims = repcap.Ims.Default) \n
		Defines a message text to be sent to the DUT via an established chat session. Initiate the message transfer via method
		RsCmwDau.Configure.Data.Control.Ims.Update.Rcs.Chat.Perform.set. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: text: Message as string"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:RCS:CHAT:TEXT?')
		return trim_str_response(response)
