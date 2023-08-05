from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, ripple=repcap.Ripple.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:ESFLatness:RIPPle<nr>:CURRent \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.listPy.esFlatness.ripple.current.fetch(ripple = repcap.Ripple.Default) \n
		Return equalizer spectrum flatness single value results (ripple 1 or ripple 2) for all measured list mode segments. The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param ripple: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ripple')
			:return: ripple: Comma-separated list of values, one per measured segment"""
		ripple_cmd_val = self._base.get_repcap_cmd_value(ripple, repcap.Ripple)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:LIST:ESFLatness:RIPPle{ripple_cmd_val}:CURRent?', suppressed)
		return response

	def calculate(self, ripple=repcap.Ripple.Default) -> List[float]:
		"""SCPI: CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:ESFLatness:RIPPle<nr>:CURRent \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.listPy.esFlatness.ripple.current.calculate(ripple = repcap.Ripple.Default) \n
		Return equalizer spectrum flatness single value results (ripple 1 or ripple 2) for all measured list mode segments. The
		values described below are returned by FETCh commands. CALCulate commands return limit check results instead, one value
		for each result listed below. \n
		Suppressed linked return values: reliability \n
			:param ripple: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ripple')
			:return: ripple: Comma-separated list of values, one per measured segment"""
		ripple_cmd_val = self._base.get_repcap_cmd_value(ripple, repcap.Ripple)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:NRMMw:MEASurement<Instance>:MEValuation:LIST:ESFLatness:RIPPle{ripple_cmd_val}:CURRent?', suppressed)
		return response
