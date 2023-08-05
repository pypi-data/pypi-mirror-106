from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	def get(self, ims=repcap.Ims.Default) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS<Suffix>:SUBScriber:CATalog \n
		Snippet: value: str = driver.sense.data.control.ims.subscriber.catalog.get(ims = repcap.Ims.Default) \n
		Queries a list of all subscriber profile names. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: catalog: String listing all profile names, separated by commas String example: 'Subscriber 1,Subscriber 2'"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'SENSe:DATA:CONTrol:IMS{ims_cmd_val}:SUBScriber:CATalog?')
		return trim_str_response(response)
