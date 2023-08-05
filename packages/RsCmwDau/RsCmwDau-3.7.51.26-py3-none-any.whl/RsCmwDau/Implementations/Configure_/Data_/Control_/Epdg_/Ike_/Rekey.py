from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rekey:
	"""Rekey commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rekey", core, parent)

	def get_enable(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:REKey:ENABle \n
		Snippet: value: bool = driver.configure.data.control.epdg.ike.rekey.get_enable() \n
		No command help available \n
			:return: rekey_enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:IKE:REKey:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, rekey_enable: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:REKey:ENABle \n
		Snippet: driver.configure.data.control.epdg.ike.rekey.set_enable(rekey_enable = False) \n
		No command help available \n
			:param rekey_enable: No help available
		"""
		param = Conversions.bool_to_str(rekey_enable)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:IKE:REKey:ENABle {param}')

	def get_time(self) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:REKey:TIME \n
		Snippet: value: int = driver.configure.data.control.epdg.ike.rekey.get_time() \n
		No command help available \n
			:return: ikesa_rekeying_time: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:EPDG:IKE:REKey:TIME?')
		return Conversions.str_to_int(response)

	def set_time(self, ikesa_rekeying_time: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:IKE:REKey:TIME \n
		Snippet: driver.configure.data.control.epdg.ike.rekey.set_time(ikesa_rekeying_time = 1) \n
		No command help available \n
			:param ikesa_rekeying_time: No help available
		"""
		param = Conversions.decimal_value_to_str(ikesa_rekeying_time)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:IKE:REKey:TIME {param}')
