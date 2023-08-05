from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EePeriods:
	"""EePeriods commands group definition. 3 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("eePeriods", core, parent)

	@property
	def pusch(self):
		"""pusch commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_pusch'):
			from .EePeriods_.Pusch import Pusch
			self._pusch = Pusch(self._core, self._base)
		return self._pusch

	def get_pucch(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:PUCCh \n
		Snippet: value: bool = driver.configure.nrMmwMeas.multiEval.modulation.eePeriods.get_pucch() \n
		No command help available \n
			:return: pucch: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:PUCCh?')
		return Conversions.str_to_bool(response)

	def set_pucch(self, pucch: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:PUCCh \n
		Snippet: driver.configure.nrMmwMeas.multiEval.modulation.eePeriods.set_pucch(pucch = False) \n
		No command help available \n
			:param pucch: No help available
		"""
		param = Conversions.bool_to_str(pucch)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:MEValuation:MODulation:EEPeriods:PUCCh {param}')

	def clone(self) -> 'EePeriods':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EePeriods(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
