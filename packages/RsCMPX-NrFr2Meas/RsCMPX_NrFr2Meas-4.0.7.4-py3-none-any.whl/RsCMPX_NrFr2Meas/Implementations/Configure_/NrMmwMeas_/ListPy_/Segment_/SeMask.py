from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMask:
	"""SeMask commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("seMask", core, parent)

	# noinspection PyTypeChecker
	class SeMaskStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Sem_Statistics: int: Statistical length in slots
			- Sem_Enable: bool: Enable or disable the measurement of spectrum emission results"""
		__meta_args_list = [
			ArgStruct.scalar_int('Sem_Statistics'),
			ArgStruct.scalar_bool('Sem_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sem_Statistics: int = None
			self.Sem_Enable: bool = None

	def set(self, structure: SeMaskStruct, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:SEMask \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.seMask.set(value = [PROPERTY_STRUCT_NAME](), sEGMent = repcap.SEGMent.Default) \n
		Defines settings for spectrum emission measurements in list mode for segment <no>. \n
			:param structure: for set value, see the help for SeMaskStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SEMask', structure)

	def get(self, sEGMent=repcap.SEGMent.Default) -> SeMaskStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:SEMask \n
		Snippet: value: SeMaskStruct = driver.configure.nrMmwMeas.listPy.segment.seMask.get(sEGMent = repcap.SEGMent.Default) \n
		Defines settings for spectrum emission measurements in list mode for segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SeMaskStruct structure arguments."""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SEMask?', self.__class__.SeMaskStruct())
