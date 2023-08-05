from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Allocation:
	"""Allocation commands group definition. 4 total commands, 1 Sub-groups, 1 group commands
	Repeated Capability: Allocation, default value after init: Allocation.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("allocation", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_allocation_get', 'repcap_allocation_set', repcap.Allocation.Nr1)

	def repcap_allocation_set(self, enum_value: repcap.Allocation) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Allocation.Default
		Default value after init: Allocation.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_allocation_get(self) -> repcap.Allocation:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_pusch'):
			from .Allocation_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	# noinspection PyTypeChecker
	class AllocationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Bandwidth_Part: enums.BandwidthPart: No parameter help available
			- Slot_Format: int: No parameter help available
			- Content: enums.ChannelTypeA: No parameter help available
			- Allocated_Slots: enums.AllocatedSlots: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Bandwidth_Part', enums.BandwidthPart),
			ArgStruct.scalar_int('Slot_Format'),
			ArgStruct.scalar_enum('Content', enums.ChannelTypeA),
			ArgStruct.scalar_enum('Allocated_Slots', enums.AllocatedSlots)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Bandwidth_Part: enums.BandwidthPart = None
			self.Slot_Format: int = None
			self.Content: enums.ChannelTypeA = None
			self.Allocated_Slots: enums.AllocatedSlots = None

	def set(self, structure: AllocationStruct, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation> \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.set(value = [PROPERTY_STRUCT_NAME](), carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		No command help available \n
			:param structure: for set value, see the help for AllocationStruct structure arguments.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')"""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}', structure)

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> AllocationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation> \n
		Snippet: value: AllocationStruct = driver.configure.nrMmwMeas.cc.allocation.get(carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		No command help available \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for AllocationStruct structure arguments."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}?', self.__class__.AllocationStruct())

	def clone(self) -> 'Allocation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Allocation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
