from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AcSpacing:
	"""AcSpacing commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("acSpacing", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:ACSPacing \n
		Snippet: driver.configure.nrMmwMeas.caggregation.acSpacing.set() \n
		Adjusts the component carrier frequencies, so that the carriers are aggregated contiguously, with nominal channel spacing. \n
		"""
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:ACSPacing')

	def set_with_opc(self) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:ACSPacing \n
		Snippet: driver.configure.nrMmwMeas.caggregation.acSpacing.set_with_opc() \n
		Adjusts the component carrier frequencies, so that the carriers are aggregated contiguously, with nominal channel spacing. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsCMPX_NrFr2Meas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:ACSPacing')
