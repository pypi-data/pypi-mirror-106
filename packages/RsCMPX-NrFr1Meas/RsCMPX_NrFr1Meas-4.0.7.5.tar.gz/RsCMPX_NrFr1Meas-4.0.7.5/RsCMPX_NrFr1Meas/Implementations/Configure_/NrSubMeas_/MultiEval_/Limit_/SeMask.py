from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SeMask:
	"""SeMask commands group definition. 6 total commands, 2 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("seMask", core, parent)

	@property
	def obwLimit(self):
		"""obwLimit commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_obwLimit'):
			from .SeMask_.ObwLimit import ObwLimit
			self._obwLimit = ObwLimit(self._core, self._base)
		return self._obwLimit

	@property
	def area(self):
		"""area commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_area'):
			from .SeMask_.Area import Area
			self._area = Area(self._core, self._base)
		return self._area

	# noinspection PyTypeChecker
	class TtoleranceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Test_Tol_Sub_3_Ghz: float: Test tolerance for carrier frequencies ≤ 3 GHz
			- Test_Tol_Sub_4_Ghz: float: Test tolerance for carrier frequencies 3 GHz and ≤ 4.2 GHz
			- Test_Tol_Sub_6_Gh_Z: float: Test tolerance for carrier frequencies 4.2 GHz"""
		__meta_args_list = [
			ArgStruct.scalar_float('Test_Tol_Sub_3_Ghz'),
			ArgStruct.scalar_float('Test_Tol_Sub_4_Ghz'),
			ArgStruct.scalar_float('Test_Tol_Sub_6_Gh_Z')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Test_Tol_Sub_3_Ghz: float = None
			self.Test_Tol_Sub_4_Ghz: float = None
			self.Test_Tol_Sub_6_Gh_Z: float = None

	def get_ttolerance(self) -> TtoleranceStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:TTOLerance \n
		Snippet: value: TtoleranceStruct = driver.configure.nrSubMeas.multiEval.limit.seMask.get_ttolerance() \n
		Defines the test tolerance for spectrum emission masks, depending on the carrier frequency. \n
			:return: structure: for return value, see the help for TtoleranceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:TTOLerance?', self.__class__.TtoleranceStruct())

	def set_ttolerance(self, value: TtoleranceStruct) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:TTOLerance \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.seMask.set_ttolerance(value = TtoleranceStruct()) \n
		Defines the test tolerance for spectrum emission masks, depending on the carrier frequency. \n
			:param value: see the help for TtoleranceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:TTOLerance', value)

	def clone(self) -> 'SeMask':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SeMask(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
