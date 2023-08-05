from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Margin:
	"""Margin commands group definition. 6 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("margin", core, parent)

	@property
	def area(self):
		"""area commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_area'):
			from .Margin_.Area import Area
			self._area = Area(self._core, self._base)
		return self._area

	def clone(self) -> 'Margin':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Margin(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
