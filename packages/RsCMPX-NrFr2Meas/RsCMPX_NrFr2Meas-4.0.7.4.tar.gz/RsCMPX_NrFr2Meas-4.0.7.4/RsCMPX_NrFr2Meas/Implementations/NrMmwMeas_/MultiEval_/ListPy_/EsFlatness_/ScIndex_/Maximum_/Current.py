from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, maximum=repcap.Maximum.Default) -> List[int]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:ESFLatness:SCINdex:MAXimum<nr>:CURRent \n
		Snippet: value: List[int] = driver.nrMmwMeas.multiEval.listPy.esFlatness.scIndex.maximum.current.fetch(maximum = repcap.Maximum.Default) \n
		Return subcarrier indices of the equalizer spectrum flatness measurement for all measured list mode segments. At these SC
		indices, the current MINimum or MAXimum power of the equalizer coefficients has been detected within the selected range. \n
		Suppressed linked return values: reliability \n
			:param maximum: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Maximum')
			:return: maximum: Comma-separated list of values, one per measured segment"""
		maximum_cmd_val = self._base.get_repcap_cmd_value(maximum, repcap.Maximum)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:ESFLatness:SCINdex:MAXimum{maximum_cmd_val}:CURRent?', suppressed)
		return response
