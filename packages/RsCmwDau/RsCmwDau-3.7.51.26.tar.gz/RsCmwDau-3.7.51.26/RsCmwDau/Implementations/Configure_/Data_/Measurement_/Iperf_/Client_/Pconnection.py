from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pconnection:
	"""Pconnection commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pconnection", core, parent)

	def set(self, par_conn: int, client=repcap.Client.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:PCONnection \n
		Snippet: driver.configure.data.measurement.iperf.client.pconnection.set(par_conn = 1, client = repcap.Client.Default) \n
		Specifies the number of parallel connections for an iperf/iperf3 client instance. Only applicable for protocol type TCP. \n
			:param par_conn: Range: 1 to 4
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')"""
		param = Conversions.decimal_value_to_str(par_conn)
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:PCONnection {param}')

	def get(self, client=repcap.Client.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:CLIent<Index>:PCONnection \n
		Snippet: value: int = driver.configure.data.measurement.iperf.client.pconnection.get(client = repcap.Client.Default) \n
		Specifies the number of parallel connections for an iperf/iperf3 client instance. Only applicable for protocol type TCP. \n
			:param client: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Client')
			:return: par_conn: Range: 1 to 4"""
		client_cmd_val = self._base.get_repcap_cmd_value(client, repcap.Client)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:CLIent{client_cmd_val}:PCONnection?')
		return Conversions.str_to_int(response)
