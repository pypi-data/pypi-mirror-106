from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	def get_modulation(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.result.get_modulation() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation?')
		return Conversions.str_to_bool(response)

	def set_modulation(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_modulation(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:MODulation {param}')

	def get_ev_preamble(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:EVPReamble \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.result.get_ev_preamble() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:EVPReamble?')
		return Conversions.str_to_bool(response)

	def set_ev_preamble(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:EVPReamble \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_ev_preamble(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:EVPReamble {param}')

	def get_pdynamics(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.result.get_pdynamics() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics?')
		return Conversions.str_to_bool(response)

	def set_pdynamics(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_pdynamics(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PDYNamics {param}')

	def get_pv_preamble(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PVPReamble \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.result.get_pv_preamble() \n
		No command help available \n
			:return: enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PVPReamble?')
		return Conversions.str_to_bool(response)

	def set_pv_preamble(self, enable: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PVPReamble \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_pv_preamble(enable = False) \n
		No command help available \n
			:param enable: No help available
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:PVPReamble {param}')

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Modulation: bool: No parameter help available
			- Power_Dynamics: bool: No parameter help available
			- Evm_Vs_Preamble: bool: No parameter help available
			- Power_Vs_Preamble: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Modulation'),
			ArgStruct.scalar_bool('Power_Dynamics'),
			ArgStruct.scalar_bool('Evm_Vs_Preamble'),
			ArgStruct.scalar_bool('Power_Vs_Preamble')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Modulation: bool = None
			self.Power_Dynamics: bool = None
			self.Evm_Vs_Preamble: bool = None
			self.Power_Vs_Preamble: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.nrMmwMeas.prach.result.get_all() \n
		No command help available \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult[:ALL] \n
		Snippet: driver.configure.nrMmwMeas.prach.result.set_all(value = AllStruct()) \n
		No command help available \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:PRACh:RESult:ALL', value)
