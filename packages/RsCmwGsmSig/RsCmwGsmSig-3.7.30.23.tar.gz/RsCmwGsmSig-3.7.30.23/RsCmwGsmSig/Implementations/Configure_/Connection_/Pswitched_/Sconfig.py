from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sconfig:
	"""Sconfig commands group definition. 8 total commands, 6 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("sconfig", core, parent)

	@property
	def combined(self):
		"""combined commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_combined'):
			from .Sconfig_.Combined import Combined
			self._combined = Combined(self._core, self._base)
		return self._combined

	@property
	def enable(self):
		"""enable commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Sconfig_.Enable import Enable
			self._enable = Enable(self._core, self._base)
		return self._enable

	@property
	def gamma(self):
		"""gamma commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gamma'):
			from .Sconfig_.Gamma import Gamma
			self._gamma = Gamma(self._core, self._base)
		return self._gamma

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Sconfig_.Level import Level
			self._level = Level(self._core, self._base)
		return self._level

	@property
	def cscheme(self):
		"""cscheme commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cscheme'):
			from .Sconfig_.Cscheme import Cscheme
			self._cscheme = Cscheme(self._core, self._base)
		return self._cscheme

	@property
	def udCycle(self):
		"""udCycle commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_udCycle'):
			from .Sconfig_.UdCycle import UdCycle
			self._udCycle = UdCycle(self._core, self._base)
		return self._udCycle

	def clone(self) -> 'Sconfig':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sconfig(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
