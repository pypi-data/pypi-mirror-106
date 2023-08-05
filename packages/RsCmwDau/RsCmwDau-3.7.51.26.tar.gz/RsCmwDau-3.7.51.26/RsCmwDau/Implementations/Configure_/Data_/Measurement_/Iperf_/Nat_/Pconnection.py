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

	def set(self, par_conn: int, nat=repcap.Nat.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:PCONnection \n
		Snippet: driver.configure.data.measurement.iperf.nat.pconnection.set(par_conn = 1, nat = repcap.Nat.Default) \n
		Specifies the number of parallel connections for an iperf(NAT) client instance. Only applicable for protocol type TCP. \n
			:param par_conn: Range: 1 to 4
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')"""
		param = Conversions.decimal_value_to_str(par_conn)
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:PCONnection {param}')

	def get(self, nat=repcap.Nat.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:NAT<Index>:PCONnection \n
		Snippet: value: int = driver.configure.data.measurement.iperf.nat.pconnection.get(nat = repcap.Nat.Default) \n
		Specifies the number of parallel connections for an iperf(NAT) client instance. Only applicable for protocol type TCP. \n
			:param nat: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nat')
			:return: par_conn: Range: 1 to 4"""
		nat_cmd_val = self._base.get_repcap_cmd_value(nat, repcap.Nat)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:NAT{nat_cmd_val}:PCONnection?')
		return Conversions.str_to_int(response)
