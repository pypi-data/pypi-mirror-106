from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factory:
	"""Factory commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("factory", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Factory_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	def delete(self, factory: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:CONFerence:FACTory:DELete \n
		Snippet: driver.configure.data.control.ims.conference.factory.delete(factory = '1', ims = repcap.Ims.Default) \n
		Deletes an entry of the factory list (list of reachable conference server addresses) . \n
			:param factory: Conference server address to be deleted, as string
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(factory)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:CONFerence:FACTory:DELete {param}')

	def clone(self) -> 'Factory':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Factory(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
