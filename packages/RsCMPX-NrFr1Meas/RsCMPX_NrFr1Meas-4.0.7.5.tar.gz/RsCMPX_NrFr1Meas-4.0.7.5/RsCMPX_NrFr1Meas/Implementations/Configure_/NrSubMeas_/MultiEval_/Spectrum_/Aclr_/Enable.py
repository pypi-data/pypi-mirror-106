from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("enable", core, parent)

	def get_endc(self) -> bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle:ENDC \n
		Snippet: value: bool = driver.configure.nrSubMeas.multiEval.spectrum.aclr.enable.get_endc() \n
		Enables or disables the evaluation of the adjacent channel power in EN-DC mode. \n
			:return: endc: No help available
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle:ENDC?')
		return Conversions.str_to_bool(response)

	def set_endc(self, endc: bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle:ENDC \n
		Snippet: driver.configure.nrSubMeas.multiEval.spectrum.aclr.enable.set_endc(endc = False) \n
		Enables or disables the evaluation of the adjacent channel power in EN-DC mode. \n
			:param endc: No help available
		"""
		param = Conversions.bool_to_str(endc)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle:ENDC {param}')

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Utra_1: bool: No parameter help available
			- Utra_2: bool: No parameter help available
			- Nr: bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Utra_1'),
			ArgStruct.scalar_bool('Utra_2'),
			ArgStruct.scalar_bool('Nr')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Utra_1: bool = None
			self.Utra_2: bool = None
			self.Nr: bool = None

	def get_value(self) -> ValueStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: value: ValueStruct = driver.configure.nrSubMeas.multiEval.spectrum.aclr.enable.get_value() \n
		Enables or disables the evaluation of the first adjacent UTRA channels, second adjacent UTRA channels and first adjacent
		NR channels. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle?', self.__class__.ValueStruct())

	def set_value(self, value: ValueStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle \n
		Snippet: driver.configure.nrSubMeas.multiEval.spectrum.aclr.enable.set_value(value = ValueStruct()) \n
		Enables or disables the evaluation of the first adjacent UTRA channels, second adjacent UTRA channels and first adjacent
		NR channels. \n
			:param value: see the help for ValueStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:SPECtrum:ACLR:ENABle', value)
