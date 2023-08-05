from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Udp:
	"""Udp commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("udp", core, parent)

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_test'):
			from .Udp_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	@property
	def bind(self):
		"""bind commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bind'):
			from .Udp_.Bind import Bind
			self._bind = Bind(self._core, self._base)
		return self._bind

	def close(self, ip_address: str, port: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:UDP:CLOSe \n
		Snippet: driver.configure.data.control.udp.close(ip_address = '1', port = 1) \n
		No command help available \n
			:param ip_address: No help available
			:param port: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('ip_address', ip_address, DataType.String), ArgSingle('port', port, DataType.Integer))
		self._core.io.write(f'CONFigure:DATA:CONTrol:UDP:CLOSe {param}'.rstrip())

	def clone(self) -> 'Udp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Udp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
