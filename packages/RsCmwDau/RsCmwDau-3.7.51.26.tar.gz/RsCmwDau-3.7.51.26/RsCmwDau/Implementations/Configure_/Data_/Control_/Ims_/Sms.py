from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Types import DataType
from ......Internal.Utilities import trim_str_response
from ......Internal.ArgSingleList import ArgSingleList
from ......Internal.ArgSingle import ArgSingle
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sms:
	"""Sms commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sms", core, parent)

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.SmsTypeB:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:SMS:TYPE \n
		Snippet: value: enums.SmsTypeB = driver.configure.data.control.ims.sms.get_type_py() \n
		No command help available \n
			:return: sms_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:SMS:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.SmsTypeB)

	def set_type_py(self, sms_type: enums.SmsTypeB) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:SMS:TYPE \n
		Snippet: driver.configure.data.control.ims.sms.set_type_py(sms_type = enums.SmsTypeB.TGP2) \n
		No command help available \n
			:param sms_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(sms_type, enums.SmsTypeB)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:SMS:TYPE {param}')

	def get_text(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:SMS:TEXT \n
		Snippet: value: str = driver.configure.data.control.ims.sms.get_text() \n
		No command help available \n
			:return: sms_text: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IMS:SMS:TEXT?')
		return trim_str_response(response)

	def set_text(self, sms_text: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:SMS:TEXT \n
		Snippet: driver.configure.data.control.ims.sms.set_text(sms_text = '1') \n
		No command help available \n
			:param sms_text: No help available
		"""
		param = Conversions.value_to_quoted_str(sms_text)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:SMS:TEXT {param}')

	def send(self, sms_text: str = None, sms_type: enums.SmsTypeB = None) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS:SMS:SEND \n
		Snippet: driver.configure.data.control.ims.sms.send(sms_text = '1', sms_type = enums.SmsTypeB.TGP2) \n
		No command help available \n
			:param sms_text: No help available
			:param sms_type: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('sms_text', sms_text, DataType.String, True), ArgSingle('sms_type', sms_type, DataType.Enum, True))
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS:SMS:SEND {param}'.rstrip())
