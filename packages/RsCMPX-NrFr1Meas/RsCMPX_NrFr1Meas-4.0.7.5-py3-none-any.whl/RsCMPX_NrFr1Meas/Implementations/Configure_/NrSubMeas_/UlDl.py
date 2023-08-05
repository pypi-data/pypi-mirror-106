from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UlDl:
	"""UlDl commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ulDl", core, parent)

	# noinspection PyTypeChecker
	def get_periodicity(self) -> enums.Periodicity:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:ULDL:PERiodicity \n
		Snippet: value: enums.Periodicity = driver.configure.nrSubMeas.ulDl.get_periodicity() \n
		Configures the periodicity of the TDD UL-DL pattern.
		For Signal Path = Network, use [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:PERiodicity. \n
			:return: periodicity: 0.5 ms, 1 ms, 1.25 ms, 2 ms, 2.5 ms, 3 ms, 4 ms, 5 ms, 10 ms
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:ULDL:PERiodicity?')
		return Conversions.str_to_scalar_enum(response, enums.Periodicity)

	def set_periodicity(self, periodicity: enums.Periodicity) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:ULDL:PERiodicity \n
		Snippet: driver.configure.nrSubMeas.ulDl.set_periodicity(periodicity = enums.Periodicity.MS05) \n
		Configures the periodicity of the TDD UL-DL pattern.
		For Signal Path = Network, use [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:PERiodicity. \n
			:param periodicity: 0.5 ms, 1 ms, 1.25 ms, 2 ms, 2.5 ms, 3 ms, 4 ms, 5 ms, 10 ms
		"""
		param = Conversions.enum_scalar_to_str(periodicity, enums.Periodicity)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:ULDL:PERiodicity {param}')

	# noinspection PyTypeChecker
	class PatternStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Sc_Spacing: enums.SubCarrSpacing: Subcarrier spacing for which the other settings apply.
			- Dl_Slots: int: Specifies 'nrofDownlinkSlots'.
			- Dl_Symbols: int: Specifies 'nrofDownlinkSymbols'.
			- Ul_Slots: int: Specifies 'nrofUplinkSlots'.
			- Ul_Symbols: int: Specifies 'nrofUplinkSymbols'."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Sc_Spacing', enums.SubCarrSpacing),
			ArgStruct.scalar_int('Dl_Slots'),
			ArgStruct.scalar_int('Dl_Symbols'),
			ArgStruct.scalar_int('Ul_Slots'),
			ArgStruct.scalar_int('Ul_Symbols')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Sc_Spacing: enums.SubCarrSpacing = None
			self.Dl_Slots: int = None
			self.Dl_Symbols: int = None
			self.Ul_Slots: int = None
			self.Ul_Symbols: int = None

	# noinspection PyTypeChecker
	def get_pattern(self) -> PatternStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:ULDL:PATTern \n
		Snippet: value: PatternStruct = driver.configure.nrSubMeas.ulDl.get_pattern() \n
		Configures the TDD UL-DL pattern for the <SCSpacing>. The ranges have dependencies, see 'TDD UL-DL configuration'.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:FSSYmbol
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:FSSYmbol  \n
			:return: structure: for return value, see the help for PatternStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:ULDL:PATTern?', self.__class__.PatternStruct())

	def set_pattern(self, value: PatternStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:ULDL:PATTern \n
		Snippet: driver.configure.nrSubMeas.ulDl.set_pattern(value = PatternStruct()) \n
		Configures the TDD UL-DL pattern for the <SCSpacing>. The ranges have dependencies, see 'TDD UL-DL configuration'.
			INTRO_CMD_HELP: For Signal Path = Network, use: \n
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:DL:FSSYmbol
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:NSLots
			- [CONFigure:]SIGNaling:NRADio:CELL:TDD:PATTern{p}:UL:FSSYmbol  \n
			:param value: see the help for PatternStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:ULDL:PATTern', value)
