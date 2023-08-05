from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("add", core, parent)

	def set(self, name: str, url: str, protocol: enums.Protocol, port: int) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DNS:ASERvices:ADD \n
		Snippet: driver.configure.data.control.dns.aservices.add.set(name = '1', url = '1', protocol = enums.Protocol.TCP, port = 1) \n
		Adds an entry to the database of the local DNS server for type SRV DNS queries. \n
			:param name: String specifying the service name, e.g. 'pcscf'
			:param url: String specifying the URL of the domain, e.g. 'www.example.com'
			:param protocol: UDP | TCP
			:param port: Range: 0 to 65654
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('name', name, DataType.String), ArgSingle('url', url, DataType.String), ArgSingle('protocol', protocol, DataType.Enum), ArgSingle('port', port, DataType.Integer))
		self._core.io.write(f'CONFigure:DATA:CONTrol:DNS:ASERvices:ADD {param}'.rstrip())
