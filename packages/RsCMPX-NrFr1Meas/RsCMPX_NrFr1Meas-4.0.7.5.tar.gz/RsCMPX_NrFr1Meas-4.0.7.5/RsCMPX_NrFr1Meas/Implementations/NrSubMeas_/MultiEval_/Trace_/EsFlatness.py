from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EsFlatness:
	"""EsFlatness commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("esFlatness", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NRSub:MEASurement<Instance>:MEValuation:TRACe:ESFLatness \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.trace.esFlatness.read() \n
		Returns the values of the equalizer spectrum flatness trace. See also 'Square Equalizer Spectrum Flatness'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per subcarrier For not allocated subcarriers, NCAP is returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRSub:MEASurement<Instance>:MEValuation:TRACe:ESFLatness?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:TRACe:ESFLatness \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.trace.esFlatness.fetch() \n
		Returns the values of the equalizer spectrum flatness trace. See also 'Square Equalizer Spectrum Flatness'. \n
		Suppressed linked return values: reliability \n
			:return: power: Comma-separated list of power values, one value per subcarrier For not allocated subcarriers, NCAP is returned."""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:TRACe:ESFLatness?', suppressed)
		return response
