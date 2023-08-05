from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Diagnostic:
	"""Diagnostic commands group definition. 16 total commands, 5 Sub-groups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("diagnostic", core, parent)

	@property
	def gprf(self):
		"""gprf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gprf'):
			from .Diagnostic_.Gprf import Gprf
			self._gprf = Gprf(self._core, self._base)
		return self._gprf

	@property
	def generic(self):
		"""generic commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_generic'):
			from .Diagnostic_.Generic import Generic
			self._generic = Generic(self._core, self._base)
		return self._generic

	@property
	def meas(self):
		"""meas commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_meas'):
			from .Diagnostic_.Meas import Meas
			self._meas = Meas(self._core, self._base)
		return self._meas

	@property
	def route(self):
		"""route commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_route'):
			from .Diagnostic_.Route import Route
			self._route = Route(self._core, self._base)
		return self._route

	@property
	def catalog(self):
		"""catalog commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catalog'):
			from .Diagnostic_.Catalog import Catalog
			self._catalog = Catalog(self._core, self._base)
		return self._catalog

	def clone(self) -> 'Diagnostic':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Diagnostic(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
