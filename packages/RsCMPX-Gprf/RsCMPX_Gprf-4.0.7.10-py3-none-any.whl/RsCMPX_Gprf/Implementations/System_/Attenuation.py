from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Attenuation:
	"""Attenuation commands group definition. 2 total commands, 1 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("attenuation", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_correctionTable'):
			from .Attenuation_.CorrectionTable import CorrectionTable
			self._correctionTable = CorrectionTable(self._core, self._base)
		return self._correctionTable

	def clone(self) -> 'Attenuation':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Attenuation(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
