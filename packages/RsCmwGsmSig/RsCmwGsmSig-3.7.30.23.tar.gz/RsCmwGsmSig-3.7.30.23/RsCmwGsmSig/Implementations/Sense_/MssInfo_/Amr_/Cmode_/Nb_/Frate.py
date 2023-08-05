from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frate:
	"""Frate commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("frate", core, parent)

	@property
	def gmsk(self):
		"""gmsk commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_gmsk'):
			from .Frate_.Gmsk import Gmsk
			self._gmsk = Gmsk(self._core, self._base)
		return self._gmsk

	def clone(self) -> 'Frate':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frate(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
