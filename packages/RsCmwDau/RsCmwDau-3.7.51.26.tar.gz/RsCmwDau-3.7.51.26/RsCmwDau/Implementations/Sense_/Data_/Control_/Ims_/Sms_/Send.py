from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Send:
	"""Send commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("send", core, parent)

	# noinspection PyTypeChecker
	def get_status(self) -> enums.SmsStatus:
		"""SCPI: SENSe:DATA:CONTrol:IMS:SMS:SEND:STATus \n
		Snippet: value: enums.SmsStatus = driver.sense.data.control.ims.sms.send.get_status() \n
		No command help available \n
			:return: sms_status: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:SMS:SEND:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.SmsStatus)
