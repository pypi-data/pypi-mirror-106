from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 31 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	@property
	def phbpsk(self):
		"""phbpsk commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_phbpsk'):
			from .Limit_.Phbpsk import Phbpsk
			self._phbpsk = Phbpsk(self._core, self._base)
		return self._phbpsk

	@property
	def qpsk(self):
		"""qpsk commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_qpsk'):
			from .Limit_.Qpsk import Qpsk
			self._qpsk = Qpsk(self._core, self._base)
		return self._qpsk

	@property
	def qam(self):
		"""qam commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Limit_.Qam import Qam
			self._qam = Qam(self._core, self._base)
		return self._qam

	@property
	def seMask(self):
		"""seMask commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_seMask'):
			from .Limit_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_aclr'):
			from .Limit_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	def clone(self) -> 'Limit':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Limit(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
