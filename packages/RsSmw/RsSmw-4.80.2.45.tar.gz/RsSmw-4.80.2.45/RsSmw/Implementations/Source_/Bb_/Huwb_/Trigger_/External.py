from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class External:
	"""External commands group definition. 5 total commands, 1 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("external", core, parent)

	@property
	def sync(self):
		"""sync commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sync'):
			from .External_.Sync import Sync
			self._sync = Sync(self._core, self._base)
		return self._sync

	def get_rdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:EXTernal:RDELay \n
		Snippet: value: float = driver.source.bb.huwb.trigger.external.get_rdelay() \n
		No command help available \n
			:return: res_ext_delay_sec: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:RDELay?')
		return Conversions.str_to_float(response)

	def get_tdelay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:EXTernal:TDELay \n
		Snippet: value: float = driver.source.bb.huwb.trigger.external.get_tdelay() \n
		No command help available \n
			:return: trig_ext_time_del: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:TDELay?')
		return Conversions.str_to_float(response)

	def set_tdelay(self, trig_ext_time_del: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:EXTernal:TDELay \n
		Snippet: driver.source.bb.huwb.trigger.external.set_tdelay(trig_ext_time_del = 1.0) \n
		No command help available \n
			:param trig_ext_time_del: No help available
		"""
		param = Conversions.decimal_value_to_str(trig_ext_time_del)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:TDELay {param}')

	def get_delay(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:DELay \n
		Snippet: value: float = driver.source.bb.huwb.trigger.external.get_delay() \n
		No command help available \n
			:return: delay: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:DELay?')
		return Conversions.str_to_float(response)

	def set_delay(self, delay: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:DELay \n
		Snippet: driver.source.bb.huwb.trigger.external.set_delay(delay = 1.0) \n
		No command help available \n
			:param delay: No help available
		"""
		param = Conversions.decimal_value_to_str(delay)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:DELay {param}')

	def get_inhibit(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:INHibit \n
		Snippet: value: int = driver.source.bb.huwb.trigger.external.get_inhibit() \n
		No command help available \n
			:return: inhibit: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:INHibit?')
		return Conversions.str_to_int(response)

	def set_inhibit(self, inhibit: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:INHibit \n
		Snippet: driver.source.bb.huwb.trigger.external.set_inhibit(inhibit = 1) \n
		No command help available \n
			:param inhibit: No help available
		"""
		param = Conversions.decimal_value_to_str(inhibit)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:INHibit {param}')

	def clone(self) -> 'External':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = External(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
