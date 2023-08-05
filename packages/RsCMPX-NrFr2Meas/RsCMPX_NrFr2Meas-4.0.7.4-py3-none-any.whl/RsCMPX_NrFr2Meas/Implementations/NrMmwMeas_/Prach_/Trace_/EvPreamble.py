from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvPreamble:
	"""EvPreamble commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evPreamble", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:PRACh:TRACe:EVPReamble \n
		Snippet: value: List[float] = driver.nrMmwMeas.prach.trace.evPreamble.read() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: results: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRMMw:MEASurement<Instance>:PRACh:TRACe:EVPReamble?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:TRACe:EVPReamble \n
		Snippet: value: List[float] = driver.nrMmwMeas.prach.trace.evPreamble.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: results: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:TRACe:EVPReamble?', suppressed)
		return response
