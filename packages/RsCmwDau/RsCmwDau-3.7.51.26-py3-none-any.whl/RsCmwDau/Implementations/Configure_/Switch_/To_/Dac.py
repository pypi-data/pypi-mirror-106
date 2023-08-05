from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dac:
	"""Dac commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dac", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:SWITch:TO:DAC \n
		Snippet: driver.configure.switch.to.dac.set() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:SWITch:TO:DAC')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:SWITch:TO:DAC \n
		Snippet: driver.configure.switch.to.dac.set_with_opc() \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:SWITch:TO:DAC')
