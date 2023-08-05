from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Route:
	"""Route commands group definition. 5 total commands, 4 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("route", core, parent)

	@property
	def gprf(self):
		"""gprf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Route_.Gprf import Gprf
			self._gprf = Gprf(self._core, self._base)
		return self._gprf

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Route_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	@property
	def nrMmw(self):
		"""nrMmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrMmw'):
			from .Route_.NrMmw import NrMmw
			self._nrMmw = NrMmw(self._core, self._base)
		return self._nrMmw

	@property
	def uwb(self):
		"""uwb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uwb'):
			from .Route_.Uwb import Uwb
			self._uwb = Uwb(self._core, self._base)
		return self._uwb

	def clone(self) -> 'Route':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Route(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
