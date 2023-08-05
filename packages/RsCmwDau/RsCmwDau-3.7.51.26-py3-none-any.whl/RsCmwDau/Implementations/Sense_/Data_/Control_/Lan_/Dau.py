from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dau:
	"""Dau commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dau", core, parent)

	# noinspection PyTypeChecker
	def get_status(self) -> enums.DauStatus:
		"""SCPI: SENSe:DATA:CONTrol:LAN:DAU:STATus \n
		Snippet: value: enums.DauStatus = driver.sense.data.control.lan.dau.get_status() \n
		Queries the state of the LAN DAU connector. \n
			:return: status: NOTConn | CONN NOTConn: no external network connected CONN: active external network connected
		"""
		response = self._core.io.query_str('SENSe:DATA:CONTrol:LAN:DAU:STATus?')
		return Conversions.str_to_scalar_enum(response, enums.DauStatus)
