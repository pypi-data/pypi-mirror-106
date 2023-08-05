from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmonitor:
	"""Pmonitor commands group definition. 4 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pmonitor", core, parent)

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rms'):
			from .Pmonitor_.Rms import Rms
			self._rms = Rms(self._core, self._base)
		return self._rms

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Pmonitor_.Peak import Peak
			self._peak = Peak(self._core, self._base)
		return self._peak

	@property
	def array(self):
		"""array commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_array'):
			from .Pmonitor_.Array import Array
			self._array = Array(self._core, self._base)
		return self._array

	def clone(self) -> 'Pmonitor':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pmonitor(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
