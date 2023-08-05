from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMask:
	"""SeMask commands group definition. 4 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("seMask", core, parent)

	@property
	def obwLimit(self):
		"""obwLimit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_obwLimit'):
			from .SeMask_.ObwLimit import ObwLimit
			self._obwLimit = ObwLimit(self._core, self._base)
		return self._obwLimit

	@property
	def area(self):
		"""area commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_area'):
			from .SeMask_.Area import Area
			self._area = Area(self._core, self._base)
		return self._area

	# noinspection PyTypeChecker
	class AtToleranceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tol_2330: float: Test tolerance for carrier frequencies ≥ 23.45 GHz and ≤ 32.125 GHz
			- Tol_3040: float: Test tolerance for carrier frequencies 32.125 GHz and ≤ 40.8 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Tol_2330'),
			ArgStruct.scalar_float('Tol_3040')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tol_2330: float = None
			self.Tol_3040: float = None

	def get_at_tolerance(self) -> AtToleranceStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance \n
		Snippet: value: AtToleranceStruct = driver.configure.nrMmwMeas.multiEval.limit.seMask.get_at_tolerance() \n
		Defines the test tolerance for spectrum emission masks, depending on the carrier frequency. \n
			:return: structure: for return value, see the help for AtToleranceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance?', self.__class__.AtToleranceStruct())

	def set_at_tolerance(self, value: AtToleranceStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.seMask.set_at_tolerance(value = AtToleranceStruct()) \n
		Defines the test tolerance for spectrum emission masks, depending on the carrier frequency. \n
			:param value: see the help for AtToleranceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:SEMask:ATTolerance', value)

	def clone(self) -> 'SeMask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SeMask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
