from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Call:
	"""Call commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("call", core, parent)

	# noinspection PyTypeChecker
	def get_state(self) -> enums.CallState:
		"""SCPI: SENSe:DATA:CONTrol:IMS:VOICe:CALL:STATe \n
		Snippet: value: enums.CallState = driver.sense.data.control.ims.voice.call.get_state() \n
		No command help available \n
			:return: call_state: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:VOICe:CALL:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.CallState)
