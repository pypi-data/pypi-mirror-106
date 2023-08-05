from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Qam:
	"""Qam commands group definition. 8 total commands, 7 Sub-groups, 0 group commands
	Repeated Capability: Qam, default value after init: Qam.Order16"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("qam", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_qam_get', 'repcap_qam_set', repcap.Qam.Order16)

	def repcap_qam_set(self, enum_value: repcap.Qam) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Qam.Default
		Default value after init: Qam.Order16"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_qam_get(self) -> repcap.Qam:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .Qam_.EvMagnitude import EvMagnitude
			self._evMagnitude = EvMagnitude(self._core, self._base)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_merror'):
			from .Qam_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perror'):
			from .Qam_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def freqError(self):
		"""freqError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_freqError'):
			from .Qam_.FreqError import FreqError
			self._freqError = FreqError(self._core, self._base)
		return self._freqError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .Qam_.IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._base)
		return self._iqOffset

	@property
	def ibe(self):
		"""ibe commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ibe'):
			from .Qam_.Ibe import Ibe
			self._ibe = Ibe(self._core, self._base)
		return self._ibe

	@property
	def esFlatness(self):
		"""esFlatness commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_esFlatness'):
			from .Qam_.EsFlatness import EsFlatness
			self._esFlatness = EsFlatness(self._core, self._base)
		return self._esFlatness

	def clone(self) -> 'Qam':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Qam(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
