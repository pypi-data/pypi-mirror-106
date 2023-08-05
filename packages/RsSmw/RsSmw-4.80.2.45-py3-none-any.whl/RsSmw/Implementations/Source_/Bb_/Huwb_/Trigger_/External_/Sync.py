from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sync", core, parent)

	def get_output(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:SYNC:OUTPut \n
		Snippet: value: bool = driver.source.bb.huwb.trigger.external.sync.get_output() \n
		No command help available \n
			:return: output: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:SYNC:OUTPut?')
		return Conversions.str_to_bool(response)

	def set_output(self, output: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:TRIGger:[EXTernal]:SYNC:OUTPut \n
		Snippet: driver.source.bb.huwb.trigger.external.sync.set_output(output = False) \n
		No command help available \n
			:param output: No help available
		"""
		param = Conversions.bool_to_str(output)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:TRIGger:EXTernal:SYNC:OUTPut {param}')
