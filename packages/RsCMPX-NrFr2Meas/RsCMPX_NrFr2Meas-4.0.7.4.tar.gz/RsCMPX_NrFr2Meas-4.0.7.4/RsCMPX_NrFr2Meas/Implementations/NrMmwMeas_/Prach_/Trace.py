from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 29 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def evm(self):
		"""evm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Trace_.Evm import Evm
			self._evm = Evm(self._core, self._base)
		return self._evm

	@property
	def evPreamble(self):
		"""evPreamble commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_evPreamble'):
			from .Trace_.EvPreamble import EvPreamble
			self._evPreamble = EvPreamble(self._core, self._base)
		return self._evPreamble

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Trace_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Trace_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def iq(self):
		"""iq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iq'):
			from .Trace_.Iq import Iq
			self._iq = Iq(self._core, self._base)
		return self._iq

	@property
	def pdynamics(self):
		"""pdynamics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Trace_.Pdynamics import Pdynamics
			self._pdynamics = Pdynamics(self._core, self._base)
		return self._pdynamics

	@property
	def pvPreamble(self):
		"""pvPreamble commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pvPreamble'):
			from .Trace_.PvPreamble import PvPreamble
			self._pvPreamble = PvPreamble(self._core, self._base)
		return self._pvPreamble

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
