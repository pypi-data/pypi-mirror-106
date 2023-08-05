from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iperf:
	"""Iperf commands group definition. 31 total commands, 3 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iperf", core, parent)

	@property
	def server(self):
		"""server commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_server'):
			from .Iperf_.Server import Server
			self._server = Server(self._core, self._base)
		return self._server

	@property
	def client(self):
		"""client commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_client'):
			from .Iperf_.Client import Client
			self._client = Client(self._core, self._base)
		return self._client

	@property
	def nat(self):
		"""nat commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_nat'):
			from .Iperf_.Nat import Nat
			self._nat = Nat(self._core, self._base)
		return self._nat

	def get_type_py(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:TYPE \n
		Snippet: value: float = driver.configure.data.measurement.iperf.get_type_py() \n
		Selects the type of iperf to be used. \n
			:return: iperf_type: IPERf | IP3 | IPNat Iperf or iperf3 or iperf(NAT)
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:TYPE?')
		return Conversions.str_to_float(response)

	def set_type_py(self, iperf_type: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:TYPE \n
		Snippet: driver.configure.data.measurement.iperf.set_type_py(iperf_type = 1.0) \n
		Selects the type of iperf to be used. \n
			:param iperf_type: IPERf | IP3 | IPNat Iperf or iperf3 or iperf(NAT)
		"""
		param = Conversions.decimal_value_to_str(iperf_type)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:TYPE {param}')

	def get_tduration(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:TDURation \n
		Snippet: value: int = driver.configure.data.measurement.iperf.get_tduration() \n
		Defines the duration of the test. \n
			:return: test_duration: Range: 1 s to 1E+6 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:TDURation?')
		return Conversions.str_to_int(response)

	def set_tduration(self, test_duration: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:TDURation \n
		Snippet: driver.configure.data.measurement.iperf.set_tduration(test_duration = 1) \n
		Defines the duration of the test. \n
			:param test_duration: Range: 1 s to 1E+6 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(test_duration)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:TDURation {param}')

	def get_psize(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PSIZe \n
		Snippet: value: int = driver.configure.data.measurement.iperf.get_psize() \n
		Defines the packet size for iperf tests. \n
			:return: packet_size: Range: 40 bytes to 65507 bytes, Unit: bytes
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PSIZe?')
		return Conversions.str_to_int(response)

	def set_psize(self, packet_size: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PSIZe \n
		Snippet: driver.configure.data.measurement.iperf.set_psize(packet_size = 1) \n
		Defines the packet size for iperf tests. \n
			:param packet_size: Range: 40 bytes to 65507 bytes, Unit: bytes
		"""
		param = Conversions.decimal_value_to_str(packet_size)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PSIZe {param}')

	# noinspection PyTypeChecker
	def get_stype(self) -> enums.ServiceTypeB:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:STYPe \n
		Snippet: value: enums.ServiceTypeB = driver.configure.data.measurement.iperf.get_stype() \n
		No command help available \n
			:return: service_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.ServiceTypeB)

	def set_stype(self, service_type: enums.ServiceTypeB) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:STYPe \n
		Snippet: driver.configure.data.measurement.iperf.set_stype(service_type = enums.ServiceTypeB.BIDirectional) \n
		No command help available \n
			:param service_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(service_type, enums.ServiceTypeB)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:STYPe {param}')

	def get_wsize(self) -> float:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:WSIZe \n
		Snippet: value: float = driver.configure.data.measurement.iperf.get_wsize() \n
		No command help available \n
			:return: window_size: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:WSIZe?')
		return Conversions.str_to_float(response)

	def set_wsize(self, window_size: float) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:WSIZe \n
		Snippet: driver.configure.data.measurement.iperf.set_wsize(window_size = 1.0) \n
		No command help available \n
			:param window_size: No help available
		"""
		param = Conversions.decimal_value_to_str(window_size)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:WSIZe {param}')

	def get_port(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PORT \n
		Snippet: value: int = driver.configure.data.measurement.iperf.get_port() \n
		No command help available \n
			:return: port: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PORT?')
		return Conversions.str_to_int(response)

	def set_port(self, port: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PORT \n
		Snippet: driver.configure.data.measurement.iperf.set_port(port = 1) \n
		No command help available \n
			:param port: No help available
		"""
		param = Conversions.decimal_value_to_str(port)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PORT {param}')

	def get_lport(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:LPORt \n
		Snippet: value: int = driver.configure.data.measurement.iperf.get_lport() \n
		No command help available \n
			:return: listen_port: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:LPORt?')
		return Conversions.str_to_int(response)

	def set_lport(self, listen_port: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:LPORt \n
		Snippet: driver.configure.data.measurement.iperf.set_lport(listen_port = 1) \n
		No command help available \n
			:param listen_port: No help available
		"""
		param = Conversions.decimal_value_to_str(listen_port)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:LPORt {param}')

	# noinspection PyTypeChecker
	def get_protocol(self) -> enums.Protocol:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PROTocol \n
		Snippet: value: enums.Protocol = driver.configure.data.measurement.iperf.get_protocol() \n
		No command help available \n
			:return: protocol: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.Protocol)

	def set_protocol(self, protocol: enums.Protocol) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PROTocol \n
		Snippet: driver.configure.data.measurement.iperf.set_protocol(protocol = enums.Protocol.TCP) \n
		No command help available \n
			:param protocol: No help available
		"""
		param = Conversions.enum_scalar_to_str(protocol, enums.Protocol)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PROTocol {param}')

	def get_ip_address(self) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:IPADdress \n
		Snippet: value: str = driver.configure.data.measurement.iperf.get_ip_address() \n
		No command help available \n
			:return: ip_address: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:IPADdress?')
		return trim_str_response(response)

	def set_ip_address(self, ip_address: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:IPADdress \n
		Snippet: driver.configure.data.measurement.iperf.set_ip_address(ip_address = '1') \n
		No command help available \n
			:param ip_address: No help available
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:IPADdress {param}')

	def get_bitrate(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:BITRate \n
		Snippet: value: int = driver.configure.data.measurement.iperf.get_bitrate() \n
		No command help available \n
			:return: bitrate: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:BITRate?')
		return Conversions.str_to_int(response)

	def set_bitrate(self, bitrate: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:BITRate \n
		Snippet: driver.configure.data.measurement.iperf.set_bitrate(bitrate = 1) \n
		No command help available \n
			:param bitrate: No help available
		"""
		param = Conversions.decimal_value_to_str(bitrate)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:BITRate {param}')

	def get_pconnection(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PCONnection \n
		Snippet: value: int = driver.configure.data.measurement.iperf.get_pconnection() \n
		No command help available \n
			:return: par_conn: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PCONnection?')
		return Conversions.str_to_int(response)

	def set_pconnection(self, par_conn: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPERf:PCONnection \n
		Snippet: driver.configure.data.measurement.iperf.set_pconnection(par_conn = 1) \n
		No command help available \n
			:param par_conn: No help available
		"""
		param = Conversions.decimal_value_to_str(par_conn)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPERf:PCONnection {param}')

	def clone(self) -> 'Iperf':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iperf(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
