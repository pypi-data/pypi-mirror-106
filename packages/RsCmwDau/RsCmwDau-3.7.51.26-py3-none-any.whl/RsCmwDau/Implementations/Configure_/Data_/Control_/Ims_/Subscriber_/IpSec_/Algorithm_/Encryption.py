from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Encryption:
	"""Encryption commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("encryption", core, parent)

	def set(self, encryption_alg: enums.IpSecEalgorithm, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:IPSec:ALGorithm:ENCRyption \n
		Snippet: driver.configure.data.control.ims.subscriber.ipSec.algorithm.encryption.set(encryption_alg = enums.IpSecEalgorithm.AES, ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Selects an encryption algorithm for subscriber profile number <s>. \n
			:param encryption_alg: DES | AES | NOC | AUTO DES: DES-EDE3-CBC AES: AES-CBC NOC: NULL, no encryption AUTO: as indicated in REGISTER message
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')"""
		param = Conversions.enum_scalar_to_str(encryption_alg, enums.IpSecEalgorithm)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:IPSec:ALGorithm:ENCRyption {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, subscriber=repcap.Subscriber.Default) -> enums.IpSecEalgorithm:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:SUBScriber<Subscriber>:IPSec:ALGorithm:ENCRyption \n
		Snippet: value: enums.IpSecEalgorithm = driver.configure.data.control.ims.subscriber.ipSec.algorithm.encryption.get(ims = repcap.Ims.Default, subscriber = repcap.Subscriber.Default) \n
		Selects an encryption algorithm for subscriber profile number <s>. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param subscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subscriber')
			:return: encryption_alg: DES | AES | NOC | AUTO DES: DES-EDE3-CBC AES: AES-CBC NOC: NULL, no encryption AUTO: as indicated in REGISTER message"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		subscriber_cmd_val = self._base.get_repcap_cmd_value(subscriber, repcap.Subscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber{subscriber_cmd_val}:IPSec:ALGorithm:ENCRyption?')
		return Conversions.str_to_scalar_enum(response, enums.IpSecEalgorithm)
