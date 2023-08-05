from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("data", core, parent)

	def get_dselection(self) -> str:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DATA:DSELection \n
		Snippet: value: str = driver.source.bb.huwb.fconfig.data.get_dselection() \n
		No command help available \n
			:return: dselection: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:DATA:DSELection?')
		return trim_str_response(response)

	def set_dselection(self, dselection: str) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DATA:DSELection \n
		Snippet: driver.source.bb.huwb.fconfig.data.set_dselection(dselection = '1') \n
		No command help available \n
			:param dselection: No help available
		"""
		param = Conversions.value_to_quoted_str(dselection)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:DATA:DSELection {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.HrpUwbDataSource:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DATA \n
		Snippet: value: enums.HrpUwbDataSource = driver.source.bb.huwb.fconfig.data.get_value() \n
		No command help available \n
			:return: data_source: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:DATA?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbDataSource)

	def set_value(self, data_source: enums.HrpUwbDataSource) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DATA \n
		Snippet: driver.source.bb.huwb.fconfig.data.set_value(data_source = enums.HrpUwbDataSource.ONE) \n
		No command help available \n
			:param data_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(data_source, enums.HrpUwbDataSource)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:DATA {param}')
