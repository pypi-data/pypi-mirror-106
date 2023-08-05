from typing import List

from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbIndex:
	"""RbIndex commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("rbIndex", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Rb_Index: List[int]: Resource block index for the general margin (at non-allocated RBs)
			- Iq_Image: List[int]: Resource block index for the IQ image margin (at image frequencies of allocated RBs)
			- Carr_Leakage: List[int]: Resource block index for the carrier leakage margin (at carrier frequency)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct('Rb_Index', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Iq_Image', DataType.IntegerList, None, False, True, 1),
			ArgStruct('Carr_Leakage', DataType.IntegerList, None, False, True, 1)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Rb_Index: List[int] = None
			self.Iq_Image: List[int] = None
			self.Carr_Leakage: List[int] = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:IEMission:MARGin:AVERage:RBINdex \n
		Snippet: value: FetchStruct = driver.nrSubMeas.multiEval.listPy.iemission.margin.average.rbIndex.fetch() \n
		Return resource block indices of the inband emission measurement for all measured list mode segments. At these RB indices,
		the CURRent, AVERage and EXTReme margins have been detected. The results are returned as triplets per segment:
		<Reliability>, {<RBindex>, <IQImage>, <CarrLeakage>}seg 1, {<RBindex>, <IQImage>, <CarrLeakage>}seg 2, ... \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:LIST:IEMission:MARGin:AVERage:RBINdex?', self.__class__.FetchStruct())
