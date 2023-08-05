from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("add", core, parent)

	def set(self, url: str, ip: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:LOCal:ADD \n
		Snippet: driver.configure.data.control.dns.local.add.set(url = '1', ip = '1') \n
		Adds an entry to the database of the local DNS server for type A or type AAAA DNS queries. Each entry consists of two
		strings, one specifying a domain and the other indicating the assigned IP address. \n
			:param url: String specifying the URL of a domain, e.g. 'www.example.com'
			:param ip: Assigned IPv4 address or IPv6 address as string, e.g. '192.168.168.170' or 'fcb1:abab:1::1'
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('url', url, DataType.String), ArgSingle('ip', ip, DataType.String))
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:LOCal:ADD {param}'.rstrip())
