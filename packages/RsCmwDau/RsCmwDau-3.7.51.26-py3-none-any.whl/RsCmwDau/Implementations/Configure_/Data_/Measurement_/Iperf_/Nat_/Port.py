from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("port", core, parent)

	def set(self, port: int, nat=repcap.Nat.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:PORT \n
		Snippet: driver.configure.data.measurement.iperf.nat.port.set(port = 1, nat = repcap.Nat.Default) \n
		Defines the LAN DAU port number for an iperf(NAT) client instance. \n
			:param port: Range: 0 to 65535
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')"""
		param = Conversions.decimal_value_to_str(port)
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:PORT {param}')

	def get(self, nat=repcap.Nat.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:PORT \n
		Snippet: value: int = driver.configure.data.measurement.iperf.nat.port.get(nat = repcap.Nat.Default) \n
		Defines the LAN DAU port number for an iperf(NAT) client instance. \n
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')
			:return: port: Range: 0 to 65535"""
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:PORT?')
		return Conversions.str_to_int(response)
