from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 30 total commands, 7 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prach", core, parent)

	@property
	def pfOffset(self):
		"""pfOffset commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pfOffset'):
			from .Prach_.PfOffset import PfOffset
			self._pfOffset = PfOffset(self._core, self._base)
		return self._pfOffset

	@property
	def sindex(self):
		"""sindex commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_sindex'):
			from .Prach_.Sindex import Sindex
			self._sindex = Sindex(self._core, self._base)
		return self._sindex

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_modulation'):
			from .Prach_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Prach_.Power import Power
			self._power = Power(self._core, self._base)
		return self._power

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_scount'):
			from .Prach_.Scount import Scount
			self._scount = Scount(self._core, self._base)
		return self._scount

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_result'):
			from .Prach_.Result import Result
			self._result = Result(self._core, self._base)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_limit'):
			from .Prach_.Limit import Limit
			self._limit = Limit(self._core, self._base)
		return self._limit

	def get_timeout(self) -> float:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:TOUT \n
		Snippet: value: float = driver.configure.nrMmwMeas.prach.get_timeout() \n
		No command help available \n
			:return: timeout: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:TOUT?')
		return Conversions.str_to_float(response)

	def set_timeout(self, timeout: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:TOUT \n
		Snippet: driver.configure.nrMmwMeas.prach.set_timeout(timeout = 1.0) \n
		No command help available \n
			:param timeout: No help available
		"""
		param = Conversions.decimal_value_to_str(timeout)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:TOUT {param}')

	# noinspection PyTypeChecker
	def get_repetition(self) -> enums.Repeat:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:REPetition \n
		Snippet: value: enums.Repeat = driver.configure.nrMmwMeas.prach.get_repetition() \n
		No command help available \n
			:return: repetition: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:REPetition?')
		return Conversions.str_to_scalar_enum(response, enums.Repeat)

	def set_repetition(self, repetition: enums.Repeat) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:REPetition \n
		Snippet: driver.configure.nrMmwMeas.prach.set_repetition(repetition = enums.Repeat.CONTinuous) \n
		No command help available \n
			:param repetition: No help available
		"""
		param = Conversions.enum_scalar_to_str(repetition, enums.Repeat)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:REPetition {param}')

	# noinspection PyTypeChecker
	def get_scondition(self) -> enums.StopCondition:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCONdition \n
		Snippet: value: enums.StopCondition = driver.configure.nrMmwMeas.prach.get_scondition() \n
		No command help available \n
			:return: stop_condition: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCONdition?')
		return Conversions.str_to_scalar_enum(response, enums.StopCondition)

	def set_scondition(self, stop_condition: enums.StopCondition) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCONdition \n
		Snippet: driver.configure.nrMmwMeas.prach.set_scondition(stop_condition = enums.StopCondition.NONE) \n
		No command help available \n
			:param stop_condition: No help available
		"""
		param = Conversions.enum_scalar_to_str(stop_condition, enums.StopCondition)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCONdition {param}')

	def get_mo_exception(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:MOEXception \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.get_mo_exception() \n
		No command help available \n
			:return: meas_on_exception: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:MOEXception?')
		return Conversions.str_to_bool(response)

	def set_mo_exception(self, meas_on_exception: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:MOEXception \n
		Snippet: driver.configure.nrMmwMeas.prach.set_mo_exception(meas_on_exception = False) \n
		No command help available \n
			:param meas_on_exception: No help available
		"""
		param = Conversions.bool_to_str(meas_on_exception)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:MOEXception {param}')

	def get_pc_index(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PCINdex \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.get_pc_index() \n
		No command help available \n
			:return: prach_conf_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:PCINdex?')
		return Conversions.str_to_int(response)

	def set_pc_index(self, prach_conf_index: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PCINdex \n
		Snippet: driver.configure.nrMmwMeas.prach.set_pc_index(prach_conf_index = 1) \n
		No command help available \n
			:param prach_conf_index: No help available
		"""
		param = Conversions.decimal_value_to_str(prach_conf_index)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:PCINdex {param}')

	def get_pformat(self) -> float:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFORmat \n
		Snippet: value: float = driver.configure.nrMmwMeas.prach.get_pformat() \n
		No command help available \n
			:return: preamble_format: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFORmat?')
		return Conversions.str_to_float(response)

	def set_pformat(self, preamble_format: float) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFORmat \n
		Snippet: driver.configure.nrMmwMeas.prach.set_pformat(preamble_format = 1.0) \n
		No command help available \n
			:param preamble_format: No help available
		"""
		param = Conversions.decimal_value_to_str(preamble_format)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:PFORmat {param}')

	def get_no_preambles(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:NOPReambles \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.get_no_preambles() \n
		No command help available \n
			:return: number_preamble: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:NOPReambles?')
		return Conversions.str_to_int(response)

	def set_no_preambles(self, number_preamble: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:NOPReambles \n
		Snippet: driver.configure.nrMmwMeas.prach.set_no_preambles(number_preamble = 1) \n
		No command help available \n
			:param number_preamble: No help available
		"""
		param = Conversions.decimal_value_to_str(number_preamble)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:NOPReambles {param}')

	# noinspection PyTypeChecker
	def get_po_preambles(self) -> enums.PeriodPreamble:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:POPReambles \n
		Snippet: value: enums.PeriodPreamble = driver.configure.nrMmwMeas.prach.get_po_preambles() \n
		No command help available \n
			:return: period_preamble: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:POPReambles?')
		return Conversions.str_to_scalar_enum(response, enums.PeriodPreamble)

	def set_po_preambles(self, period_preamble: enums.PeriodPreamble) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:POPReambles \n
		Snippet: driver.configure.nrMmwMeas.prach.set_po_preambles(period_preamble = enums.PeriodPreamble.MS05) \n
		No command help available \n
			:param period_preamble: No help available
		"""
		param = Conversions.enum_scalar_to_str(period_preamble, enums.PeriodPreamble)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:POPReambles {param}')

	# noinspection PyTypeChecker
	def get_sc_spacing(self) -> enums.ScSpacing:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCSPacing \n
		Snippet: value: enums.ScSpacing = driver.configure.nrMmwMeas.prach.get_sc_spacing() \n
		No command help available \n
			:return: sc_spacing: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.ScSpacing)

	def set_sc_spacing(self, sc_spacing: enums.ScSpacing) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCSPacing \n
		Snippet: driver.configure.nrMmwMeas.prach.set_sc_spacing(sc_spacing = enums.ScSpacing.S120k) \n
		No command help available \n
			:param sc_spacing: No help available
		"""
		param = Conversions.enum_scalar_to_str(sc_spacing, enums.ScSpacing)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:SCSPacing {param}')

	def get_lrs_index(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LRSindex \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.get_lrs_index() \n
		No command help available \n
			:return: log_root_seq_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:LRSindex?')
		return Conversions.str_to_int(response)

	def set_lrs_index(self, log_root_seq_index: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:LRSindex \n
		Snippet: driver.configure.nrMmwMeas.prach.set_lrs_index(log_root_seq_index = 1) \n
		No command help available \n
			:param log_root_seq_index: No help available
		"""
		param = Conversions.decimal_value_to_str(log_root_seq_index)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:LRSindex {param}')

	def get_zcz_config(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:ZCZConfig \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.get_zcz_config() \n
		No command help available \n
			:return: zero_corr_zone_con: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:ZCZConfig?')
		return Conversions.str_to_int(response)

	def set_zcz_config(self, zero_corr_zone_con: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:ZCZConfig \n
		Snippet: driver.configure.nrMmwMeas.prach.set_zcz_config(zero_corr_zone_con = 1) \n
		No command help available \n
			:param zero_corr_zone_con: No help available
		"""
		param = Conversions.decimal_value_to_str(zero_corr_zone_con)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:ZCZConfig {param}')

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
