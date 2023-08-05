from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aclr:
	"""Aclr commands group definition. 4 total commands, 2 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("aclr", core, parent)

	@property
	def utra(self):
		"""utra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_utra'):
			from .Aclr_.Utra import Utra
			self._utra = Utra(self._core, self._base)
		return self._utra

	@property
	def nr(self):
		"""nr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nr'):
			from .Aclr_.Nr import Nr
			self._nr = Nr(self._core, self._base)
		return self._nr

	# noinspection PyTypeChecker
	class TtoleranceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Test_Tol_Sub_4_Ghz: float: Test tolerance for carrier frequencies ≤ 4 GHz
			- Test_Tol_Sub_6_Gh_Z: float: Test tolerance for carrier frequencies 4 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Test_Tol_Sub_4_Ghz'),
			ArgStruct.scalar_float('Test_Tol_Sub_6_Gh_Z')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Test_Tol_Sub_4_Ghz: float = None
			self.Test_Tol_Sub_6_Gh_Z: float = None

	def get_ttolerance(self) -> TtoleranceStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance \n
		Snippet: value: TtoleranceStruct = driver.configure.nrSubMeas.multiEval.limit.aclr.get_ttolerance() \n
		Defines the test tolerance for relative ACLR limits, depending on the carrier frequency. \n
			:return: structure: for return value, see the help for TtoleranceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance?', self.__class__.TtoleranceStruct())

	def set_ttolerance(self, value: TtoleranceStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.aclr.set_ttolerance(value = TtoleranceStruct()) \n
		Defines the test tolerance for relative ACLR limits, depending on the carrier frequency. \n
			:param value: see the help for TtoleranceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:TTOLerance', value)

	def get_endc(self) -> float or bool:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:ENDC \n
		Snippet: value: float or bool = driver.configure.nrSubMeas.multiEval.limit.aclr.get_endc() \n
		Defines a relative limit for the ACLR measured in an adjacent channel in EN-DC mode. \n
			:return: relative_level: Relative lower ACLR limit without test tolerance
		"""
		response = self._core.io.query_str('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:ENDC?')
		return Conversions.str_to_float_or_bool(response)

	def set_endc(self, relative_level: float or bool) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:ENDC \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.aclr.set_endc(relative_level = 1.0) \n
		Defines a relative limit for the ACLR measured in an adjacent channel in EN-DC mode. \n
			:param relative_level: Relative lower ACLR limit without test tolerance
		"""
		param = Conversions.decimal_or_bool_value_to_str(relative_level)
		self._core.io.write(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:ACLR:ENDC {param}')

	def clone(self) -> 'Aclr':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aclr(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
