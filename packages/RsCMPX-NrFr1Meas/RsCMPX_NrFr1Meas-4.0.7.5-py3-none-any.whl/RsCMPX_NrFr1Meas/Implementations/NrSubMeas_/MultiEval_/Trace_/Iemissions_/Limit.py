from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ......Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limit:
	"""Limit commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("limit", core, parent)

	def read(self) -> List[float]:
		"""SCPI: READ:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:LIMit \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.trace.iemissions.limit.read() \n
		Returns the values of the inband emissions limit line. \n
		Suppressed linked return values: reliability \n
			:return: limit: Comma-separated list of limit values, one value per resource block"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'READ:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:LIMit?', suppressed)
		return response

	def fetch(self) -> List[float]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:LIMit \n
		Snippet: value: List[float] = driver.nrSubMeas.multiEval.trace.iemissions.limit.fetch() \n
		Returns the values of the inband emissions limit line. \n
		Suppressed linked return values: reliability \n
			:return: limit: Comma-separated list of limit values, one value per resource block"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_float_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:TRACe:IEMissions:LIMit?', suppressed)
		return response
