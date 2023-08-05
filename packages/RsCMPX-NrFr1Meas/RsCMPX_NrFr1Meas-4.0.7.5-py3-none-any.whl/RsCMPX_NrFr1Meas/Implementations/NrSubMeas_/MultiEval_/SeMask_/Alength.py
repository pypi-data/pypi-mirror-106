from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alength:
	"""Alength commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("alength", core, parent)

	def fetch(self) -> List[int]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:SEMask:ALENgth \n
		Snippet: value: List[int] = driver.nrSubMeas.multiEval.seMask.alength.fetch() \n
		No command help available \n
		Suppressed linked return values: reliability \n
			:return: length: No help available"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:SEMask:ALENgth?', suppressed)
		return response
