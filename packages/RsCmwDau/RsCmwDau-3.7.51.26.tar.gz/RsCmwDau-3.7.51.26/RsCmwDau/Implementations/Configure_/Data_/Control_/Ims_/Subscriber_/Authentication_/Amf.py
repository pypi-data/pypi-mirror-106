from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amf:
	"""Amf commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("amf", core, parent)

	def set(self, auth_amf: str, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:AUTHenticati:AMF \n
		Snippet: driver.configure.data.control.ims.subscriber.authentication.amf.set(auth_amf = r1, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies the authentication management field (AMF) for the subscriber profile number <s>. \n
			:param auth_amf: AMF as four-digit hexadecimal number A query returns a string. A setting supports the string format and the hexadecimal format (#H...) .
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.value_to_str(auth_amf)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:AUTHenticati:AMF {param}')

	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:AUTHenticati:AMF \n
		Snippet: value: str = driver.configure.data.control.ims.subscriber.authentication.amf.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies the authentication management field (AMF) for the subscriber profile number <s>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: auth_amf: AMF as four-digit hexadecimal number A query returns a string. A setting supports the string format and the hexadecimal format (#H...) ."""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:AUTHenticati:AMF?')
		return trim_str_response(response)
