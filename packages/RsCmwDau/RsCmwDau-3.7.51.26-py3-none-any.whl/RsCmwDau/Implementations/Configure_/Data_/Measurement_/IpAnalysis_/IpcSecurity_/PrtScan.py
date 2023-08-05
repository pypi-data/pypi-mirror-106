from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PrtScan:
	"""PrtScan commands group definition. 7 total commands, 2 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prtScan", core, parent)

	@property
	def clean(self):
		"""clean commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clean'):
			from .PrtScan_.Clean import Clean
			self._clean = Clean(self._core, self._base)
		return self._clean

	@property
	def layer(self):
		"""layer commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_layer'):
			from .PrtScan_.Layer import Layer
			self._layer = Layer(self._core, self._base)
		return self._layer

	def get_timeout(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:TIMeout \n
		Snippet: value: int = driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.get_timeout() \n
		Configures a timeout in milliseconds, for waiting for an answer from the DUT during the port scan. \n
			:return: timeout: Range: 0 to 5000
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:TIMeout?')
		return Conversions.str_to_int(response)

	def set_timeout(self, timeout: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:TIMeout \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.set_timeout(timeout = 1) \n
		Configures a timeout in milliseconds, for waiting for an answer from the DUT during the port scan. \n
			:param timeout: Range: 0 to 5000
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:TIMeout {param}')

	def stop(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:STOP \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.stop() \n
		Aborts a port scan. \n
		"""
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:STOP')

	def stop_with_opc(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:STOP \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.stop_with_opc() \n
		Aborts a port scan. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:STOP')

	# noinspection PyTypeChecker
	class RangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Range_From: int: Lower end of the range Range: 0 to 65.535E+3
			- Range_To: int: Upper end of the range Range: 0 to 65.535E+3"""
		__meta_args_list = [
			ArgStruct.scalar_int('Range_From'),
			ArgStruct.scalar_int('Range_To')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Range_From: int = None
			self.Range_To: int = None

	def get_range(self) -> RangeStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:RANGe \n
		Snippet: value: RangeStruct = driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.get_range() \n
		Defines the port range to be scanned. \n
			:return: structure: for return value, see the help for RangeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:RANGe?', self.__class__.RangeStruct())

	def set_range(self, value: RangeStruct) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:RANGe \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.set_range(value = RangeStruct()) \n
		Defines the port range to be scanned. \n
			:param value: see the help for RangeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:RANGe', value)

	def get_dest_ip(self) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:DESTip \n
		Snippet: value: str = driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.get_dest_ip() \n
		Configures the IP address of the destination to be scanned. \n
			:return: dst_ip: String containing the IP address
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:DESTip?')
		return trim_str_response(response)

	def set_dest_ip(self, dst_ip: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:DESTip \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.set_dest_ip(dst_ip = '1') \n
		Configures the IP address of the destination to be scanned. \n
			:param dst_ip: String containing the IP address
		"""
		param = Conversions.value_to_quoted_str(dst_ip)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:DESTip {param}')

	def start(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:STARt \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.start() \n
		Initiates a port scan. \n
		"""
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:STARt')

	def start_with_opc(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:STARt \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.start_with_opc() \n
		Initiates a port scan. \n
		Same as start, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:STARt')

	def clone(self) -> 'PrtScan':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PrtScan(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
