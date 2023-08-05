from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ttolerance:
	"""Ttolerance commands group definition. 2 total commands, 0 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ttolerance", core, parent)

	# noinspection PyTypeChecker
	class CbltStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tt_Power_Less_3_G: float: For carrier center frequencies up to 3 GHz
			- Tt_Power_Great_3_G: float: For carrier center frequencies 3 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Tt_Power_Less_3_G'),
			ArgStruct.scalar_float('Tt_Power_Great_3_G')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tt_Power_Less_3_G: float = None
			self.Tt_Power_Great_3_G: float = None

	def get_cblt(self) -> CbltStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBLT \n
		Snippet: value: CbltStruct = driver.configure.nrSubMeas.multiEval.limit.pdynamics.ttolerance.get_cblt() \n
		Defines test tolerances for power dynamics limits, for channel BW up to 40 MHz. \n
			:return: structure: for return value, see the help for CbltStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBLT?', self.__class__.CbltStruct())

	def set_cblt(self, value: CbltStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBLT \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.pdynamics.ttolerance.set_cblt(value = CbltStruct()) \n
		Defines test tolerances for power dynamics limits, for channel BW up to 40 MHz. \n
			:param value: see the help for CbltStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBLT', value)

	# noinspection PyTypeChecker
	class CbgtStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Tt_Power_Less_3_G: float: For carrier center frequencies up to 3 GHz
			- Tt_Power_Great_3_G: float: For carrier center frequencies 3 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Tt_Power_Less_3_G'),
			ArgStruct.scalar_float('Tt_Power_Great_3_G')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tt_Power_Less_3_G: float = None
			self.Tt_Power_Great_3_G: float = None

	def get_cbgt(self) -> CbgtStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBGT \n
		Snippet: value: CbgtStruct = driver.configure.nrSubMeas.multiEval.limit.pdynamics.ttolerance.get_cbgt() \n
		Defines test tolerances for power dynamics limits, for channel BW > 40 MHz. \n
			:return: structure: for return value, see the help for CbgtStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBGT?', self.__class__.CbgtStruct())

	def set_cbgt(self, value: CbgtStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBGT \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.pdynamics.ttolerance.set_cbgt(value = CbgtStruct()) \n
		Defines test tolerances for power dynamics limits, for channel BW > 40 MHz. \n
			:param value: see the help for CbgtStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:PDYNamics:TTOLerance:CBGT', value)
