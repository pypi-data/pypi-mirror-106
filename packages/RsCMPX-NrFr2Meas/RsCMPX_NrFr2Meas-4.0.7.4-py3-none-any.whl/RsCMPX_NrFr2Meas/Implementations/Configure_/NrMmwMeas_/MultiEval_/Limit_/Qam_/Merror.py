from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Merror:
	"""Merror commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("merror", core, parent)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def set(self, structure: MerrorStruct, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:MERRor \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.qam.merror.set(value = [PROPERTY_STRUCT_NAME](), qam = repcap.Qam.Default) \n
		Defines upper limits for the RMS and peak values of the magnitude error for QAM modulations. \n
			:param structure: for set value, see the help for MerrorStruct structure arguments.
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')"""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:MERRor', structure)

	def get(self, qam=repcap.Qam.Default) -> MerrorStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.nrMmwMeas.multiEval.limit.qam.merror.get(qam = repcap.Qam.Default) \n
		Defines upper limits for the RMS and peak values of the magnitude error for QAM modulations. \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for MerrorStruct structure arguments."""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:MERRor?', self.__class__.MerrorStruct())
