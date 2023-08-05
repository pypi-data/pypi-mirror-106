from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Wb:
	"""Wb commands group definition. 6 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("wb", core, parent)

	@property
	def frate(self):
		"""frate commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frate'):
			from .Wb_.Frate import Frate
			self._frate = Frate(self._core, self._base)
		return self._frate

	@property
	def hrate(self):
		"""hrate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hrate'):
			from .Wb_.Hrate import Hrate
			self._hrate = Hrate(self._core, self._base)
		return self._hrate

	def clone(self) -> 'Wb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Wb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
