from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Types import DataType
from .....Internal.ArgSingleList import ArgSingleList
from .....Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Deploy:
	"""Deploy commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("deploy", core, parent)

	def set(self, app_name: str, hash_py: str, bin_fil_name: str) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:DEPLoy \n
		Snippet: driver.configure.data.control.deploy.set(app_name = '1', hash_py = r1, bin_fil_name = '1') \n
		No command help available \n
			:param app_name: No help available
			:param hash_py: No help available
			:param bin_fil_name: No help available
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('app_name', app_name, DataType.String), ArgSingle('hash_py', hash_py, DataType.RawString), ArgSingle('bin_fil_name', bin_fil_name, DataType.String))
		self._core.io.write(f'CONFigure:DATA:CONTrol:DEPLoy {param}'.rstrip())
