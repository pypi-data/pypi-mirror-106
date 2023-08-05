from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wsize:
	"""Wsize commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("wsize", core, parent)

	def set(self, window_size: float, server=repcap.Server.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:WSIZe \n
		Snippet: driver.configure.data.measurement.iperf.server.wsize.set(window_size = 1.0, server = repcap.Server.Default) \n
		No command help available \n
			:param window_size: No help available
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')"""
		param = Conversions.decimal_value_to_str(window_size)
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:WSIZe {param}')

	def get(self, server=repcap.Server.Default) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:SERVer<Index>:WSIZe \n
		Snippet: value: float = driver.configure.data.measurement.iperf.server.wsize.get(server = repcap.Server.Default) \n
		No command help available \n
			:param server: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Server')
			:return: window_size: No help available"""
		server_cmd_val = self._base.get_repcap_cmd_value(server, repcap.Server)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:SERVer{server_cmd_val}:WSIZe?')
		return Conversions.str_to_float(response)
