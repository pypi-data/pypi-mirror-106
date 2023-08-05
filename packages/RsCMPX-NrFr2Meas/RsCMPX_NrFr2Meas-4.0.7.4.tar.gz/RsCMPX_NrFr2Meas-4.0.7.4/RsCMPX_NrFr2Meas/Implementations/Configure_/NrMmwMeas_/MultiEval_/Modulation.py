from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 8 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("modulation", core, parent)

	@property
	def ewLength(self):
		"""ewLength commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ewLength'):
			from .Modulation_.EwLength import EwLength
			self._ewLength = EwLength(self._core, self._base)
		return self._ewLength

	@property
	def eePeriods(self):
		"""eePeriods commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_eePeriods'):
			from .Modulation_.EePeriods import EePeriods
			self._eePeriods = EePeriods(self._core, self._base)
		return self._eePeriods

	@property
	def tracking(self):
		"""tracking commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_tracking'):
			from .Modulation_.Tracking import Tracking
			self._tracking = Tracking(self._core, self._base)
		return self._tracking

	# noinspection PyTypeChecker
	class EvmSymbolStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Symbol: int: OFDM symbol to be evaluated
			- Low_High: enums.LowHigh: Low or high EVM window position"""
		__meta_args_list = [
			ArgStruct.scalar_int('Symbol'),
			ArgStruct.scalar_enum('Low_High', enums.LowHigh)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Symbol: int = None
			self.Low_High: enums.LowHigh = None

	def get_evm_symbol(self) -> EvmSymbolStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol \n
		Snippet: value: EvmSymbolStruct = driver.configure.nrMmwMeas.multiEval.modulation.get_evm_symbol() \n
		Configures the scope of the EVM vs modulation symbol results. \n
			:return: structure: for return value, see the help for EvmSymbolStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol?', self.__class__.EvmSymbolStruct())

	def set_evm_symbol(self, value: EvmSymbolStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.set_evm_symbol(value = EvmSymbolStruct()) \n
		Configures the scope of the EVM vs modulation symbol results. \n
			:param value: see the help for EvmSymbolStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EVMSymbol', value)

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
