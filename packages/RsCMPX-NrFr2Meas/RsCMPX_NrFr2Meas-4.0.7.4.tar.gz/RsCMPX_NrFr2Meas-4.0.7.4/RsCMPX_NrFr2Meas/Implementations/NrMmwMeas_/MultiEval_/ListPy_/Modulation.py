from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 177 total commands, 12 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	@property
	def evm(self):
		"""evm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Modulation_.Evm import Evm
			self._evm = Evm(self._core, self._base)
		return self._evm

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Modulation_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Modulation_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def iqOffset(self):
		"""iqOffset commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .Modulation_.IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._base)
		return self._iqOffset

	@property
	def freqError(self):
		"""freqError commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .Modulation_.FreqError import FreqError
			self._freqError = FreqError(self._core, self._base)
		return self._freqError

	@property
	def terror(self):
		"""terror commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_terror'):
			from .Modulation_.Terror import Terror
			self._terror = Terror(self._core, self._base)
		return self._terror

	@property
	def tpower(self):
		"""tpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_tpower'):
			from .Modulation_.Tpower import Tpower
			self._tpower = Tpower(self._core, self._base)
		return self._tpower

	@property
	def ppower(self):
		"""ppower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppower'):
			from .Modulation_.Ppower import Ppower
			self._ppower = Ppower(self._core, self._base)
		return self._ppower

	@property
	def psd(self):
		"""psd commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_psd'):
			from .Modulation_.Psd import Psd
			self._psd = Psd(self._core, self._base)
		return self._psd

	@property
	def dmodulation(self):
		"""dmodulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmodulation'):
			from .Modulation_.Dmodulation import Dmodulation
			self._dmodulation = Dmodulation(self._core, self._base)
		return self._dmodulation

	@property
	def dchType(self):
		"""dchType commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dchType'):
			from .Modulation_.DchType import DchType
			self._dchType = DchType(self._core, self._base)
		return self._dchType

	@property
	def dallocation(self):
		"""dallocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dallocation'):
			from .Modulation_.Dallocation import Dallocation
			self._dallocation = Dallocation(self._core, self._base)
		return self._dallocation

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
