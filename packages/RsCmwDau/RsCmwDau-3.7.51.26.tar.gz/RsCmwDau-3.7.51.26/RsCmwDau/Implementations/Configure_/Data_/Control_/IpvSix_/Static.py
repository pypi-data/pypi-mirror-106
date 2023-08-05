from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Static:
	"""Static commands group definition. 4 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("static", core, parent)

	@property
	def prefixes(self):
		"""prefixes commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_prefixes'):
			from .Static_.Prefixes import Prefixes
			self._prefixes = Prefixes(self._core, self._base)
		return self._prefixes

	def get_address(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:STATic:ADDRess \n
		Snippet: value: str = driver.configure.data.control.ipvSix.static.get_address() \n
		Sets the IP address of the DAU to be used for static IPv6 configuration. \n
			:return: ip_address: IPv6 address as string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVSix:STATic:ADDRess?')
		return trim_str_response(response)

	def set_address(self, ip_address: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:STATic:ADDRess \n
		Snippet: driver.configure.data.control.ipvSix.static.set_address(ip_address = '1') \n
		Sets the IP address of the DAU to be used for static IPv6 configuration. \n
			:param ip_address: IPv6 address as string
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:STATic:ADDRess {param}')

	def get_drouter(self) -> str:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:STATic:DROuter \n
		Snippet: value: str = driver.configure.data.control.ipvSix.static.get_drouter() \n
		Sets the IP address of the external default router to be used for static IPv6 configuration. \n
			:return: router: IPv6 address as string
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:IPVSix:STATic:DROuter?')
		return trim_str_response(response)

	def set_drouter(self, router: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:STATic:DROuter \n
		Snippet: driver.configure.data.control.ipvSix.static.set_drouter(router = '1') \n
		Sets the IP address of the external default router to be used for static IPv6 configuration. \n
			:param router: IPv6 address as string
		"""
		param = Conversions.value_to_quoted_str(router)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:STATic:DROuter {param}')

	def clone(self) -> 'Static':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Static(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
