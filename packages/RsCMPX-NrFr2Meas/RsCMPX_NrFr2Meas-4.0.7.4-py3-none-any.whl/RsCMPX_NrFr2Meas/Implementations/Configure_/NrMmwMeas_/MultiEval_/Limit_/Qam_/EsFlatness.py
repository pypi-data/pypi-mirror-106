from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatness:
	"""EsFlatness commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esFlatness", core, parent)

	# noinspection PyTypeChecker
	class EsFlatnessStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Range_1: float: Upper limit for max(range 1) - min(range 1)
			- Range_2: float: Upper limit for max(range 2) - min(range 2)
			- Max_1_Min_2: float: Upper limit for max(range 1) - min(range 2)
			- Max_2_Min_1: float: Upper limit for max(range 2) - min(range 1)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Range_1'),
			ArgStruct.scalar_float('Range_2'),
			ArgStruct.scalar_float('Max_1_Min_2'),
			ArgStruct.scalar_float('Max_2_Min_1')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Range_1: float = None
			self.Range_2: float = None
			self.Max_1_Min_2: float = None
			self.Max_2_Min_1: float = None

	def set(self, structure: EsFlatnessStruct, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:ESFLatness \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.qam.esFlatness.set(value = [PROPERTY_STRUCT_NAME](), qam = repcap.Qam.Default) \n
		Defines limits for the equalizer spectrum flatness (QAM modulations) . \n
			:param structure: for set value, see the help for EsFlatnessStruct structure arguments.
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')"""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:ESFLatness', structure)

	def get(self, qam=repcap.Qam.Default) -> EsFlatnessStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:ESFLatness \n
		Snippet: value: EsFlatnessStruct = driver.configure.nrMmwMeas.multiEval.limit.qam.esFlatness.get(qam = repcap.Qam.Default) \n
		Defines limits for the equalizer spectrum flatness (QAM modulations) . \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for EsFlatnessStruct structure arguments."""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:ESFLatness?', self.__class__.EsFlatnessStruct())
