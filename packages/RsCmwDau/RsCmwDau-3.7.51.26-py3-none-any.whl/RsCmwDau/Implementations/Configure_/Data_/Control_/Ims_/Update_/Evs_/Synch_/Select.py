from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("select", core, parent)

	def set(self, bw_ranges: enums.BwRange, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:SYNCh:SELect \n
		Snippet: driver.configure.data.control.ims.update.evs.synch.select.set(bw_ranges = enums.BwRange.COMMon, ims = repcap.Ims.Default) \n
		Selects a configuration mode for the bandwidth and bit-rate settings of the EVS primary mode, for a call update. \n
			:param bw_ranges: COMMon | SENDrx Common configuration or send/receive configured separately
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.enum_scalar_to_str(bw_ranges, enums.BwRange)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:SYNCh:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, ims=repcap.Ims.Default) -> enums.BwRange:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:UPDate:EVS:SYNCh:SELect \n
		Snippet: value: enums.BwRange = driver.configure.data.control.ims.update.evs.synch.select.get(ims = repcap.Ims.Default) \n
		Selects a configuration mode for the bandwidth and bit-rate settings of the EVS primary mode, for a call update. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: bw_ranges: COMMon | SENDrx Common configuration or send/receive configured separately"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:UPDate:EVS:SYNCh:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.BwRange)
