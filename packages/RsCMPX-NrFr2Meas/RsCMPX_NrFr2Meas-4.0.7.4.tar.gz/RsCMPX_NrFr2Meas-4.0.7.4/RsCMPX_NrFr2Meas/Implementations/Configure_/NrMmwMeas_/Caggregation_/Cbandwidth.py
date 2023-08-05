from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbandwidth:
	"""Cbandwidth commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cbandwidth", core, parent)

	def get_aggregated(self) -> float:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:CBANdwidth:AGGRegated \n
		Snippet: value: float = driver.configure.nrMmwMeas.caggregation.cbandwidth.get_aggregated() \n
		Queries the width of the aggregated channel bandwidth. \n
			:return: agg_bandwidth: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:CAGGregation:CBANdwidth:AGGRegated?')
		return Conversions.str_to_float(response)
