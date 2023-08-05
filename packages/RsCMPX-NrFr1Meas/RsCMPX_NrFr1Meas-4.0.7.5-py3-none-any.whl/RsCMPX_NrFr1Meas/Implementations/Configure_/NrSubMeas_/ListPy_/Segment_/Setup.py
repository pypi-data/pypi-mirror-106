from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("setup", core, parent)

	# noinspection PyTypeChecker
	class SetupStruct(StructBase):
		"""Structure for setting input parameters. Contains optional setting parameters. Fields: \n
			- Segment_Length: int: Number of subframes in the segment
			- Level: float: Expected nominal power in the segment. The range can be calculated as follows: Range (Expected Nominal Power) = Range (Input Power) + External Attenuation - User Margin The input power range is stated in the data sheet.
			- Duplex_Mode: enums.DuplexModeB: Duplex mode used in the segment
			- Band: enums.Band: TDD: OB34 | OB38 | ... | OB41 | OB48 | OB50 | OB51 | OB77 | ... | OB84 | OB86 Operating band used in the segment
			- Retrigger_Flag: enums.RetriggerFlag: Specifies whether the measurement waits for a trigger event before measuring the segment, or not. For the first segment, the value OFF is always interpreted as ON. For subsequent segments, the retrigger flag is ignored for trigger mode ONCE and evaluated for trigger mode SEGMent, see [CMDLINK: TRIGger:NRSub:MEASi:MEValuation:LIST:MODE CMDLINK]. OFF: measure the segment without retrigger ON: wait for a trigger event from the trigger source configured via [CMDLINK: TRIGger:NRSub:MEASi:MEValuation:SOURce CMDLINK] IFPower: wait for a trigger event from the trigger source IF Power
			- Evaluat_Offset: int: Number of subframes at the beginning of the segment that are not evaluated
			- Network_Sig_Val: enums.NetworkSigVal: Optional setting parameter. Network signaled value to be used for the segment"""
		__meta_args_list = [
			ArgStruct.scalar_int('Segment_Length'),
			ArgStruct.scalar_float('Level'),
			ArgStruct.scalar_enum('Duplex_Mode', enums.DuplexModeB),
			ArgStruct.scalar_enum('Band', enums.Band),
			ArgStruct.scalar_enum('Retrigger_Flag', enums.RetriggerFlag),
			ArgStruct.scalar_int('Evaluat_Offset'),
			ArgStruct.scalar_enum('Network_Sig_Val', enums.NetworkSigVal)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Segment_Length: int = None
			self.Level: float = None
			self.Duplex_Mode: enums.DuplexModeB = None
			self.Band: enums.Band = None
			self.Retrigger_Flag: enums.RetriggerFlag = None
			self.Evaluat_Offset: int = None
			self.Network_Sig_Val: enums.NetworkSigVal = None

	def set(self, structure: SetupStruct, sEGMent=repcap.SEGMent.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>:SETup \n
		Snippet: driver.configure.nrSubMeas.listPy.segment.setup.set(value = [PROPERTY_STRUCT_NAME](), sEGMent = repcap.SEGMent.Default) \n
		Defines the length and analyzer settings of segment <no>. For carrier-specific settings, there are additional commands.
		This command and the other segment configuration commands must be sent for all segments to be measured (method
		RsCMPX_NrFr1Meas.Configure.NrSubMeas.MultiEval.ListPy.lrange) . \n
			:param structure: for set value, see the help for SetupStruct structure arguments.
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')"""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup', structure)

	def get(self, sEGMent=repcap.SEGMent.Default) -> SetupStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent<no>:SETup \n
		Snippet: value: SetupStruct = driver.configure.nrSubMeas.listPy.segment.setup.get(sEGMent = repcap.SEGMent.Default) \n
		Defines the length and analyzer settings of segment <no>. For carrier-specific settings, there are additional commands.
		This command and the other segment configuration commands must be sent for all segments to be measured (method
		RsCMPX_NrFr1Meas.Configure.NrSubMeas.MultiEval.ListPy.lrange) . \n
			:param sEGMent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:return: structure: for return value, see the help for SetupStruct structure arguments."""
		sEGMent_cmd_val = self._base.get_repcap_cmd_value(sEGMent, repcap.SEGMent)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:LIST:SEGMent{sEGMent_cmd_val}:SETup?', self.__class__.SetupStruct())
