from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Routing:
	"""Routing commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("routing", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Routing_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	def delete(self, prefix: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:MANual:ROUTing:DELete \n
		Snippet: driver.configure.data.control.ipvSix.manual.routing.delete(prefix = 1) \n
		Deletes an entry from the pool of manual routes for IPv6. \n
			:param prefix: Entry to be deleted, either identified via its index number or its prefix string Range: 0 to total number of entries - 1 | 'prefix'
		"""
		param = Conversions.decimal_value_to_str(prefix)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:MANual:ROUTing:DELete {param}')

	def clone(self) -> 'Routing':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Routing(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
