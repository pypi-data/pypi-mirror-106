from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpAddress:
	"""IpAddress commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipAddress", core, parent)

	def set(self, ip_address: str, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:IPADdress \n
		Snippet: driver.configure.data.measurement.qos.filterPy.ipAddress.set(ip_address = '1', fltr = repcap.Fltr.Default) \n
		Specifies the destination address as filter criterion for IP packets. \n
			:param ip_address: String indicating a full IPv4 address or a full IPv6 address or an IPv6 prefix
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.value_to_quoted_str(ip_address)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:IPADdress {param}')

	def get(self, fltr=repcap.Fltr.Default) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:IPADdress \n
		Snippet: value: str = driver.configure.data.measurement.qos.filterPy.ipAddress.get(fltr = repcap.Fltr.Default) \n
		Specifies the destination address as filter criterion for IP packets. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: ip_address: String indicating a full IPv4 address or a full IPv6 address or an IPv6 prefix"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:IPADdress?')
		return trim_str_response(response)
