from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("range", core, parent)

	def get_lower(self) -> float:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:FREQuency:RANGe:LOWer \n
		Snippet: value: float = driver.source.efrontend.alignment.file.frequency.range.get_lower() \n
		No command help available \n
			:return: cable_corr_freq_lo: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:FILE:FREQuency:RANGe:LOWer?')
		return Conversions.str_to_float(response)

	def get_upper(self) -> float:
		"""SCPI: [SOURce<HW>]:EFRontend:ALIGnment:FILE:FREQuency:RANGe:UPPer \n
		Snippet: value: float = driver.source.efrontend.alignment.file.frequency.range.get_upper() \n
		No command help available \n
			:return: cable_corr_freq_up: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:ALIGnment:FILE:FREQuency:RANGe:UPPer?')
		return Conversions.str_to_float(response)
