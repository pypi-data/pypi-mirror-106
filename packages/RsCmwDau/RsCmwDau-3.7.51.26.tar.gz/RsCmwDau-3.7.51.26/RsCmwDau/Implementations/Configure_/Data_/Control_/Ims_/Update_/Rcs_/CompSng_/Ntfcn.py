from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ntfcn:
	"""Ntfcn commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ntfcn", core, parent)

	def set(self, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:RCS:COMPsng:NTFCn \n
		Snippet: driver.configure.data.control.ims.update.rcs.compSng.ntfcn.set(ims = repcap.Ims.Default) \n
		Send an 'active' notification to the DUT as 'isComposing' status message. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:RCS:COMPsng:NTFCn')

	def set_with_opc(self, ims=repcap.Ims.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:RCS:COMPsng:NTFCn \n
		Snippet: driver.configure.data.control.ims.update.rcs.compSng.ntfcn.set_with_opc(ims = repcap.Ims.Default) \n
		Send an 'active' notification to the DUT as 'isComposing' status message. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:RCS:COMPsng:NTFCn')
