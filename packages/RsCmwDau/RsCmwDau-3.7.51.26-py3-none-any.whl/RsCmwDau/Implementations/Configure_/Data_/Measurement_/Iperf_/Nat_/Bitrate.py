from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bitrate:
	"""Bitrate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bitrate", core, parent)

	def set(self, bitrate: float, nat=repcap.Nat.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:BITRate \n
		Snippet: driver.configure.data.measurement.iperf.nat.bitrate.set(bitrate = 1.0, nat = repcap.Nat.Default) \n
		Defines the maximum bit rate for an iperf(NAT) instance. \n
			:param bitrate: Maximum bit rate to be transferred Range: 0 bit/s to 4E+9 bit/s, Unit: bit/s
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')"""
		param = Conversions.decimal_value_to_str(bitrate)
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:BITRate {param}')

	def get(self, nat=repcap.Nat.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:BITRate \n
		Snippet: value: float = driver.configure.data.measurement.iperf.nat.bitrate.get(nat = repcap.Nat.Default) \n
		Defines the maximum bit rate for an iperf(NAT) instance. \n
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')
			:return: bitrate: Maximum bit rate to be transferred Range: 0 bit/s to 4E+9 bit/s, Unit: bit/s"""
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:BITRate?')
		return Conversions.str_to_float(response)
