from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Adelay:
	"""Adelay commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("adelay", core, parent)

	def get_samples(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:ADELay:SAMPles \n
		Snippet: value: int = driver.configure.data.measurement.adelay.get_samples() \n
		Queries the fixed duration of a measurement interval. \n
			:return: interval: Range: 1 s , Unit: s
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:ADELay:SAMPles?')
		return Conversions.str_to_int(response)

	def get_sp_interval(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:ADELay:SPINterval \n
		Snippet: value: int = driver.configure.data.measurement.adelay.get_sp_interval() \n
		Queries the fixed number of measurement samples per interval. \n
			:return: smpl_per_interval: Range: 50
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:ADELay:SPINterval?')
		return Conversions.str_to_int(response)

	def get_msamples(self) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:ADELay:MSAMples \n
		Snippet: value: int = driver.configure.data.measurement.adelay.get_msamples() \n
		Configures the maximum number of samples that can be displayed in the result diagrams. The traces cover the sample range
		-<MaxSamples> + 1 to 0. \n
			:return: max_samples: Range: 1500 to 6000
		"""
		response = self._core.io.query_str('CONFigure:DATA:MEASurement<MeasInstance>:ADELay:MSAMples?')
		return Conversions.str_to_int(response)

	def set_msamples(self, max_samples: int) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:ADELay:MSAMples \n
		Snippet: driver.configure.data.measurement.adelay.set_msamples(max_samples = 1) \n
		Configures the maximum number of samples that can be displayed in the result diagrams. The traces cover the sample range
		-<MaxSamples> + 1 to 0. \n
			:param max_samples: Range: 1500 to 6000
		"""
		param = Conversions.decimal_value_to_str(max_samples)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:ADELay:MSAMples {param}')
