from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Extreme:
	"""Extreme commands group definition. 3 total commands, 0 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("extreme", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Evm_Rms_Low: float: EVM RMS value, low EVM window position
			- Evm_Rms_High: float: EVM RMS value, high EVM window position
			- Evm_Peak_Low: float: EVM peak value, low EVM window position
			- Evm_Peak_High: float: EVM peak value, high EVM window position
			- Mag_Error_Rms_Low: float: Magnitude error RMS value, low EVM window position
			- Mag_Error_Rms_High: float: Magnitude error RMS value, low EVM window position
			- Mag_Error_Peak_Low: float: Magnitude error peak value, low EVM window position
			- Mag_Err_Peak_High: float: Magnitude error peak value, high EVM window position
			- Ph_Error_Rms_Low: float: Phase error RMS value, low EVM window position
			- Ph_Error_Rms_High: float: Phase error RMS value, high EVM window position
			- Ph_Error_Peak_Low: float: Phase error peak value, low EVM window position
			- Ph_Error_Peak_High: float: Phase error peak value, high EVM window position
			- Iq_Offset: float: I/Q origin offset
			- Frequency_Error: float: Carrier frequency error
			- Sample_Clock_Err: float: No parameter help available
			- Timing_Error: float: Transmit time error
			- Tx_Power_Min: float: Minimum user equipment power
			- Tx_Power_Max: float: Maximum user equipment power
			- Peak_Power_Min: float: Minimum user equipment peak power
			- Peak_Power_Max: float: Maximum user equipment peak power
			- Psd_Min: float: No parameter help available
			- Psd_Max: float: No parameter help available
			- Evm_Dmrs_Low: float: EVM DMRS value, low EVM window position
			- Evm_Dmrs_High: float: EVM DMRS value, high EVM window position
			- Mag_Err_Dmrs_Low: float: Magnitude error DMRS value, low EVM window position
			- Mag_Err_Dmrs_High: float: Magnitude error DMRS value, high EVM window position
			- Ph_Error_Dmrs_Low: float: Phase error DMRS value, low EVM window position
			- Ph_Error_Dmrs_High: float: Phase error DMRS value, high EVM window position
			- Freq_Err_Ppm: float: Carrier frequency error in ppm"""
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
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Sample_Clock_Err'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power_Min'),
			ArgStruct.scalar_float('Tx_Power_Max'),
			ArgStruct.scalar_float('Peak_Power_Min'),
			ArgStruct.scalar_float('Peak_Power_Max'),
			ArgStruct.scalar_float('Psd_Min'),
			ArgStruct.scalar_float('Psd_Max'),
			ArgStruct.scalar_float('Evm_Dmrs_Low'),
			ArgStruct.scalar_float('Evm_Dmrs_High'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_Low'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_High'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_Low'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_High'),
			ArgStruct.scalar_float('Freq_Err_Ppm')]

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
			self.Iq_Offset: float = None
			self.Frequency_Error: float = None
			self.Sample_Clock_Err: float = None
			self.Timing_Error: float = None
			self.Tx_Power_Min: float = None
			self.Tx_Power_Max: float = None
			self.Peak_Power_Min: float = None
			self.Peak_Power_Max: float = None
			self.Psd_Min: float = None
			self.Psd_Max: float = None
			self.Evm_Dmrs_Low: float = None
			self.Evm_Dmrs_High: float = None
			self.Mag_Err_Dmrs_Low: float = None
			self.Mag_Err_Dmrs_High: float = None
			self.Ph_Error_Dmrs_Low: float = None
			self.Ph_Error_Dmrs_High: float = None
			self.Freq_Err_Ppm: float = None

	def read(self, carrierComponent=repcap.CarrierComponent.Default) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:MODulation:EXTReme \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.cc.modulation.extreme.read(carrierComponent = repcap.CarrierComponent.Default) \n
		Return the extreme single value results for carrier <no>. The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:MODulation:EXTReme?', self.__class__.ResultData())

	def fetch(self, carrierComponent=repcap.CarrierComponent.Default) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:MODulation:EXTReme \n
		Snippet: value: ResultData = driver.nrMmwMeas.multiEval.cc.modulation.extreme.fetch(carrierComponent = repcap.CarrierComponent.Default) \n
		Return the extreme single value results for carrier <no>. The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:MODulation:EXTReme?', self.__class__.ResultData())

	# noinspection PyTypeChecker
	class CalculateStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Evm_Rms_Low: float: EVM RMS value, low EVM window position
			- Evm_Rms_High: float: EVM RMS value, high EVM window position
			- Evm_Peak_Low: float: EVM peak value, low EVM window position
			- Evm_Peak_High: float: EVM peak value, high EVM window position
			- Mag_Error_Rms_Low: float: Magnitude error RMS value, low EVM window position
			- Mag_Error_Rms_High: float: Magnitude error RMS value, low EVM window position
			- Mag_Error_Peak_Low: float: Magnitude error peak value, low EVM window position
			- Mag_Err_Peak_High: float: Magnitude error peak value, high EVM window position
			- Ph_Error_Rms_Low: float: Phase error RMS value, low EVM window position
			- Ph_Error_Rms_High: float: Phase error RMS value, high EVM window position
			- Ph_Error_Peak_Low: float: Phase error peak value, low EVM window position
			- Ph_Error_Peak_High: float: Phase error peak value, high EVM window position
			- Iq_Offset: float: I/Q origin offset
			- Frequency_Error: float: Carrier frequency error
			- Sample_Clock_Err: float: No parameter help available
			- Timing_Error: float: Transmit time error
			- Tx_Power_Min: float: Minimum user equipment power
			- Tx_Power_Max: float: Maximum user equipment power
			- Peak_Power_Min: float: Minimum user equipment peak power
			- Peak_Power_Max: float: Maximum user equipment peak power
			- Psd_Min: float: No parameter help available
			- Psd_Max: float: No parameter help available
			- Evm_Dmrs_Low: float: EVM DMRS value, low EVM window position
			- Evm_Dmrs_High: float: EVM DMRS value, high EVM window position
			- Mag_Err_Dmrs_Low: float: Magnitude error DMRS value, low EVM window position
			- Mag_Err_Dmrs_High: float: Magnitude error DMRS value, high EVM window position
			- Ph_Error_Dmrs_Low: float: Phase error DMRS value, low EVM window position
			- Ph_Error_Dmrs_High: float: Phase error DMRS value, high EVM window position
			- Freq_Err_Ppm: float: Carrier frequency error in ppm"""
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
			ArgStruct.scalar_float('Iq_Offset'),
			ArgStruct.scalar_float('Frequency_Error'),
			ArgStruct.scalar_float('Sample_Clock_Err'),
			ArgStruct.scalar_float('Timing_Error'),
			ArgStruct.scalar_float('Tx_Power_Min'),
			ArgStruct.scalar_float('Tx_Power_Max'),
			ArgStruct.scalar_float('Peak_Power_Min'),
			ArgStruct.scalar_float('Peak_Power_Max'),
			ArgStruct.scalar_float('Psd_Min'),
			ArgStruct.scalar_float('Psd_Max'),
			ArgStruct.scalar_float('Evm_Dmrs_Low'),
			ArgStruct.scalar_float('Evm_Dmrs_High'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_Low'),
			ArgStruct.scalar_float('Mag_Err_Dmrs_High'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_Low'),
			ArgStruct.scalar_float('Ph_Error_Dmrs_High'),
			ArgStruct.scalar_float('Freq_Err_Ppm')]

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
			self.Iq_Offset: float = None
			self.Frequency_Error: float = None
			self.Sample_Clock_Err: float = None
			self.Timing_Error: float = None
			self.Tx_Power_Min: float = None
			self.Tx_Power_Max: float = None
			self.Peak_Power_Min: float = None
			self.Peak_Power_Max: float = None
			self.Psd_Min: float = None
			self.Psd_Max: float = None
			self.Evm_Dmrs_Low: float = None
			self.Evm_Dmrs_High: float = None
			self.Mag_Err_Dmrs_Low: float = None
			self.Mag_Err_Dmrs_High: float = None
			self.Ph_Error_Dmrs_Low: float = None
			self.Ph_Error_Dmrs_High: float = None
			self.Freq_Err_Ppm: float = None

	def calculate(self, carrierComponent=repcap.CarrierComponent.Default) -> CalculateStruct:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:MODulation:EXTReme \n
		Snippet: value: CalculateStruct = driver.nrMmwMeas.multiEval.cc.modulation.extreme.calculate(carrierComponent = repcap.CarrierComponent.Default) \n
		Return the extreme single value results for carrier <no>. The values described below are returned by FETCh and READ
		commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: structure: for return value, see the help for CalculateStruct structure arguments."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		return self._core.io.query_struct(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:MODulation:EXTReme?', self.__class__.CalculateStruct())
