from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scheme:
	"""Scheme commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scheme", core, parent)

	def set(self, auth_scheme: enums.AuthScheme, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:AUTHenticati:SCHeme \n
		Snippet: driver.configure.data.control.ims.subscriber.authentication.scheme.set(auth_scheme = enums.AuthScheme.AKA1, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies whether authentication is performed for the subscriber profile number <s> and selects the authentication and
		key agreement version to be used. \n
			:param auth_scheme: AKA1 | AKA2 | NOAuthentic AKA1: authentication with AKA version 1 AKA2: authentication with AKA version 2 NOAuthentic: no authentication
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.enum_scalar_to_str(auth_scheme, enums.AuthScheme)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:AUTHenticati:SCHeme {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> enums.AuthScheme:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:AUTHenticati:SCHeme \n
		Snippet: value: enums.AuthScheme = driver.configure.data.control.ims.subscriber.authentication.scheme.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies whether authentication is performed for the subscriber profile number <s> and selects the authentication and
		key agreement version to be used. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: auth_scheme: AKA1 | AKA2 | NOAuthentic AKA1: authentication with AKA version 1 AKA2: authentication with AKA version 2 NOAuthentic: no authentication"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:AUTHenticati:SCHeme?')
		return Conversions.str_to_scalar_enum(response, enums.AuthScheme)
