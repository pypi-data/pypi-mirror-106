from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RemoveList:
	"""RemoveList commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("removeList", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:REMovelist \n
		Snippet: driver.configure.data.measurement.ipReplay.removeList.set() \n
		Removes all files from the playlist (measurement must be OFF) . \n
		"""
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:REMovelist')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPReplay:REMovelist \n
		Snippet: driver.configure.data.measurement.ipReplay.removeList.set_with_opc() \n
		Removes all files from the playlist (measurement must be OFF) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:DATA:MEASurement<MeasInstance>:IPReplay:REMovelist')
