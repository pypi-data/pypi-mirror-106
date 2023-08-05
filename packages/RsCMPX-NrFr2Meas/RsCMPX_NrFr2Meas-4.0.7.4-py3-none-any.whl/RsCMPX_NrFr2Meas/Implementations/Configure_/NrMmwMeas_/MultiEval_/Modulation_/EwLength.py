from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Types import DataType
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EwLength:
	"""EwLength commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ewLength", core, parent)

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .EwLength_.Cbandwidth import Cbandwidth
			self._cbandwidth = Cbandwidth(self._core, self._base)
		return self._cbandwidth

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Length_Cp_Norm_60: List[int]: Comma-separated list of 4 values: for 50 MHz, 100 MHz, 200 MHz, 400 MHz Samples for normal CP, 60-kHz SC spacing
			- Length_Cp_Norm_120: List[int]: Comma-separated list of 4 values: for 50 MHz, 100 MHz, 200 MHz, 400 MHz Samples for normal CP, 120-kHz SC spacing"""
		__meta_args_list = [
			ArgStruct('Length_Cp_Norm_60', DataType.IntegerList, None, False, False, 4),
			ArgStruct('Length_Cp_Norm_120', DataType.IntegerList, None, False, False, 4)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Length_Cp_Norm_60: List[int] = None
			self.Length_Cp_Norm_120: List[int] = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength \n
		Snippet: value: ValueStruct = driver.configure.nrMmwMeas.multiEval.modulation.ewLength.get_value() \n
		Specifies the EVM window length in samples for all channel bandwidths, depending on the SC spacing. For ranges and *RST
		values, see Table 'Ranges and *RST values'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.ewLength.set_value(value = ValueStruct()) \n
		Specifies the EVM window length in samples for all channel bandwidths, depending on the SC spacing. For ranges and *RST
		values, see Table 'Ranges and *RST values'. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EWLength', value)

	def clone(self) -> 'EwLength':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EwLength(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
