from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Http:
	"""Http commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("http", core, parent)

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Http_.Start import Start
			self._start = Start(self._core, self._base)
		return self._start

	def get_en_connection(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:HTTP:ENConnection \n
		Snippet: value: bool = driver.configure.data.control.http.get_en_connection() \n
		Specifies whether access to the internal web server is allowed from an external network (via LAN DAU) . \n
			:return: ext_net_conn: OFF | ON OFF: not allowed ON: allowed
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:HTTP:ENConnection?')
		return Conversions.str_to_bool(response)

	def set_en_connection(self, ext_net_conn: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:HTTP:ENConnection \n
		Snippet: driver.configure.data.control.http.set_en_connection(ext_net_conn = False) \n
		Specifies whether access to the internal web server is allowed from an external network (via LAN DAU) . \n
			:param ext_net_conn: OFF | ON OFF: not allowed ON: allowed
		"""
		param = Conversions.bool_to_str(ext_net_conn)
		self._core.io.write(f'CONFigure:DATA:CONTrol:HTTP:ENConnection {param}')

	def get_ipv_six(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:HTTP:IPVSix \n
		Snippet: value: bool = driver.configure.data.control.http.get_ipv_six() \n
		Specifies whether the internal web server supports IPv6. \n
			:return: ip_v_6_enable: OFF | ON OFF: IPv4 support only ON: support of IPv4 and IPv6
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:HTTP:IPVSix?')
		return Conversions.str_to_bool(response)

	def set_ipv_six(self, ip_v_6_enable: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:HTTP:IPVSix \n
		Snippet: driver.configure.data.control.http.set_ipv_six(ip_v_6_enable = False) \n
		Specifies whether the internal web server supports IPv6. \n
			:param ip_v_6_enable: OFF | ON OFF: IPv4 support only ON: support of IPv4 and IPv6
		"""
		param = Conversions.bool_to_str(ip_v_6_enable)
		self._core.io.write(f'CONFigure:DATA:CONTrol:HTTP:IPVSix {param}')

	def clone(self) -> 'Http':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Http(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
