from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pcscf:
	"""Pcscf commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pcscf", core, parent)

	def get_address(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS:INTern:PCSCf:ADDRess \n
		Snippet: value: str = driver.sense.data.control.ims.intern.pcscf.get_address() \n
		No command help available \n
			:return: address: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:INTern:PCSCf:ADDRess?')
		return trim_str_response(response)
