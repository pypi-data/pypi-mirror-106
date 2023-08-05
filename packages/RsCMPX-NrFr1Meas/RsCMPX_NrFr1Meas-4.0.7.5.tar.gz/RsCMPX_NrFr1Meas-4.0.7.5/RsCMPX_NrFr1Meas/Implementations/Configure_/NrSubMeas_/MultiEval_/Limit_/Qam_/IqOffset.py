from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IqOffset:
	"""IqOffset commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("iqOffset", core, parent)

	# noinspection PyTypeChecker
	class IqOffsetStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Offset_0: float: I/Q origin offset limit for TX power 10 dBm
			- Offset_1: float: I/Q origin offset limit for TX power 0 dBm
			- Offset_2: float: I/Q origin offset limit for TX power -30 dBm
			- Offset_3: float: I/Q origin offset limit for TX power -40 dBm"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Offset_0'),
			ArgStruct.scalar_float('Offset_1'),
			ArgStruct.scalar_float('Offset_2'),
			ArgStruct.scalar_float('Offset_3')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Offset_0: float = None
			self.Offset_1: float = None
			self.Offset_2: float = None
			self.Offset_3: float = None

	def set(self, structure: IqOffsetStruct, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:IQOFfset \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.qam.iqOffset.set(value = [PROPERTY_STRUCT_NAME](), qam = repcap.Qam.Default) \n
		Defines upper limits for the I/Q origin offset (QAM modulations) . Four different I/Q origin offset limits can be set for
		four TX power ranges. \n
			:param structure: for set value, see the help for IqOffsetStruct structure arguments.
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')"""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:IQOFfset', structure)

	def get(self, qam=repcap.Qam.Default) -> IqOffsetStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:IQOFfset \n
		Snippet: value: IqOffsetStruct = driver.configure.nrSubMeas.multiEval.limit.qam.iqOffset.get(qam = repcap.Qam.Default) \n
		Defines upper limits for the I/Q origin offset (QAM modulations) . Four different I/Q origin offset limits can be set for
		four TX power ranges. \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IqOffsetStruct structure arguments."""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:IQOFfset?', self.__class__.IqOffsetStruct())
