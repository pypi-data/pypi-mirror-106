from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 2 total commands, 0 Sub-groups, 2 group commands
	Repeated Capability: Preamble, default value after init: Preamble.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("preamble", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_preamble_get', 'repcap_preamble_set', repcap.Preamble.Nr1)

	def repcap_preamble_set(self, enum_value: repcap.Preamble) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Preamble.Default
		Default value after init: Preamble.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_preamble_get(self) -> repcap.Preamble:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: No parameter help available
			- Preamble_Rel: int: No parameter help available
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
			ArgStruct.scalar_int('Preamble_Rel'),
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
			self.Preamble_Rel: int = None
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

	def read(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble<Number> \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.modulation.preamble.read(preamble = repcap.Preamble.Default) \n
		No command help available \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._base.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'READ:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble{preamble_cmd_val}?', self.__class__.ResultData())

	def fetch(self, preamble=repcap.Preamble.Default) -> ResultData:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble<Number> \n
		Snippet: value: ResultData = driver.nrMmwMeas.prach.modulation.preamble.fetch(preamble = repcap.Preamble.Default) \n
		No command help available \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: structure: for return value, see the help for ResultData structure arguments."""
		preamble_cmd_val = self._base.get_repcap_cmd_value(preamble, repcap.Preamble)
		return self._core.io.query_struct(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:PREamble{preamble_cmd_val}?', self.__class__.ResultData())

	def clone(self) -> 'Preamble':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Preamble(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
