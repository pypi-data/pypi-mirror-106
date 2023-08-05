from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ploss:
	"""Ploss commands group definition. 12 total commands, 5 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("ploss", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .Ploss_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def clear(self):
		"""clear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clear'):
			from .Ploss_.Clear import Clear
			self._clear = Clear(self._core, self._base)
		return self._clear

	@property
	def open(self):
		"""open commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_open'):
			from .Ploss_.Open import Open
			self._open = Open(self._core, self._base)
		return self._open

	@property
	def short(self):
		"""short commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_short'):
			from .Ploss_.Short import Short
			self._short = Short(self._core, self._base)
		return self._short

	@property
	def eval(self):
		"""eval commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_eval'):
			from .Ploss_.Eval import Eval
			self._eval = Eval(self._core, self._base)
		return self._eval

	def stop(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.gprf.measurement.ploss.stop() \n
		No command help available \n
		"""
		self._core.io.write(f'STOP:GPRF:MEASurement<Instance>:PLOSs')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.gprf.measurement.ploss.stop_with_opc() \n
		No command help available \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:GPRF:MEASurement<Instance>:PLOSs')

	def abort(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.gprf.measurement.ploss.abort() \n
		No command help available \n
		"""
		self._core.io.write(f'ABORt:GPRF:MEASurement<Instance>:PLOSs')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:GPRF:MEASurement<Instance>:PLOSs \n
		Snippet: driver.gprf.measurement.ploss.abort_with_opc() \n
		No command help available \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCMPX_Gprf.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:GPRF:MEASurement<Instance>:PLOSs')

	def clone(self) -> 'Ploss':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ploss(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
