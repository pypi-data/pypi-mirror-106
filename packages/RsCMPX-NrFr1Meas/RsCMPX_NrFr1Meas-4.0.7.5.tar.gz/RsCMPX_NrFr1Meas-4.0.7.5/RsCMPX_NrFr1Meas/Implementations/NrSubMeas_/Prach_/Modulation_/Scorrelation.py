from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.ArgSingleSuppressed import ArgSingleSuppressed
from .....Internal.Types import DataType


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scorrelation:
	"""Scorrelation commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scorrelation", core, parent)

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Scorrelation_.Preamble import Preamble
			self._preamble = Preamble(self._core, self._base)
		return self._preamble

	def fetch(self) -> float:
		"""SCPI: FETCh:NRSub:MEASurement<Instance>:PRACh:MODulation:SCORrelation \n
		Snippet: value: float = driver.nrSubMeas.prach.modulation.scorrelation.fetch() \n
		Returns the sequence correlation for single-preamble measurements. It indicates the correlation between the ideal
		preamble sequence determined from the parameter settings and the measured preamble sequence. A value of 1 corresponds to
		perfect correlation. A value much smaller than 1 indicates that the preamble sequence was not found. \n
		Suppressed linked return values: reliability \n
			:return: seq_correlation: Sequence correlation"""
		suppressed = ArgSingleSuppressed(0, DataType.Integer, False, 1, 'Reliability')
		response = self._core.io.query_str_suppressed(f'FETCh:NRSub:MEASurement<Instance>:PRACh:MODulation:SCORrelation?', suppressed)
		return Conversions.str_to_float(response)

	def clone(self) -> 'Scorrelation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scorrelation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
