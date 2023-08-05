from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rreport:
	"""Rreport commands group definition. 1 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rreport", core, parent)

	@property
	def cswitched(self):
		"""cswitched commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cswitched'):
			from .Rreport_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	def clone(self) -> 'Rreport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rreport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
