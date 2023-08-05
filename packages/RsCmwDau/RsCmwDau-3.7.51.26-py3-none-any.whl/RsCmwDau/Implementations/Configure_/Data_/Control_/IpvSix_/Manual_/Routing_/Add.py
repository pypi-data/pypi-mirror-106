from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("add", core, parent)

	def set(self, prefix: str, router: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IPVSix:MANual:ROUTing:ADD \n
		Snippet: driver.configure.data.control.ipvSix.manual.routing.add.set(prefix = '1', router = '1') \n
		Adds a route to the pool of manual routes for IPv6. If the destination address of a packet matches the <Prefix>, it is
		routed to the <Router>. \n
			:param prefix: String, e.g. 'fcb1:abab:cdcd:efe0::/64', 64-bit prefixes and shorter prefixes allowed
			:param router: Router address as string, e.g. 'fcb1:abcd:17c5:efe0::1'
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('prefix', prefix, DataType.String), ArgSingle('router', router, DataType.String))
		self._core.io.write(f'CONFigure:DATA:CONTrol:IPVSix:MANual:ROUTing:ADD {param}'.rstrip())
