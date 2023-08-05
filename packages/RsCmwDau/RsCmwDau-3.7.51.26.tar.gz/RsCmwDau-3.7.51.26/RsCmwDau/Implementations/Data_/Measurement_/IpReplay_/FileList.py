from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FileList:
	"""FileList commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fileList", core, parent)

	def fetch(self) -> List[str]:
		"""SCPI: FETCh:DATA:MEASurement<Instance>:IPReplay:FILelist \n
		Snippet: value: List[str] = driver.data.measurement.ipReplay.fileList.fetch() \n
		Queries a list of all files in the directory ip_replay of the samba share. \n
			:return: files: Comma-separated list of strings, one string per filename"""
		response = self._core.io.query_str(f'FETCh:DATA:MEASurement<MeasInstance>:IPReplay:FILelist?')
		return Conversions.str_to_str_list(response)
