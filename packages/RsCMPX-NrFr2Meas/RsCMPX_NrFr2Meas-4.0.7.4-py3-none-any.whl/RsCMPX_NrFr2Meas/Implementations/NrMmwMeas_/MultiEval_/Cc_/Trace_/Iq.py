from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iq", core, parent)

	@property
	def low(self):
		"""low commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_low'):
			from .Iq_.Low import Low
			self._low = Low(self._core, self._base)
		return self._low

	@property
	def high(self):
		"""high commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_high'):
			from .Iq_.High import High
			self._high = High(self._core, self._base)
		return self._high

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
