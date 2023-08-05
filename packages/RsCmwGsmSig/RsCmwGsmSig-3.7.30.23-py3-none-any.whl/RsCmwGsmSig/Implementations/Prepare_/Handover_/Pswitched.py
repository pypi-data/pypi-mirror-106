from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 7 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	@property
	def enable(self):
		"""enable commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Pswitched_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def gamma(self):
		"""gamma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gamma'):
			from .Pswitched_.Gamma import Gamma
			self._gamma = Gamma(self._core, self._base)
		return self._gamma

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Pswitched_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def cscheme(self):
		"""cscheme commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cscheme'):
			from .Pswitched_.Cscheme import Cscheme
			self._cscheme = Cscheme(self._core, self._base)
		return self._cscheme

	@property
	def udCycle(self):
		"""udCycle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_udCycle'):
			from .Pswitched_.UdCycle import UdCycle
			self._udCycle = UdCycle(self._core, self._base)
		return self._udCycle

	def clone(self) -> 'Pswitched':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pswitched(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
