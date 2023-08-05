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

	def set(self, enable: bool, server=repcap.Server.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:ENABle \n
		Snippet: driver.configure.data.measurement.iperf.server.enable.set(enable = False, server = repcap.Server.Default) \n
		Activates or deactivates an iperf server instance. \n
			:param enable: OFF | ON
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')"""
		param = Conversions.bool_to_str(enable)
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:ENABle {param}')

	def get(self, server=repcap.Server.Default) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:ENABle \n
		Snippet: value: bool = driver.configure.data.measurement.iperf.server.enable.get(server = repcap.Server.Default) \n
		Activates or deactivates an iperf server instance. \n
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')
			:return: enable: OFF | ON"""
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:ENABle?')
		return Conversions.str_to_bool(response)
