from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 6 total commands, 1 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prach", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Prach_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	def get_source(self) -> str:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:SOURce \n
		Snippet: value: str = driver.trigger.nrMmwMeas.prach.get_source() \n
		No command help available \n
			:return: source: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRMMw:MEASurement<Instance>:PRACh:SOURce?')
		return trim_str_response(response)

	def set_source(self, source: str) -> None:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:SOURce \n
		Snippet: driver.trigger.nrMmwMeas.prach.set_source(source = '1') \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.value_to_quoted_str(source)
		self._core.io.write(f'TRIGger:NRMMw:MEASurement<Instance>:PRACh:SOURce {param}')

	def get_threshold(self) -> float or bool:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:THReshold \n
		Snippet: value: float or bool = driver.trigger.nrMmwMeas.prach.get_threshold() \n
		No command help available \n
			:return: trig_threshold: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRMMw:MEASurement<Instance>:PRACh:THReshold?')
		return Conversions.str_to_float_or_bool(response)

	def set_threshold(self, trig_threshold: float or bool) -> None:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:THReshold \n
		Snippet: driver.trigger.nrMmwMeas.prach.set_threshold(trig_threshold = 1.0) \n
		No command help available \n
			:param trig_threshold: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(trig_threshold)
		self._core.io.write(f'TRIGger:NRMMw:MEASurement<Instance>:PRACh:THReshold {param}')

	# noinspection PyTypeChecker
	def get_slope(self) -> enums.SignalSlope:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:SLOPe \n
		Snippet: value: enums.SignalSlope = driver.trigger.nrMmwMeas.prach.get_slope() \n
		No command help available \n
			:return: slope: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRMMw:MEASurement<Instance>:PRACh:SLOPe?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSlope)

	def set_slope(self, slope: enums.SignalSlope) -> None:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:SLOPe \n
		Snippet: driver.trigger.nrMmwMeas.prach.set_slope(slope = enums.SignalSlope.FEDGe) \n
		No command help available \n
			:param slope: No help available
		"""
		param = Conversions.enum_scalar_to_str(slope, enums.SignalSlope)
		self._core.io.write(f'TRIGger:NRMMw:MEASurement<Instance>:PRACh:SLOPe {param}')

	def get_timeout(self) -> float or bool:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:TOUT \n
		Snippet: value: float or bool = driver.trigger.nrMmwMeas.prach.get_timeout() \n
		No command help available \n
			:return: trigger_timeout: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRMMw:MEASurement<Instance>:PRACh:TOUT?')
		return Conversions.str_to_float_or_bool(response)

	def set_timeout(self, trigger_timeout: float or bool) -> None:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:TOUT \n
		Snippet: driver.trigger.nrMmwMeas.prach.set_timeout(trigger_timeout = 1.0) \n
		No command help available \n
			:param trigger_timeout: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(trigger_timeout)
		self._core.io.write(f'TRIGger:NRMMw:MEASurement<Instance>:PRACh:TOUT {param}')

	def get_mgap(self) -> float:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:MGAP \n
		Snippet: value: float = driver.trigger.nrMmwMeas.prach.get_mgap() \n
		No command help available \n
			:return: min_trig_gap: No help available
		"""
		response = self._core.io.query_str('TRIGger:NRMMw:MEASurement<Instance>:PRACh:MGAP?')
		return Conversions.str_to_float(response)

	def set_mgap(self, min_trig_gap: float) -> None:
		"""SCPI: TRIGger:NRMMw:MEASurement<Instance>:PRACh:MGAP \n
		Snippet: driver.trigger.nrMmwMeas.prach.set_mgap(min_trig_gap = 1.0) \n
		No command help available \n
			:param min_trig_gap: No help available
		"""
		param = Conversions.decimal_value_to_str(min_trig_gap)
		self._core.io.write(f'TRIGger:NRMMw:MEASurement<Instance>:PRACh:MGAP {param}')

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
