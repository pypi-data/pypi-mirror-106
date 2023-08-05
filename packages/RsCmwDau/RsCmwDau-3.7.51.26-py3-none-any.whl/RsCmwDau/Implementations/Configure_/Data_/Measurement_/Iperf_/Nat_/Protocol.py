from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protocol:
	"""Protocol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("protocol", core, parent)

	def set(self, protocol: enums.Protocol, nat=repcap.Nat.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:PROTocol \n
		Snippet: driver.configure.data.measurement.iperf.nat.protocol.set(protocol = enums.Protocol.TCP, nat = repcap.Nat.Default) \n
		Selects the protocol type to be used for an iperf(NAT) client instance. \n
			:param protocol: UDP | TCP UDP: use the user datagram protocol TCP: use the transport control protocol
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')"""
		param = Conversions.enum_scalar_to_str(protocol, enums.Protocol)
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:PROTocol {param}')

	# noinspection PyTypeChecker
	def get(self, nat=repcap.Nat.Default) -> enums.Protocol:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:PROTocol \n
		Snippet: value: enums.Protocol = driver.configure.data.measurement.iperf.nat.protocol.get(nat = repcap.Nat.Default) \n
		Selects the protocol type to be used for an iperf(NAT) client instance. \n
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')
			:return: protocol: UDP | TCP UDP: use the user datagram protocol TCP: use the transport control protocol"""
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Protocol)
