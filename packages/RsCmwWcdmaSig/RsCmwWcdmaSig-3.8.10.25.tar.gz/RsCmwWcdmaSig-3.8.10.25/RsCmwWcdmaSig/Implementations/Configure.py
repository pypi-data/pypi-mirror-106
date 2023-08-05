from ..Internal.Core import Core
from ..Internal.CommandsGroup import CommandsGroup
from ..Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 464 total commands, 24 Sub-groups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("configure", core, parent)

	@property
	def psettings(self):
		"""psettings commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_psettings'):
			from .Configure_.Psettings import Psettings
			self._psettings = Psettings(self._core, self._base)
		return self._psettings

	@property
	def mmonitor(self):
		"""mmonitor commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mmonitor'):
			from .Configure_.Mmonitor import Mmonitor
			self._mmonitor = Mmonitor(self._core, self._base)
		return self._mmonitor

	@property
	def ueReport(self):
		"""ueReport commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_ueReport'):
			from .Configure_.UeReport import UeReport
			self._ueReport = UeReport(self._core, self._base)
		return self._ueReport

	@property
	def cmode(self):
		"""cmode commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmode'):
			from .Configure_.Cmode import Cmode
			self._cmode = Cmode(self._core, self._base)
		return self._cmode

	@property
	def rfSettings(self):
		"""rfSettings commands group. 5 Sub-classes, 4 commands."""
		if not hasattr(self, '_rfSettings'):
			from .Configure_.RfSettings import RfSettings
			self._rfSettings = RfSettings(self._core, self._base)
		return self._rfSettings

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrier'):
			from .Configure_.Carrier import Carrier
			self._carrier = Carrier(self._core, self._base)
		return self._carrier

	@property
	def iqIn(self):
		"""iqIn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqIn'):
			from .Configure_.IqIn import IqIn
			self._iqIn = IqIn(self._core, self._base)
		return self._iqIn

	@property
	def downlink(self):
		"""downlink commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_downlink'):
			from .Configure_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def uplink(self):
		"""uplink commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_uplink'):
			from .Configure_.Uplink import Uplink
			self._uplink = Uplink(self._core, self._base)
		return self._uplink

	@property
	def connection(self):
		"""connection commands group. 6 Sub-classes, 3 commands."""
		if not hasattr(self, '_connection'):
			from .Configure_.Connection import Connection
			self._connection = Connection(self._core, self._base)
		return self._connection

	@property
	def ihMobility(self):
		"""ihMobility commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ihMobility'):
			from .Configure_.IhMobility import IhMobility
			self._ihMobility = IhMobility(self._core, self._base)
		return self._ihMobility

	@property
	def cell(self):
		"""cell commands group. 14 Sub-classes, 12 commands."""
		if not hasattr(self, '_cell'):
			from .Configure_.Cell import Cell
			self._cell = Cell(self._core, self._base)
		return self._cell

	@property
	def ncell(self):
		"""ncell commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ncell'):
			from .Configure_.Ncell import Ncell
			self._ncell = Ncell(self._core, self._base)
		return self._ncell

	@property
	def ber(self):
		"""ber commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_ber'):
			from .Configure_.Ber import Ber
			self._ber = Ber(self._core, self._base)
		return self._ber

	@property
	def throughput(self):
		"""throughput commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_throughput'):
			from .Configure_.Throughput import Throughput
			self._throughput = Throughput(self._core, self._base)
		return self._throughput

	@property
	def hack(self):
		"""hack commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_hack'):
			from .Configure_.Hack import Hack
			self._hack = Hack(self._core, self._base)
		return self._hack

	@property
	def hcqi(self):
		"""hcqi commands group. 3 Sub-classes, 2 commands."""
		if not hasattr(self, '_hcqi'):
			from .Configure_.Hcqi import Hcqi
			self._hcqi = Hcqi(self._core, self._base)
		return self._hcqi

	@property
	def uplinkLogging(self):
		"""uplinkLogging commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_uplinkLogging'):
			from .Configure_.UplinkLogging import UplinkLogging
			self._uplinkLogging = UplinkLogging(self._core, self._base)
		return self._uplinkLogging

	@property
	def eagch(self):
		"""eagch commands group. 1 Sub-classes, 5 commands."""
		if not hasattr(self, '_eagch'):
			from .Configure_.Eagch import Eagch
			self._eagch = Eagch(self._core, self._base)
		return self._eagch

	@property
	def ehich(self):
		"""ehich commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_ehich'):
			from .Configure_.Ehich import Ehich
			self._ehich = Ehich(self._core, self._base)
		return self._ehich

	@property
	def ergch(self):
		"""ergch commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_ergch'):
			from .Configure_.Ergch import Ergch
			self._ergch = Ergch(self._core, self._base)
		return self._ergch

	@property
	def sms(self):
		"""sms commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_sms'):
			from .Configure_.Sms import Sms
			self._sms = Sms(self._core, self._base)
		return self._sms

	@property
	def cbs(self):
		"""cbs commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cbs'):
			from .Configure_.Cbs import Cbs
			self._cbs = Cbs(self._core, self._base)
		return self._cbs

	@property
	def fading(self):
		"""fading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fading'):
			from .Configure_.Fading import Fading
			self._fading = Fading(self._core, self._base)
		return self._fading

	def get_etoe(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ETOE \n
		Snippet: value: bool = driver.configure.get_etoe() \n
		Enables the setup of a connection between the signaling unit and the data application unit (DAU) . DAU is required for
		IP-based data tests. \n
			:return: end_to_end_enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ETOE?')
		return Conversions.str_to_bool(response)

	def set_etoe(self, end_to_end_enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ETOE \n
		Snippet: driver.configure.set_etoe(end_to_end_enable = False) \n
		Enables the setup of a connection between the signaling unit and the data application unit (DAU) . DAU is required for
		IP-based data tests. \n
			:param end_to_end_enable: OFF | ON
		"""
		param = Conversions.bool_to_str(end_to_end_enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ETOE {param}')

	def get_es_code(self) -> bool:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ESCode \n
		Snippet: value: bool = driver.configure.get_es_code() \n
		Enables audio tests involving the 'audio measurements' application in remote operation only. It can only be set in the
		signal OFF state. \n
			:return: enable: OFF | ON
		"""
		response = self._core.io.query_str('CONFigure:WCDMa:SIGNaling<Instance>:ESCode?')
		return Conversions.str_to_bool(response)

	def set_es_code(self, enable: bool) -> None:
		"""SCPI: CONFigure:WCDMa:SIGNaling<instance>:ESCode \n
		Snippet: driver.configure.set_es_code(enable = False) \n
		Enables audio tests involving the 'audio measurements' application in remote operation only. It can only be set in the
		signal OFF state. \n
			:param enable: OFF | ON
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'CONFigure:WCDMa:SIGNaling<Instance>:ESCode {param}')

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
