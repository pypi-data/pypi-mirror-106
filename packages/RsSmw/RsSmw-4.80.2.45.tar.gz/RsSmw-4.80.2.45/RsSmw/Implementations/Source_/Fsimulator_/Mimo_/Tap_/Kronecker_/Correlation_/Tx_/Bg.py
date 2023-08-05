from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bg:
	"""Bg commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bg", core, parent)

	@property
	def imaginary(self):
		"""imaginary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_imaginary'):
			from .Bg_.Imaginary import Imaginary
			self._imaginary = Imaginary(self._core, self._base)
		return self._imaginary

	@property
	def magnitude(self):
		"""magnitude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_magnitude'):
			from .Bg_.Magnitude import Magnitude
			self._magnitude = Magnitude(self._core, self._base)
		return self._magnitude

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Bg_.Phase import Phase
			self._phase = Phase(self._core, self._base)
		return self._phase

	@property
	def real(self):
		"""real commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_real'):
			from .Bg_.Real import Real
			self._real = Real(self._core, self._base)
		return self._real

	def clone(self) -> 'Bg':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bg(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
