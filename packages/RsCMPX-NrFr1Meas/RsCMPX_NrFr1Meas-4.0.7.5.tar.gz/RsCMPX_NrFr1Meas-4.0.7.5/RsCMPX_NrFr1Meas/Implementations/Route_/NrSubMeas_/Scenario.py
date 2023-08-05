from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 4 total commands, 1 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def maProtocol(self):
		"""maProtocol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maProtocol'):
			from .Scenario_.MaProtocol import MaProtocol
			self._maProtocol = MaProtocol(self._core, self._base)
		return self._maProtocol

	# noinspection PyTypeChecker
	class SaloneStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Rx_Connector: enums.RxConnector: RF connector for the input path Single R&S CMW500: RFnC for RF n COM CMWflexx: RabC for CMW a, connector RF b COM
			- Rf_Converter: enums.RfConverter: RX module for the input path Single R&S CMW500: TX1 to TX4 CMWflexx: TXab for CMW a, TX b"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rf_Converter', enums.RfConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rx_Connector: enums.RxConnector = None
			self.Rf_Converter: enums.RfConverter = None

	# noinspection PyTypeChecker
	def get_salone(self) -> SaloneStruct:
		"""SCPI: ROUTe:NRSub:MEASurement<Instance>:SCENario:SALone \n
		Snippet: value: SaloneStruct = driver.route.nrSubMeas.scenario.get_salone() \n
		Selects the signal path for the measured signal.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM and RF 2 COM are compatible with TX 1 and TX 3.
			- RF 3 COM and RF 4 COM are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:return: structure: for return value, see the help for SaloneStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:NRSub:MEASurement<Instance>:SCENario:SALone?', self.__class__.SaloneStruct())

	def set_salone(self, value: SaloneStruct) -> None:
		"""SCPI: ROUTe:NRSub:MEASurement<Instance>:SCENario:SALone \n
		Snippet: driver.route.nrSubMeas.scenario.set_salone(value = SaloneStruct()) \n
		Selects the signal path for the measured signal.
			INTRO_CMD_HELP: Value combinations: \n
			- RF 1 COM and RF 2 COM are compatible with TX 1 and TX 3.
			- RF 3 COM and RF 4 COM are compatible with TX 2 and TX 4.
		Note: This command is an interim solution. It is planned to replace this command in a later software version. \n
			:param value: see the help for SaloneStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:NRSub:MEASurement<Instance>:SCENario:SALone', value)

	# noinspection PyTypeChecker
	class CspathStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Master: str: No parameter help available
			- Carrier: str: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_str('Master'),
			ArgStruct.scalar_str('Carrier')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Master: str = None
			self.Carrier: str = None

	def get_cspath(self) -> CspathStruct:
		"""SCPI: ROUTe:NRSub:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: value: CspathStruct = driver.route.nrSubMeas.scenario.get_cspath() \n
		No command help available \n
			:return: structure: for return value, see the help for CspathStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:NRSub:MEASurement<Instance>:SCENario:CSPath?', self.__class__.CspathStruct())

	def set_cspath(self, value: CspathStruct) -> None:
		"""SCPI: ROUTe:NRSub:MEASurement<Instance>:SCENario:CSPath \n
		Snippet: driver.route.nrSubMeas.scenario.set_cspath(value = CspathStruct()) \n
		No command help available \n
			:param value: see the help for CspathStruct structure arguments.
		"""
		self._core.io.write_struct('ROUTe:NRSub:MEASurement<Instance>:SCENario:CSPath', value)

	# noinspection PyTypeChecker
	def get_value(self) -> enums.Scenario:
		"""SCPI: ROUTe:NRSub:MEASurement<Instance>:SCENario \n
		Snippet: value: enums.Scenario = driver.route.nrSubMeas.scenario.get_value() \n
		No command help available \n
			:return: scenario: No help available
		"""
		response = self._core.io.query_str('ROUTe:NRSub:MEASurement<Instance>:SCENario?')
		return Conversions.str_to_scalar_enum(response, enums.Scenario)

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
