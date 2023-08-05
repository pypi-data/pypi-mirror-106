from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Caggregation:
	"""Caggregation commands group definition. 6 total commands, 3 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("caggregation", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Caggregation_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def cbandwidth(self):
		"""cbandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbandwidth'):
			from .Caggregation_.Cbandwidth import Cbandwidth
			self._cbandwidth = Cbandwidth(self._core, self._base)
		return self._cbandwidth

	@property
	def acSpacing(self):
		"""acSpacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acSpacing'):
			from .Caggregation_.AcSpacing import AcSpacing
			self._acSpacing = AcSpacing(self._core, self._base)
		return self._acSpacing

	# noinspection PyTypeChecker
	def get_mcarrier(self) -> enums.MeasCarrier:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier \n
		Snippet: value: enums.MeasCarrier = driver.configure.nrMmwMeas.caggregation.get_mcarrier() \n
		Selects the measured component carrier for single-carrier measurements (power dynamics) . \n
			:return: meas_carrier: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier?')
		return Conversions.str_to_scalar_enum(response, enums.MeasCarrier)

	def set_mcarrier(self, meas_carrier: enums.MeasCarrier) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier \n
		Snippet: driver.configure.nrMmwMeas.caggregation.set_mcarrier(meas_carrier = enums.MeasCarrier.CC1) \n
		Selects the measured component carrier for single-carrier measurements (power dynamics) . \n
			:param meas_carrier: No help available
		"""
		param = Conversions.enum_scalar_to_str(meas_carrier, enums.MeasCarrier)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:MCARrier {param}')

	def clone(self) -> 'Caggregation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Caggregation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
