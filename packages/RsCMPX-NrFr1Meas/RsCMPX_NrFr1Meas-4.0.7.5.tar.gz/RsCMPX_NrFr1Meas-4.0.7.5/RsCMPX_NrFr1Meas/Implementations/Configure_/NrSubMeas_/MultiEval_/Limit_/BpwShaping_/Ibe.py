from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ibe:
	"""Ibe commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ibe", core, parent)

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Offset_0: float: I/Q origin offset limit for TX power 10 dBm
			- Offset_1: float: I/Q origin offset limit for TX power 0 dBm
			- Offset_2: float: I/Q origin offset limit for TX power -30 dBm
			- Offset_3: float: I/Q origin offset limit for TX power -40 dBm"""
		__meta_args_list = [
			ArgStruct.scalar_float('Offset_0'),
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Offset_0: float = None
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def get_iq_offset(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.ibe.get_iq_offset() \n
		Defines I/Q origin offset values used for calculation of an upper limit for the inband emission, for π/2-BPSK modulation
		with shaping. Four different values can be set for four TX power ranges. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset?', self.__class__.IqOffsetStruct())

	def set_iq_offset(self, value: IqOffsetStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.ibe.set_iq_offset(value = IqOffsetStruct()) \n
		Defines I/Q origin offset values used for calculation of an upper limit for the inband emission, for π/2-BPSK modulation
		with shaping. Four different values can be set for four TX power ranges. \n
			:param value: see the help for IqOffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE:IQOFfset', value)

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Minimum: float: No parameter help available
			- Evm: float: No parameter help available
			- Rb_Power: float: No parameter help available
			- Iq_Image_Lesser: float: IQ image for low TX power range
			- Iq_Image_Greater: float: IQ image for high TX power range"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Minimum'),
			ArgStruct.scalar_float('Evm'),
			ArgStruct.scalar_float('Rb_Power'),
			ArgStruct.scalar_float('Iq_Image_Lesser'),
			ArgStruct.scalar_float('Iq_Image_Greater')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Minimum: float = None
			self.Evm: float = None
			self.Rb_Power: float = None
			self.Iq_Image_Lesser: float = None
			self.Iq_Image_Greater: float = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE \n
		Snippet: value: ValueStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.ibe.get_value() \n
		Defines parameters used for calculation of an upper limit for the inband emission (π/2-BPSK modulation with shaping) ,
		see 'Inband Emissions Limits'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.ibe.set_value(value = ValueStruct()) \n
		Defines parameters used for calculation of an upper limit for the inband emission (π/2-BPSK modulation with shaping) ,
		see 'Inband Emissions Limits'. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IBE', value)
