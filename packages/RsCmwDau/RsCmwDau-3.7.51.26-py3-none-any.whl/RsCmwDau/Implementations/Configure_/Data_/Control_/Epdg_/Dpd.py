from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpd:
	"""Dpd commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dpd", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:DPD:ENABle \n
		Snippet: value: bool = driver.configure.data.control.epdg.dpd.get_enable() \n
		Enables dead peer detection. \n
			:return: dpd_enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:DPD:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, dpd_enable: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:DPD:ENABle \n
		Snippet: driver.configure.data.control.epdg.dpd.set_enable(dpd_enable = False) \n
		Enables dead peer detection. \n
			:param dpd_enable: OFF | ON
		"""
		param = Conversions.bool_to_str(dpd_enable)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:DPD:ENABle {param}')

	def get_interval(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:DPD:INTerval \n
		Snippet: value: int = driver.configure.data.control.epdg.dpd.get_interval() \n
		Configures the inactivity time interval for dead peer detection. \n
			:return: dpd_interval: Range: 1 s to 100 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:DPD:INTerval?')
		return Conversions.str_to_int(response)

	def set_interval(self, dpd_interval: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:DPD:INTerval \n
		Snippet: driver.configure.data.control.epdg.dpd.set_interval(dpd_interval = 1) \n
		Configures the inactivity time interval for dead peer detection. \n
			:param dpd_interval: Range: 1 s to 100 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(dpd_interval)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:DPD:INTerval {param}')

	def get_timeout(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:DPD:TIMeout \n
		Snippet: value: int = driver.configure.data.control.epdg.dpd.get_timeout() \n
		Configures the no answer timeout for dead peer detection. \n
			:return: dpd_timeout: Range: 1 s to 10E+3 s, Unit: s
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:DPD:TIMeout?')
		return Conversions.str_to_int(response)

	def set_timeout(self, dpd_timeout: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:DPD:TIMeout \n
		Snippet: driver.configure.data.control.epdg.dpd.set_timeout(dpd_timeout = 1) \n
		Configures the no answer timeout for dead peer detection. \n
			:param dpd_timeout: Range: 1 s to 10E+3 s, Unit: s
		"""
		param = Conversions.decimal_value_to_str(dpd_timeout)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:DPD:TIMeout {param}')
