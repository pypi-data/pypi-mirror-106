from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Caggregation:
	"""Caggregation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("caggregation", core, parent)

	# noinspection PyTypeChecker
	class CaggregationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area = FrequencyStart * aggregated channel bandwidth, relative to the edges of the aggregated channel bandwidth
			- Frequency_End: float: Stop frequency of the area = FrequencyEnd * aggregated channel bandwidth, relative to the edges of the aggregated channel bandwidth
			- Level: float: Upper limit for the area
			- Rbw: enums.RbwA: Resolution bandwidth to be used for the area, 120 kHz or 1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.RbwA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.RbwA = None

	def set(self, structure: CaggregationStruct, area=repcap.Area.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<area>:CAGGregation \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.seMask.area.caggregation.set(value = [PROPERTY_STRUCT_NAME](), area = repcap.Area.Default) \n
		Defines general requirements for the emission mask area number <area>. The activation state, the area borders, an upper
		limit and the resolution bandwidth must be specified. The emission mask applies to carrier aggregation (aggregated
		bandwidth) . \n
			:param structure: for set value, see the help for CaggregationStruct structure arguments.
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')"""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:CAGGregation', structure)

	def get(self, area=repcap.Area.Default) -> CaggregationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<area>:CAGGregation \n
		Snippet: value: CaggregationStruct = driver.configure.nrMmwMeas.multiEval.limit.seMask.area.caggregation.get(area = repcap.Area.Default) \n
		Defines general requirements for the emission mask area number <area>. The activation state, the area borders, an upper
		limit and the resolution bandwidth must be specified. The emission mask applies to carrier aggregation (aggregated
		bandwidth) . \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for CaggregationStruct structure arguments."""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:CAGGregation?', self.__class__.CaggregationStruct())
