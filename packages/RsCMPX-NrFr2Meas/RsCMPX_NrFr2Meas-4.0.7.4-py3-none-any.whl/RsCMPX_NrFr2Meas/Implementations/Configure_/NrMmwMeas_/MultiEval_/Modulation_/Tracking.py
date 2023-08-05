from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tracking:
	"""Tracking commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tracking", core, parent)

	def get_timing(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.tracking.get_timing() \n
		Activate or deactivate timing tracking. With enabled tracking, fluctuations are compensated. \n
			:return: tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing?')
		return Conversions.str_to_bool(response)

	def set_timing(self, tracking: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.tracking.set_timing(tracking = False) \n
		Activate or deactivate timing tracking. With enabled tracking, fluctuations are compensated. \n
			:param tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(tracking)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:TIMing {param}')

	def get_phase(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.tracking.get_phase() \n
		Activate or deactivate phase tracking. With enabled tracking, fluctuations are compensated. \n
			:return: tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe?')
		return Conversions.str_to_bool(response)

	def set_phase(self, tracking: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.tracking.set_phase(tracking = False) \n
		Activate or deactivate phase tracking. With enabled tracking, fluctuations are compensated. \n
			:param tracking: OFF: Tracking disabled ON: Tracking enabled
		"""
		param = Conversions.bool_to_str(tracking)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:TRACking:PHASe {param}')
