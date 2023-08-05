from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Start:
	"""Start commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("start", core, parent)

	def get_indexing(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:HTTP:STARt:INDexing \n
		Snippet: value: bool = driver.configure.data.control.http.start.get_indexing() \n
		No command help available \n
			:return: index_trigger: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:HTTP:STARt:INDexing?')
		return Conversions.str_to_bool(response)

	def set_indexing(self, index_trigger: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:HTTP:STARt:INDexing \n
		Snippet: driver.configure.data.control.http.start.set_indexing(index_trigger = False) \n
		No command help available \n
			:param index_trigger: No help available
		"""
		param = Conversions.bool_to_str(index_trigger)
		self._core.io.write(f'CONFigure:DATA:CONTrol:HTTP:STARt:INDexing {param}')
