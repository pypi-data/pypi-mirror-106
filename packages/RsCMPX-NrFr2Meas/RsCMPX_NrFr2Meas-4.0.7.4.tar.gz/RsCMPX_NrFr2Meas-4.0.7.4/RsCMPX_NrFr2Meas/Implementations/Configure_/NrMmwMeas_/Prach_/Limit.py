from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_ev_magnitude(self) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.nrMmwMeas.prach.limit.get_ev_magnitude() \n
		No command help available \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:EVMagnitude \n
		Snippet: driver.configure.nrMmwMeas.prach.limit.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		No command help available \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:EVMagnitude', value)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_merror(self) -> MerrorStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.nrMmwMeas.prach.limit.get_merror() \n
		No command help available \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:MERRor \n
		Snippet: driver.configure.nrMmwMeas.prach.limit.set_merror(value = MerrorStruct()) \n
		No command help available \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:MERRor', value)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_perror(self) -> PerrorStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.nrMmwMeas.prach.limit.get_perror() \n
		No command help available \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PERRor \n
		Snippet: driver.configure.nrMmwMeas.prach.limit.set_perror(value = PerrorStruct()) \n
		No command help available \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PERRor', value)

	def get_freq_error(self) -> float or bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:FERRor \n
		Snippet: value: float or bool = driver.configure.nrMmwMeas.prach.limit.get_freq_error() \n
		No command help available \n
			:return: frequency_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:FERRor?')
		return Conversions.str_to_float_or_bool(response)

	def set_freq_error(self, frequency_error: float or bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:FERRor \n
		Snippet: driver.configure.nrMmwMeas.prach.limit.set_freq_error(frequency_error = 1.0) \n
		No command help available \n
			:param frequency_error: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(frequency_error)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:FERRor {param}')

	# noinspection PyTypeChecker
	class PdynamicsStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: No parameter help available
			- On_Power_Upper: float: No parameter help available
			- On_Power_Lower: float: No parameter help available
			- Off_Power_Upper: float: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('On_Power_Upper'),
			ArgStruct.scalar_float('On_Power_Lower'),
			ArgStruct.scalar_float('Off_Power_Upper')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.On_Power_Upper: float = None
			self.On_Power_Lower: float = None
			self.Off_Power_Upper: float = None

	def get_pdynamics(self) -> PdynamicsStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics \n
		Snippet: value: PdynamicsStruct = driver.configure.nrMmwMeas.prach.limit.get_pdynamics() \n
		No command help available \n
			:return: structure: for return value, see the help for PdynamicsStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics?', self.__class__.PdynamicsStruct())

	def set_pdynamics(self, value: PdynamicsStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics \n
		Snippet: driver.configure.nrMmwMeas.prach.limit.set_pdynamics(value = PdynamicsStruct()) \n
		No command help available \n
			:param value: see the help for PdynamicsStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LIMit:PDYNamics', value)
