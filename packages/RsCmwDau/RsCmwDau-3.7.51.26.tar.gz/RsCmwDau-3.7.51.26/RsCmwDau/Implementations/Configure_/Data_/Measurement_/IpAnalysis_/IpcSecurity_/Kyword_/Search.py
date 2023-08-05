from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Search:
	"""Search commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("search", core, parent)

	def set_import_py(self, filename: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:KYWord:SEARch:IMPort \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.kyword.search.set_import_py(filename = '1') \n
		Imports a list of keywords from a text file. \n
			:param filename: File name as string, including the extension. The file must be available in the directory ip_analysis of the samba share.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:KYWord:SEARch:IMPort {param}')

	def set_add(self, keyword: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:KYWord:SEARch:ADD \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.kyword.search.set_add(keyword = '1') \n
		Adds an entry to the keyword list. \n
			:param keyword: New keyword as string
		"""
		param = Conversions.value_to_quoted_str(keyword)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:KYWord:SEARch:ADD {param}')

	def delete(self, keyword: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:KYWord:SEARch:DELete \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.kyword.search.delete(keyword = '1') \n
		Deletes a selected keyword from the keyword list. \n
			:param keyword: Keyword to be deleted, as string
		"""
		param = Conversions.value_to_quoted_str(keyword)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:KYWord:SEARch:DELete {param}')
