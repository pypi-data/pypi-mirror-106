from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Participant:
	"""Participant commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("participant", core, parent)

	def set(self, max_participant: int, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:CONFerence:MAX:PARTicipant \n
		Snippet: driver.configure.data.control.ims.conference.max.participant.set(max_participant = 1, ims = repcap.Ims.Default) \n
		Configures the maximum number of virtual subscribers allowed to participate in a conference call. \n
			:param max_participant: The value 0 means that there is no limit. Range: 0 to 10
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.decimal_value_to_str(max_participant)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:CONFerence:MAX:PARTicipant {param}')

	def get(self, ims=repcap.Ims.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:CONFerence:MAX:PARTicipant \n
		Snippet: value: int = driver.configure.data.control.ims.conference.max.participant.get(ims = repcap.Ims.Default) \n
		Configures the maximum number of virtual subscribers allowed to participate in a conference call. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: max_participant: The value 0 means that there is no limit. Range: 0 to 10"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:CONFerence:MAX:PARTicipant?')
		return Conversions.str_to_int(response)
