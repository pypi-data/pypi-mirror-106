from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dns:
	"""Dns commands group definition. 18 total commands, 6 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dns", core, parent)

	@property
	def primary(self):
		"""primary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_primary'):
			from .Dns_.Primary import Primary
			self._primary = Primary(self._core, self._base)
		return self._primary

	@property
	def secondary(self):
		"""secondary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_secondary'):
			from .Dns_.Secondary import Secondary
			self._secondary = Secondary(self._core, self._base)
		return self._secondary

	@property
	def foreign(self):
		"""foreign commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_foreign'):
			from .Dns_.Foreign import Foreign
			self._foreign = Foreign(self._core, self._base)
		return self._foreign

	@property
	def local(self):
		"""local commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_local'):
			from .Dns_.Local import Local
			self._local = Local(self._core, self._base)
		return self._local

	@property
	def aservices(self):
		"""aservices commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_aservices'):
			from .Dns_.Aservices import Aservices
			self._aservices = Aservices(self._core, self._base)
		return self._aservices

	@property
	def test(self):
		"""test commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_test'):
			from .Dns_.Test import Test
			self._test = Test(self._core, self._base)
		return self._test

	def get_res_all_query(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:RESallquery \n
		Snippet: value: bool = driver.configure.data.control.dns.get_res_all_query() \n
		Configures the response of the internal DNS server, if no matching database entry is found for a DNS query of type A or
		AAAA. \n
			:return: dns_resolve_all: OFF | ON OFF: Return no IP address ON: Return the DAU IP address
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:DNS:RESallquery?')
		return Conversions.str_to_bool(response)

	def set_res_all_query(self, dns_resolve_all: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:RESallquery \n
		Snippet: driver.configure.data.control.dns.set_res_all_query(dns_resolve_all = False) \n
		Configures the response of the internal DNS server, if no matching database entry is found for a DNS query of type A or
		AAAA. \n
			:param dns_resolve_all: OFF | ON OFF: Return no IP address ON: Return the DAU IP address
		"""
		param = Conversions.bool_to_str(dns_resolve_all)
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:RESallquery {param}')

	def clone(self) -> 'Dns':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dns(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
