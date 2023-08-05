from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	def get(self, ims=repcap.Ims.Default) -> List[str]:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:RELease:LIST \n
		Snippet: value: List[str] = driver.sense.data.control.ims.release.listPy.get(ims = repcap.Ims.Default) \n
		Queries the IDs of all established calls. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: ids: Comma-separated list of ID strings, one string per established call"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:RELease:LIST?')
		return Conversions.str_to_str_list(response)
