from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	def get_destination(self) -> List[str]:
		"""SCPI: PREPare:GSM:SIGNaling<Instance>:HANDover:CATalog:DESTination \n
		Snippet: value: List[str] = driver.prepare.handover.catalog.get_destination() \n
		Lists all handover destinations that can be selected using method RsCmwGsmSig.Prepare.Handover.destination. \n
			:return: destination: Comma-separated list of all supported destinations. Each destination is represented as a string.
		"""
		response = self._core.io.query_str('PREPare:GSM:SIGNaling<Instance>:HANDover:CATalog:DESTination?')
		return Conversions.str_to_str_list(response)
