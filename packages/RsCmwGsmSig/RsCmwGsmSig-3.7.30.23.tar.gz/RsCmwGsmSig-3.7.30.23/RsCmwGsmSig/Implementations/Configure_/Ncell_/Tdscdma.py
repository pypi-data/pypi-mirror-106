from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tdscdma:
	"""Tdscdma commands group definition. 2 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("tdscdma", core, parent)

	@property
	def cell(self):
		"""cell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cell'):
			from .Tdscdma_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def thresholds(self):
		"""thresholds commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_thresholds'):
			from .Tdscdma_.Thresholds import Thresholds
			self._thresholds = Thresholds(self._core, self._base)
		return self._thresholds

	def clone(self) -> 'Tdscdma':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tdscdma(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
