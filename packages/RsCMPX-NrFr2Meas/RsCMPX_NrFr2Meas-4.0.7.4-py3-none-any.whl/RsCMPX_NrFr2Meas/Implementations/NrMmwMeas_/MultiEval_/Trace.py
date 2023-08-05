from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 18 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trace", core, parent)

	@property
	def seMask(self):
		"""seMask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_seMask'):
			from .Trace_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Trace_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def pmonitor(self):
		"""pmonitor commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pmonitor'):
			from .Trace_.Pmonitor import Pmonitor
			self._pmonitor = Pmonitor(self._core, self._base)
		return self._pmonitor

	@property
	def pdynamics(self):
		"""pdynamics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Trace_.Pdynamics import Pdynamics
			self._pdynamics = Pdynamics(self._core, self._base)
		return self._pdynamics

	def clone(self) -> 'Trace':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trace(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
