from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Local:
	"""Local commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("local", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Local_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	def delete(self, url_or_ip: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:LOCal:DELete \n
		Snippet: driver.configure.data.control.dns.local.delete(url_or_ip = '1') \n
		Deletes an entry from the database of the local DNS server for type A or type AAAA DNS queries. Each entry consists of
		two strings, one specifying a domain and the other indicating the assigned IP address. Enter one of these strings to
		select the entry to be deleted. \n
			:param url_or_ip: String selecting the entry to be deleted
		"""
		param = Conversions.value_to_quoted_str(url_or_ip)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:LOCal:DELete {param}')

	def clone(self) -> 'Local':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Local(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
