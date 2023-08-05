from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbandwidth:
	"""Cbandwidth commands group definition. 1 total commands, 1 Sub-groups, 0 group commands
	Repeated Capability: ChannelBw, default value after init: ChannelBw.Bw50"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cbandwidth", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_channelBw_get', 'repcap_channelBw_set', repcap.ChannelBw.Bw50)

	def repcap_channelBw_set(self, enum_value: repcap.ChannelBw) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to ChannelBw.Default
		Default value after init: ChannelBw.Bw50"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_channelBw_get(self) -> repcap.ChannelBw:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def blimits(self):
		"""blimits commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blimits'):
			from .Cbandwidth_.Blimits import Blimits
			self._blimits = Blimits(self._core, self._base)
		return self._blimits

	def clone(self) -> 'Cbandwidth':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cbandwidth(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
