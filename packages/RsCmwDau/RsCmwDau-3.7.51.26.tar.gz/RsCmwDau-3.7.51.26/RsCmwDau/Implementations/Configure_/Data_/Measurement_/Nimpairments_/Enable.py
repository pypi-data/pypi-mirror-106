from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def set(self, enable: bool, impairments=repcap.Impairments.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:ENABle \n
		Snippet: driver.configure.data.measurement.nimpairments.enable.set(enable = False, impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param enable: No help available
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')"""
		param = Conversions.bool_to_str(enable)
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:ENABle {param}')

	def get(self, impairments=repcap.Impairments.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:ENABle \n
		Snippet: value: bool = driver.configure.data.measurement.nimpairments.enable.get(impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')
			:return: enable: No help available"""
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
