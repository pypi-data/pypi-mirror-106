from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("minimum", core, parent)

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:MODulation:PSD:MINimum \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.listPy.modulation.psd.minimum.fetch() \n
		Return RB power values (power spectral density) for all measured list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: psd: Comma-separated list of values, one per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:MODulation:PSD:MINimum?', suppressed)
		return response

	def calculate(self) -> List[float]:
		"""SCPI: CALCulate:NRSub:MEASurement<Instance>:MEValuation:LIST:MODulation:PSD:MINimum \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.listPy.modulation.psd.minimum.calculate() \n
		Return RB power values (power spectral density) for all measured list mode segments. The values described below are
		returned by FETCh commands. CALCulate commands return limit check results instead, one value for each result listed below. \n
		Suppressed linked return values: reliability \n
			:return: psd: Comma-separated list of values, one per measured segment"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'CALCulate:NRSub:MEASurement<Instance>:MEValuation:LIST:MODulation:PSD:MINimum?', suppressed)
		return response
