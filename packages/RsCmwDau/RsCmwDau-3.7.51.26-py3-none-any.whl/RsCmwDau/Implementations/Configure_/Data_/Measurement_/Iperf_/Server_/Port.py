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

	def set(self, port: int, server=repcap.Server.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:PORT \n
		Snippet: driver.configure.data.measurement.iperf.server.port.set(port = 1, server = repcap.Server.Default) \n
		Defines the LAN DAU port number for an iperf server instance. \n
			:param port: Range: 0 to 65535
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')"""
		param = Conversions.decimal_value_to_str(port)
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:PORT {param}')

	def get(self, server=repcap.Server.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:PORT \n
		Snippet: value: int = driver.configure.data.measurement.iperf.server.port.get(server = repcap.Server.Default) \n
		Defines the LAN DAU port number for an iperf server instance. \n
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')
			:return: port: Range: 0 to 65535"""
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:PORT?')
		return Conversions.str_to_int(response)
