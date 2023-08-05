from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pusch:
	"""Pusch commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pusch", core, parent)

	@property
	def additional(self):
		"""additional commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_additional'):
			from .Pusch_.Additional import Additional
			self._additional = Additional(self._core, self._base)
		return self._additional

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Pusch_.Sgeneration import Sgeneration
			self._sgeneration = Sgeneration(self._core, self._base)
		return self._sgeneration

	# noinspection PyTypeChecker
	class PuschStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Mapping_Type: enums.MappingType: PUSCH mapping type
			- No_Symbols: int: Number of allocated OFDM symbols in each uplink slot.
			- Start_Symbol: int: Index of the first allocated OFDM symbol in each uplink slot. For mapping type A, only 0 is allowed.
			- No_Rbs: int: Number of allocated UL RBs.
			- Start_Rb: int: Index of the first allocated RB.
			- Mod_Scheme: enums.ModScheme: Modulation scheme π/2-BPSK, QPSK, 16-QAM, 64-QAM, 256-QAM"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Mapping_Type', enums.MappingType),
			ArgStruct.scalar_int('No_Symbols'),
			ArgStruct.scalar_int('Start_Symbol'),
			ArgStruct.scalar_int('No_Rbs'),
			ArgStruct.scalar_int('Start_Rb'),
			ArgStruct.scalar_enum('Mod_Scheme', enums.ModScheme)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Mapping_Type: enums.MappingType = None
			self.No_Symbols: int = None
			self.Start_Symbol: int = None
			self.No_Rbs: int = None
			self.Start_Rb: int = None
			self.Mod_Scheme: enums.ModScheme = None

	def set(self, structure: PuschStruct, sEGMent=repcap.SEGMent.Default, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<cc>]:ALLocation<Allocation>:PUSCh \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.set(value = [PROPERTY_STRUCT_NAME](), sEGMent = repcap.SEGMent.Default, carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Specifies settings related to the PUSCH allocation, for carrier <cc>, allocation <a> in segment <no>. The ranges for the
		allocated RBs have dependencies, see 'Resource Elements, Grids and Blocks'. \n
			:param structure: for set value, see the help for PuschStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh', structure)

	def get(self, sEGMent=repcap.SEGMent.Default, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> PuschStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<cc>]:ALLocation<Allocation>:PUSCh \n
		Snippet: value: PuschStruct = driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.get(sEGMent = repcap.SEGMent.Default, carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Specifies settings related to the PUSCH allocation, for carrier <cc>, allocation <a> in segment <no>. The ranges for the
		allocated RBs have dependencies, see 'Resource Elements, Grids and Blocks'. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for PuschStruct structure arguments."""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh?', self.__class__.PuschStruct())

	def clone(self) -> 'Pusch':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pusch(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
