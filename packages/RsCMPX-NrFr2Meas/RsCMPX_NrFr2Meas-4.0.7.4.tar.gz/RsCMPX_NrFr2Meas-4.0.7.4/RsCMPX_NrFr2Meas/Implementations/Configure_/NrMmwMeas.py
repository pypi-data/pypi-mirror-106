from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrMmwMeas:
	"""NrMmwMeas commands group definition. 160 total commands, 9 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nrMmwMeas", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenario'):
			from .NrMmwMeas_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	@property
	def rfSettings(self):
		"""rfSettings commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_rfSettings'):
			from .NrMmwMeas_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def ulDl(self):
		"""ulDl commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ulDl'):
			from .NrMmwMeas_.UlDl import UlDl
			self._ulDl = UlDl(self._core, self._base)
		return self._ulDl

	@property
	def cc(self):
		"""cc commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .NrMmwMeas_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def ccall(self):
		"""ccall commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccall'):
			from .NrMmwMeas_.Ccall import Ccall
			self._ccall = Ccall(self._core, self._base)
		return self._ccall

	@property
	def caggregation(self):
		"""caggregation commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_caggregation'):
			from .NrMmwMeas_.Caggregation import Caggregation
			self._caggregation = Caggregation(self._core, self._base)
		return self._caggregation

	@property
	def multiEval(self):
		"""multiEval commands group. 7 Sub-classes, 11 commands."""
		if not hasattr(self, '_multiEval'):
			from .NrMmwMeas_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def listPy(self):
		"""listPy commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_listPy'):
			from .NrMmwMeas_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def prach(self):
		"""prach commands group. 7 Sub-classes, 11 commands."""
		if not hasattr(self, '_prach'):
			from .NrMmwMeas_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	# noinspection PyTypeChecker
	def get_band(self) -> enums.Band:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:BAND \n
		Snippet: value: enums.Band = driver.configure.nrMmwMeas.get_band() \n
		Selects the frequency band. \n
			:return: band: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def set_band(self, band: enums.Band) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:BAND \n
		Snippet: driver.configure.nrMmwMeas.set_band(band = enums.Band.B257) \n
		Selects the frequency band. \n
			:param band: No help available
		"""
		param = Conversions.enum_scalar_to_str(band, enums.Band)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:BAND {param}')

	def get_ncarrier(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NCARrier \n
		Snippet: value: int = driver.configure.nrMmwMeas.get_ncarrier() \n
		Configures the number of contiguously aggregated UL carriers in the measured signal. \n
			:return: meas_carrier: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:NCARrier?')
		return Conversions.str_to_int(response)

	def set_ncarrier(self, meas_carrier: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:NCARrier \n
		Snippet: driver.configure.nrMmwMeas.set_ncarrier(meas_carrier = 1) \n
		Configures the number of contiguously aggregated UL carriers in the measured signal. \n
			:param meas_carrier: No help available
		"""
		param = Conversions.decimal_value_to_str(meas_carrier)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:NCARrier {param}')

	def clone(self) -> 'NrMmwMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrMmwMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
