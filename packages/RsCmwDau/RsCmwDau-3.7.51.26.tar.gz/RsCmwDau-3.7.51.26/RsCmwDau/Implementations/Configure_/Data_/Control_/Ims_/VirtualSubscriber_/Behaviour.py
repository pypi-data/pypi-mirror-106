from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Behaviour:
	"""Behaviour commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("behaviour", core, parent)

	def set(self, behaviour: enums.BehaviourA, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:BEHaviour \n
		Snippet: driver.configure.data.control.ims.virtualSubscriber.behaviour.set(behaviour = enums.BehaviourA.AFTRng, ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Defines the reaction of virtual subscriber number <v> to incoming calls. \n
			:param behaviour: ANSWer | NOANswer | DECLined | BUSY | BEFRng | AFTRng | CD ANSWer: answer the call NOANswer: keep 'ringing' DECLined: reject call BUSY: subscriber busy BEFRng: call forwarding before ringing AFTRng: call forwarding after ringing CD: communication deflection
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')"""
		param = Conversions.enum_scalar_to_str(behaviour, enums.BehaviourA)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:BEHaviour {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, virtualSubscriber=repcap.VirtualSubscriber.Default) -> enums.BehaviourA:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:VIRTualsub<VirtualSubscriber>:BEHaviour \n
		Snippet: value: enums.BehaviourA = driver.configure.data.control.ims.virtualSubscriber.behaviour.get(ims = repcap.Ims.Default, virtualSubscriber = repcap.VirtualSubscriber.Default) \n
		Defines the reaction of virtual subscriber number <v> to incoming calls. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param virtualSubscriber: optional repeated capability selector. Default value: Nr1 (settable in the interface 'VirtualSubscriber')
			:return: behaviour: ANSWer | NOANswer | DECLined | BUSY | BEFRng | AFTRng | CD ANSWer: answer the call NOANswer: keep 'ringing' DECLined: reject call BUSY: subscriber busy BEFRng: call forwarding before ringing AFTRng: call forwarding after ringing CD: communication deflection"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		virtualSubscriber_cmd_val = self._base.get_repcap_cmd_value(virtualSubscriber, repcap.VirtualSubscriber)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:VIRTualsub{virtualSubscriber_cmd_val}:BEHaviour?')
		return Conversions.str_to_scalar_enum(response, enums.BehaviourA)
