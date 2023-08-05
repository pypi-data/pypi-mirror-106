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

	def set(self, behaviour: enums.BehaviourB, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:BEHaviour \n
		Snippet: driver.configure.data.control.ims.pcscf.behaviour.set(behaviour = enums.BehaviourB.FAILure, ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines the behavior of the P-CSCF number {p} when it receives a SIP message from the DUT. \n
			:param behaviour: NORMal | FAILure NORMal: normal behavior FAILure: return failure code
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')"""
		param = Conversions.enum_scalar_to_str(behaviour, enums.BehaviourB)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:BEHaviour {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default, pcscFnc=repcap.PcscFnc.Default) -> enums.BehaviourB:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:PCSCf<Pcscf>:BEHaviour \n
		Snippet: value: enums.BehaviourB = driver.configure.data.control.ims.pcscf.behaviour.get(ims = repcap.Ims.Default, pcscFnc = repcap.PcscFnc.Default) \n
		Defines the behavior of the P-CSCF number {p} when it receives a SIP message from the DUT. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:param pcscFnc: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pcscf')
			:return: behaviour: NORMal | FAILure NORMal: normal behavior FAILure: return failure code"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		pcscFnc_cmd_val = self._base.get_repcap_cmd_value(pcscFnc, repcap.PcscFnc)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:PCSCf{pcscFnc_cmd_val}:BEHaviour?')
		return Conversions.str_to_scalar_enum(response, enums.BehaviourB)
