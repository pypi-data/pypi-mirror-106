from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Area:
	"""Area commands group definition. 6 total commands, 2 Sub-groups, 0 group commands
	Repeated Capability: Area, default value after init: Area.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("area", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_area_get', 'repcap_area_set', repcap.Area.Nr1)

	def repcap_area_set(self, enum_value: repcap.Area) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Area.Default
		Default value after init: Area.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_area_get(self) -> repcap.Area:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def negativ(self):
		"""negativ commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_negativ'):
			from .Area_.Negativ import Negativ
			self._negativ = Negativ(self._core, self._base)
		return self._negativ

	@property
	def positiv(self):
		"""positiv commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_positiv'):
			from .Area_.Positiv import Positiv
			self._positiv = Positiv(self._core, self._base)
		return self._positiv

	def clone(self) -> 'Area':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Area(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
