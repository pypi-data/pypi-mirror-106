from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ber:
	"""Ber commands group definition. 5 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ber", core, parent)

	@property
	def cswitched(self):
		"""cswitched commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cswitched'):
			from .Ber_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	@property
	def pswitched(self):
		"""pswitched commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pswitched'):
			from .Ber_.Pswitched import Pswitched
			self._pswitched = Pswitched(self._core, self._base)
		return self._pswitched

	def clone(self) -> 'Ber':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ber(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
