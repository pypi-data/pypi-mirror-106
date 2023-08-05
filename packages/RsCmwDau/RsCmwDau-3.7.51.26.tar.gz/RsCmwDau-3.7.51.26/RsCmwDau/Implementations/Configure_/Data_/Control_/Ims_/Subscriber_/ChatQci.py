from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChatQci:
	"""ChatQci commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("chatQci", core, parent)

	def set(self, chat_qci: int, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:CHATqci \n
		Snippet: driver.configure.data.control.ims.subscriber.chatQci.set(chat_qci = 1, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies the QCI used by the DUT for RCS message transfer. \n
			:param chat_qci: Range: 0 to 255
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.decimal_value_to_str(chat_qci)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:CHATqci {param}')

	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:CHATqci \n
		Snippet: value: int = driver.configure.data.control.ims.subscriber.chatQci.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies the QCI used by the DUT for RCS message transfer. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: chat_qci: Range: 0 to 255"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:CHATqci?')
		return Conversions.str_to_int(response)
