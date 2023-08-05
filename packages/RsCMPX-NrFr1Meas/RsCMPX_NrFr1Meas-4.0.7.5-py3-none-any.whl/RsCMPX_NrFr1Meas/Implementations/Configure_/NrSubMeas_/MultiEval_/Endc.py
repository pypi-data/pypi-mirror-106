from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Endc:
	"""Endc commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("endc", core, parent)

	# noinspection PyTypeChecker
	class EutraStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Channel_Bw: enums.ChannelBwidthB: Channel bandwidth in MHz (5 MHz to 20 MHz)
			- Carrier_Position: enums.CarrierPosition: Position of LTE carrier left (LONR) or right (RONR) of NR carrier."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Channel_Bw', enums.ChannelBwidthB),
			ArgStruct.scalar_enum('Carrier_Position', enums.CarrierPosition)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Channel_Bw: enums.ChannelBwidthB = None
			self.Carrier_Position: enums.CarrierPosition = None

	# noinspection PyTypeChecker
	def get_eutra(self) -> EutraStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC:EUTRa \n
		Snippet: value: EutraStruct = driver.configure.nrSubMeas.multiEval.endc.get_eutra() \n
		Configures LTE settings for EN-DC. \n
			:return: structure: for return value, see the help for EutraStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC:EUTRa?', self.__class__.EutraStruct())

	def set_eutra(self, value: EutraStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC:EUTRa \n
		Snippet: driver.configure.nrSubMeas.multiEval.endc.set_eutra(value = EutraStruct()) \n
		Configures LTE settings for EN-DC. \n
			:param value: see the help for EutraStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC:EUTRa', value)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC \n
		Snippet: value: bool = driver.configure.nrSubMeas.multiEval.endc.get_value() \n
		Enables or disables the EN-DC mode of the measurement. \n
			:return: on_off: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC?')
		return Conversions.str_to_bool(response)

	def set_value(self, on_off: bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC \n
		Snippet: driver.configure.nrSubMeas.multiEval.endc.set_value(on_off = False) \n
		Enables or disables the EN-DC mode of the measurement. \n
			:param on_off: No help available
		"""
		param = Conversions.bool_to_str(on_off)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:ENDC {param}')
