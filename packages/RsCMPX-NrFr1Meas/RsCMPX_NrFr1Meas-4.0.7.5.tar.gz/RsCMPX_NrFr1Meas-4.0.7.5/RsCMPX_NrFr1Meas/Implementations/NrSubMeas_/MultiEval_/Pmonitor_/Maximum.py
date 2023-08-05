from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("maximum", core, parent)

	# noinspection PyTypeChecker
	class ResultData(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for power measurements exceeding the specified power limits.
			- Tx_Power: float: Total TX power"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_float('Tx_Power')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Tx_Power: float = None

	def read(self) -> ResultData:
		"""SCPI: READ:NRSub:MEASurement<Instance>:MEValuation:PMONitor:MAXimum \n
		Snippet: value: ResultData = driver.nrSubMeas.multiEval.pmonitor.maximum.read() \n
		Returns the total TX power. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'READ:NRSub:MEASurement<Instance>:MEValuation:PMONitor:MAXimum?', self.__class__.ResultData())

	def fetch(self) -> ResultData:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:PMONitor:MAXimum \n
		Snippet: value: ResultData = driver.nrSubMeas.multiEval.pmonitor.maximum.fetch() \n
		Returns the total TX power. \n
			:return: structure: for return value, see the help for ResultData structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:PMONitor:MAXimum?', self.__class__.ResultData())
