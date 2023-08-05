from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TflowId:
	"""TflowId commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tflowId", core, parent)

	def set(self, flow_id: int, trace=repcap.Trace.Default) -> None:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:FTTRigger:TRACe<TraceIndex>:TFLowid \n
		Snippet: driver.configure.data.measurement.ipAnalysis.ftTrigger.trace.tflowId.set(flow_id = 1, trace = repcap.Trace.Default) \n
		Assigns a connection (flow ID) to a trace index. \n
			:param flow_id: Flow ID of the connection to be assigned to the trace index To assign all connections matching the flow filter criteria, set the value 0.
			:param trace: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Trace')"""
		param = Conversions.decimal_value_to_str(flow_id)
		trace_cmd_val = self._base.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:FTTRigger:TRACe{trace_cmd_val}:TFLowid {param}')

	def get(self, trace=repcap.Trace.Default) -> int:
		"""SCPI: CONFigure:DATA:MEASurement<Instance>:IPANalysis:FTTRigger:TRACe<TraceIndex>:TFLowid \n
		Snippet: value: int = driver.configure.data.measurement.ipAnalysis.ftTrigger.trace.tflowId.get(trace = repcap.Trace.Default) \n
		Assigns a connection (flow ID) to a trace index. \n
			:param trace: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Trace')
			:return: flow_id: Flow ID of the connection to be assigned to the trace index To assign all connections matching the flow filter criteria, set the value 0."""
		trace_cmd_val = self._base.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CONFigure:DATA:MEASurement<MeasInstance>:IPANalysis:FTTRigger:TRACe{trace_cmd_val}:TFLowid?')
		return Conversions.str_to_int(response)
