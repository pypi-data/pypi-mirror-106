from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uid:
	"""Uid commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("uid", core, parent)

	def get_private(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS:MOBile:UID:PRIVate \n
		Snippet: value: str = driver.sense.data.control.ims.mobile.uid.get_private() \n
		No command help available \n
			:return: priv_user_id: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:MOBile:UID:PRIVate?')
		return trim_str_response(response)

	def get_public(self) -> str:
		"""SCPI: SENSe:DATA:CONTrol:IMS:MOBile:UID:PUBLic \n
		Snippet: value: str = driver.sense.data.control.ims.mobile.uid.get_public() \n
		No command help available \n
			:return: publ_user_id: No help available
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:IMS:MOBile:UID:PUBLic?')
		return trim_str_response(response)
