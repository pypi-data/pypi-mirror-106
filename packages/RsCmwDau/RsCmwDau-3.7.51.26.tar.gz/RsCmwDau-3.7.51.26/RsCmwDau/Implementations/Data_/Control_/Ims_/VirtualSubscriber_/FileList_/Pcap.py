from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcap:
	"""Pcap commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcap", core, parent)

	def fetch(self, ims=repcap.Ims.Default) -> List[str]:
		"""SCPI: FETCh:DATA:CONTrol:IMS<Suffix>:VIRTualsub:FILelist:PCAP \n
		Snippet: value: List[str] = driver.data.control.ims.virtualSubscriber.fileList.pcap.fetch(ims = repcap.Ims.Default) \n
		No command help available \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: files: No help available"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'FETCh:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub:FILelist:PCAP?')
		return Conversions.str_to_str_list(response)
