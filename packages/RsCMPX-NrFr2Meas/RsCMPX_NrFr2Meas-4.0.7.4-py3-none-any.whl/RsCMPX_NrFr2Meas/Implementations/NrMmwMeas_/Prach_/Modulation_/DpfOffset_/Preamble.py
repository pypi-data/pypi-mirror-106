from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 1 total commands, 0 Sub-groups, 1 group commands
	Repeated Capability: Preamble, default value after init: Preamble.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("preamble", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_preamble_get', 'repcap_preamble_set', repcap.Preamble.Nr1)

	def repcap_preamble_set(self, enum_value: repcap.Preamble) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Preamble.Default
		Default value after init: Preamble.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_preamble_get(self) -> repcap.Preamble:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	def fetch(self, preamble=repcap.Preamble.Default) -> int:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:DPFoffset:PREamble<Number> \n
		Snippet: value: int = driver.nrMmwMeas.prach.modulation.dpfOffset.preamble.fetch(preamble = repcap.Preamble.Default) \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:param preamble: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Preamble')
			:return: prach_freq_offset: No help available"""
		preamble_cmd_val = self._base.get_repcap_cmd_value(preamble, repcap.Preamble)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:PRACh:MODulation:DPFoffset:PREamble{preamble_cmd_val}?', suppressed)
		return Conversions.str_to_int(response)

	def clone(self) -> 'Preamble':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Preamble(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
