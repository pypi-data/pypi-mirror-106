from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tolerance: int: No parameter help available
			- Off_Power_Before: float: No parameter help available
			- On_Power_Rms: float: No parameter help available
			- On_Power_Peak: float: No parameter help available
			- Off_Power_After: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Off_Power_Before'),
			ArgStruct.scalar_float('On_Power_Rms'),
			ArgStruct.scalar_float('On_Power_Peak'),
			ArgStruct.scalar_float('Off_Power_After')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Off_Power_Before: float = None
			self.On_Power_Rms: float = None
			self.On_Power_Peak: float = None
			self.Off_Power_After: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:PRACh:PDYNamics:CURRent \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.pdynamics.current.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:PRACh:PDYNamics:CURRent?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:PDYNamics:CURRent \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.pdynamics.current.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:PDYNamics:CURRent?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tolerance: int: No parameter help available
			- Off_Power_Before: float: No parameter help available
			- On_Power_Rms: float: No parameter help available
			- On_Power_Peak: float: No parameter help available
			- Off_Power_After: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Off_Power_Before'),
			ArgStruct.scalar_float('On_Power_Rms'),
			ArgStruct.scalar_float('On_Power_Peak'),
			ArgStruct.scalar_float('Off_Power_After')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Off_Power_Before: float = None
			self.On_Power_Rms: float = None
			self.On_Power_Peak: float = None
			self.Off_Power_After: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:PRACh:PDYNamics:CURRent \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.prach.pdynamics.current.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:PRACh:PDYNamics:CURRent?', self.__class__.CalculateStruct())
