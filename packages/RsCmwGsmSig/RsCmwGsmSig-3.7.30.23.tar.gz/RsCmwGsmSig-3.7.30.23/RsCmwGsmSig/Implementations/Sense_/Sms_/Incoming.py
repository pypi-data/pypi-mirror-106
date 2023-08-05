from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Incoming:
	"""Incoming commands group definition. 4 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("incoming", core, parent)

	@property
	def info(self):
		"""info commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_info'):
			from .Incoming_.Info import Info
			self._info = Info(self._core, self._base)
		return self._info

	def clone(self) -> 'Incoming':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Incoming(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
