from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Perror:
	"""Perror commands group definition. 1 total commands, 0 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("perror", core, parent)

	# noinspection PyTypeChecker
	class PerrorStruct(StructBase):
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

	def set(self, structure: PerrorStruct, qam=repcap.Qam.Default) -> None:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:PERRor \n
		Snippet: driver.configure.nrSubMeas.multiEval.limit.qam.perror.set(value = [PROPERTY_STRUCT_NAME](), qam = repcap.Qam.Default) \n
		Defines symmetric limits for the RMS and peak values of the phase error for QAM modulations. The limit check fails if the
		absolute value of the measured phase error exceeds the specified values. \n
			:param structure: for set value, see the help for PerrorStruct structure arguments.
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')"""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		self._core.io.write_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:PERRor', structure)

	def get(self, qam=repcap.Qam.Default) -> PerrorStruct:
		"""SCPI: CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM<order>:PERRor \n
		Snippet: value: PerrorStruct = driver.configure.nrSubMeas.multiEval.limit.qam.perror.get(qam = repcap.Qam.Default) \n
		Defines symmetric limits for the RMS and peak values of the phase error for QAM modulations. The limit check fails if the
		absolute value of the measured phase error exceeds the specified values. \n
			:param qam: optional repeated capability selector. Default value: Order16 (settable in the interface 'Qam')
			:return: structure: for return value, see the help for PerrorStruct structure arguments."""
		qam_cmd_val = self._base.get_repcap_cmd_value(qam, repcap.Qam)
		return self._core.io.query_struct(f'CONFigure:NRSub:MEASurement<Instance>:MEValuation:LIMit:QAM{qam_cmd_val}:PERRor?', self.__class__.PerrorStruct())
