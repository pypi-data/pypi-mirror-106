from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 12 total commands, 0 Sub-groups, 12 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("result", core, parent)

	# noinspection PyTypeChecker
	class AllStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Evm: bool: OFF | ON Error vector magnitude ON: Evaluate results and show the view OFF: Do not evaluate results, hide the view
			- Magnitude_Error: bool: OFF | ON Magnitude error
			- Phase_Error: bool: OFF | ON Phase error
			- Acp: bool: OFF | ON Adjacent channel power
			- Cdp: bool: OFF | ON Code domain power
			- Cde: bool: OFF | ON Code domain error
			- Power: bool: OFF | ON Power
			- Tx_Measurements: bool: OFF | ON TX measurement
			- Channel_Power: bool: OFF | ON Channel power
			- Obw: bool: OFF | ON Occupied bandwidth
			- Iq: bool: OFF | ON IQ"""
		__meta_args_list = [
			ArgStruct.scalar_bool('Evm'),
			ArgStruct.scalar_bool('Magnitude_Error'),
			ArgStruct.scalar_bool('Phase_Error'),
			ArgStruct.scalar_bool('Acp'),
			ArgStruct.scalar_bool('Cdp'),
			ArgStruct.scalar_bool('Cde'),
			ArgStruct.scalar_bool('Power'),
			ArgStruct.scalar_bool('Tx_Measurements'),
			ArgStruct.scalar_bool('Channel_Power'),
			ArgStruct.scalar_bool('Obw'),
			ArgStruct.scalar_bool('Iq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Evm: bool = None
			self.Magnitude_Error: bool = None
			self.Phase_Error: bool = None
			self.Acp: bool = None
			self.Cdp: bool = None
			self.Cde: bool = None
			self.Power: bool = None
			self.Tx_Measurements: bool = None
			self.Channel_Power: bool = None
			self.Obw: bool = None
			self.Iq: bool = None

	def get_all(self) -> AllStruct:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult[:ALL] \n
		Snippet: value: AllStruct = driver.configure.multiEval.result.get_all() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		This command combines all other CONFigure:EVDO:MEAS<i>:MEValuation:RESult... commands. \n
			:return: structure: for return value, see the help for AllStruct structure arguments.
		"""
		return self._core.io.query_struct('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:ALL?', self.__class__.AllStruct())

	def set_all(self, value: AllStruct) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult[:ALL] \n
		Snippet: driver.configure.multiEval.result.set_all(value = AllStruct()) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		This command combines all other CONFigure:EVDO:MEAS<i>:MEValuation:RESult... commands. \n
			:param value: see the help for AllStruct structure arguments.
		"""
		self._core.io.write_struct('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:ALL', value)

	def get_ev_magnitude(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: value: bool = driver.configure.multiEval.result.get_ev_magnitude() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:EVMagnitude?')
		return Conversions.str_to_bool(response)

	def set_ev_magnitude(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:EVMagnitude \n
		Snippet: driver.configure.multiEval.result.set_ev_magnitude(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:EVMagnitude {param}')

	def get_merror(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:MERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_merror() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:MERRor?')
		return Conversions.str_to_bool(response)

	def set_merror(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:MERRor \n
		Snippet: driver.configure.multiEval.result.set_merror(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:MERRor {param}')

	def get_perror(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:PERRor \n
		Snippet: value: bool = driver.configure.multiEval.result.get_perror() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:PERRor?')
		return Conversions.str_to_bool(response)

	def set_perror(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:PERRor \n
		Snippet: driver.configure.multiEval.result.set_perror(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:PERRor {param}')

	def get_cdp(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:CDP \n
		Snippet: value: bool = driver.configure.multiEval.result.get_cdp() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:CDP?')
		return Conversions.str_to_bool(response)

	def set_cdp(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:CDP \n
		Snippet: driver.configure.multiEval.result.set_cdp(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:CDP {param}')

	def get_cde(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:CDE \n
		Snippet: value: bool = driver.configure.multiEval.result.get_cde() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:CDE?')
		return Conversions.str_to_bool(response)

	def set_cde(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:CDE \n
		Snippet: driver.configure.multiEval.result.set_cde(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:CDE {param}')

	def get_acp(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:ACP \n
		Snippet: value: bool = driver.configure.multiEval.result.get_acp() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:ACP?')
		return Conversions.str_to_bool(response)

	def set_acp(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:ACP \n
		Snippet: driver.configure.multiEval.result.set_acp(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:ACP {param}')

	def get_power(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:POWer \n
		Snippet: value: bool = driver.configure.multiEval.result.get_power() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:POWer?')
		return Conversions.str_to_bool(response)

	def set_power(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:POWer \n
		Snippet: driver.configure.multiEval.result.set_power(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:POWer {param}')

	def get_txm(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:TXM \n
		Snippet: value: bool = driver.configure.multiEval.result.get_txm() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:TXM?')
		return Conversions.str_to_bool(response)

	def set_txm(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:TXM \n
		Snippet: driver.configure.multiEval.result.set_txm(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:TXM {param}')

	def get_cp(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:CP \n
		Snippet: value: bool = driver.configure.multiEval.result.get_cp() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:CP?')
		return Conversions.str_to_bool(response)

	def set_cp(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:CP \n
		Snippet: driver.configure.multiEval.result.set_cp(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:CP {param}')

	def get_obw(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:OBW \n
		Snippet: value: bool = driver.configure.multiEval.result.get_obw() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:OBW?')
		return Conversions.str_to_bool(response)

	def set_obw(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:OBW \n
		Snippet: driver.configure.multiEval.result.set_obw(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:OBW {param}')

	def get_iq(self) -> bool:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:IQ \n
		Snippet: value: bool = driver.configure.multiEval.result.get_iq() \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:return: enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		response = self._core.io.query_str('CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:IQ?')
		return Conversions.str_to_bool(response)

	def set_iq(self, enable: bool) -> None:
		"""SCPI: CONFigure:EVDO:MEASurement<instance>:MEValuation:RESult:IQ \n
		Snippet: driver.configure.multiEval.result.set_iq(enable = False) \n
		Enables or disables the evaluation of results and shows or hides the views in the multi-evaluation measurement.
		The mnemonic after 'RESult' denotes the view type: Error vector magnitude, magnitude error, phase error, adjacent channel
		power, occupied bandwidth, code domain power, code domain error, channel power, IQ, power and TX measurement. \n
			:param enable: OFF | ON ON: Evaluate results and show view OFF: Do not evaluate results, hide view
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:EVDO:MEASurement<Instance>:MEValuation:RESult:IQ {param}')
