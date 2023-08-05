from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.StructBase import StructBase
from .....Internal.ArgStruct import ArgStruct
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dmrs:
	"""Dmrs commands group definition. 5 total commands, 0 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("dmrs", core, parent)

	def get_config_type(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:CONFigtype \n
		Snippet: value: int = driver.configure.nrSubMeas.multiEval.dmrs.get_config_type() \n
		No command help available \n
			:return: config_type: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:CONFigtype?')
		return Conversions.str_to_int(response)

	def get_max_length(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:MAXLength \n
		Snippet: value: int = driver.configure.nrSubMeas.multiEval.dmrs.get_max_length() \n
		No command help available \n
			:return: max_length: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:MAXLength?')
		return Conversions.str_to_int(response)

	def set_max_length(self, max_length: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:MAXLength \n
		Snippet: driver.configure.nrSubMeas.multiEval.dmrs.set_max_length(max_length = 1) \n
		No command help available \n
			:param max_length: No help available
		"""
		param = Conversions.decimal_value_to_str(max_length)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:MAXLength {param}')

	def get_aposition(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:APOSition \n
		Snippet: value: int = driver.configure.nrSubMeas.multiEval.dmrs.get_aposition() \n
		No command help available \n
			:return: add_position: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:APOSition?')
		return Conversions.str_to_int(response)

	def set_aposition(self, add_position: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:APOSition \n
		Snippet: driver.configure.nrSubMeas.multiEval.dmrs.set_aposition(add_position = 1) \n
		No command help available \n
			:param add_position: No help available
		"""
		param = Conversions.decimal_value_to_str(add_position)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:APOSition {param}')

	def get_lzero(self) -> int:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:LZERo \n
		Snippet: value: int = driver.configure.nrSubMeas.multiEval.dmrs.get_lzero() \n
		No command help available \n
			:return: lzero: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:LZERo?')
		return Conversions.str_to_int(response)

	def set_lzero(self, lzero: int) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:LZERo \n
		Snippet: driver.configure.nrSubMeas.multiEval.dmrs.set_lzero(lzero = 1) \n
		No command help available \n
			:param lzero: No help available
		"""
		param = Conversions.decimal_value_to_str(lzero)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:LZERo {param}')

	# noinspection PyTypeChecker
	class SgenerationStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Generator: enums.Generator: No parameter help available
			- Dmrs_Id: int: No parameter help available
			- Scid: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Generator', enums.Generator),
			ArgStruct.scalar_int('Dmrs_Id'),
			ArgStruct.scalar_int('Scid')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Generator: enums.Generator = None
			self.Dmrs_Id: int = None
			self.Scid: int = None

	# noinspection PyTypeChecker
	def get_sgeneration(self) -> SgenerationStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:SGENeration \n
		Snippet: value: SgenerationStruct = driver.configure.nrSubMeas.multiEval.dmrs.get_sgeneration() \n
		No command help available \n
			:return: structure: for return value, see the help for SgenerationStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:SGENeration?', self.__class__.SgenerationStruct())

	def set_sgeneration(self, value: SgenerationStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:SGENeration \n
		Snippet: driver.configure.nrSubMeas.multiEval.dmrs.set_sgeneration(value = SgenerationStruct()) \n
		No command help available \n
			:param value: see the help for SgenerationStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:DMRS:SGENeration', value)
