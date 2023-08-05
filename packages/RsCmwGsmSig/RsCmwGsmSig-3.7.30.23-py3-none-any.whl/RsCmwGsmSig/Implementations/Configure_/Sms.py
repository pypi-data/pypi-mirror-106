from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sms:
	"""Sms commands group definition. 13 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sms", core, parent)

	@property
	def outgoing(self):
		"""outgoing commands group. 1 Sub-classes, 10 commands."""
		if not hasattr(self, '_outgoing'):
			from .Sms_.Outgoing import Outgoing
			self._outgoing = Outgoing(self._core, self._base)
		return self._outgoing

	def clone(self) -> 'Sms':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sms(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
