from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pswitched:
	"""Pswitched commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("pswitched", core, parent)

	# noinspection PyTypeChecker
	def get_cerror(self) -> enums.ConnectError:
		"""SCPI: SENSe:GSM:SIGNaling<Instance>:CELL:PSWitched:CERRor \n
		Snippet: value: enums.ConnectError = driver.sense.cell.pswitched.get_cerror() \n
		Returns error information related to the active CS/PS connection. \n
			:return: connection_error: NERRor | REJected | RLTimeout | PTIMeout | STIMeout | IGNored | ATIMeout NERRor: no error REJected: connection rejected RLTimeout: radio link timeout PTIMeout: paging timeout STIMeout: signaling timeout IGNored: connection ignored ATIMeout: alerting timeout
		"""
		response = self._core.io.query_str('SENSe:GSM:SIGNaling<Instance>:CELL:PSWitched:CERRor?')
		return Conversions.str_to_scalar_enum(response, enums.ConnectError)
