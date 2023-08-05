from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aservices:
	"""Aservices commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aservices", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Aservices_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	def delete(self, name: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:ASERvices:DELete \n
		Snippet: driver.configure.data.control.dns.aservices.delete(name = '1') \n
		Deletes an entry from the database of the local DNS server for type SRV DNS queries. \n
			:param name: String specifying the service name of the entry to be deleted
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:ASERvices:DELete {param}')

	def clone(self) -> 'Aservices':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aservices(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
