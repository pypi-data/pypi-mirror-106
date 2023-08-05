from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, nat=repcap.Nat.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:ENABle \n
		Snippet: driver.configure.data.measurement.iperf.nat.enable.set(enable = False, nat = repcap.Nat.Default) \n
		Activates or deactivates an iperf(NAT) client instance. \n
			:param enable: OFF | ON
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')"""
		param = Conversions.bool_to_str(enable)
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:ENABle {param}')

	def get(self, nat=repcap.Nat.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:ENABle \n
		Snippet: value: bool = driver.configure.data.measurement.iperf.nat.enable.get(nat = repcap.Nat.Default) \n
		Activates or deactivates an iperf(NAT) client instance. \n
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')
			:return: enable: OFF | ON"""
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
