from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("value", core, parent)

	def set(self, threshold_value: int, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:THReshold:VALue \n
		Snippet: driver.configure.data.control.ims.threshold.value.set(threshold_value = 1, ims = repcap.Ims.Default) \n
		Configures a threshold for the usage of UDP (below threshold) and TCP (above threshold) . The setting is only relevant
		for method RsCmwDau.Configure.Data.Control.Ims.Transport.Selection.set CUSTom. \n
			:param threshold_value: Number of characters per SIP message Range: 1 to 65535
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.decimal_value_to_str(threshold_value)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:THReshold:VALue {param}')

	def get(self, ims=repcap.Ims.Default) -> int:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:THReshold:VALue \n
		Snippet: value: int = driver.configure.data.control.ims.threshold.value.get(ims = repcap.Ims.Default) \n
		Configures a threshold for the usage of UDP (below threshold) and TCP (above threshold) . The setting is only relevant
		for method RsCmwDau.Configure.Data.Control.Ims.Transport.Selection.set CUSTom. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: threshold_value: Number of characters per SIP message Range: 1 to 65535"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:THReshold:VALue?')
		return Conversions.str_to_int(response)
