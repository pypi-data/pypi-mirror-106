from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Efrontend:
	"""Efrontend commands group definition. 17 total commands, 3 Sub-groups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("efrontend", core, parent)

	@property
	def alignment(self):
		"""alignment commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_alignment'):
			from .Efrontend_.Alignment import Alignment
			self._alignment = Alignment(self._core, self._base)
		return self._alignment

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Efrontend_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def firmwareUpdate(self):
		"""firmwareUpdate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_firmwareUpdate'):
			from .Efrontend_.FirmwareUpdate import FirmwareUpdate
			self._firmwareUpdate = FirmwareUpdate(self._core, self._base)
		return self._firmwareUpdate

	def get_did(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:DID \n
		Snippet: value: str = driver.source.efrontend.get_did() \n
		Queries the device ID of the external frontends connected to the R&S SMW. \n
			:return: fe_dev_id: string MaterialNumber-SerialNumber
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:DID?')
		return trim_str_response(response)

	def get_idn(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:IDN \n
		Snippet: value: str = driver.source.efrontend.get_idn() \n
		No command help available \n
			:return: idn_string: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:IDN?')
		return trim_str_response(response)

	def get_info(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:INFO \n
		Snippet: value: str = driver.source.efrontend.get_info() \n
		Queries information about the connected external frontend. \n
			:return: fe_info: string
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:INFO?')
		return trim_str_response(response)

	def get_ip_address(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:IPADdress \n
		Snippet: value: str = driver.source.efrontend.get_ip_address() \n
		No command help available \n
			:return: ip_address: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:IPADdress?')
		return trim_str_response(response)

	def get_list_py(self) -> List[str]:
		"""SCPI: [SOURce<HW>]:EFRontend:LIST \n
		Snippet: value: List[str] = driver.source.efrontend.get_list_py() \n
		Queries connected external frontends in a comma-separated list. \n
			:return: freq_conv_fe_cat: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:LIST?')
		return Conversions.str_to_str_list(response)

	def get_opt(self) -> str:
		"""SCPI: [SOURce<HW>]:EFRontend:OPT \n
		Snippet: value: str = driver.source.efrontend.get_opt() \n
		No command help available \n
			:return: opt_string: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:OPT?')
		return trim_str_response(response)

	# noinspection PyTypeChecker
	def get_rf_connector(self) -> enums.FenUmbRfCon:
		"""SCPI: [SOURce<HW>]:EFRontend:RFConnector \n
		Snippet: value: enums.FenUmbRfCon = driver.source.efrontend.get_rf_connector() \n
		Sets the active RF output connector at the connected RF frontend. \n
			:return: fe_output_path: NONE| RF1| RF2| RF3| RF4
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:EFRontend:RFConnector?')
		return Conversions.str_to_scalar_enum(response, enums.FenUmbRfCon)

	def set_rf_connector(self, fe_output_path: enums.FenUmbRfCon) -> None:
		"""SCPI: [SOURce<HW>]:EFRontend:RFConnector \n
		Snippet: driver.source.efrontend.set_rf_connector(fe_output_path = enums.FenUmbRfCon.NONE) \n
		Sets the active RF output connector at the connected RF frontend. \n
			:param fe_output_path: NONE| RF1| RF2| RF3| RF4
		"""
		param = Conversions.enum_scalar_to_str(fe_output_path, enums.FenUmbRfCon)
		self._core.io.write(f'SOURce<HwInstance>:EFRontend:RFConnector {param}')

	def clone(self) -> 'Efrontend':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Efrontend(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
