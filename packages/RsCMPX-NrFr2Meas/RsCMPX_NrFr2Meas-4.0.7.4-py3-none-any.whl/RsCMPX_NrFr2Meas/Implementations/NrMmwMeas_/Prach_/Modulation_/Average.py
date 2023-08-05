from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("average", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tolerance: int: No parameter help available
			- Evm_Rms_Low: float: No parameter help available
			- Evm_Rms_High: float: No parameter help available
			- Evm_Peak_Low: float: No parameter help available
			- Evm_Peak_High: float: No parameter help available
			- Mag_Error_Rms_Low: float: No parameter help available
			- Mag_Error_Rms_High: float: No parameter help available
			- Mag_Error_Peak_Low: float: No parameter help available
			- Mag_Err_Peak_High: float: No parameter help available
			- Ph_Error_Rms_Low: float: No parameter help available
			- Ph_Error_Rms_High: float: No parameter help available
			- Ph_Error_Peak_Low: float: No parameter help available
			- Ph_Error_Peak_High: float: No parameter help available
			- Frequency_Error: float: No parameter help available
			- Timing_Error: float: No parameter help available
			- Tx_Power: float: No parameter help available
			- Peak_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Evm_Rms_Low'),
			ArgStruct.scalar_float('Evm_Rms_High'),
			ArgStruct.scalar_float('Evm_Peak_Low'),
			ArgStruct.scalar_float('Evm_Peak_High'),
			ArgStruct.scalar_float('Mag_Error_Rms_Low'),
			ArgStruct.scalar_float('Mag_Error_Rms_High'),
			ArgStruct.scalar_float('Mag_Error_Peak_Low'),
			ArgStruct.scalar_float('Mag_Err_Peak_High'),
			ArgStruct.scalar_float('Ph_Error_Rms_Low'),
			ArgStruct.scalar_float('Ph_Error_Rms_High'),
			ArgStruct.scalar_float('Ph_Error_Peak_Low'),
			ArgStruct.scalar_float('Ph_Error_Peak_High'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power'),
			ArgStruct.scalar_float('Peak_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms_Low: float = None
			self.Evm_Rms_High: float = None
			self.Evm_Peak_Low: float = None
			self.Evm_Peak_High: float = None
			self.Mag_Error_Rms_Low: float = None
			self.Mag_Error_Rms_High: float = None
			self.Mag_Error_Peak_Low: float = None
			self.Mag_Err_Peak_High: float = None
			self.Ph_Error_Rms_Low: float = None
			self.Ph_Error_Rms_High: float = None
			self.Ph_Error_Peak_Low: float = None
			self.Ph_Error_Peak_High: float = None
			self.Frequency_Error: float = None
			self.Timing_Error: float = None
			self.Tx_Power: float = None
			self.Peak_Power: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:PRACh:MODulation:AVERage \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.modulation.average.read() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:PRACh:MODulation:AVERage?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:AVERage \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.modulation.average.fetch() \n
		No command help available \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:AVERage?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Out_Of_Tolerance: int: No parameter help available
			- Evm_Rms_Low: float: No parameter help available
			- Evm_Rms_High: float: No parameter help available
			- Evm_Peak_Low: float: No parameter help available
			- Evm_Peak_High: float: No parameter help available
			- Mag_Error_Rms_Low: float: No parameter help available
			- Mag_Error_Rms_High: float: No parameter help available
			- Mag_Error_Peak_Low: float: No parameter help available
			- Mag_Err_Peak_High: float: No parameter help available
			- Ph_Error_Rms_Low: float: No parameter help available
			- Ph_Error_Rms_High: float: No parameter help available
			- Ph_Error_Peak_Low: float: No parameter help available
			- Ph_Error_Peak_High: float: No parameter help available
			- Frequency_Error: float: No parameter help available
			- Timing_Error: float: No parameter help available
			- Tx_Power: float: No parameter help available
			- Peak_Power: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Evm_Rms_Low'),
			ArgStruct.scalar_float('Evm_Rms_High'),
			ArgStruct.scalar_float('Evm_Peak_Low'),
			ArgStruct.scalar_float('Evm_Peak_High'),
			ArgStruct.scalar_float('Mag_Error_Rms_Low'),
			ArgStruct.scalar_float('Mag_Error_Rms_High'),
			ArgStruct.scalar_float('Mag_Error_Peak_Low'),
			ArgStruct.scalar_float('Mag_Err_Peak_High'),
			ArgStruct.scalar_float('Ph_Error_Rms_Low'),
			ArgStruct.scalar_float('Ph_Error_Rms_High'),
			ArgStruct.scalar_float('Ph_Error_Peak_Low'),
			ArgStruct.scalar_float('Ph_Error_Peak_High'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power'),
			ArgStruct.scalar_float('Peak_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Evm_Rms_Low: float = None
			self.Evm_Rms_High: float = None
			self.Evm_Peak_Low: float = None
			self.Evm_Peak_High: float = None
			self.Mag_Error_Rms_Low: float = None
			self.Mag_Error_Rms_High: float = None
			self.Mag_Error_Peak_Low: float = None
			self.Mag_Err_Peak_High: float = None
			self.Ph_Error_Rms_Low: float = None
			self.Ph_Error_Rms_High: float = None
			self.Ph_Error_Peak_Low: float = None
			self.Ph_Error_Peak_High: float = None
			self.Frequency_Error: float = None
			self.Timing_Error: float = None
			self.Tx_Power: float = None
			self.Peak_Power: float = None

	def calculate(self) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:PRACh:MODulation:AVERage \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.prach.modulation.average.calculate() \n
		No command help available \n
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:PRACh:MODulation:AVERage?', self.__class__.CalculateStruct())
