from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Advanced:
	"""Advanced commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("advanced", core, parent)

	def get_ip_buffering(self) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:ADVanced:IPBuffering \n
		Snippet: value: bool = driver.configure.data.control.advanced.get_ip_buffering() \n
		No command help available \n
			:return: buffering_cnfg: No help available
		"""
		response = self._core.io.query_str('CONFigure:DATA:CONTrol:ADVanced:IPBuffering?')
		return Conversions.str_to_bool(response)

	def set_ip_buffering(self, buffering_cnfg: bool) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:ADVanced:IPBuffering \n
		Snippet: driver.configure.data.control.advanced.set_ip_buffering(buffering_cnfg = False) \n
		No command help available \n
			:param buffering_cnfg: No help available
		"""
		param = Conversions.bool_to_str(buffering_cnfg)
		self._core.io.write(f'CONFigure:DATA:CONTrol:ADVanced:IPBuffering {param}')
