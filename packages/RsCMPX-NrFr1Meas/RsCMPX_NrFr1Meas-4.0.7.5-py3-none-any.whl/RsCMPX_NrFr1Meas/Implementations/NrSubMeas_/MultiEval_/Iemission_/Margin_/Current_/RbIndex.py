from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


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
			- Out_Of_Tolerance: int: Out of tolerance result, i.e. percentage of measurement intervals of the statistic count for modulation measurements exceeding the specified modulation limits.
			- Rb_Index: int: Resource block index for the general margin (at non-allocated RBs)
			- Iq_Image: int: Resource block index for the IQ image margin (at image frequencies of allocated RBs)
			- Carr_Leakage: int: Resource block index for the carrier leakage margin (at carrier frequency)"""
		__meta_args_list = [
			ArgStruct.scalar_int('Reliability', 'Reliability'),
			ArgStruct.scalar_int('Out_Of_Tolerance'),
			ArgStruct.scalar_int('Rb_Index'),
			ArgStruct.scalar_int('Iq_Image'),
			ArgStruct.scalar_int('Carr_Leakage')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Reliability: int = None
			self.Out_Of_Tolerance: int = None
			self.Rb_Index: int = None
			self.Iq_Image: int = None
			self.Carr_Leakage: int = None

	def fetch(self) -> FetchStruct:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:MEValuation:IEMission:MARGin:CURRent:RBINdex \n
		Snippet: value: FetchStruct = driver.nrSubMeas.multiEval.iemission.margin.current.rbIndex.fetch() \n
		Return resource block indices for inband emission margins. At these RB indices, the CURRent, AVERage and EXTReme margins
		have been detected (see method RsCMPX_NrFr1Meas.NrSubMeas.MultiEval.Iemission.Margin.Current.fetch and ...
		:AVERage/EXTReme) . \n
			:return: structure: for return value, see the help for FetchStruct structure arguments."""
		return self._core.io.query_struct(f'FETCh:NRSub:MEASurement<Instance>:MEValuation:IEMission:MARGin:CURRent:RBINdex?', self.__class__.FetchStruct())
