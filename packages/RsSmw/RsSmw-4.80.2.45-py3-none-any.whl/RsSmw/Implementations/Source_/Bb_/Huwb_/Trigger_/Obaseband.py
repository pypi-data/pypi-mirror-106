from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Obaseband:
	"""Obaseband commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("obaseband", core, parent)

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:DELay \n
		Snippet: value: float = driver.source.bb.huwb.trigger.obaseband.get_delay() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:DELay \n
		Snippet: driver.source.bb.huwb.trigger.obaseband.set_delay(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:INHibit \n
		Snippet: value: int = driver.source.bb.huwb.trigger.obaseband.get_inhibit() \n
		No command help available \n
			:return: inhibit: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:INHibit \n
		Snippet: driver.source.bb.huwb.trigger.obaseband.set_inhibit(inhibit = 1) \n
		No command help available \n
			:param inhibit: No help available
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:INHibit {param}')

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:RDELay \n
		Snippet: value: float = driver.source.bb.huwb.trigger.obaseband.get_rdelay() \n
		No command help available \n
			:return: int_oth_rdelay_sec: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:TDELay \n
		Snippet: value: float = driver.source.bb.huwb.trigger.obaseband.get_tdelay() \n
		No command help available \n
			:return: int_oth_delay_sec: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, int_oth_delay_sec: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:OBASeband:TDELay \n
		Snippet: driver.source.bb.huwb.trigger.obaseband.set_tdelay(int_oth_delay_sec = 1.0) \n
		No command help available \n
			:param int_oth_delay_sec: No help available
		"""
		param = Conversions.decimal_value_to_str(int_oth_delay_sec)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:OBASeband:TDELay {param}')
