from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Search:
	"""Search commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("search", core, parent)

	def get_list_py(self) -> List[str]:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:KYWord:SEARch:LIST \n
		Snippet: value: List[str] = driver.sense.data.measurement.ipAnalysis.ipcSecurity.kyword.search.get_list_py() \n
		Queries the keyword list. \n
			:return: list_py: Comma-separated list of strings, one string per keyword
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:KYWord:SEARch:LIST?')
		return Conversions.str_to_str_list(response)
