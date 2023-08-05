from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.ArgSingleSuppressed import ArgSingleSuppressed
from ........Internal.Types import DataType
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("current", core, parent)

	def fetch(self, minimum=repcap.Minimum.Default) -> List[int]:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:ESFLatness:SCINdex:MINimum<nr6g>:CURRent \n
		Snippet: value: List[int] = driver.nrSubMeas.multiEval.listPy.esFlatness.scIndex.minimum.current.fetch(minimum = repcap.Minimum.Default) \n
		Return subcarrier indices of the equalizer spectrum flatness measurement for all measured list mode segments. At these SC
		indices, the current MINimum or MAXimum power of the equalizer coefficients has been detected within the selected range. \n
		Suppressed linked return values: reliability \n
			:param minimum: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Minimum')
			:return: minimum: Comma-separated list of values, one per measured segment"""
		minimum_cmd_val = self._base.get_repcap_cmd_value(minimum, repcap.Minimum)
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_bin_or_ascii_int_list_suppressed(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:ESFLatness:SCINdex:MINimum{minimum_cmd_val}:CURRent?', suppressed)
		return response
