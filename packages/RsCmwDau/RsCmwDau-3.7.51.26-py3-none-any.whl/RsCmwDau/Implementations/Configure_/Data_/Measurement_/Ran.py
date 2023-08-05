from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ran:
	"""Ran commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ran", core, parent)

	def get_cataloge(self) -> List[str]:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:RAN:CATaloge \n
		Snippet: value: List[str] = driver.configure.data.measurement.ran.get_cataloge() \n
		Lists all available signaling applications. You can use the returned strings in other commands to select a RAN. \n
			:return: ran: Comma-separated list of all supported values. Each value is represented as a string.
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:RAN:CATaloge?')
		return Conversions.str_to_str_list(response)

	def get_value(self) -> str:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:RAN \n
		Snippet: value: str = driver.configure.data.measurement.ran.get_value() \n
		Selects an installed signaling application instance. You can query a complete list of all supported strings via the
		command method RsCmwDau.Configure.Data.Measurement.Ran.cataloge. \n
			:return: ran: String parameter, selecting a signaling application instance
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:RAN?')
		return trim_str_response(response)

	def set_value(self, ran: str) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:RAN \n
		Snippet: driver.configure.data.measurement.ran.set_value(ran = '1') \n
		Selects an installed signaling application instance. You can query a complete list of all supported strings via the
		command method RsCmwDau.Configure.Data.Measurement.Ran.cataloge. \n
			:param ran: String parameter, selecting a signaling application instance
		"""
		param = Conversions.value_to_quoted_str(ran)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:RAN {param}')
