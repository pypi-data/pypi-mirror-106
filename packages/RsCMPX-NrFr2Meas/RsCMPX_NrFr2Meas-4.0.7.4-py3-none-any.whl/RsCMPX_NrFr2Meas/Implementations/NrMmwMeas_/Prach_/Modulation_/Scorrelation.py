from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scorrelation:
	"""Scorrelation commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scorrelation", core, parent)

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Scorrelation_.Preamble import Preamble
			self._preamble = Preamble(self._core, self._base)
		return self._preamble

	def fetch(self) -> float:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:SCORrelation \n
		Snippet: value: float = driver.nrMmwMeas.prach.modulation.scorrelation.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: seq_correlation: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:SCORrelation?', suppressed)
		return Conversions.str_to_float(response)

	def clone(self) -> 'Scorrelation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scorrelation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
