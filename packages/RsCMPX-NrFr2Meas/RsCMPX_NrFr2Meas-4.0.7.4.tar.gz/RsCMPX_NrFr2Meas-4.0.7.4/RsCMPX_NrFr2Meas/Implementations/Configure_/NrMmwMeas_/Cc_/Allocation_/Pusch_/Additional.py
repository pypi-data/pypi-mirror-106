from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Additional:
	"""Additional commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("additional", core, parent)

	# noinspection PyTypeChecker
	class AdditionalStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Dmrs_Length: int: Length of the DM-RS in symbols. The maximum value is limited by the 'maxLength' setting for the bandwidth part.
			- Cdm_Groups: int: Number of DM-RS CDM groups without data.
			- Dmrs_Power: float: Power of DM-RS relative to the PUSCH power.
			- Antenna_Port: int: Antenna port of the DM-RS."""
		__meta_args_list = [
			ArgStruct.scalar_int('Dmrs_Length'),
			ArgStruct.scalar_int('Cdm_Groups'),
			ArgStruct.scalar_float('Dmrs_Power'),
			ArgStruct.scalar_int('Antenna_Port')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Dmrs_Length: int = None
			self.Cdm_Groups: int = None
			self.Dmrs_Power: float = None
			self.Antenna_Port: int = None

	def set(self, structure: AdditionalStruct, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:ADDitional \n
		Snippet: driver.configure.nrMmwMeas.cc.allocation.pusch.additional.set(value = [PROPERTY_STRUCT_NAME](), carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Configures special PUSCH settings, for carrier <no>, allocation <a>. \n
			:param structure: for set value, see the help for AdditionalStruct structure arguments.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')"""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:ADDitional', structure)

	def get(self, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> AdditionalStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>[:CC<no>]:ALLocation<Allocation>:PUSCh:ADDitional \n
		Snippet: value: AdditionalStruct = driver.configure.nrMmwMeas.cc.allocation.pusch.additional.get(carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Configures special PUSCH settings, for carrier <no>, allocation <a>. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for AdditionalStruct structure arguments."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:ADDitional?', self.__class__.AdditionalStruct())
