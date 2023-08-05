from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class JitterDistribution:
	"""JitterDistribution commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("jitterDistribution", core, parent)

	def set(self, jitter_distr: enums.JitterDistrib, impairments=repcap.Impairments.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:JDIStribut \n
		Snippet: driver.configure.data.measurement.nimpairments.jitterDistribution.set(jitter_distr = enums.JitterDistrib.NORMal, impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param jitter_distr: No help available
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')"""
		param = Conversions.enum_scalar_to_str(jitter_distr, enums.JitterDistrib)
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:JDIStribut {param}')

	# noinspection PyTypeChecker
	def get(self, impairments=repcap.Impairments.Default) -> enums.JitterDistrib:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:NIMPairments<Index>:JDIStribut \n
		Snippet: value: enums.JitterDistrib = driver.configure.data.measurement.nimpairments.jitterDistribution.get(impairments = repcap.Impairments.Default) \n
		No command help available \n
			:param impairments: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Nimpairments')
			:return: jitter_distr: No help available"""
		impairments_cmd_val = self._base.get_repcap_cmd_value(impairments, repcap.Impairments)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:NIMPairments{impairments_cmd_val}:JDIStribut?')
		return Conversions.str_to_scalar_enum(response, enums.JitterDistrib)
