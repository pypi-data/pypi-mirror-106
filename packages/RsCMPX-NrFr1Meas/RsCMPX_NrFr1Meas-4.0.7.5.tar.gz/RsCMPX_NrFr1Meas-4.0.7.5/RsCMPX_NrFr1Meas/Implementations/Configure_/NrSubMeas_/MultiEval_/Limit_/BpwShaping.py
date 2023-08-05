from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BpwShaping:
	"""BpwShaping commands group definition. 8 total commands, 1 Sub-groups, 6 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("bpwShaping", core, parent)

	@property
	def ibe(self):
		"""ibe commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ibe'):
			from .BpwShaping_.Ibe import Ibe
			self._ibe = Ibe(self._core, self._base)
		return self._ibe

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_ev_magnitude(self) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.get_ev_magnitude() \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) for π/2-BPSK with shaping. \n
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:EVMagnitude?', self.__class__.EvMagnitudeStruct())

	def set_ev_magnitude(self, value: EvMagnitudeStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:EVMagnitude \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.set_ev_magnitude(value = EvMagnitudeStruct()) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) for π/2-BPSK with shaping. \n
			:param value: see the help for EvMagnitudeStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:EVMagnitude', value)

	# noinspection PyTypeChecker
	class MerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_merror(self) -> MerrorStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:MERRor \n
		Snippet: value: MerrorStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.get_merror() \n
		Defines upper limits for the RMS and peak values of the magnitude error for π/2-BPSK with shaping. \n
			:return: structure: for return value, see the help for MerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:MERRor?', self.__class__.MerrorStruct())

	def set_merror(self, value: MerrorStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:MERRor \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.set_merror(value = MerrorStruct()) \n
		Defines upper limits for the RMS and peak values of the magnitude error for π/2-BPSK with shaping. \n
			:param value: see the help for MerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:MERRor', value)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def get_perror(self) -> PerrorStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.get_perror() \n
		Defines symmetric limits for the RMS and peak values of the phase error for π/2-BPSK with shaping. The limit check fails
		if the absolute value of the measured phase error exceeds the specified values. \n
			:return: structure: for return value, see the help for PerrorStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:PERRor?', self.__class__.PerrorStruct())

	def set_perror(self, value: PerrorStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:PERRor \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.set_perror(value = PerrorStruct()) \n
		Defines symmetric limits for the RMS and peak values of the phase error for π/2-BPSK with shaping. The limit check fails
		if the absolute value of the measured phase error exceeds the specified values. \n
			:param value: see the help for PerrorStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:PERRor', value)

	def get_freq_error(self) -> float or bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:FERRor \n
		Snippet: value: float or bool = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.get_freq_error() \n
		Defines an upper limit for the carrier frequency error (π/2-BPSK modulation with shaping) . \n
			:return: frequency_error: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:FERRor?')
		return Conversions.str_to_float_or_bool(response)

	def set_freq_error(self, frequency_error: float or bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:FERRor \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.set_freq_error(frequency_error = 1.0) \n
		Defines an upper limit for the carrier frequency error (π/2-BPSK modulation with shaping) . \n
			:param frequency_error: No help available
		"""
		param = Conversions.decimal_or_bool_value_to_str(frequency_error)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:FERRor {param}')

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Offset_0: float: I/Q origin offset limit for TX power 10 dBm
			- Offset_1: float: I/Q origin offset limit for TX power 0 dBm
			- Offset_2: float: I/Q origin offset limit for TX power -30 dBm
			- Offset_3: float: I/Q origin offset limit for TX power -40 dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Offset_0'),
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Offset_0: float = None
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def get_iq_offset(self) -> IqOffsetStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.get_iq_offset() \n
		Defines upper limits for the I/Q origin offset (π/2-BPSK modulation with shaping) . Four different I/Q origin offset
		limits can be set for four TX power ranges. \n
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IQOFfset?', self.__class__.IqOffsetStruct())

	def set_iq_offset(self, value: IqOffsetStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IQOFfset \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.set_iq_offset(value = IqOffsetStruct()) \n
		Defines upper limits for the I/Q origin offset (π/2-BPSK modulation with shaping) . Four different I/Q origin offset
		limits can be set for four TX power ranges. \n
			:param value: see the help for IqOffsetStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:IQOFfset', value)

	# noinspection PyTypeChecker
	class EsFlatnessStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Range_1: float: Upper limit for max(range 1) - min(range 1)
			- Range_2: float: Upper limit for max(range 2) - min(range 2)"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Range_1'),
			ArgStruct.scalar_float('Range_2')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Range_1: float = None
			self.Range_2: float = None

	def get_es_flatness(self) -> EsFlatnessStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:ESFLatness \n
		Snippet: value: EsFlatnessStruct = driver.configure.nrSubMeas.multiEval.limit.bpwShaping.get_es_flatness() \n
		Defines limits for the equalizer spectrum flatness (π/2-BPSK modulation with shaping) . \n
			:return: structure: for return value, see the help for EsFlatnessStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:ESFLatness?', self.__class__.EsFlatnessStruct())

	def set_es_flatness(self, value: EsFlatnessStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:ESFLatness \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.bpwShaping.set_es_flatness(value = EsFlatnessStruct()) \n
		Defines limits for the equalizer spectrum flatness (π/2-BPSK modulation with shaping) . \n
			:param value: see the help for EsFlatnessStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:BPWShaping:ESFLatness', value)

	def clone(self) -> 'BpwShaping':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = BpwShaping(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
