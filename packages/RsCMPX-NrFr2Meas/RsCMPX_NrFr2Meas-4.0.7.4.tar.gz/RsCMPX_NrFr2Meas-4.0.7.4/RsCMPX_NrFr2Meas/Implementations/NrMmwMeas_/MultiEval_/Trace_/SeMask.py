from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMask:
	"""SeMask commands group definition. 6 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("seMask", core, parent)

	@property
	def rbw(self):
		"""rbw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbw'):
			from .SeMask_.Rbw import Rbw
			self._rbw = Rbw(self._core, self._base)
		return self._rbw

	def clone(self) -> 'SeMask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SeMask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
