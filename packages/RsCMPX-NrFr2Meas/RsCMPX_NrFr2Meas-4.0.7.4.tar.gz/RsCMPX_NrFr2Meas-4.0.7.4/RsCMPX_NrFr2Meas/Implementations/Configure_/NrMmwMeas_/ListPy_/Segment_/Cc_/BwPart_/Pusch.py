from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 3 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pusch", core, parent)

	@property
	def dmta(self):
		"""dmta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmta'):
			from .Pusch_.Dmta import Dmta
			self._dmta = Dmta(self._core, self._base)
		return self._dmta

	@property
	def dmtb(self):
		"""dmtb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmtb'):
			from .Pusch_.Dmtb import Dmtb
			self._dmtb = Dmtb(self._core, self._base)
		return self._dmtb

	@property
	def dftPrecoding(self):
		"""dftPrecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dftPrecoding'):
			from .Pusch_.DftPrecoding import DftPrecoding
			self._dftPrecoding = DftPrecoding(self._core, self._base)
		return self._dftPrecoding

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
