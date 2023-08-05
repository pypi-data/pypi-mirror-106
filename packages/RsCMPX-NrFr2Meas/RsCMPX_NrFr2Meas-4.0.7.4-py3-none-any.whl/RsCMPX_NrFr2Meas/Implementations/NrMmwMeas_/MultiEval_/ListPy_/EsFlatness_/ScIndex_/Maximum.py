from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: Maximum, default value after init: Maximum.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_maximum_get', 'repcap_maximum_set', repcap.Maximum.Nr1)

	def repcap_maximum_set(self, enum_value: repcap.Maximum) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Maximum.Default
		Default value after init: Maximum.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_maximum_get(self) -> repcap.Maximum:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Maximum_.Current import Current
			self._current = Current(self._core, self._base)
		return self._current

	def clone(self) -> 'Maximum':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Maximum(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
