from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MultiEval:
	"""MultiEval commands group definition. 519 total commands, 16 Sub-groups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("multiEval", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .MultiEval_.State import State
			self._state = State(self._core, self._base)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .MultiEval_.Trace import Trace
			self._trace = Trace(self._core, self._base)
		return self._trace

	@property
	def vfThroughput(self):
		"""vfThroughput commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vfThroughput'):
			from .MultiEval_.VfThroughput import VfThroughput
			self._vfThroughput = VfThroughput(self._core, self._base)
		return self._vfThroughput

	@property
	def evMagnitude(self):
		"""evMagnitude commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evMagnitude'):
			from .MultiEval_.EvMagnitude import EvMagnitude
			self._evMagnitude = EvMagnitude(self._core, self._base)
		return self._evMagnitude

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .MultiEval_.Merror import Merror
			self._merror = Merror(self._core, self._base)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .MultiEval_.Perror import Perror
			self._perror = Perror(self._core, self._base)
		return self._perror

	@property
	def inbandEmission(self):
		"""inbandEmission commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_inbandEmission'):
			from .MultiEval_.InbandEmission import InbandEmission
			self._inbandEmission = InbandEmission(self._core, self._base)
		return self._inbandEmission

	@property
	def esFlatness(self):
		"""esFlatness commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_esFlatness'):
			from .MultiEval_.EsFlatness import EsFlatness
			self._esFlatness = EsFlatness(self._core, self._base)
		return self._esFlatness

	@property
	def evmc(self):
		"""evmc commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_evmc'):
			from .MultiEval_.Evmc import Evmc
			self._evmc = Evmc(self._core, self._base)
		return self._evmc

	@property
	def modulation(self):
		"""modulation commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_modulation'):
			from .MultiEval_.Modulation import Modulation
			self._modulation = Modulation(self._core, self._base)
		return self._modulation

	@property
	def seMask(self):
		"""seMask commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_seMask'):
			from .MultiEval_.SeMask import SeMask
			self._seMask = SeMask(self._core, self._base)
		return self._seMask

	@property
	def aclr(self):
		"""aclr commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .MultiEval_.Aclr import Aclr
			self._aclr = Aclr(self._core, self._base)
		return self._aclr

	@property
	def pdynamics(self):
		"""pdynamics commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdynamics'):
			from .MultiEval_.Pdynamics import Pdynamics
			self._pdynamics = Pdynamics(self._core, self._base)
		return self._pdynamics

	@property
	def pmonitor(self):
		"""pmonitor commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmonitor'):
			from .MultiEval_.Pmonitor import Pmonitor
			self._pmonitor = Pmonitor(self._core, self._base)
		return self._pmonitor

	@property
	def bler(self):
		"""bler commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_bler'):
			from .MultiEval_.Bler import Bler
			self._bler = Bler(self._core, self._base)
		return self._bler

	@property
	def listPy(self):
		"""listPy commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .MultiEval_.ListPy import ListPy
			self._listPy = ListPy(self._core, self._base)
		return self._listPy

	def initiate(self) -> None:
		"""SCPI: INITiate:LTE:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.initiate() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'INITiate:LTE:MEASurement<Instance>:MEValuation')

	def initiate_with_opc(self) -> None:
		"""SCPI: INITiate:LTE:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.initiate_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as initiate, but waits for the operation to complete before continuing further. Use the RsCmwLteMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'INITiate:LTE:MEASurement<Instance>:MEValuation')

	def stop(self) -> None:
		"""SCPI: STOP:LTE:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.stop() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'STOP:LTE:MEASurement<Instance>:MEValuation')

	def stop_with_opc(self) -> None:
		"""SCPI: STOP:LTE:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.stop_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as stop, but waits for the operation to complete before continuing further. Use the RsCmwLteMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'STOP:LTE:MEASurement<Instance>:MEValuation')

	def abort(self) -> None:
		"""SCPI: ABORt:LTE:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.abort() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		"""
		self._core.io.write(f'ABORt:LTE:MEASurement<Instance>:MEValuation')

	def abort_with_opc(self) -> None:
		"""SCPI: ABORt:LTE:MEASurement<Instance>:MEValuation \n
		Snippet: driver.multiEval.abort_with_opc() \n
			INTRO_CMD_HELP: Starts, stops, or aborts the measurement: \n
			- INITiate... starts or restarts the measurement. The measurement enters the 'RUN' state.
			- STOP... halts the measurement immediately. The measurement enters the 'RDY' state. Measurement results are kept. The resources remain allocated to the measurement.
			- ABORt... halts the measurement immediately. The measurement enters the 'OFF' state. All measurement values are set to NAV. Allocated resources are released.
		Use FETCh...STATe? to query the current measurement state. \n
		Same as abort, but waits for the operation to complete before continuing further. Use the RsCmwLteMeas.utilities.opc_timeout_set() to set the timeout value. \n
		"""
		self._core.io.write_with_opc(f'ABORt:LTE:MEASurement<Instance>:MEValuation')

	def clone(self) -> 'MultiEval':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MultiEval(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
