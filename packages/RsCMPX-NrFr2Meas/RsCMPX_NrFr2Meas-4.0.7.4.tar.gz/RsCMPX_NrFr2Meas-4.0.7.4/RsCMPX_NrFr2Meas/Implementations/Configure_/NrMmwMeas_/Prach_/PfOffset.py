from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PfOffset:
	"""PfOffset commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pfOffset", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset:AUTO \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.pfOffset.get_auto() \n
		No command help available \n
			:return: prach_freq_auto: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, prach_freq_auto: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset:AUTO \n
		Snippet: driver.configure.nrMmwMeas.prach.pfOffset.set_auto(prach_freq_auto = False) \n
		No command help available \n
			:param prach_freq_auto: No help available
		"""
		param = Conversions.bool_to_str(prach_freq_auto)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset:AUTO {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.pfOffset.get_value() \n
		No command help available \n
			:return: prach_freq_offset: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset?')
		return Conversions.str_to_int(response)

	def set_value(self, prach_freq_offset: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset \n
		Snippet: driver.configure.nrMmwMeas.prach.pfOffset.set_value(prach_freq_offset = 1) \n
		No command help available \n
			:param prach_freq_offset: No help available
		"""
		param = Conversions.decimal_value_to_str(prach_freq_offset)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFOFfset {param}')
