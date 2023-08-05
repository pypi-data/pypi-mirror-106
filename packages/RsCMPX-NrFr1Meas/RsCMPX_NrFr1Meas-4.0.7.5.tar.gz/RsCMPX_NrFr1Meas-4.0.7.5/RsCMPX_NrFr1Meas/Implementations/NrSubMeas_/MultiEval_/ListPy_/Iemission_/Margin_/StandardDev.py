from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StandardDev:
	"""StandardDev commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("standardDev", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Margin: List[float]: Margin over all non-allocated RBs (scope of general limit component)
			- Iq_Image: List[float]: Margin at image frequencies of allocated RBs (scope of IQ image limit component)
			- Carr_Leakage: List[float]: Margin at the carrier frequency (scope of IQ offset limit component)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Margin', DataType.FloatList, None, False, True, 1),
			ArgStruct('Iq_Image', DataType.FloatList, None, False, True, 1),
			ArgStruct('Carr_Leakage', DataType.FloatList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Margin: List[float] = None
			self.Iq_Image: List[float] = None
			self.Carr_Leakage: List[float] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:IEMission:MARGin:SDEViation \n
		Snippet: value: FetchStruct = driver.nrSubMeas.multiEval.listPy.iemission.margin.standardDev.fetch() \n
		Return the inband emission limit line margin results for all measured list mode segments. The CURRent margins indicate
		the minimum (vertical) distance between the limit line and the current trace. A negative result indicates that the limit
		is exceeded. The AVERage, EXTReme and SDEViation values are calculated from the current margins. The results are returned
		as triplets per segment: <Reliability>, {<Margin>, <IQImage>, <CarrLeakage>}seg 1, {<Margin>, <IQImage>,
		<CarrLeakage>}seg 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:IEMission:MARGin:SDEViation?', self.__class__.FetchStruct())
