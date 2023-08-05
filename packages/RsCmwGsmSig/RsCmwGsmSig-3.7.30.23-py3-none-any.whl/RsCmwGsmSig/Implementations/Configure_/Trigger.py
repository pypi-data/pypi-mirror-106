from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trigger:
	"""Trigger commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("trigger", core, parent)

	# noinspection PyTypeChecker
	def get_ftmode(self) -> enums.FrameTriggerMod:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:TRIGger:FTMode \n
		Snippet: value: enums.FrameTriggerMod = driver.configure.trigger.get_ftmode() \n
		Configures the frame trigger signal. \n
			:return: frame_trigger_mod: EVERy | EWIDle | M26 | M52 | M104 EVERy: The frame trigger signal is generated for each uplink frame (single frame trigger) . EWIDle: The frame trigger signal is generated for each uplink frame except for idle frames (single frame trigger) . M26 | M52 | M104: The frame trigger signal is generated for each 26th, 52nd or 104th uplink frame (multiframe trigger) .
		"""
		response = self._core.io.query_str('CONFigure:GSM:SIGNaling<Instance>:TRIGger:FTMode?')
		return Conversions.str_to_scalar_enum(response, enums.FrameTriggerMod)

	def set_ftmode(self, frame_trigger_mod: enums.FrameTriggerMod) -> None:
		"""SCPI: CONFigure:GSM:SIGNaling<Instance>:TRIGger:FTMode \n
		Snippet: driver.configure.trigger.set_ftmode(frame_trigger_mod = enums.FrameTriggerMod.EVERy) \n
		Configures the frame trigger signal. \n
			:param frame_trigger_mod: EVERy | EWIDle | M26 | M52 | M104 EVERy: The frame trigger signal is generated for each uplink frame (single frame trigger) . EWIDle: The frame trigger signal is generated for each uplink frame except for idle frames (single frame trigger) . M26 | M52 | M104: The frame trigger signal is generated for each 26th, 52nd or 104th uplink frame (multiframe trigger) .
		"""
		param = Conversions.enum_scalar_to_str(frame_trigger_mod, enums.FrameTriggerMod)
		self._core.io.write(f'CONFigure:GSM:SIGNaling<Instance>:TRIGger:FTMode {param}')
