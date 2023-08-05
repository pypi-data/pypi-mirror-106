from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Supl:
	"""Supl commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("supl", core, parent)

	def set_transmit(self, message: bytes) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:SUPL:TRANsmit \n
		Snippet: driver.configure.data.control.supl.set_transmit(message = b'ABCDEFGH') \n
		No command help available \n
			:param message: No help available
		"""
		self._core.io.write_bin_block('CONFigure:DATA:CONTrol:SUPL:TRANsmit ', message)
