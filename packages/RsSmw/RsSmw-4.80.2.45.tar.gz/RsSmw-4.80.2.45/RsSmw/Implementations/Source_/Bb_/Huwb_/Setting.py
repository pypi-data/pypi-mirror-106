from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setting:
	"""Setting commands group definition. 4 total commands, 0 Sub-groups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setting", core, parent)

	def get_catalog(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:CATalog \n
		Snippet: value: List[str] = driver.source.bb.huwb.setting.get_catalog() \n
		No command help available \n
			:return: hrp_uwb_cat_name: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SETTing:CATalog?')
		return Conversions.str_to_str_list(response)

	def get_delete(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:DELete \n
		Snippet: value: str = driver.source.bb.huwb.setting.get_delete() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SETTing:DELete?')
		return trim_str_response(response)

	def set_delete(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:DELete \n
		Snippet: driver.source.bb.huwb.setting.set_delete(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SETTing:DELete {param}')

	def get_load(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:LOAD \n
		Snippet: value: str = driver.source.bb.huwb.setting.get_load() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SETTing:LOAD?')
		return trim_str_response(response)

	def set_load(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:LOAD \n
		Snippet: driver.source.bb.huwb.setting.set_load(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SETTing:LOAD {param}')

	def get_store(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:STORe \n
		Snippet: value: str = driver.source.bb.huwb.setting.get_store() \n
		No command help available \n
			:return: filename: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SETTing:STORe?')
		return trim_str_response(response)

	def set_store(self, filename: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SETTing:STORe \n
		Snippet: driver.source.bb.huwb.setting.set_store(filename = '1') \n
		No command help available \n
			:param filename: No help available
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SETTing:STORe {param}')
