from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srs:
	"""Srs commands group definition. 14 total commands, 13 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("srs", core, parent)

	@property
	def bhop(self):
		"""bhop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bhop'):
			from .Srs_.Bhop import Bhop
			self._bhop = Bhop(self._core, self._base)
		return self._bhop

	@property
	def bsrs(self):
		"""bsrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsrs'):
			from .Srs_.Bsrs import Bsrs
			self._bsrs = Bsrs(self._core, self._base)
		return self._bsrs

	@property
	def cycShift(self):
		"""cycShift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycShift'):
			from .Srs_.CycShift import CycShift
			self._cycShift = CycShift(self._core, self._base)
		return self._cycShift

	@property
	def isrs(self):
		"""isrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isrs'):
			from .Srs_.Isrs import Isrs
			self._isrs = Isrs(self._core, self._base)
		return self._isrs

	@property
	def naPort(self):
		"""naPort commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_naPort'):
			from .Srs_.NaPort import NaPort
			self._naPort = NaPort(self._core, self._base)
		return self._naPort

	@property
	def nrrc(self):
		"""nrrc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrrc'):
			from .Srs_.Nrrc import Nrrc
			self._nrrc = Nrrc(self._core, self._base)
		return self._nrrc

	@property
	def powOffset(self):
		"""powOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_powOffset'):
			from .Srs_.PowOffset import PowOffset
			self._powOffset = PowOffset(self._core, self._base)
		return self._powOffset

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Srs_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def sym(self):
		"""sym commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sym'):
			from .Srs_.Sym import Sym
			self._sym = Sym(self._core, self._base)
		return self._sym

	@property
	def toffset(self):
		"""toffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toffset'):
			from .Srs_.Toffset import Toffset
			self._toffset = Toffset(self._core, self._base)
		return self._toffset

	@property
	def trComb(self):
		"""trComb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trComb'):
			from .Srs_.TrComb import TrComb
			self._trComb = TrComb(self._core, self._base)
		return self._trComb

	@property
	def tsrs(self):
		"""tsrs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsrs'):
			from .Srs_.Tsrs import Tsrs
			self._tsrs = Tsrs(self._core, self._base)
		return self._tsrs

	@property
	def tt0(self):
		"""tt0 commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tt0'):
			from .Srs_.Tt0 import Tt0
			self._tt0 = Tt0(self._core, self._base)
		return self._tt0

	def clone(self) -> 'Srs':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Srs(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
