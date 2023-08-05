from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("test", core, parent)

	# noinspection PyTypeChecker
	class ResultsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- V_4_Savailable: enums.TestResult: NONE | SUCCeded | FAILed Indicates whether the server was reachable via its IPv4 address
			- V_4_Ares_Rec: enums.TestResult: NONE | SUCCeded | FAILed Indicates whether a query type A, sent to the IPv4 address was successful
			- V_44_Ar_Es_Rec: enums.TestResult: NONE | SUCCeded | FAILed Indicates whether a query type AAAA, sent to the IPv4 address was successful
			- V_6_Savailable: enums.TestResult: NONE | SUCCeded | FAILed Indicates whether the server was reachable via its IPv6 address
			- V_6_Ares_Rec: enums.TestResult: NONE | SUCCeded | FAILed Indicates whether a query type A, sent to the IPv6 address was successful
			- V_64_Ares_Rec: enums.TestResult: NONE | SUCCeded | FAILed Indicates whether a query type AAAA, sent to the IPv6 address was successful"""
		__meta_args_list = [
			ArgStruct.scalar_enum('V_4_Savailable', enums.TestResult),
			ArgStruct.scalar_enum('V_4_Ares_Rec', enums.TestResult),
			ArgStruct.scalar_enum('V_44_Ar_Es_Rec', enums.TestResult),
			ArgStruct.scalar_enum('V_6_Savailable', enums.TestResult),
			ArgStruct.scalar_enum('V_6_Ares_Rec', enums.TestResult),
			ArgStruct.scalar_enum('V_64_Ares_Rec', enums.TestResult)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.V_4_Savailable: enums.TestResult = None
			self.V_4_Ares_Rec: enums.TestResult = None
			self.V_44_Ar_Es_Rec: enums.TestResult = None
			self.V_6_Savailable: enums.TestResult = None
			self.V_6_Ares_Rec: enums.TestResult = None
			self.V_64_Ares_Rec: enums.TestResult = None

	# noinspection PyTypeChecker
	def get_results(self) -> ResultsStruct:
		"""SCPI: SENSe:DATA:CONTrol:DNS:TEST:RESults \n
		Snippet: value: ResultsStruct = driver.sense.data.control.dns.test.get_results() \n
		Queries the results of a foreign DNS server test. NONE indicates that no result is available (e.g. no test started yet) .
		'Successful query' means that the domain could be resolved and the DNS server has returned an IP address. \n
			:return: structure: for return value, see the help for ResultsStruct structure arguments.
		"""
		return self._core.io.query_struct('SENSe:DATA:CONTrol:DNS:TEST:RESults?', self.__class__.ResultsStruct())
