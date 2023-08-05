from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAddress", core, parent)

	def set(self, ip_address: str, impairments=repcap.Impairments.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:IPADdress \n
		Snippet: driver.configure.data.measurement.nimpairments.ipAddress.set(ip_address = '1', impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param ip_address: No help available
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')"""
		param = Conversions.value_to_quoted_str(ip_address)
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:IPADdress {param}')

	def get(self, impairments=repcap.Impairments.Default) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:IPADdress \n
		Snippet: value: str = driver.configure.data.measurement.nimpairments.ipAddress.get(impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')
			:return: ip_address: No help available"""
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:IPADdress?')
		return trim_str_response(response)
