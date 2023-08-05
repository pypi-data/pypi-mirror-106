from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	def get(self, ims=repcap.Ims.Default) -> List[str]:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:RCS:PARTicipant:LIST \n
		Snippet: value: List[str] = driver.sense.data.control.ims.rcs.participant.listPy.get(ims = repcap.Ims.Default) \n
		Queries the list of participants for group chats. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: list_py: Comma-separated list of strings, one string per participant"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:RCS:PARTicipant:LIST?')
		return Conversions.str_to_str_list(response)
