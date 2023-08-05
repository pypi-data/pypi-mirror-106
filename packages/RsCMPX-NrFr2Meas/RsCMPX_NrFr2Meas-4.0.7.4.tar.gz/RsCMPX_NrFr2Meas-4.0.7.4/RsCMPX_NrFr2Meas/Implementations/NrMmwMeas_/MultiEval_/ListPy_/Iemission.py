from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iemission:
	"""Iemission commands group definition. 6 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iemission", core, parent)

	@property
	def margin(self):
		"""margin commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .Iemission_.Margin import Margin
			self._margin = Margin(self._core, self._base)
		return self._margin

	def clone(self) -> 'Iemission':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iemission(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
