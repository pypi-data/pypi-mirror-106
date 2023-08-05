from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 17 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("filterPy", core, parent)

	@property
	def parameter(self):
		"""parameter commands group. 2 Sub-classes, 8 commands."""
		if not hasattr(self, '_parameter'):
			from .FilterPy_.Parameter import Parameter
			self._parameter = Parameter(self._core, self._base)
		return self._parameter

	def get_auto(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:AUTO \n
		Snippet: value: bool = driver.source.bb.huwb.filterPy.get_auto() \n
		No command help available \n
			:return: auto: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FILTer:AUTO?')
		return Conversions.str_to_bool(response)

	# noinspection PyTypeChecker
	def get_osampling(self) -> enums.HrpUwbOverSampling:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:OSAMpling \n
		Snippet: value: enums.HrpUwbOverSampling = driver.source.bb.huwb.filterPy.get_osampling() \n
		No command help available \n
			:return: over_sampling: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FILTer:OSAMpling?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbOverSampling)

	def set_osampling(self, over_sampling: enums.HrpUwbOverSampling) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:OSAMpling \n
		Snippet: driver.source.bb.huwb.filterPy.set_osampling(over_sampling = enums.HrpUwbOverSampling.OS_1) \n
		No command help available \n
			:param over_sampling: No help available
		"""
		param = Conversions.enum_scalar_to_str(over_sampling, enums.HrpUwbOverSampling)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FILTer:OSAMpling {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DmFilterB:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:TYPE \n
		Snippet: value: enums.DmFilterB = driver.source.bb.huwb.filterPy.get_type_py() \n
		No command help available \n
			:return: type_py: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DmFilterB)

	def set_type_py(self, type_py: enums.DmFilterB) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FILTer:TYPE \n
		Snippet: driver.source.bb.huwb.filterPy.set_type_py(type_py = enums.DmFilterB.APCO25) \n
		No command help available \n
			:param type_py: No help available
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DmFilterB)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FILTer:TYPE {param}')

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
