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

	def read(self, carrierComponent=repcap.CarrierComponent.Default) -> List[float]:
		"""SCPI: READ:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:TRACe:EVMSymbol:CURRent \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.cc.trace.evmSymbol.current.read(carrierComponent = repcap.CarrierComponent.Default) \n
		Returns the values of the EVM vs modulation symbol trace for carrier <no>. See also 'Square EVM'. To select the scope of
		the trace, see method RsCMPX_NrFr2Meas.Configure.NrMmwMeas.MultiEval.Modulation.evmSymbol. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: ratio: Comma-separated list of EVM values, one value per modulation symbol"""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:TRACe:EVMSymbol:CURRent?', suppressed)
		return response

	def fetch(self, carrierComponent=repcap.CarrierComponent.Default) -> List[float]:
		"""SCPI: FETCh:NRMMw:MEASurement<Instance>:MEValuation[:CC<no>]:TRACe:EVMSymbol:CURRent \n
		Snippet: value: List[float] = driver.nrMmwMeas.multiEval.cc.trace.evmSymbol.current.fetch(carrierComponent = repcap.CarrierComponent.Default) \n
		Returns the values of the EVM vs modulation symbol trace for carrier <no>. See also 'Square EVM'. To select the scope of
		the trace, see method RsCMPX_NrFr2Meas.Configure.NrMmwMeas.MultiEval.Modulation.evmSymbol. \n
		Suppressed linked return values: reliability \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: ratio: Comma-separated list of EVM values, one value per modulation symbol"""
		carrierComponent_cmd_val = self._base.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRMMw:MEASurement<Instance>:MEValuation:CC{carrierComponent_cmd_val}:TRACe:EVMSymbol:CURRent?', suppressed)
		return response
