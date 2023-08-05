from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 14 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	@property
	def nr(self):
		"""nr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_nr'):
			from .Aclr_.Nr import Nr
			self._nr = Nr(self._core, self._base)
		return self._nr

	@property
	def dchType(self):
		"""dchType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dchType'):
			from .Aclr_.DchType import DchType
			self._dchType = DchType(self._core, self._base)
		return self._dchType

	@property
	def dallocation(self):
		"""dallocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dallocation'):
			from .Aclr_.Dallocation import Dallocation
			self._dallocation = Dallocation(self._core, self._base)
		return self._dallocation

	def clone(self) -> 'Aclr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aclr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
