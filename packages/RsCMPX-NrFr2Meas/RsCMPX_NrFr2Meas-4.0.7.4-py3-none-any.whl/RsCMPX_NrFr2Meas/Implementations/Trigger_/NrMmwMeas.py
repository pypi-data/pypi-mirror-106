from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NrMmwMeas:
	"""NrMmwMeas commands group definition. 15 total commands, 3 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nrMmwMeas", core, parent)

	@property
	def multiEval(self):
		"""multiEval commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_multiEval'):
			from .NrMmwMeas_.MultiEval import MultiEval
			self._multiEval = MultiEval(self._core, self._base)
		return self._multiEval

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .NrMmwMeas_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	@property
	def prach(self):
		"""prach commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_prach'):
			from .NrMmwMeas_.Prach import Prach
			self._prach = Prach(self._core, self._base)
		return self._prach

	def clone(self) -> 'NrMmwMeas':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = NrMmwMeas(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
