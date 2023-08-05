from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nb:
	"""Nb commands group definition. 3 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("nb", core, parent)

	@property
	def frate(self):
		"""frate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frate'):
			from .Nb_.Frate import Frate
			self._frate = Frate(self._core, self._base)
		return self._frate

	@property
	def hrate(self):
		"""hrate commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_hrate'):
			from .Nb_.Hrate import Hrate
			self._hrate = Hrate(self._core, self._base)
		return self._hrate

	def clone(self) -> 'Nb':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Nb(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
