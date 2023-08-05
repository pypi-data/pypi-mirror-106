from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Info:
	"""Info commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("info", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:CLEan:GENeral:INFO \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.clean.general.info.set() \n
		Clears the event log. \n
		"""
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:CLEan:GENeral:INFO')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:IPCSecurity:PRTScan:CLEan:GENeral:INFO \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ipcSecurity.prtScan.clean.general.info.set_with_opc() \n
		Clears the event log. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:IPCSecurity:PRTScan:CLEan:GENeral:INFO')
