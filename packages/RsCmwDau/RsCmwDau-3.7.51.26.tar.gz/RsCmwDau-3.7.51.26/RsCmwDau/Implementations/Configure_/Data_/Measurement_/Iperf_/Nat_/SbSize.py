from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SbSize:
	"""SbSize commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sbSize", core, parent)

	def set(self, sb_size: float, nat=repcap.Nat.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:SBSize \n
		Snippet: driver.configure.data.measurement.iperf.nat.sbSize.set(sb_size = 1.0, nat = repcap.Nat.Default) \n
		Specifies the size of the socket buffer for an iperf(NAT) client instance. \n
			:param sb_size: Range: 0 kByte to 10240 kByte, Unit: kByte
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')"""
		param = Conversions.decimal_value_to_str(sb_size)
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:SBSize {param}')

	def get(self, nat=repcap.Nat.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:SBSize \n
		Snippet: value: float = driver.configure.data.measurement.iperf.nat.sbSize.get(nat = repcap.Nat.Default) \n
		Specifies the size of the socket buffer for an iperf(NAT) client instance. \n
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')
			:return: sb_size: Range: 0 kByte to 10240 kByte, Unit: kByte"""
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:SBSize?')
		return Conversions.str_to_float(response)
