from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 11 total commands, 3 Sub-groups, 5 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_frequency'):
			from .ListPy_.Frequency import Frequency
			self._frequency = Frequency(self._core, self._base)
		return self._frequency

	@property
	def envelopePower(self):
		"""envelopePower commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_envelopePower'):
			from .ListPy_.EnvelopePower import EnvelopePower
			self._envelopePower = EnvelopePower(self._core, self._base)
		return self._envelopePower

	@property
	def retrigger(self):
		"""retrigger commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_retrigger'):
			from .ListPy_.Retrigger import Retrigger
			self._retrigger = Retrigger(self._core, self._base)
		return self._retrigger

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.listPy.get_start() \n
		Selects the first subsweep to be measured. The <StartIndex> must not be greater than the <StopIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:return: start_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_start(start_index = 1) \n
		Selects the first subsweep to be measured. The <StartIndex> must not be greater than the <StopIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:param start_index: No help available
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.listPy.get_stop() \n
		Selects the last subsweep to be measured. The <StopIndex> must not be smaller than the <StartIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:return: stop_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_stop(stop_index = 1) \n
		Selects the last subsweep to be measured. The <StopIndex> must not be smaller than the <StartIndex>. The total number of
		steps must not exceed 3000 (step count times number of subsweeps) . \n
			:param stop_index: No help available
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:STOP {param}')

	# noinspection PyTypeChecker
	class SstopStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Start_Index: int: No parameter help available
			- Stop_Index: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_int('Start_Index'),
			ArgStruct.scalar_int('Stop_Index')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: int = None
			self.Stop_Index: int = None

	def get_sstop(self) -> SstopStruct:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop \n
		Snippet: value: SstopStruct = driver.configure.gprf.measurement.iqVsSlot.listPy.get_sstop() \n
		Selects the range of subsweeps to be measured (first and last subsweep of a sweep) . The total number of steps must not
		exceed 3000 (step count times number of subsweeps) . \n
			:return: structure: for return value, see the help for SstopStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop?', self.__class__.SstopStruct())

	def set_sstop(self, value: SstopStruct) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_sstop(value = SstopStruct()) \n
		Selects the range of subsweeps to be measured (first and last subsweep of a sweep) . The total number of steps must not
		exceed 3000 (step count times number of subsweeps) . \n
			:param value: see the help for SstopStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:SSTop', value)

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:COUNt \n
		Snippet: value: int = driver.configure.gprf.measurement.iqVsSlot.listPy.get_count() \n
		Queries the number of subsweeps per sweep. The total number of steps must not exceed 3000 (step count times number of
		subsweeps) . \n
			:return: sweep_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST \n
		Snippet: value: bool = driver.configure.gprf.measurement.iqVsSlot.listPy.get_value() \n
		Enables or disables the list mode for the I/Q vs slot measurement. \n
			:return: list_mode: OFF: list mode off ON: list mode on
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST \n
		Snippet: driver.configure.gprf.measurement.iqVsSlot.listPy.set_value(list_mode = False) \n
		Enables or disables the list mode for the I/Q vs slot measurement. \n
			:param list_mode: OFF: list mode off ON: list mode on
		"""
		param = Conversions.bool_to_str(list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:IQVSlot:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
