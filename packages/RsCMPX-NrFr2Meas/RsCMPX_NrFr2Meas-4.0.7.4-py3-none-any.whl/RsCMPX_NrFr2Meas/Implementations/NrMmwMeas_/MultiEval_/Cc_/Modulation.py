from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 14 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_current'):
			from .Modulation_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_average'):
			from .Modulation_.Average import Average
			self._average = Average(self._core, self._base)
		return self._average

	@property
	def extreme(self):
		"""extreme commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_extreme'):
			from .Modulation_.Extreme import Extreme
			self._extreme = Extreme(self._core, self._base)
		return self._extreme

	@property
	def standardDev(self):
		"""standardDev commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_standardDev'):
			from .Modulation_.StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._base)
		return self._standardDev

	@property
	def dmodulation(self):
		"""dmodulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmodulation'):
			from .Modulation_.Dmodulation import Dmodulation
			self._dmodulation = Dmodulation(self._core, self._base)
		return self._dmodulation

	@property
	def dchType(self):
		"""dchType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dchType'):
			from .Modulation_.DchType import DchType
			self._dchType = DchType(self._core, self._base)
		return self._dchType

	@property
	def dallocation(self):
		"""dallocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dallocation'):
			from .Modulation_.Dallocation import Dallocation
			self._dallocation = Dallocation(self._core, self._base)
		return self._dallocation

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
