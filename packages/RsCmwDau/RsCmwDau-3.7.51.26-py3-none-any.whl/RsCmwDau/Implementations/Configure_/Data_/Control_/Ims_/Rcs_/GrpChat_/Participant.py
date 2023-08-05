from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Participant:
	"""Participant commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("participant", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Participant_.Add import Add
			self._add = Add(self._core, self._base)
		return self._add

	def delete(self, participant: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:RCS:GRPChat:PARTicipant:DELete \n
		Snippet: driver.configure.data.control.ims.rcs.grpChat.participant.delete(participant = '1', ims = repcap.Ims.Default) \n
		Removes an entry from the list of participants for group chats. \n
			:param participant: String to be removed
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(participant)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:RCS:GRPChat:PARTicipant:DELete {param}')

	def clone(self) -> 'Participant':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Participant(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
