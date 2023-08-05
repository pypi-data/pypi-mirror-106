from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("add", core, parent)

	def set(self, participant: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:RCS:GRPChat:PARTicipant:ADD \n
		Snippet: driver.configure.data.control.ims.rcs.grpChat.participant.add.set(participant = '1', ims = repcap.Ims.Default) \n
		Adds an entry to the list of participants for group chats. \n
			:param participant: String to be added
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(participant)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:RCS:GRPChat:PARTicipant:ADD {param}')
