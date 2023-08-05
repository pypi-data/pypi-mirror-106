from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 9 total commands, 7 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("catalog", core, parent)

	@property
	def gprf(self):
		"""gprf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Catalog_.Gprf import Gprf
			self._gprf = Gprf(self._core, self._base)
		return self._gprf

	@property
	def lte(self):
		"""lte commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Catalog_.Lte import Lte
			self._lte = Lte(self._core, self._base)
		return self._lte

	@property
	def nrMmw(self):
		"""nrMmw commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrMmw'):
			from .Catalog_.NrMmw import NrMmw
			self._nrMmw = NrMmw(self._core, self._base)
		return self._nrMmw

	@property
	def nrSub(self):
		"""nrSub commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_nrSub'):
			from .Catalog_.NrSub import NrSub
			self._nrSub = NrSub(self._core, self._base)
		return self._nrSub

	@property
	def uwb(self):
		"""uwb commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_uwb'):
			from .Catalog_.Uwb import Uwb
			self._uwb = Uwb(self._core, self._base)
		return self._uwb

	@property
	def tenvironment(self):
		"""tenvironment commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tenvironment'):
			from .Catalog_.Tenvironment import Tenvironment
			self._tenvironment = Tenvironment(self._core, self._base)
		return self._tenvironment

	@property
	def system(self):
		"""system commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .Catalog_.System import System
			self._system = System(self._core, self._base)
		return self._system

	def clone(self) -> 'Catalog':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Catalog(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
