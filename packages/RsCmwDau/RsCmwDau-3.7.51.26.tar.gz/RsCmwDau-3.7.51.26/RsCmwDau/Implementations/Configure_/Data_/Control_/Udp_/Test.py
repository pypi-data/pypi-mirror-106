from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("test", core, parent)

	def set(self, src_port: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:UDP:TEST \n
		Snippet: driver.configure.data.control.udp.test.set(src_port = 1) \n
		No command help available \n
			:param src_port: No help available
		"""
		param = Conversions.decimal_value_to_str(src_port)
		self._core.io.write(f'CONFigure:DATA:CONTrol:UDP:TEST {param}')

	def get(self) -> List[int]:
		"""SCPI: CONFigure:DATA:CONTrol:UDP:TEST \n
		Snippet: value: List[int] = driver.configure.data.control.udp.test.get() \n
		No command help available \n
			:return: result: No help available"""
		response = self._core.io.query_bin_or_ascii_int_list(f'CONFigure:DATA:CONTrol:UDP:TEST?')
		return response
