from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("level", core, parent)

	@property
	def bcch(self):
		"""bcch commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_bcch'):
			from .Level_.Bcch import Bcch
			self._bcch = Bcch(self._core, self._base)
		return self._bcch

	@property
	def tch(self):
		"""tch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tch'):
			from .Level_.Tch import Tch
			self._tch = Tch(self._core, self._base)
		return self._tch

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
