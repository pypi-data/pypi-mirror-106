from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 253 total commands, 19 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def band(self):
		"""band commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_band'):
			from .Configure_.Band import Band
			self._band = Band(self._core, self._base)
		return self._band

	@property
	def dualBand(self):
		"""dualBand commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dualBand'):
			from .Configure_.DualBand import DualBand
			self._dualBand = DualBand(self._core, self._base)
		return self._dualBand

	@property
	def mslot(self):
		"""mslot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mslot'):
			from .Configure_.Mslot import Mslot
			self._mslot = Mslot(self._core, self._base)
		return self._mslot

	@property
	def rfSettings(self):
		"""rfSettings commands group. 9 Sub-classes, 4 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def iqIn(self):
		"""iqIn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqIn'):
			from .Configure_.IqIn import IqIn
			self._iqIn = IqIn(self._core, self._base)
		return self._iqIn

	@property
	def fading(self):
		"""fading commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Configure_.Fading import Fading
			self._fading = Fading(self._core, self._base)
		return self._fading

	@property
	def connection(self):
		"""connection commands group. 3 Sub-classes, 4 commands."""
		if not hasattr(self, '_connection'):
			from .Configure_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def ncell(self):
		"""ncell commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncell'):
			from .Configure_.Ncell import Ncell
			self._ncell = Ncell(self._core, self._base)
		return self._ncell

	@property
	def cell(self):
		"""cell commands group. 13 Sub-classes, 25 commands."""
		if not hasattr(self, '_cell'):
			from .Configure_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def trigger(self):
		"""trigger commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trigger'):
			from .Configure_.Trigger import Trigger
			self._trigger = Trigger(self._core, self._base)
		return self._trigger

	@property
	def rreport(self):
		"""rreport commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rreport'):
			from .Configure_.Rreport import Rreport
			self._rreport = Rreport(self._core, self._base)
		return self._rreport

	@property
	def sms(self):
		"""sms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sms'):
			from .Configure_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def cbs(self):
		"""cbs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cbs'):
			from .Configure_.Cbs import Cbs
			self._cbs = Cbs(self._core, self._base)
		return self._cbs

	@property
	def ber(self):
		"""ber commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ber'):
			from .Configure_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def bler(self):
		"""bler commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bler'):
			from .Configure_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_throughput'):
			from .Configure_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def cperformance(self):
		"""cperformance commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cperformance'):
			from .Configure_.Cperformance import Cperformance
			self._cperformance = Cperformance(self._core, self._base)
		return self._cperformance

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Configure_.Mmonitor import Mmonitor
			self._mmonitor = Mmonitor(self._core, self._base)
		return self._mmonitor

	@property
	def msReport(self):
		"""msReport commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_msReport'):
			from .Configure_.MsReport import MsReport
			self._msReport = MsReport(self._core, self._base)
		return self._msReport

	def get_etoe(self) -> bool:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:ETOE \n
		Snippet: value: bool = driver.configure.get_etoe() \n
		No command help available \n
			:return: end_to_end_enable: No help available
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:ETOE?')
		return Conversions.str_to_bool(response)

	def set_etoe(self, end_to_end_enable: bool) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:ETOE \n
		Snippet: driver.configure.set_etoe(end_to_end_enable = False) \n
		No command help available \n
			:param end_to_end_enable: No help available
		"""
		param = Conversions.bool_to_str(end_to_end_enable)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:ETOE {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
