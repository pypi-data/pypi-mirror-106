from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Endc:
	"""Endc commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("endc", core, parent)

	# noinspection PyTypeChecker
	class EndcStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF: disables the check of these requirements ON: enables the check of these requirements
			- Frequency_Start: float: Start frequency of the area, relative to the edges of the channel bandwidth
			- Frequency_End: float: Stop frequency of the area, relative to the edges of the channel bandwidth
			- Level: float: Upper limit for the area
			- Rbw: enums.RbwA: Resolution bandwidth to be used for the area K030: 30 kHz PC1: 1 % of aggregated channel bandwidth M1: 1 MHz"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Frequency_Start'),
			ArgStruct.scalar_float('Frequency_End'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Rbw', enums.RbwA)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Frequency_Start: float = None
			self.Frequency_End: float = None
			self.Level: float = None
			self.Rbw: enums.RbwA = None

	def set(self, structure: EndcStruct, area=repcap.Area.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<nr>:ENDC \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.seMask.area.endc.set(value = [PROPERTY_STRUCT_NAME](), area = repcap.Area.Default) \n
		Defines general requirements for the emission mask area number <no> (for EN-DC) . The activation state, the area borders,
		an upper limit and the resolution bandwidth must be specified. \n
			:param structure: for set value, see the help for EndcStruct structure arguments.
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')"""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:ENDC', structure)

	def get(self, area=repcap.Area.Default) -> EndcStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA<nr>:ENDC \n
		Snippet: value: EndcStruct = driver.configure.nrSubMeas.multiEval.limit.seMask.area.endc.get(area = repcap.Area.Default) \n
		Defines general requirements for the emission mask area number <no> (for EN-DC) . The activation state, the area borders,
		an upper limit and the resolution bandwidth must be specified. \n
			:param area: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Area')
			:return: structure: for return value, see the help for EndcStruct structure arguments."""
		area_cmd_val = self._base.get_repcap_cmd_value(area, repcap.Area)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:SEMask:AREA{area_cmd_val}:ENDC?', self.__class__.EndcStruct())
