from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TcpAlive:
	"""TcpAlive commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tcpAlive", core, parent)

	def set(self, tcp_keep: bool, ims=repcap.Ims.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:TCPalive \n
		Snippet: driver.configure.data.control.ims.tcpAlive.set(tcp_keep = False, ims = repcap.Ims.Default) \n
		Selects whether the IMS server sends TCP keep-alive messages or not. \n
			:param tcp_keep: OFF | ON
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')"""
		param = Conversions.bool_to_str(tcp_keep)
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		self._core.io.write(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:TCPalive {param}')

	def get(self, ims=repcap.Ims.Default) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:IMS<Suffix>:TCPalive \n
		Snippet: value: bool = driver.configure.data.control.ims.tcpAlive.get(ims = repcap.Ims.Default) \n
		Selects whether the IMS server sends TCP keep-alive messages or not. \n
			:param ims: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Ims')
			:return: tcp_keep: OFF | ON"""
		ims_cmd_val = self._base.get_repcap_cmd_value(ims, repcap.Ims)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:IMS{ims_cmd_val}:TCPalive?')
		return Conversions.str_to_bool(response)
