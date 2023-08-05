from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prach:
	"""Prach commands group definition. 67 total commands, 4 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("prach", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Prach_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Prach_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def modulation(self):
		"""modulation commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .Prach_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def pdynamics(self):
		"""pdynamics commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .Prach_.Pdynamics import Pdynamics
			self._pdynamics = Pdynamics(self._core, self._base)
		return self._pdynamics

	def initiate(self) -> None:
		"""SCPI: INITiate:NRMMw:MEASurement<Instance>:PRACh \n
		Snippet: driver.nrMmwMeas.prach.initiate() \n
		No command help available \n
		"""
		self._core.io.write(f'INITiate:NRMMw:MEASurement<Instance>:PRACh')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:NRMMw:MEASurement<Instance>:PRACh \n
		Snippet: driver.nrMmwMeas.prach.initiate_with_opc() \n
		No command help available \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCMPX_NrFr2Meas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:NRMMw:MEASurement<Instance>:PRACh')

	def stop(self) -> None:
		"""SCPI: STOP:NRMMw:MEASurement<Instance>:PRACh \n
		Snippet: driver.nrMmwMeas.prach.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:NRMMw:MEASurement<Instance>:PRACh')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:NRMMw:MEASurement<Instance>:PRACh \n
		Snippet: driver.nrMmwMeas.prach.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_NrFr2Meas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:NRMMw:MEASurement<Instance>:PRACh')

	def abort(self) -> None:
		"""SCPI: ABORt:NRMMw:MEASurement<Instance>:PRACh \n
		Snippet: driver.nrMmwMeas.prach.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:NRMMw:MEASurement<Instance>:PRACh')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:NRMMw:MEASurement<Instance>:PRACh \n
		Snippet: driver.nrMmwMeas.prach.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_NrFr2Meas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:NRMMw:MEASurement<Instance>:PRACh')

	def clone(self) -> 'Prach':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prach(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
