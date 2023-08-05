from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Release:
	"""Release commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("release", core, parent)

	def set(self, release: bool, imsi=repcap.Imsi.Default, accPointName=repcap.AccPointName.Default) -> None:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CONNections:IMSI<Suffix>:APN<APNSuffix>:RELease \n
		Snippet: driver.configure.data.control.epdg.connections.imsi.apn.release.set(release = False, imsi = repcap.Imsi.Default, accPointName = repcap.AccPointName.Default) \n
		No command help available \n
			:param release: No help available
			:param imsi: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Imsi')
			:param accPointName: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Apn')"""
		param = Conversions.bool_to_str(release)
		imsi_cmd_val = self._base.get_repcap_cmd_value(imsi, repcap.Imsi)
		accPointName_cmd_val = self._base.get_repcap_cmd_value(accPointName, repcap.AccPointName)
		self._core.io.write(f'CONFigure:DATA:CONTrol:EPDG:CONNections:IMSI{imsi_cmd_val}:APN{accPointName_cmd_val}:RELease {param}')

	def get(self, imsi=repcap.Imsi.Default, accPointName=repcap.AccPointName.Default) -> bool:
		"""SCPI: CONFigure:DATA:CONTrol:EPDG:CONNections:IMSI<Suffix>:APN<APNSuffix>:RELease \n
		Snippet: value: bool = driver.configure.data.control.epdg.connections.imsi.apn.release.get(imsi = repcap.Imsi.Default, accPointName = repcap.AccPointName.Default) \n
		No command help available \n
			:param imsi: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Imsi')
			:param accPointName: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Apn')
			:return: release: No help available"""
		imsi_cmd_val = self._base.get_repcap_cmd_value(imsi, repcap.Imsi)
		accPointName_cmd_val = self._base.get_repcap_cmd_value(accPointName, repcap.AccPointName)
		response = self._core.io.query_str(f'CONFigure:DATA:CONTrol:EPDG:CONNections:IMSI{imsi_cmd_val}:APN{accPointName_cmd_val}:RELease?')
		return Conversions.str_to_bool(response)
