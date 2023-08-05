from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Algorithm:
	"""Algorithm commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("algorithm", core, parent)

	def set(self, auth_key_gen_alg: enums.AuthAlgorithm, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:AUTHenticati:ALGorithm \n
		Snippet: driver.configure.data.control.ims.subscriber.authentication.algorithm.set(auth_key_gen_alg = enums.AuthAlgorithm.MILenage, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies which algorithm set is used for the subscriber profile number <s>. \n
			:param auth_key_gen_alg: XOR | MILenage
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.enum_scalar_to_str(auth_key_gen_alg, enums.AuthAlgorithm)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:AUTHenticati:ALGorithm {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> enums.AuthAlgorithm:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:AUTHenticati:ALGorithm \n
		Snippet: value: enums.AuthAlgorithm = driver.configure.data.control.ims.subscriber.authentication.algorithm.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Specifies which algorithm set is used for the subscriber profile number <s>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: auth_key_gen_alg: XOR | MILenage"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:AUTHenticati:ALGorithm?')
		return Conversions.str_to_scalar_enum(response, enums.AuthAlgorithm)
