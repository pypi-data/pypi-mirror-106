from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	@property
	def nr(self):
		"""nr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nr'):
			from .Aclr_.Nr import Nr
			self._nr = Nr(self._core, self._base)
		return self._nr

	# noinspection PyTypeChecker
	class AtToleranceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tol_2330: float: Test tolerance for carrier frequencies ≥ 23.45 GHz and ≤ 30.3 GHz
			- Tol_3040: float: Test tolerance for carrier frequencies 30.3 GHz and ≤ 40.8 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Tol_2330'),
			ArgStruct.scalar_float('Tol_3040')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tol_2330: float = None
			self.Tol_3040: float = None

	def get_at_tolerance(self) -> AtToleranceStruct:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance \n
		Snippet: value: AtToleranceStruct = driver.configure.nrMmwMeas.multiEval.limit.aclr.get_at_tolerance() \n
		Defines the test tolerance for relative ACLR limits, depending on the carrier frequency. \n
			:return: structure: for return value, see the help for AtToleranceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance?', self.__class__.AtToleranceStruct())

	def set_at_tolerance(self, value: AtToleranceStruct) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance \n
		Snippet: driver.configure.nrMmwMeas.multiEval.limit.aclr.set_at_tolerance(value = AtToleranceStruct()) \n
		Defines the test tolerance for relative ACLR limits, depending on the carrier frequency. \n
			:param value: see the help for AtToleranceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:LIMit:ACLR:ATTolerance', value)

	def clone(self) -> 'Aclr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aclr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
