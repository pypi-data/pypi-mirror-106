from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("add", core, parent)

	def set(self, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf:ADD \n
		Snippet: driver.configure.data.control.ims.pcscf.add.set(ims = repcap.Ims.Default) \n
		Creates a P-CSCF profile. See also method RsCmwDau.Configure.Data.Control.Ims.Pcscf.Create.set \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf:ADD')

	def set_with_opc(self, ims=repcap.Ims.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf:ADD \n
		Snippet: driver.configure.data.control.ims.pcscf.add.set_with_opc(ims = repcap.Ims.Default) \n
		Creates a P-CSCF profile. See also method RsCmwDau.Configure.Data.Control.Ims.Pcscf.Create.set \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf:ADD')
