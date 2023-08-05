from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Huwb:
	"""Huwb commands group definition. 91 total commands, 11 Sub-groups, 11 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("huwb", core, parent)

	@property
	def clipping(self):
		"""clipping commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_clipping'):
			from .Huwb_.Clipping import Clipping
			self._clipping = Clipping(self._core, self._base)
		return self._clipping

	@property
	def clock(self):
		"""clock commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_clock'):
			from .Huwb_.Clock import Clock
			self._clock = Clock(self._core, self._base)
		return self._clock

	@property
	def fconfig(self):
		"""fconfig commands group. 3 Sub-classes, 9 commands."""
		if not hasattr(self, '_fconfig'):
			from .Huwb_.Fconfig import Fconfig
			self._fconfig = Fconfig(self._core, self._base)
		return self._fconfig

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_filterPy'):
			from .Huwb_.FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._base)
		return self._filterPy

	@property
	def impairments(self):
		"""impairments commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_impairments'):
			from .Huwb_.Impairments import Impairments
			self._impairments = Impairments(self._core, self._base)
		return self._impairments

	@property
	def phr(self):
		"""phr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phr'):
			from .Huwb_.Phr import Phr
			self._phr = Phr(self._core, self._base)
		return self._phr

	@property
	def setting(self):
		"""setting commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_setting'):
			from .Huwb_.Setting import Setting
			self._setting = Setting(self._core, self._base)
		return self._setting

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .Huwb_.SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._base)
		return self._symbolRate

	@property
	def sts(self):
		"""sts commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_sts'):
			from .Huwb_.Sts import Sts
			self._sts = Sts(self._core, self._base)
		return self._sts

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 5 commands."""
		if not hasattr(self, '_trigger'):
			from .Huwb_.Trigger import Trigger
			self._trigger = Trigger(self._core, self._base)
		return self._trigger

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_waveform'):
			from .Huwb_.Waveform import Waveform
			self._waveform = Waveform(self._core, self._base)
		return self._waveform

	# noinspection PyTypeChecker
	def get_asl(self) -> enums.HrpUwbActSegmentLength:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASL \n
		Snippet: value: enums.HrpUwbActSegmentLength = driver.source.bb.huwb.get_asl() \n
		No command help available \n
			:return: act_seg_length: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:ASL?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbActSegmentLength)

	def set_asl(self, act_seg_length: enums.HrpUwbActSegmentLength) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASL \n
		Snippet: driver.source.bb.huwb.set_asl(act_seg_length = enums.HrpUwbActSegmentLength.ASL_128) \n
		No command help available \n
			:param act_seg_length: No help available
		"""
		param = Conversions.enum_scalar_to_str(act_seg_length, enums.HrpUwbActSegmentLength)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:ASL {param}')

	# noinspection PyTypeChecker
	def get_asn(self) -> enums.HrpUwbActSegmentNum:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASN \n
		Snippet: value: enums.HrpUwbActSegmentNum = driver.source.bb.huwb.get_asn() \n
		No command help available \n
			:return: acg_seg_number: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:ASN?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbActSegmentNum)

	def set_asn(self, acg_seg_number: enums.HrpUwbActSegmentNum) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:ASN \n
		Snippet: driver.source.bb.huwb.set_asn(acg_seg_number = enums.HrpUwbActSegmentNum.ASN_1) \n
		No command help available \n
			:param acg_seg_number: No help available
		"""
		param = Conversions.enum_scalar_to_str(acg_seg_number, enums.HrpUwbActSegmentNum)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:ASN {param}')

	def get_bandwidth(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:BWIDth \n
		Snippet: value: float = driver.source.bb.huwb.get_bandwidth() \n
		No command help available \n
			:return: hrp_uwb_band_width: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:BWIDth?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_cccl(self) -> enums.HrpUwbConvConsLen:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CCCL \n
		Snippet: value: enums.HrpUwbConvConsLen = driver.source.bb.huwb.get_cccl() \n
		No command help available \n
			:return: cccl: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CCCL?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbConvConsLen)

	def set_cccl(self, cccl: enums.HrpUwbConvConsLen) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CCCL \n
		Snippet: driver.source.bb.huwb.set_cccl(cccl = enums.HrpUwbConvConsLen.CL3) \n
		No command help available \n
			:param cccl: No help available
		"""
		param = Conversions.enum_scalar_to_str(cccl, enums.HrpUwbConvConsLen)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CCCL {param}')

	def get_cnumber(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CNUMber \n
		Snippet: value: int = driver.source.bb.huwb.get_cnumber() \n
		No command help available \n
			:return: channel_number: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:CNUMber?')
		return Conversions.str_to_int(response)

	def set_cnumber(self, channel_number: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:CNUMber \n
		Snippet: driver.source.bb.huwb.set_cnumber(channel_number = 1) \n
		No command help available \n
			:param channel_number: No help available
		"""
		param = Conversions.decimal_value_to_str(channel_number)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:CNUMber {param}')

	def get_iinterval(self) -> float:
		"""SCPI: [SOURce<HW>]:BB:HUWB:IINTerval \n
		Snippet: value: float = driver.source.bb.huwb.get_iinterval() \n
		No command help available \n
			:return: iinterval: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:IINTerval?')
		return Conversions.str_to_float(response)

	def set_iinterval(self, iinterval: float) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:IINTerval \n
		Snippet: driver.source.bb.huwb.set_iinterval(iinterval = 1.0) \n
		No command help available \n
			:param iinterval: No help available
		"""
		param = Conversions.decimal_value_to_str(iinterval)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:IINTerval {param}')

	def preset(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:PRESet \n
		Snippet: driver.source.bb.huwb.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:PRESet')

	def preset_with_opc(self) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:PRESet \n
		Snippet: driver.source.bb.huwb.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:BB:HUWB:PRESet')

	# noinspection PyTypeChecker
	def get_sfd(self) -> enums.HrpUwbSfdIndex:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SFD \n
		Snippet: value: enums.HrpUwbSfdIndex = driver.source.bb.huwb.get_sfd() \n
		No command help available \n
			:return: sfd_index: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SFD?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbSfdIndex)

	def set_sfd(self, sfd_index: enums.HrpUwbSfdIndex) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SFD \n
		Snippet: driver.source.bb.huwb.set_sfd(sfd_index = enums.HrpUwbSfdIndex.SFD_0) \n
		No command help available \n
			:param sfd_index: No help available
		"""
		param = Conversions.enum_scalar_to_str(sfd_index, enums.HrpUwbSfdIndex)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SFD {param}')

	def get_slength(self) -> int:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SLENgth \n
		Snippet: value: int = driver.source.bb.huwb.get_slength() \n
		No command help available \n
			:return: slength: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:SLENgth?')
		return Conversions.str_to_int(response)

	def set_slength(self, slength: int) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:SLENgth \n
		Snippet: driver.source.bb.huwb.set_slength(slength = 1) \n
		No command help available \n
			:param slength: No help available
		"""
		param = Conversions.decimal_value_to_str(slength)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:SLENgth {param}')

	def get_state(self) -> bool:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STATe \n
		Snippet: value: bool = driver.source.bb.huwb.get_state() \n
		No command help available \n
			:return: hrp_uwb_state: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, hrp_uwb_state: bool) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STATe \n
		Snippet: driver.source.bb.huwb.set_state(hrp_uwb_state = False) \n
		No command help available \n
			:param hrp_uwb_state: No help available
		"""
		param = Conversions.bool_to_str(hrp_uwb_state)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:STATe {param}')

	# noinspection PyTypeChecker
	def get_std(self) -> enums.HrpUwbMode:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STD \n
		Snippet: value: enums.HrpUwbMode = driver.source.bb.huwb.get_std() \n
		No command help available \n
			:return: mode: No help available
		"""
		response = self._core.io.query_str('SOURce<HwInstance>:BB:HUWB:STD?')
		return Conversions.str_to_scalar_enum(response, enums.HrpUwbMode)

	def set_std(self, mode: enums.HrpUwbMode) -> None:
		"""SCPI: [SOURce<HW>]:BB:HUWB:STD \n
		Snippet: driver.source.bb.huwb.set_std(mode = enums.HrpUwbMode.HPRF) \n
		No command help available \n
			:param mode: No help available
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.HrpUwbMode)
		self._core.io.write(f'SOURce<HwInstance>:BB:HUWB:STD {param}')

	def clone(self) -> 'Huwb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Huwb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
