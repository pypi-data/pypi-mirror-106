from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Waveform:
	"""Waveform commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("waveform", core, parent)

	def get_create(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:HUWB:WAVeform:CREate \n
		Snippet: value: str = driver.source.bb.huwb.waveform.get_create() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:WAVeform:CREate?')
		return trim_str_response(response)

	def set_create(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:WAVeform:CREate \n
		Snippet: driver.source.bb.huwb.waveform.set_create(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:WAVeform:CREate {param}')
