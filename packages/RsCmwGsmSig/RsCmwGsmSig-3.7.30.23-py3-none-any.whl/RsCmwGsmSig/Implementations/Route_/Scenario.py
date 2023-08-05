from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 8 total commands, 5 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def scell(self):
		"""scell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scell'):
			from .Scenario_.Scell import Scell
			self._scell = Scell(self._core, self._base)
		return self._scell

	@property
	def iori(self):
		"""iori commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iori'):
			from .Scenario_.Iori import Iori
			self._iori = Iori(self._core, self._base)
		return self._iori

	@property
	def batch(self):
		"""batch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_batch'):
			from .Scenario_.Batch import Batch
			self._batch = Batch(self._core, self._base)
		return self._batch

	@property
	def scFading(self):
		"""scFading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scFading'):
			from .Scenario_.ScFading import ScFading
			self._scFading = ScFading(self._core, self._base)
		return self._scFading

	@property
	def scfDiversity(self):
		"""scfDiversity commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scfDiversity'):
			from .Scenario_.ScfDiversity import ScfDiversity
			self._scfDiversity = ScfDiversity(self._core, self._base)
		return self._scfDiversity

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: SCEL | IORI | BATC | SCF | SCFDiversity SCEL: 'Standard Cell' IORI: 'IQ out - RF in' BATC: 'BCCH and TCH/PDCH' SCF: 'Standard Cell Fading' SCFDiversity: 'Standard Cell Fading with RX Diversity'
			- Fader: enums.SourceInt: EXTernal | INTernal Only returned for fading scenarios, e.g. SCF Indicates whether internal or external fading is active."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_enum('Fader', enums.SourceInt)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Fader: enums.SourceInt = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:GSM:SIGNaling<Instance>:SCENario \n
		Snippet: value: ValueStruct = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:GSM:SIGNaling<Instance>:SCENario?', self.__class__.ValueStruct())

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
