from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Protocol:
	"""Protocol commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("protocol", core, parent)

	def set(self, protocol: enums.ProtocolB, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:PROTocol \n
		Snippet: driver.configure.data.measurement.qos.filterPy.protocol.set(protocol = enums.ProtocolB.ALL, fltr = repcap.Fltr.Default) \n
		Specifies the protocol as filter criterion for IP packets. \n
			:param protocol: ALL | TCP | UDP No filtering, TCP only, UDP only
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.enum_scalar_to_str(protocol, enums.ProtocolB)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:PROTocol {param}')

	# noinspection PyTypeChecker
	def get(self, fltr=repcap.Fltr.Default) -> enums.ProtocolB:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:PROTocol \n
		Snippet: value: enums.ProtocolB = driver.configure.data.measurement.qos.filterPy.protocol.get(fltr = repcap.Fltr.Default) \n
		Specifies the protocol as filter criterion for IP packets. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: protocol: ALL | TCP | UDP No filtering, TCP only, UDP only"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:PROTocol?')
		return Conversions.str_to_scalar_enum(response, enums.ProtocolB)
