from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Caggregation:
	"""Caggregation commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("caggregation", core, parent)

	@property
	def acSpacing(self):
		"""acSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acSpacing'):
			from .Caggregation_.AcSpacing import AcSpacing
			self._acSpacing = AcSpacing(self._core, self._base)
		return self._acSpacing

	@property
	def mcarrier(self):
		"""mcarrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcarrier'):
			from .Caggregation_.Mcarrier import Mcarrier
			self._mcarrier = Mcarrier(self._core, self._base)
		return self._mcarrier

	def clone(self) -> 'Caggregation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Caggregation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
