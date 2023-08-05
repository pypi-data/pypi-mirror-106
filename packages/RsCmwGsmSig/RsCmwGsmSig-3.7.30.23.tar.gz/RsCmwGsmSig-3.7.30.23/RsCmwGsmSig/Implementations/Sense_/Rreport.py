from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rreport:
	"""Rreport commands group definition. 42 total commands, 12 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rreport", core, parent)

	@property
	def cswitched(self):
		"""cswitched commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_cswitched'):
			from .Rreport_.Cswitched import Cswitched
			self._cswitched = Cswitched(self._core, self._base)
		return self._cswitched

	@property
	def rxLevel(self):
		"""rxLevel commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_rxLevel'):
			from .Rreport_.RxLevel import RxLevel
			self._rxLevel = RxLevel(self._core, self._base)
		return self._rxLevel

	@property
	def rxQuality(self):
		"""rxQuality commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_rxQuality'):
			from .Rreport_.RxQuality import RxQuality
			self._rxQuality = RxQuality(self._core, self._base)
		return self._rxQuality

	@property
	def cvalue(self):
		"""cvalue commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cvalue'):
			from .Rreport_.Cvalue import Cvalue
			self._cvalue = Cvalue(self._core, self._base)
		return self._cvalue

	@property
	def svariance(self):
		"""svariance commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_svariance'):
			from .Rreport_.Svariance import Svariance
			self._svariance = Svariance(self._core, self._base)
		return self._svariance

	@property
	def gmbep(self):
		"""gmbep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_gmbep'):
			from .Rreport_.Gmbep import Gmbep
			self._gmbep = Gmbep(self._core, self._base)
		return self._gmbep

	@property
	def gcbep(self):
		"""gcbep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_gcbep'):
			from .Rreport_.Gcbep import Gcbep
			self._gcbep = Gcbep(self._core, self._base)
		return self._gcbep

	@property
	def embep(self):
		"""embep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_embep'):
			from .Rreport_.Embep import Embep
			self._embep = Embep(self._core, self._base)
		return self._embep

	@property
	def ecbep(self):
		"""ecbep commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ecbep'):
			from .Rreport_.Ecbep import Ecbep
			self._ecbep = Ecbep(self._core, self._base)
		return self._ecbep

	@property
	def nsrqam(self):
		"""nsrqam commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_nsrqam'):
			from .Rreport_.Nsrqam import Nsrqam
			self._nsrqam = Nsrqam(self._core, self._base)
		return self._nsrqam

	@property
	def hsrQam(self):
		"""hsrQam commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hsrQam'):
			from .Rreport_.HsrQam import HsrQam
			self._hsrQam = HsrQam(self._core, self._base)
		return self._hsrQam

	@property
	def ncell(self):
		"""ncell commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncell'):
			from .Rreport_.Ncell import Ncell
			self._ncell = Ncell(self._core, self._base)
		return self._ncell

	def get_count(self) -> int:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:RREPort:COUNt \n
		Snippet: value: int = driver.sense.rreport.get_count() \n
		Returns the number of measurement reports received since the connection was established. \n
			:return: count: Range: 0 to n
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:RREPort:COUNt?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Rreport':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rreport(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
