from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)

	# noinspection PyTypeChecker
	def get_connections(self) -> enums.FilterConnect:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:FILTer:CONNections \n
		Snippet: value: enums.FilterConnect = driver.configure.data.measurement.ipAnalysis.filterPy.get_connections() \n
		Configures a flow filter criterion for the connection state. \n
			:return: filter_conn: OPEN | CLOSed | BOTH Evaluate only open connections, only closed connections or open and closed connections.
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:FILTer:CONNections?')
		return Conversions.str_to_scalar_enum(response, enums.FilterConnect)

	def set_connections(self, filter_conn: enums.FilterConnect) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:FILTer:CONNections \n
		Snippet: driver.configure.data.measurement.ipAnalysis.filterPy.set_connections(filter_conn = enums.FilterConnect.BOTH) \n
		Configures a flow filter criterion for the connection state. \n
			:param filter_conn: OPEN | CLOSed | BOTH Evaluate only open connections, only closed connections or open and closed connections.
		"""
		param = Conversions.enum_scalar_to_str(filter_conn, enums.FilterConnect)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:FILTer:CONNections {param}')
