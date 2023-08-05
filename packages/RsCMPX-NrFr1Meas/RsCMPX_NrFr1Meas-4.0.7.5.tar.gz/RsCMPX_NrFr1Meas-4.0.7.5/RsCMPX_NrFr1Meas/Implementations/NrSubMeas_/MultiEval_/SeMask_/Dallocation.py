from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dallocation:
	"""Dallocation commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dallocation", core, parent)

	# noinspection PyTypeChecker
	class FetchStruct(StructBase):
		"""Response structure. Fields: \n
			- Reliability: int: 'Reliability Indicator'
			- Nr_Res_Blocks: int: Number of allocated resource blocks
			- Offset_Res_Blocks: int: Offset of the first allocated resource block from the edge of the allocated UL transmission bandwidth"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Nr_Res_Blocks'),
			ArgStruct.scalar_int('Offset_Res_Blocks')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Nr_Res_Blocks: int = None
			self.Offset_Res_Blocks: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:SEMask:DALLocation \n
		Snippet: value: FetchStruct = driver.nrSubMeas.multiEval.seMask.dallocation.fetch() \n
		Returns the detected allocation for the measured slot. If the same slot is measured by the individual measurements, all
		commands yield the same result. If different statistic counts are defined for the modulation, ACLR and spectrum emission
		mask measurements, different slots can be measured and different results can be returned by the individual commands. \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:SEMask:DALLocation?', self.__class__.FetchStruct())
