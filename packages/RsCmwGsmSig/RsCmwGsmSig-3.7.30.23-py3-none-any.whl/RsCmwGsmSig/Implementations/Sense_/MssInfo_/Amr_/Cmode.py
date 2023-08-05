from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cmode:
	"""Cmode commands group definition. 12 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("cmode", core, parent)

	@property
	def nb(self):
		"""nb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nb'):
			from .Cmode_.Nb import Nb
			self._nb = Nb(self._core, self._base)
		return self._nb

	@property
	def wb(self):
		"""wb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_wb'):
			from .Cmode_.Wb import Wb
			self._wb = Wb(self._core, self._base)
		return self._wb

	def clone(self) -> 'Cmode':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cmode(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
