from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal.StructBase import StructBase
from ..Internal.ArgStruct import ArgStruct
from .. import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Route:
	"""Route commands group definition. 6 total commands, 1 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("route", core, parent)

	@property
	def scenario(self):
		"""scenario commands group. 2 Sub-classes, 3 commands."""
		if not hasattr(self, '_scenario'):
			from .Route_.Scenario import Scenario
			self._scenario = Scenario(self._core, self._base)
		return self._scenario

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.TestScenarioB: SALone | CSPath SALone: Standalone (non-signaling) CSPath: Combined signal path
			- Controller: str: string Controlling application while scenario CSPath is active.
			- Rx_Connector: enums.RxConnector: RF connector for the input path
			- Rx_Converter: enums.RxConverter: RX module for the input path"""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.TestScenarioB),
			ArgStruct.scalar_str('Controller'),
			ArgStruct.scalar_enum('Rx_Connector', enums.RxConnector),
			ArgStruct.scalar_enum('Rx_Converter', enums.RxConverter)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.TestScenarioB = None
			self.Controller: str = None
			self.Rx_Connector: enums.RxConnector = None
			self.Rx_Converter: enums.RxConverter = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:EVDO:MEASurement<instance> \n
		Snippet: value: ValueStruct = driver.route.get_value() \n
		Returns the configured routing settings. For possible connector and converter values, see 'Values for RF Path Selection'. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:EVDO:MEASurement<Instance>?', self.__class__.ValueStruct())

	def clone(self) -> 'Route':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Route(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
