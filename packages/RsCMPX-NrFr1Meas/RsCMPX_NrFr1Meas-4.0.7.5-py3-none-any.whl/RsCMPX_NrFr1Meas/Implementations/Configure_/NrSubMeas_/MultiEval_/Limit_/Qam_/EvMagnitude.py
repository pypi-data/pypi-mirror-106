from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EvMagnitude:
	"""EvMagnitude commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("evMagnitude", core, parent)

	# noinspection PyTypeChecker
	class EvMagnitudeStruct(StructBase):
		"""Structure for setting input parameters. Fields: \n
			- Rms: float or bool: No parameter help available
			- Peak: float or bool: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float_ext('Rms'),
			ArgStruct.scalar_float_ext('Peak')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Rms: float or bool = None
			self.Peak: float or bool = None

	def set(self, structure: EvMagnitudeStruct, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:EVMagnitude \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.qam.evMagnitude.set(value = [PROPERTY_STRUCT_NAME](), qam = repcap.Qam.Default) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) for QAM modulations. \n
			:param structure: for set value, see the help for EvMagnitudeStruct structure arguments.
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')"""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:EVMagnitude', structure)

	def get(self, qam=repcap.Qam.Default) -> EvMagnitudeStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:EVMagnitude \n
		Snippet: value: EvMagnitudeStruct = driver.configure.nrSubMeas.multiEval.limit.qam.evMagnitude.get(qam = repcap.Qam.Default) \n
		Defines upper limits for the RMS and peak values of the error vector magnitude (EVM) for QAM modulations. \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for EvMagnitudeStruct structure arguments."""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:EVMagnitude?', self.__class__.EvMagnitudeStruct())
