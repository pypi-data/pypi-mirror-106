from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class File:
	"""File commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("file", core, parent)

	def get_path(self) -> str:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:EXPort:FILE:PATH \n
		Snippet: value: str = driver.sense.data.measurement.ipAnalysis.export.file.get_path() \n
		Queries the path and name of the JSON file used for export of the IP analysis result database. \n
			:return: path: Path and file name as string
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:EXPort:FILE:PATH?')
		return trim_str_response(response)
