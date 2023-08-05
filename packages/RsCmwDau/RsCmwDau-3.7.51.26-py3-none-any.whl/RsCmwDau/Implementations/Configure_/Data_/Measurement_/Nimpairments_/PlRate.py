from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PlRate:
	"""PlRate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("plRate", core, parent)

	def set(self, packet_loss_rate: float, impairments=repcap.Impairments.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:PLRate \n
		Snippet: driver.configure.data.measurement.nimpairments.plRate.set(packet_loss_rate = 1.0, impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param packet_loss_rate: No help available
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')"""
		param = Conversions.decimal_value_to_str(packet_loss_rate)
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:PLRate {param}')

	def get(self, impairments=repcap.Impairments.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:PLRate \n
		Snippet: value: float = driver.configure.data.measurement.nimpairments.plRate.get(impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')
			:return: packet_loss_rate: No help available"""
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:PLRate?')
		return Conversions.str_to_float(response)
