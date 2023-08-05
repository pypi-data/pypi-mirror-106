from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 22 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def segment(self):
		"""segment commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .ListPy_.Segment import Segment
			self._segment = Segment(self._core, self._base)
		return self._segment

	# noinspection PyTypeChecker
	class LrangeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: First measured segment in the range of configured segments
			- Nr_Segments: int: Number of measured segments"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Nr_Segments')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Nr_Segments: int = None

	def get_lrange(self) -> LrangeStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:LRANge \n
		Snippet: value: LrangeStruct = driver.configure.nrMmwMeas.listPy.get_lrange() \n
		Select a range of measured segments. \n
			:return: structure: for return value, see the help for LrangeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:LIST:LRANge?', self.__class__.LrangeStruct())

	def set_lrange(self, value: LrangeStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:LRANge \n
		Snippet: driver.configure.nrMmwMeas.listPy.set_lrange(value = LrangeStruct()) \n
		Select a range of measured segments. \n
			:param value: see the help for LrangeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:LIST:LRANge', value)

	def get_os_index(self) -> int or bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:OSINdex \n
		Snippet: value: int or bool = driver.configure.nrMmwMeas.listPy.get_os_index() \n
		Selects the number of the segment to be displayed in offline mode. The index refers to the range of measured segments,
		see method RsCMPX_NrFr2Meas.Configure.NrMmwMeas.ListPy.lrange. Setting a value also enables the offline mode. \n
			:return: offline_seg_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:LIST:OSINdex?')
		return Conversions.str_to_int_or_bool(response)

	def set_os_index(self, offline_seg_index: int or bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:OSINdex \n
		Snippet: driver.configure.nrMmwMeas.listPy.set_os_index(offline_seg_index = 1) \n
		Selects the number of the segment to be displayed in offline mode. The index refers to the range of measured segments,
		see method RsCMPX_NrFr2Meas.Configure.NrMmwMeas.ListPy.lrange. Setting a value also enables the offline mode. \n
			:param offline_seg_index: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(offline_seg_index)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:OSINdex {param}')

	def get_value(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST \n
		Snippet: value: bool = driver.configure.nrMmwMeas.listPy.get_value() \n
		Enables or disables the list mode. \n
			:return: enable: OFF: Disable list mode ON: Enable list mode
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST \n
		Snippet: driver.configure.nrMmwMeas.listPy.set_value(enable = False) \n
		Enables or disables the list mode. \n
			:param enable: OFF: Disable list mode ON: Enable list mode
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
