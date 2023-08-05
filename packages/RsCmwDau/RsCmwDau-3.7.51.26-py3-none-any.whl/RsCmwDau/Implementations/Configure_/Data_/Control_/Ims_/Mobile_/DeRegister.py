from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeRegister:
	"""DeRegister commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("deRegister", core, parent)

	def set(self, ims=repcap.Ims.Default, profile=repcap.Profile.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:MOBile<UE>:DERegister \n
		Snippet: driver.configure.data.control.ims.mobile.deRegister.set(ims = repcap.Ims.Default, profile = repcap.Profile.Default) \n
		Deregisters a registered subscriber from the IMS server. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param profile: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mobile')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		profile_cmd_val = self._base.get_repcap_cmd_value(profile, repcap.Profile)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:MOBile{profile_cmd_val}:DERegister')

	def set_with_opc(self, ims=repcap.Ims.Default, profile=repcap.Profile.Default) -> None:
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		profile_cmd_val = self._base.get_repcap_cmd_value(profile, repcap.Profile)
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:MOBile<UE>:DERegister \n
		Snippet: driver.configure.data.control.ims.mobile.deRegister.set_with_opc(ims = repcap.Ims.Default, profile = repcap.Profile.Default) \n
		Deregisters a registered subscriber from the IMS server. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCmwDau.utilities.opc_timeout_set() to set the timeout value. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param profile: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Mobile')"""
		self._core.io.write_with_opc(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:MOBile{profile_cmd_val}:DERegister')
