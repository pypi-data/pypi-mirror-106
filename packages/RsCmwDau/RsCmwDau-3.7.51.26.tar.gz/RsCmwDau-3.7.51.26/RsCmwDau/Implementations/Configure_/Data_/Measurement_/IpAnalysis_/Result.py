from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 7 total commands, 0 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	def get_ipcs(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:IPCS \n
		Snippet: value: bool = driver.configure.data.measurement.ipAnalysis.result.get_ipcs() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:IPCS?')
		return Conversions.str_to_bool(response)

	def set_ipcs(self, enable: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:IPCS \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_ipcs(enable = False) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:IPCS {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tcp_Analysis: bool: OFF | ON 'TCP Analysis' view OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
			- Ip_Connect: bool: OFF | ON 'IP Connectivity' view
			- Dpcp: bool: OFF | ON 'Data Pie Charts' view
			- Ft_Trigger: bool: OFF | ON 'Flow Throughput and Event Trigger' view
			- Vo_Ims: bool: OFF | ON 'Voice over IMS' view
			- Ipc_Security: bool: OFF | ON 'IP Connection Security' view"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Tcp_Analysis'),
			ArgStruct.scalar_bool('Ip_Connect'),
			ArgStruct.scalar_bool('Dpcp'),
			ArgStruct.scalar_bool('Ft_Trigger'),
			ArgStruct.scalar_bool('Vo_Ims'),
			ArgStruct.scalar_bool('Ipc_Security')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tcp_Analysis: bool = None
			self.Ip_Connect: bool = None
			self.Dpcp: bool = None
			self.Ft_Trigger: bool = None
			self.Vo_Ims: bool = None
			self.Ipc_Security: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.data.measurement.ipAnalysis.result.get_all() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. This command
		combines all other CONFigure:DATA:MEAS<i>:IPANalysis:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult[:ALL] \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_all(value = AllStruct()) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. This command
		combines all other CONFigure:DATA:MEAS<i>:IPANalysis:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:ALL', value)

	def get_tcp_analysis(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:TCPanalysis \n
		Snippet: value: bool = driver.configure.data.measurement.ipAnalysis.result.get_tcp_analysis() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:TCPanalysis?')
		return Conversions.str_to_bool(response)

	def set_tcp_analysis(self, enable: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:TCPanalysis \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_tcp_analysis(enable = False) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:TCPanalysis {param}')

	def get_ip_connect(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:IPConnect \n
		Snippet: value: bool = driver.configure.data.measurement.ipAnalysis.result.get_ip_connect() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:IPConnect?')
		return Conversions.str_to_bool(response)

	def set_ip_connect(self, enable: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:IPConnect \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_ip_connect(enable = False) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:IPConnect {param}')

	def get_dpcp(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:DPCP \n
		Snippet: value: bool = driver.configure.data.measurement.ipAnalysis.result.get_dpcp() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:DPCP?')
		return Conversions.str_to_bool(response)

	def set_dpcp(self, enable: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:DPCP \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_dpcp(enable = False) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:DPCP {param}')

	def get_ft_trigger(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:FTTRigger \n
		Snippet: value: bool = driver.configure.data.measurement.ipAnalysis.result.get_ft_trigger() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:FTTRigger?')
		return Conversions.str_to_bool(response)

	def set_ft_trigger(self, enable: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:FTTRigger \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_ft_trigger(enable = False) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:FTTRigger {param}')

	def get_vo_ims(self) -> bool:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:VOIMs \n
		Snippet: value: bool = driver.configure.data.measurement.ipAnalysis.result.get_vo_ims() \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:return: enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:VOIMs?')
		return Conversions.str_to_bool(response)

	def set_vo_ims(self, enable: bool) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:RESult:VOIMs \n
		Snippet: driver.configure.data.measurement.ipAnalysis.result.set_vo_ims(enable = False) \n
		Enables or disables the display of the individual detailed views and the evaluation of the related results. The mnemonic
		after 'RESult' denotes the view: 'TCP Analysis', 'IP Connectivity', 'Data Pie Charts', 'Voice over IMS', 'IP Connection
		Security' and 'Flow Throughput and Event Trigger'. \n
			:param enable: OFF | ON OFF: Do not evaluate results, hide the view ON: Evaluate results and show the view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:RESult:VOIMs {param}')
