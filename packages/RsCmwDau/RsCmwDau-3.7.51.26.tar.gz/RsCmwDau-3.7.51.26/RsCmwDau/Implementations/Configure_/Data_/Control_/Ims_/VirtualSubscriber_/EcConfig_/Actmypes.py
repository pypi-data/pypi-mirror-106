from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Actmypes:
	"""Actmypes commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("actmypes", core, parent)

	# noinspection PyTypeChecker
	class SetStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Msd_Value_1: str: No parameter help available
			- Msd_Value_2: str: No parameter help available
			- Msd_Value_3: str: No parameter help available
			- Msd_Value_4: str: No parameter help available
			- Msd_Value_5: str: No parameter help available
			- Msd_Value_6: str: No parameter help available
			- Msd_Value_7: str: No parameter help available
			- Msd_Value_8: str: No parameter help available
			- Msd_Value_9: str: No parameter help available
			- Msd_Value_10: str: No parameter help available
			- Msd_Value_11: str: No parameter help available
			- Msd_Value_12: str: No parameter help available
			- Msd_Value_13: str: No parameter help available
			- Msd_Value_14: str: No parameter help available
			- Msd_Value_15: str: No parameter help available
			- Msd_Value_16: str: No parameter help available"""
		__meta_args_list = [
			]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Msd_Value_1: str = None
			self.Msd_Value_2: str = None
			self.Msd_Value_3: str = None
			self.Msd_Value_4: str = None
			self.Msd_Value_5: str = None
			self.Msd_Value_6: str = None
			self.Msd_Value_7: str = None
			self.Msd_Value_8: str = None
			self.Msd_Value_9: str = None
			self.Msd_Value_10: str = None
			self.Msd_Value_11: str = None
			self.Msd_Value_12: str = None
			self.Msd_Value_13: str = None
			self.Msd_Value_14: str = None
			self.Msd_Value_15: str = None
			self.Msd_Value_16: str = None

	def set(self, structure: SetStruct, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:ECConfig:ACTMypes \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.ecConfig.actmypes.set(value = [PROPERTY_STRUCT_NAME](), ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		No command help available \n
			:param structure: for set value, see the help for SetStruct structure arguments.
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write_struct(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:ECConfig:ACTMypes', structure)
