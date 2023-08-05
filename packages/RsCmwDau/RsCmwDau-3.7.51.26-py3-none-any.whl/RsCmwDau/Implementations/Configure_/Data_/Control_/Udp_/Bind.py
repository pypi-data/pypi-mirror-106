from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bind:
	"""Bind commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bind", core, parent)

	def set(self, ip_address: str, port: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:UDP:BIND \n
		Snippet: driver.configure.data.control.udp.bind.set(ip_address = '1', port = 1) \n
		No command help available \n
			:param ip_address: No help available
			:param port: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ip_address', ip_address, DataType.String), ArgSingle('port', port, DataType.Integer))
		self._core.io.write(f'CONFigure:DATA:CONTrol:UDP:BIND {param}'.rstrip())
