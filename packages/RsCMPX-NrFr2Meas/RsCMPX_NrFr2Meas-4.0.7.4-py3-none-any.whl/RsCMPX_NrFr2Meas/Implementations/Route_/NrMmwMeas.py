from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrMmwMeas:
	"""NrMmwMeas commands group definition. 6 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nrMmwMeas", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_scenario'):
			from .NrMmwMeas_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfSettings'):
			from .NrMmwMeas_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	def get_spath(self) -> str:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SPATh \n
		Snippet: value: str = driver.route.nrMmwMeas.get_spath() \n
		Selects the signal path for the measured signal. For possible values, see CATalog:NRMMw:MEAS<i>:SPATh<stream>?. \n
			:return: signal_path: No help available
		"""
		response = self._core.io.query_str('ROUTe:NRMMw:MEASurement<Instance>:SPATh?')
		return trim_str_response(response)

	def set_spath(self, signal_path: str) -> None:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SPATh \n
		Snippet: driver.route.nrMmwMeas.set_spath(signal_path = '1') \n
		Selects the signal path for the measured signal. For possible values, see CATalog:NRMMw:MEAS<i>:SPATh<stream>?. \n
			:param signal_path: No help available
		"""
		param = Conversions.value_to_quoted_str(signal_path)
		self._core.io.write(f'ROUTe:NRMMw:MEASurement<Instance>:SPATh {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: No parameter help available
			- Controller: str: No parameter help available
			- Rx_Connector: enums.RxConnector: No parameter help available
			- Rf_Converter: enums.RfConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_str('Controller'),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RfConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Controller: str = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rf_Converter: enums.RfConverter = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance> \n
		Snippet: value: ValueStruct = driver.route.nrMmwMeas.get_value() \n
		No command help available \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:NRMMw:MEASurement<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'NrMmwMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrMmwMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
