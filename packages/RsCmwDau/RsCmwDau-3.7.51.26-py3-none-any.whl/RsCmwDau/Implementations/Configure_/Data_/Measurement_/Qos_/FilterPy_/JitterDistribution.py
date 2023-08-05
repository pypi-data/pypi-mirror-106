from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class JitterDistribution:
	"""JitterDistribution commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("jitterDistribution", core, parent)

	def set(self, jitter_distr: enums.JitterDistrib, fltr=repcap.Fltr.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:JDIStribut \n
		Snippet: driver.configure.data.measurement.qos.filterPy.jitterDistribution.set(jitter_distr = enums.JitterDistrib.NORMal, fltr = repcap.Fltr.Default) \n
		Specifies the jitter distribution for a QoS profile. \n
			:param jitter_distr: UNIForm | NORMal | PAReto | PNORmal Uniform, normal, pareto, pareto normal
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')"""
		param = Conversions.enum_scalar_to_str(jitter_distr, enums.JitterDistrib)
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:JDIStribut {param}')

	# noinspection PyTypeChecker
	def get(self, fltr=repcap.Fltr.Default) -> enums.JitterDistrib:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:QOS:FILTer<Index>:JDIStribut \n
		Snippet: value: enums.JitterDistrib = driver.configure.data.measurement.qos.filterPy.jitterDistribution.get(fltr = repcap.Fltr.Default) \n
		Specifies the jitter distribution for a QoS profile. \n
			:param fltr: optional repeated capability selector. Default value: Ix1 (settable in the interface 'FilterPy')
			:return: jitter_distr: UNIForm | NORMal | PAReto | PNORmal Uniform, normal, pareto, pareto normal"""
		fltr_cmd_val = self._base.get_repcap_cmd_value(fltr, repcap.Fltr)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:QOS:FILTer{fltr_cmd_val}:JDIStribut?')
		return Conversions.str_to_scalar_enum(response, enums.JitterDistrib)
