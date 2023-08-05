from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ibe:
	"""Ibe commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ibe", core, parent)

	@property
	def iqOffset(self):
		"""iqOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqOffset'):
			from .Ibe_.IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._base)
		return self._iqOffset

	# noinspection PyTypeChecker
	class IbeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Enable: bool: OFF: disables the limit check ON: enables the limit check
			- Minimum: float: No parameter help available
			- Evm: float: No parameter help available
			- Rb_Power: float: No parameter help available
			- Iq_Image_Lesser: float: IQ image for low TX power range
			- Iq_Image_Greater: float: IQ image for high TX power range"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Enable'),
			ArgStruct.scalar_float('Minimum'),
			ArgStruct.scalar_float('Evm'),
			ArgStruct.scalar_float('Rb_Power'),
			ArgStruct.scalar_float('Iq_Image_Lesser'),
			ArgStruct.scalar_float('Iq_Image_Greater')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Enable: bool = None
			self.Minimum: float = None
			self.Evm: float = None
			self.Rb_Power: float = None
			self.Iq_Image_Lesser: float = None
			self.Iq_Image_Greater: float = None

	def set(self, structure: IbeStruct, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:IBE \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.qam.ibe.set(value = [PROPERTY_STRUCT_NAME](), qam = repcap.Qam.Default) \n
		Defines parameters used for calculation of an upper limit for the inband emission (QAM modulations) , see 'Inband
		Emissions Limits'. \n
			:param structure: for set value, see the help for IbeStruct structure arguments.
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')"""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:IBE', structure)

	def get(self, qam=repcap.Qam.Default) -> IbeStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:IBE \n
		Snippet: value: IbeStruct = driver.configure.nrSubMeas.multiEval.limit.qam.ibe.get(qam = repcap.Qam.Default) \n
		Defines parameters used for calculation of an upper limit for the inband emission (QAM modulations) , see 'Inband
		Emissions Limits'. \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for IbeStruct structure arguments."""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:IBE?', self.__class__.IbeStruct())

	def clone(self) -> 'Ibe':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ibe(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
