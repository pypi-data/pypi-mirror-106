from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatness:
	"""EsFlatness commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esFlatness", core, parent)

	def read(self, carrierComponent=repcap.CarrierComponent.Default) -> List[float]:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:TRACe:ESFLatness \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.cc.trace.esFlatness.read(carrierComponent = repcap.CarrierComponent.Default) \n
		Returns the values of the equalizer spectrum flatness trace for carrier <no>. See also 'Square Equalizer Spectrum
		Flatness'. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: power: Comma-separated list of power values, one value per subcarrier For not allocated subcarriers, NCAP is returned."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:TRACe:ESFLatness?', suppressed)
		return response

	def fetch(self, carrierComponent=repcap.CarrierComponent.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:TRACe:ESFLatness \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.cc.trace.esFlatness.fetch(carrierComponent = repcap.CarrierComponent.Default) \n
		Returns the values of the equalizer spectrum flatness trace for carrier <no>. See also 'Square Equalizer Spectrum
		Flatness'. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: power: Comma-separated list of power values, one value per subcarrier For not allocated subcarriers, NCAP is returned."""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:TRACe:ESFLatness?', suppressed)
		return response
