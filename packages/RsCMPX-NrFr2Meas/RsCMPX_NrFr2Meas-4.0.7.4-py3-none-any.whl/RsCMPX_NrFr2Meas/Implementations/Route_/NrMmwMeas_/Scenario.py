from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 3 total commands, 1 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .Scenario_.MaProtocol import MaProtocol
			self._maProtocol = MaProtocol(self._core, self._base)
		return self._maProtocol

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: No parameter help available
			- Rf_Converter: enums.RfConverter: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RfConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rf_Converter: enums.RfConverter = None

	# noinspection PyTypeChecker
	def get_salone(self) -> SaloneStruct:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.nrMmwMeas.scenario.get_salone() \n
		No command help available \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())

	def set_salone(self, value: SaloneStruct) -> None:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone \n
		Snippet: driver.route.nrMmwMeas.scenario.set_salone(value = SaloneStruct()) \n
		No command help available \n
			:param value: see the help for SaloneStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:NRMMw:MEASurement<Instance>:SCENario:SALone', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Scenario:
		"""SCPI: ROUTe:NRMMw:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.Scenario = driver.route.nrMmwMeas.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:NRMMw:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.Scenario)

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
