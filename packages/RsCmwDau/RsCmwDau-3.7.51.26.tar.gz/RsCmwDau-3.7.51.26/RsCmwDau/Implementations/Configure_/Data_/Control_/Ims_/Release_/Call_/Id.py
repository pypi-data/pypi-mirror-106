from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("id", core, parent)

	def set(self, idn: str, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:RELease:CALL:ID \n
		Snippet: driver.configure.data.control.ims.release.call.id.set(idn = '1', ims = repcap.Ims.Default) \n
		Queries a list of call IDs or releases a call selected via its ID. \n
			:param idn: ID as string, selecting the call to be released
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.value_to_quoted_str(idn)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:RELease:CALL:ID {param}')

	def get(self, ims=repcap.Ims.Default) -> List[str]:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:RELease:CALL:ID \n
		Snippet: value: List[str] = driver.configure.data.control.ims.release.call.id.get(ims = repcap.Ims.Default) \n
		Queries a list of call IDs or releases a call selected via its ID. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: ids: Comma-separated list of ID strings, one string per established call"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:RELease:CALL:ID?')
		return Conversions.str_to_str_list(response)
