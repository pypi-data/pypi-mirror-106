from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gprf:
	"""Gprf commands group definition. 15 total commands, 2 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gprf", core, parent)

	@property
	def measurement(self):
		"""measurement commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_measurement'):
			from .Gprf_.Measurement import Measurement
			self._measurement = Measurement(self._core, self._base)
		return self._measurement

	@property
	def generator(self):
		"""generator commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_generator'):
			from .Gprf_.Generator import Generator
			self._generator = Generator(self._core, self._base)
		return self._generator

	def clone(self) -> 'Gprf':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gprf(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
