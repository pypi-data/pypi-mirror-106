from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IpLogging:
	"""IpLogging commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ipLogging", core, parent)

	def get_fname(self) -> str:
		"""SCPI: SENSe:DATA:MEASurement<Instance>:IPLogging:FNAMe \n
		Snippet: value: str = driver.sense.data.measurement.ipLogging.get_fname() \n
		Queries the current or next log file name. If IP logging is on, the name of the currently used log file is returned.
		If IP logging is off, the name of the file to be created in the next logging session is returned. \n
			:return: filename: File name as string
		"""
		response = self._core.io.query_str('SENSe:DATA:MEASurement<MeasInstance>:IPLogging:FNAMe?')
		return trim_str_response(response)
