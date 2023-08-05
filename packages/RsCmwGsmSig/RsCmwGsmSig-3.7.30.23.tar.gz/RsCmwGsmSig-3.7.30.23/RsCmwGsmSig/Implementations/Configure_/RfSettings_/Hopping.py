from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 4 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("hopping", core, parent)

	@property
	def enable(self):
		"""enable commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_enable'):
			from .Hopping_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Hopping_.Sequence import Sequence
			self._sequence = Sequence(self._core, self._base)
		return self._sequence

	@property
	def hsn(self):
		"""hsn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsn'):
			from .Hopping_.Hsn import Hsn
			self._hsn = Hsn(self._core, self._base)
		return self._hsn

	@property
	def maio(self):
		"""maio commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_maio'):
			from .Hopping_.Maio import Maio
			self._maio = Maio(self._core, self._base)
		return self._maio

	def clone(self) -> 'Hopping':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Hopping(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
