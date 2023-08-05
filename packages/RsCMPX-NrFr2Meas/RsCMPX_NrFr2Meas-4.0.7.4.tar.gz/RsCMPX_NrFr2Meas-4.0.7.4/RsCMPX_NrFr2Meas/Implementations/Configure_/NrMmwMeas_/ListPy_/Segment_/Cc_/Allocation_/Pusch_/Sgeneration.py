from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.StructBase import StructBase
from .........Internal.ArgStruct import ArgStruct
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sgeneration:
	"""Sgeneration commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sgeneration", core, parent)

	# noinspection PyTypeChecker
	class SgenerationStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Initialization: enums.Initialization: CID: cell ID used DMRSid: DMRS ID used
			- Dmrs_Id: int: ID for Initialization = DMRSid.
			- Nscid: int: Parameter nSCID."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Initialization', enums.Initialization),
			ArgStruct.scalar_int('Dmrs_Id'),
			ArgStruct.scalar_int('Nscid')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Initialization: enums.Initialization = None
			self.Dmrs_Id: int = None
			self.Nscid: int = None

	def set(self, structure: SgenerationStruct, sEGMent=repcap.SEGMent.Default, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<cc>]:ALLocation<Allocation>:PUSCh:SGENeration \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.sgeneration.set(value = [PROPERTY_STRUCT_NAME](), sEGMent = repcap.SEGMent.Default, carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Configures the initialization of the DM-RS sequence generation, for carrier <cc>, allocation <a> in segment <no>. \n
			:param structure: for set value, see the help for SgenerationStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:SGENeration', structure)

	def get(self, sEGMent=repcap.SEGMent.Default, carrierComponent=repcap.CarrierComponent.Default, allocation=repcap.Allocation.Default) -> SgenerationStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>[:CC<cc>]:ALLocation<Allocation>:PUSCh:SGENeration \n
		Snippet: value: SgenerationStruct = driver.configure.nrMmwMeas.listPy.segment.cc.allocation.pusch.sgeneration.get(sEGMent = repcap.SEGMent.Default, carrierComponent = repcap.CarrierComponent.Default, allocation = repcap.Allocation.Default) \n
		Configures the initialization of the DM-RS sequence generation, for carrier <cc>, allocation <a> in segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param allocation: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Allocation')
			:return: structure: for return value, see the help for SgenerationStruct structure arguments."""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		allocation_cmd_val = self._base.get_repcap_cmd_value(allocation, repcap.Allocation)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:CC{carrierComponent_cmd_val}:ALLocation{allocation_cmd_val}:PUSCh:SGENeration?', self.__class__.SgenerationStruct())
