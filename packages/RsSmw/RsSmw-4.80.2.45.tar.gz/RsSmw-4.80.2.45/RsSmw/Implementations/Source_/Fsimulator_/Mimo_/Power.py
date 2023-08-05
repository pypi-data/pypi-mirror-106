from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("power", core, parent)

	@property
	def coupling(self):
		"""coupling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coupling'):
			from .Power_.Coupling import Coupling
			self._coupling = Coupling(self._core, self._base)
		return self._coupling

	@property
	def display(self):
		"""display commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_display'):
			from .Power_.Display import Display
			self._display = Display(self._core, self._base)
		return self._display

	# noinspection PyTypeChecker
	def get_master(self) -> enums.FadMimoPowMaster:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:POWer:MASTer \n
		Snippet: value: enums.FadMimoPowMaster = driver.source.fsimulator.mimo.power.get_master() \n
		No command help available \n
			:return: master: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:FSIMulator:MIMO:POWer:MASTer?')
		return Conversions.str_to_scalar_enum(response, enums.FadMimoPowMaster)

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
