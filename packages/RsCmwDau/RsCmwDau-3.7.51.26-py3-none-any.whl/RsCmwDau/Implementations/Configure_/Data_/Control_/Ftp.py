from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ftp:
	"""Ftp commands group definition. 7 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ftp", core, parent)

	@property
	def user(self):
		"""user commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_user'):
			from .Ftp_.User import User
			self._user = User(self._core, self._base)
		return self._user

	# noinspection PyTypeChecker
	def get_stype(self) -> enums.ServiceTypeA:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:STYPe \n
		Snippet: value: enums.ServiceTypeA = driver.configure.data.control.ftp.get_stype() \n
		Selects the FTP service type. The other CONFigure:DATA:CONTrol:FTP:... commands configure the FTP server. They are not
		relevant, if the service type TGENerator is selected. \n
			:return: service_type: SERVer | TGENerator SERVer: an FTP server runs on the R&S CMW TGENerator: the R&S CMW acts as a traffic generator
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:FTP:STYPe?')
		return Conversions.str_to_scalar_enum(response, enums.ServiceTypeA)

	def set_stype(self, service_type: enums.ServiceTypeA) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:STYPe \n
		Snippet: driver.configure.data.control.ftp.set_stype(service_type = enums.ServiceTypeA.SERVer) \n
		Selects the FTP service type. The other CONFigure:DATA:CONTrol:FTP:... commands configure the FTP server. They are not
		relevant, if the service type TGENerator is selected. \n
			:param service_type: SERVer | TGENerator SERVer: an FTP server runs on the R&S CMW TGENerator: the R&S CMW acts as a traffic generator
		"""
		param = Conversions.enum_scalar_to_str(service_type, enums.ServiceTypeA)
		self._core.io.write(f'CONFigure:DATA:CONTrol:FTP:STYPe {param}')

	def get_en_connection(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:ENConnection \n
		Snippet: value: bool = driver.configure.data.control.ftp.get_en_connection() \n
		Specifies whether access to the FTP server is allowed from an external network (via LAN DAU) . \n
			:return: ext_net_conn: OFF | ON OFF: not allowed ON: allowed
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:FTP:ENConnection?')
		return Conversions.str_to_bool(response)

	def set_en_connection(self, ext_net_conn: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:ENConnection \n
		Snippet: driver.configure.data.control.ftp.set_en_connection(ext_net_conn = False) \n
		Specifies whether access to the FTP server is allowed from an external network (via LAN DAU) . \n
			:param ext_net_conn: OFF | ON OFF: not allowed ON: allowed
		"""
		param = Conversions.bool_to_str(ext_net_conn)
		self._core.io.write(f'CONFigure:DATA:CONTrol:FTP:ENConnection {param}')

	def get_auser(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:AUSer \n
		Snippet: value: bool = driver.configure.data.control.ftp.get_auser() \n
		Specifies whether access to the FTP server is allowed for anonymous users. \n
			:return: anonymous: OFF | ON OFF: not allowed ON: allowed
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:FTP:AUSer?')
		return Conversions.str_to_bool(response)

	def set_auser(self, anonymous: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:AUSer \n
		Snippet: driver.configure.data.control.ftp.set_auser(anonymous = False) \n
		Specifies whether access to the FTP server is allowed for anonymous users. \n
			:param anonymous: OFF | ON OFF: not allowed ON: allowed
		"""
		param = Conversions.bool_to_str(anonymous)
		self._core.io.write(f'CONFigure:DATA:CONTrol:FTP:AUSer {param}')

	def get_dupload(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:DUPLoad \n
		Snippet: value: bool = driver.configure.data.control.ftp.get_dupload() \n
		Specifies whether data upload to the FTP server is allowed for anonymous users. \n
			:return: data_upload: OFF | ON OFF: not allowed ON: allowed
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:FTP:DUPLoad?')
		return Conversions.str_to_bool(response)

	def set_dupload(self, data_upload: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:DUPLoad \n
		Snippet: driver.configure.data.control.ftp.set_dupload(data_upload = False) \n
		Specifies whether data upload to the FTP server is allowed for anonymous users. \n
			:param data_upload: OFF | ON OFF: not allowed ON: allowed
		"""
		param = Conversions.bool_to_str(data_upload)
		self._core.io.write(f'CONFigure:DATA:CONTrol:FTP:DUPLoad {param}')

	def get_ipv_six(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:IPVSix \n
		Snippet: value: bool = driver.configure.data.control.ftp.get_ipv_six() \n
		Specifies whether the FTP server supports IPv6. \n
			:return: ip_v_6_enable: OFF | ON OFF: IPv4 support only ON: support of IPv4 and IPv6
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:FTP:IPVSix?')
		return Conversions.str_to_bool(response)

	def set_ipv_six(self, ip_v_6_enable: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:FTP:IPVSix \n
		Snippet: driver.configure.data.control.ftp.set_ipv_six(ip_v_6_enable = False) \n
		Specifies whether the FTP server supports IPv6. \n
			:param ip_v_6_enable: OFF | ON OFF: IPv4 support only ON: support of IPv4 and IPv6
		"""
		param = Conversions.bool_to_str(ip_v_6_enable)
		self._core.io.write(f'CONFigure:DATA:CONTrol:FTP:IPVSix {param}')

	def clone(self) -> 'Ftp':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ftp(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
