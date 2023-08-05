from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ExportDb:
	"""ExportDb commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("exportDb", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:EXPortdb \n
		Snippet: driver.configure.data.measurement.ipAnalysis.exportDb.set() \n
		Stores the IP analysis result database to a JSON file on the DAU system drive. \n
		"""
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:EXPortdb')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:EXPortdb \n
		Snippet: driver.configure.data.measurement.ipAnalysis.exportDb.set_with_opc() \n
		Stores the IP analysis result database to a JSON file on the DAU system drive. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:EXPortdb')
