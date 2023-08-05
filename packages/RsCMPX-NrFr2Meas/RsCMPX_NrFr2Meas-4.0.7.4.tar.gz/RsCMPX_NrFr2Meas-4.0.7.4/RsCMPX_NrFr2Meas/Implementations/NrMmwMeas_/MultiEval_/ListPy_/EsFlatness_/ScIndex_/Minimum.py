from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Minimum, default value after init: Minimum.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_minimum_get', 'repcap_minimum_set', repcap.Minimum.Nr1)

	def repcap_minimum_set(self, enum_value: repcap.Minimum) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Minimum.Default
		Default value after init: Minimum.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_minimum_get(self) -> repcap.Minimum:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Minimum_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def clone(self) -> 'Minimum':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Minimum(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
