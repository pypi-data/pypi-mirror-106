from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Create:
	"""Create commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("create", core, parent)

	def set(self, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf:CREate \n
		Snippet: driver.configure.data.control.ims.pcscf.create.set(ims = repcap.Ims.Default) \n
		Updates the internal list of P-CSCF profiles. If your command script adds P-CSCF profiles, you must insert this command
		before you can use the new profiles. It is sufficient to insert the command once, after adding the last P-CSCF profile /
		before using the profiles. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf:CREate')

	def set_with_opc(self, ims=repcap.Ims.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf:CREate \n
		Snippet: driver.configure.data.control.ims.pcscf.create.set_with_opc(ims = repcap.Ims.Default) \n
		Updates the internal list of P-CSCF profiles. If your command script adds P-CSCF profiles, you must insert this command
		before you can use the new profiles. It is sufficient to insert the command once, after adding the last P-CSCF profile /
		before using the profiles. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf:CREate')
