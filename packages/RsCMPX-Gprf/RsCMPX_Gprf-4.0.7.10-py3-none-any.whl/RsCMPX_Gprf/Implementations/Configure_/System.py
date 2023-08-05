from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 2 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("system", core, parent)

	@property
	def attenuation(self):
		"""attenuation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_attenuation'):
			from .System_.Attenuation import Attenuation
			self._attenuation = Attenuation(self._core, self._base)
		return self._attenuation

	# noinspection PyTypeChecker
	class EdeviceStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Device_Type: enums.DeviceType: No parameter help available
			- Device_Mode: enums.DeviceMode: No parameter help available"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Device_Type', enums.DeviceType),
			ArgStruct.scalar_enum('Device_Mode', enums.DeviceMode)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Device_Type: enums.DeviceType = None
			self.Device_Mode: enums.DeviceMode = None

	# noinspection PyTypeChecker
	def get_edevice(self) -> EdeviceStruct:
		"""SCPI: [CONFigure]:SYSTem:EDEVice \n
		Snippet: value: EdeviceStruct = driver.configure.system.get_edevice() \n
		No command help available \n
			:return: structure: for return value, see the help for EdeviceStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:SYSTem:EDEVice?', self.__class__.EdeviceStruct())

	def set_edevice(self, value: EdeviceStruct) -> None:
		"""SCPI: [CONFigure]:SYSTem:EDEVice \n
		Snippet: driver.configure.system.set_edevice(value = EdeviceStruct()) \n
		No command help available \n
			:param value: see the help for EdeviceStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:SYSTem:EDEVice', value)

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
