from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Quality:
	"""Quality commands group definition. 3 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("quality", core, parent)

	@property
	def rxLevMin(self):
		"""rxLevMin commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_rxLevMin'):
			from .Quality_.RxLevMin import RxLevMin
			self._rxLevMin = RxLevMin(self._core, self._base)
		return self._rxLevMin

	def clone(self) -> 'Quality':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Quality(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
