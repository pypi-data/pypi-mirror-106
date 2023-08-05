from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scount:
	"""Scount commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scount", core, parent)

	def get_modulation(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:MODulation \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.scount.get_modulation() \n
		No command help available \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:MODulation?')
		return Conversions.str_to_int(response)

	def set_modulation(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:MODulation \n
		Snippet: driver.configure.nrMmwMeas.prach.scount.set_modulation(statistic_count = 1) \n
		No command help available \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:MODulation {param}')

	def get_pdynamics(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:PDYNamics \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.scount.get_pdynamics() \n
		No command help available \n
			:return: statistic_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:PDYNamics?')
		return Conversions.str_to_int(response)

	def set_pdynamics(self, statistic_count: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:PDYNamics \n
		Snippet: driver.configure.nrMmwMeas.prach.scount.set_pdynamics(statistic_count = 1) \n
		No command help available \n
			:param statistic_count: No help available
		"""
		param = Conversions.decimal_value_to_str(statistic_count)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCOunt:PDYNamics {param}')
