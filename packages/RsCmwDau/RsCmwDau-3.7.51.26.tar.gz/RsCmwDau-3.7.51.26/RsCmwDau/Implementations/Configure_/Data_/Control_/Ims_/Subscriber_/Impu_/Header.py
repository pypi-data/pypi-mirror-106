from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Header:
	"""Header commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("header", core, parent)

	def set(self, pau_header: enums.PauHeader, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:IMPU:HEADer \n
		Snippet: driver.configure.data.control.ims.subscriber.impu.header.set(pau_header = enums.PauHeader.COGE, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
			INTRO_CMD_HELP: Selects which public IDs are sent to the DUT in the PAU header of the 200/OK response to REGISTER messages: \n
			- Configured: public user IDs configured in the subscriber settings
			- Registered: ID sent by the DUT in the 'from' header of the REGISTER message
			- Generated: automatically generated ID starting with 'tel:555' \n
			:param pau_header: CONRege | RECoge | CORE | RECN | COGE | REGE | CONF | REGD CONRege: configured, registered, generated RECoge: registered, configured, generated CORE: configured, registered RECN: registered, configured COGE: configured, generated REGE: registered, generated CONF: configured REGD: registered
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.enum_scalar_to_str(pau_header, enums.PauHeader)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:IMPU:HEADer {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> enums.PauHeader:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:IMPU:HEADer \n
		Snippet: value: enums.PauHeader = driver.configure.data.control.ims.subscriber.impu.header.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
			INTRO_CMD_HELP: Selects which public IDs are sent to the DUT in the PAU header of the 200/OK response to REGISTER messages: \n
			- Configured: public user IDs configured in the subscriber settings
			- Registered: ID sent by the DUT in the 'from' header of the REGISTER message
			- Generated: automatically generated ID starting with 'tel:555' \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: pau_header: CONRege | RECoge | CORE | RECN | COGE | REGE | CONF | REGD CONRege: configured, registered, generated RECoge: registered, configured, generated CORE: configured, registered RECN: registered, configured COGE: configured, generated REGE: registered, generated CONF: configured REGD: registered"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:IMPU:HEADer?')
		return Conversions.str_to_scalar_enum(response, enums.PauHeader)
