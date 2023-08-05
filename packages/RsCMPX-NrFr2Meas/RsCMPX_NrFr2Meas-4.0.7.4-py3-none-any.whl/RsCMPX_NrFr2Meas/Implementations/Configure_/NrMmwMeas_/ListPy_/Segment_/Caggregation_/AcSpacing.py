from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcSpacing:
	"""AcSpacing commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acSpacing", core, parent)

	def set(self, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CAGGregation:ACSPacing \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.caggregation.acSpacing.set(sEGMent = repcap.SEGMent.Default) \n
		No command help available \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CAGGregation:ACSPacing')

	def set_with_opc(self, sEGMent=repcap.SEGMent.Default) -> None:
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:CAGGregation:ACSPacing \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.caggregation.acSpacing.set_with_opc(sEGMent = repcap.SEGMent.Default) \n
		No command help available \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_NrFr2Meas.utilities.opc_timeout_set() to set the timeout value. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		self._core.io.write_with_opc(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CAGGregation:ACSPacing')
