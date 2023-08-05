from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Integrity:
	"""Integrity commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("integrity", core, parent)

	def set(self, integrity_alg: enums.IpSecIalgorithm, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:IPSec:ALGorithm:INTegrity \n
		Snippet: driver.configure.data.control.ims.subscriber.ipSec.algorithm.integrity.set(integrity_alg = enums.IpSecIalgorithm.AUTO, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Selects an integrity protection algorithm for subscriber profile number <s>. \n
			:param integrity_alg: HMMD | HMSH | AUTO HMMD: HMAC-MD5-96 HMSH: HMAC-SHA-1-96 AUTO: as indicated in REGISTER message
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.enum_scalar_to_str(integrity_alg, enums.IpSecIalgorithm)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:IPSec:ALGorithm:INTegrity {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> enums.IpSecIalgorithm:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:IPSec:ALGorithm:INTegrity \n
		Snippet: value: enums.IpSecIalgorithm = driver.configure.data.control.ims.subscriber.ipSec.algorithm.integrity.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Selects an integrity protection algorithm for subscriber profile number <s>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: integrity_alg: HMMD | HMSH | AUTO HMMD: HMAC-MD5-96 HMSH: HMAC-SHA-1-96 AUTO: as indicated in REGISTER message"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:IPSec:ALGorithm:INTegrity?')
		return Conversions.str_to_scalar_enum(response, enums.IpSecIalgorithm)
