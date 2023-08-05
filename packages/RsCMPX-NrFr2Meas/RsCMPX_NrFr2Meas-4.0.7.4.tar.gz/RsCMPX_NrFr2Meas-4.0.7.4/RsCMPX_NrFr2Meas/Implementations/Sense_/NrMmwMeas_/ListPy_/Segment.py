from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Segment:
	"""Segment commands group definition. 2 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: SEGMent, default value after init: SEGMent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("segment", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_sEGMent_get', 'repcap_sEGMent_set', repcap.SEGMent.Nr1)

	def repcap_sEGMent_set(self, enum_value: repcap.SEGMent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SEGMent.Default
		Default value after init: SEGMent.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_sEGMent_get(self) -> repcap.SEGMent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def rlevel(self):
		"""rlevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlevel'):
			from .Segment_.Rlevel import Rlevel
			self._rlevel = Rlevel(self._core, self._base)
		return self._rlevel

	@property
	def caggregation(self):
		"""caggregation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caggregation'):
			from .Segment_.Caggregation import Caggregation
			self._caggregation = Caggregation(self._core, self._base)
		return self._caggregation

	def clone(self) -> 'Segment':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Segment(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
