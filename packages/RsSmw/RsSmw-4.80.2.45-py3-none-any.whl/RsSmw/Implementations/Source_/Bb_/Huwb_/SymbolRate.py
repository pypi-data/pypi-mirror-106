from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("symbolRate", core, parent)

	def get_variation(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SRATe:VARiation \n
		Snippet: value: float = driver.source.bb.huwb.symbolRate.get_variation() \n
		No command help available \n
			:return: sym_rate_var: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SRATe:VARiation?')
		return Conversions.str_to_float(response)

	def set_variation(self, sym_rate_var: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SRATe:VARiation \n
		Snippet: driver.source.bb.huwb.symbolRate.set_variation(sym_rate_var = 1.0) \n
		No command help available \n
			:param sym_rate_var: No help available
		"""
		param = Conversions.decimal_value_to_str(sym_rate_var)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SRATe:VARiation {param}')
