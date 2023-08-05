from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sindex:
	"""Sindex commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sindex", core, parent)

	def get_auto(self) -> bool:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex:AUTO \n
		Snippet: value: bool = driver.configure.nrMmwMeas.prach.sindex.get_auto() \n
		No command help available \n
			:return: seq_index_auto: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex:AUTO?')
		return Conversions.str_to_bool(response)

	def set_auto(self, seq_index_auto: bool) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex:AUTO \n
		Snippet: driver.configure.nrMmwMeas.prach.sindex.set_auto(seq_index_auto = False) \n
		No command help available \n
			:param seq_index_auto: No help available
		"""
		param = Conversions.bool_to_str(seq_index_auto)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex:AUTO {param}')

	def get_value(self) -> int:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex \n
		Snippet: value: int = driver.configure.nrMmwMeas.prach.sindex.get_value() \n
		No command help available \n
			:return: sequence_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex?')
		return Conversions.str_to_int(response)

	def set_value(self, sequence_index: int) -> None:
		"""SCPI: CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex \n
		Snippet: driver.configure.nrMmwMeas.prach.sindex.set_value(sequence_index = 1) \n
		No command help available \n
			:param sequence_index: No help available
		"""
		param = Conversions.decimal_value_to_str(sequence_index)
		self._core.io.write(f'CONFigure:NRMMw:MEASurement<Instance>:PRACh:SINDex {param}')
