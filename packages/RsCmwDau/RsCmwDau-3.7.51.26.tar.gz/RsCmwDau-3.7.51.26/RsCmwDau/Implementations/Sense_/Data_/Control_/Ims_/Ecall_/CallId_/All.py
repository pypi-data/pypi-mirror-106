from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("all", core, parent)

	def get(self, ims=repcap.Ims.Default) -> List[str]:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:ECALl:CALLid:ALL \n
		Snippet: value: List[str] = driver.sense.data.control.ims.ecall.callId.all.get(ims = repcap.Ims.Default) \n
		No command help available \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: nge_call_ids: No help available"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:ECALl:CALLid:ALL?')
		return Conversions.str_to_str_list(response)
