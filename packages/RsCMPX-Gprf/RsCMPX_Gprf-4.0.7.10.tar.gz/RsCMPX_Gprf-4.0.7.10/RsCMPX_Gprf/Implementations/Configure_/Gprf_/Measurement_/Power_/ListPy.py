from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.StructBase import StructBase
from ......Internal.ArgStruct import ArgStruct
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ListPy:
	"""ListPy commands group definition. 21 total commands, 6 Sub-groups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("listPy", core, parent)

	@property
	def iqData(self):
		"""iqData commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_iqData'):
			from .ListPy_.IqData import IqData
			self._iqData = IqData(self._core, self._base)
		return self._iqData

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

	@property
	def irepetition(self):
		"""irepetition commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_irepetition'):
			from .ListPy_.Irepetition import Irepetition
			self._irepetition = Irepetition(self._core, self._base)
		return self._irepetition

	@property
	def parameterSetList(self):
		"""parameterSetList commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_parameterSetList'):
			from .ListPy_.ParameterSetList import ParameterSetList
			self._parameterSetList = ParameterSetList(self._core, self._base)
		return self._parameterSetList

	# noinspection PyTypeChecker
	def get_txi_timing(self) -> enums.Timing:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming \n
		Snippet: value: enums.Timing = driver.configure.gprf.measurement.power.listPy.get_txi_timing() \n
		Specifies the timing of the generated GPRF Meas<i>:Power trigger. \n
			:return: timing: STEP: Trigger signals are generated between step lengths. CENTered: Trigger signals are generated between measurement lengths.
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming?')
		return Conversions.str_to_scalar_enum(response, enums.Timing)

	def set_txi_timing(self, timing: enums.Timing) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_txi_timing(timing = enums.Timing.CENTered) \n
		Specifies the timing of the generated GPRF Meas<i>:Power trigger. \n
			:param timing: STEP: Trigger signals are generated between step lengths. CENTered: Trigger signals are generated between measurement lengths.
		"""
		param = Conversions.enum_scalar_to_str(timing, enums.Timing)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:TXITiming {param}')

	# noinspection PyTypeChecker
	class FillStruct(StructBase):
		"""Structure for setting input parameters. Contains optional set arguments. Fields: \n
			- Start_Index: float: No parameter help available
			- Range_Py: float: No parameter help available
			- Index_Repetition: float: No parameter help available
			- Start_Frequency: float: No parameter help available
			- Freq_Increment: float: No parameter help available
			- Start_Power: float: No parameter help available
			- Power_Increment: float: No parameter help available
			- Retrigger: bool: No parameter help available
			- Iq_Data: bool: No parameter help available
			- Parameter_Set: int: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_float('Start_Index'),
			ArgStruct.scalar_float('Range_Py'),
			ArgStruct.scalar_float('Index_Repetition'),
			ArgStruct.scalar_float('Start_Frequency'),
			ArgStruct.scalar_float('Freq_Increment'),
			ArgStruct.scalar_float('Start_Power'),
			ArgStruct.scalar_float('Power_Increment'),
			ArgStruct.scalar_bool_optional('Retrigger'),
			ArgStruct.scalar_bool_optional('Iq_Data'),
			ArgStruct.scalar_int_optional('Parameter_Set')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Start_Index: float = None
			self.Range_Py: float = None
			self.Index_Repetition: float = None
			self.Start_Frequency: float = None
			self.Freq_Increment: float = None
			self.Start_Power: float = None
			self.Power_Increment: float = None
			self.Retrigger: bool = None
			self.Iq_Data: bool = None
			self.Parameter_Set: int = None

	def set_fill(self, value: FillStruct) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FILL \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_fill(value = FillStruct()) \n
		No command help available \n
			:param value: see the help for FillStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:FILL', value)

	# noinspection PyTypeChecker
	def get_munit(self) -> enums.MagnitudeUnit:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit \n
		Snippet: value: enums.MagnitudeUnit = driver.configure.gprf.measurement.power.listPy.get_munit() \n
		No command help available \n
			:return: magnitude_unit: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit?')
		return Conversions.str_to_scalar_enum(response, enums.MagnitudeUnit)

	def set_munit(self, magnitude_unit: enums.MagnitudeUnit) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_munit(magnitude_unit = enums.MagnitudeUnit.RAW) \n
		No command help available \n
			:param magnitude_unit: No help available
		"""
		param = Conversions.enum_scalar_to_str(magnitude_unit, enums.MagnitudeUnit)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:MUNit {param}')

	def get_count(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:COUNt \n
		Snippet: value: int = driver.configure.gprf.measurement.power.listPy.get_count() \n
		Queries the total number of segments per sweep, including repetitions. \n
			:return: result_count: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:COUNt?')
		return Conversions.str_to_int(response)

	def get_start(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt \n
		Snippet: value: int = driver.configure.gprf.measurement.power.listPy.get_start() \n
		Selects the first segment to be measured (start of a sweep) . The total number of segments per sweep, including
		repetitions, must not be higher than 10000. \n
			:return: start_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt?')
		return Conversions.str_to_int(response)

	def set_start(self, start_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_start(start_index = 1) \n
		Selects the first segment to be measured (start of a sweep) . The total number of segments per sweep, including
		repetitions, must not be higher than 10000. \n
			:param start_index: No help available
		"""
		param = Conversions.decimal_value_to_str(start_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STARt {param}')

	def get_stop(self) -> int:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP \n
		Snippet: value: int = driver.configure.gprf.measurement.power.listPy.get_stop() \n
		Selects the last segment to be measured (end of a sweep) . The total number of segments per sweep, including repetitions,
		must not be higher than 10000. \n
			:return: stop_index: No help available
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP?')
		return Conversions.str_to_int(response)

	def set_stop(self, stop_index: int) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_stop(stop_index = 1) \n
		Selects the last segment to be measured (end of a sweep) . The total number of segments per sweep, including repetitions,
		must not be higher than 10000. \n
			:param stop_index: No help available
		"""
		param = Conversions.decimal_value_to_str(stop_index)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:STOP {param}')

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
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop \n
		Snippet: value: SstopStruct = driver.configure.gprf.measurement.power.listPy.get_sstop() \n
		Selects the range of segments to be measured (first and last segment of a sweep) . The total number of segments per sweep,
		including repetitions, must not be higher than 10000. \n
			:return: structure: for return value, see the help for SstopStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop?', self.__class__.SstopStruct())

	def set_sstop(self, value: SstopStruct) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_sstop(value = SstopStruct()) \n
		Selects the range of segments to be measured (first and last segment of a sweep) . The total number of segments per sweep,
		including repetitions, must not be higher than 10000. \n
			:param value: see the help for SstopStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST:SSTop', value)

	def get_value(self) -> bool:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST \n
		Snippet: value: bool = driver.configure.gprf.measurement.power.listPy.get_value() \n
		Enables or disables the list mode for the power measurement. \n
			:return: enable_list_mode: OFF: list mode off ON: list mode on
		"""
		response = self._core.io.query_str('CONFigure:GPRF:MEASurement<Instance>:POWer:LIST?')
		return Conversions.str_to_bool(response)

	def set_value(self, enable_list_mode: bool) -> None:
		"""SCPI: CONFigure:GPRF:MEASurement<Instance>:POWer:LIST \n
		Snippet: driver.configure.gprf.measurement.power.listPy.set_value(enable_list_mode = False) \n
		Enables or disables the list mode for the power measurement. \n
			:param enable_list_mode: OFF: list mode off ON: list mode on
		"""
		param = Conversions.bool_to_str(enable_list_mode)
		self._core.io.write(f'CONFigure:GPRF:MEASurement<Instance>:POWer:LIST {param}')

	def clone(self) -> 'ListPy':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ListPy(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
