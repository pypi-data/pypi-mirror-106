from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 85 total commands, 7 Sub-groups, 0 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cc", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, enum_value: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def trace(self):
		"""trace commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Cc_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .Cc_.EvMagnitude import EvMagnitude
			self._evMagnitude = EvMagnitude(self._core, self._base)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Cc_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Cc_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def iemission(self):
		"""iemission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iemission'):
			from .Cc_.Iemission import Iemission
			self._iemission = Iemission(self._core, self._base)
		return self._iemission

	@property
	def esFlatness(self):
		"""esFlatness commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_esFlatness'):
			from .Cc_.EsFlatness import EsFlatness
			self._esFlatness = EsFlatness(self._core, self._base)
		return self._esFlatness

	@property
	def modulation(self):
		"""modulation commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Cc_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
