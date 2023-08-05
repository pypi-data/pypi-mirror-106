from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fconfig:
	"""Fconfig commands group definition. 14 total commands, 3 Sub-groups, 9 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("fconfig", core, parent)

	@property
	def data(self):
		"""data commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_data'):
			from .Fconfig_.Data import Data
			self._data = Data(self._core, self._base)
		return self._data

	@property
	def dlength(self):
		"""dlength commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_dlength'):
			from .Fconfig_.Dlength import Dlength
			self._dlength = Dlength(self._core, self._base)
		return self._dlength

	@property
	def mcs(self):
		"""mcs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcs'):
			from .Fconfig_.Mcs import Mcs
			self._mcs = Mcs(self._core, self._base)
		return self._mcs

	# noinspection PyTypeChecker
	def get_cindex(self) -> enums.HrpUwbCodeIndex:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:CINDex \n
		Snippet: value: enums.HrpUwbCodeIndex = driver.source.bb.huwb.fconfig.get_cindex() \n
		No command help available \n
			:return: code_index: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:CINDex?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbCodeIndex)

	def set_cindex(self, code_index: enums.HrpUwbCodeIndex) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:CINDex \n
		Snippet: driver.source.bb.huwb.fconfig.set_cindex(code_index = enums.HrpUwbCodeIndex.CI_1) \n
		No command help available \n
			:param code_index: No help available
		"""
		param = Conversions.enum_scalar_to_str(code_index, enums.HrpUwbCodeIndex)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:CINDex {param}')

	# noinspection PyTypeChecker
	def get_cp_burst(self) -> enums.HrpUwbChipsPerBurst:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:CPBurst \n
		Snippet: value: enums.HrpUwbChipsPerBurst = driver.source.bb.huwb.fconfig.get_cp_burst() \n
		No command help available \n
			:return: chips_per_burst: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:CPBurst?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbChipsPerBurst)

	def set_cp_burst(self, chips_per_burst: enums.HrpUwbChipsPerBurst) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:CPBurst \n
		Snippet: driver.source.bb.huwb.fconfig.set_cp_burst(chips_per_burst = enums.HrpUwbChipsPerBurst.CPB_1) \n
		No command help available \n
			:param chips_per_burst: No help available
		"""
		param = Conversions.enum_scalar_to_str(chips_per_burst, enums.HrpUwbChipsPerBurst)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:CPBurst {param}')

	def get_dr(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:DR \n
		Snippet: value: float = driver.source.bb.huwb.fconfig.get_dr() \n
		No command help available \n
			:return: data_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:DR?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_hop_burst(self) -> enums.HrpUwbHopBurst:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:HOPBurst \n
		Snippet: value: enums.HrpUwbHopBurst = driver.source.bb.huwb.fconfig.get_hop_burst() \n
		No command help available \n
			:return: hop_burst: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:HOPBurst?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbHopBurst)

	def set_hop_burst(self, hop_burst: enums.HrpUwbHopBurst) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:HOPBurst \n
		Snippet: driver.source.bb.huwb.fconfig.set_hop_burst(hop_burst = enums.HrpUwbHopBurst.HB_2) \n
		No command help available \n
			:param hop_burst: No help available
		"""
		param = Conversions.enum_scalar_to_str(hop_burst, enums.HrpUwbHopBurst)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:HOPBurst {param}')

	def get_mprf(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:MPRF \n
		Snippet: value: float = driver.source.bb.huwb.fconfig.get_mprf() \n
		No command help available \n
			:return: mean_prf: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:MPRF?')
		return Conversions.str_to_float(response)

	def get_phrb_rate(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:PHRBrate \n
		Snippet: value: float = driver.source.bb.huwb.fconfig.get_phrb_rate() \n
		No command help available \n
			:return: hrp_uwb_phr_bitrate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:PHRBrate?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_sfd_length(self) -> enums.HrpUwbSfdlEngth:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:SFDLength \n
		Snippet: value: enums.HrpUwbSfdlEngth = driver.source.bb.huwb.fconfig.get_sfd_length() \n
		No command help available \n
			:return: sfd_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:SFDLength?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbSfdlEngth)

	def set_sfd_length(self, sfd_length: enums.HrpUwbSfdlEngth) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:SFDLength \n
		Snippet: driver.source.bb.huwb.fconfig.set_sfd_length(sfd_length = enums.HrpUwbSfdlEngth.SFDL_64) \n
		No command help available \n
			:param sfd_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(sfd_length, enums.HrpUwbSfdlEngth)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:SFDLength {param}')

	# noinspection PyTypeChecker
	def get_syn_length(self) -> enums.HrpUwbSyncLength:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:SYNLength \n
		Snippet: value: enums.HrpUwbSyncLength = driver.source.bb.huwb.fconfig.get_syn_length() \n
		No command help available \n
			:return: sync_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:SYNLength?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbSyncLength)

	def set_syn_length(self, sync_length: enums.HrpUwbSyncLength) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:SYNLength \n
		Snippet: driver.source.bb.huwb.fconfig.set_syn_length(sync_length = enums.HrpUwbSyncLength.SL_1024) \n
		No command help available \n
			:param sync_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(sync_length, enums.HrpUwbSyncLength)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:FCONfig:SYNLength {param}')

	# noinspection PyTypeChecker
	def get_vrate(self) -> enums.HrpUwbViterbiRate:
		"""SCPI: [SOURce<HW>]:BB:HUWB:FCONfig:VRATe \n
		Snippet: value: enums.HrpUwbViterbiRate = driver.source.bb.huwb.fconfig.get_vrate() \n
		No command help available \n
			:return: hrp_uwb_viterbi_rate: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:FCONfig:VRATe?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbViterbiRate)

	def clone(self) -> 'Fconfig':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fconfig(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
