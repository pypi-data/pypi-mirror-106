from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	# noinspection PyTypeChecker
	class AclrStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Aclr_Statistics: int: Statistical length in slots
			- Aclr_Enable: bool: Enable or disable the measurement of ACLR results"""
		__meta_args_list = [
			ArgStruct.scalar_int('Aclr_Statistics'),
			ArgStruct.scalar_bool('Aclr_Enable')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Aclr_Statistics: int = None
			self.Aclr_Enable: bool = None

	def set(self, structure: AclrStruct, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:ACLR \n
		Snippet: driver.configure.nrMmwMeas.listPy.segment.aclr.set(value = [PROPERTY_STRUCT_NAME](), sEGMent = repcap.SEGMent.Default) \n
		Defines settings for ACLR measurements in list mode for segment <no>. \n
			:param structure: for set value, see the help for AclrStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:ACLR', structure)

	def get(self, sEGMent=repcap.SEGMent.Default) -> AclrStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent<no>:ACLR \n
		Snippet: value: AclrStruct = driver.configure.nrMmwMeas.listPy.segment.aclr.get(sEGMent = repcap.SEGMent.Default) \n
		Defines settings for ACLR measurements in list mode for segment <no>. \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for AclrStruct structure arguments."""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:ACLR?', self.__class__.AclrStruct())
