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

	def set(self, sb_size: float, server=repcap.Server.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:SBSize \n
		Snippet: driver.configure.data.measurement.iperf.server.sbSize.set(sb_size = 1.0, server = repcap.Server.Default) \n
		Specifies the size of the socket buffer for an iperf server instance. \n
			:param sb_size: Range: 0 kByte to 10240 kByte, Unit: kByte
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')"""
		param = Conversions.decimal_value_to_str(sb_size)
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:SBSize {param}')

	def get(self, server=repcap.Server.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:SBSize \n
		Snippet: value: float = driver.configure.data.measurement.iperf.server.sbSize.get(server = repcap.Server.Default) \n
		Specifies the size of the socket buffer for an iperf server instance. \n
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')
			:return: sb_size: Range: 0 kByte to 10240 kByte, Unit: kByte"""
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:SBSize?')
		return Conversions.str_to_float(response)
