from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gvector:
	"""Gvector commands group definition. 131 total commands, 66 Sub-groups, 1 group commands
	Repeated Capability: GainVector, default value after init: GainVector.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("gvector", core, parent)
		self._base.rep_cap = RepeatedCapability(self._base.group_name, 'repcap_gainVector_get', 'repcap_gainVector_set', repcap.GainVector.Nr1)

	def repcap_gainVector_set(self, enum_value: repcap.GainVector) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GainVector.Default
		Default value after init: GainVector.Nr1"""
		self._base.set_repcap_enum_value(enum_value)

	def repcap_gainVector_get(self) -> repcap.GainVector:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._base.get_repcap_enum_value()

	@property
	def aa(self):
		"""aa commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_aa'):
			from .Gvector_.Aa import Aa
			self._aa = Aa(self._core, self._base)
		return self._aa

	@property
	def ab(self):
		"""ab commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ab'):
			from .Gvector_.Ab import Ab
			self._ab = Ab(self._core, self._base)
		return self._ab

	@property
	def ac(self):
		"""ac commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ac'):
			from .Gvector_.Ac import Ac
			self._ac = Ac(self._core, self._base)
		return self._ac

	@property
	def ad(self):
		"""ad commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ad'):
			from .Gvector_.Ad import Ad
			self._ad = Ad(self._core, self._base)
		return self._ad

	@property
	def ae(self):
		"""ae commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ae'):
			from .Gvector_.Ae import Ae
			self._ae = Ae(self._core, self._base)
		return self._ae

	@property
	def af(self):
		"""af commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_af'):
			from .Gvector_.Af import Af
			self._af = Af(self._core, self._base)
		return self._af

	@property
	def ag(self):
		"""ag commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ag'):
			from .Gvector_.Ag import Ag
			self._ag = Ag(self._core, self._base)
		return self._ag

	@property
	def ah(self):
		"""ah commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ah'):
			from .Gvector_.Ah import Ah
			self._ah = Ah(self._core, self._base)
		return self._ah

	@property
	def ba(self):
		"""ba commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ba'):
			from .Gvector_.Ba import Ba
			self._ba = Ba(self._core, self._base)
		return self._ba

	@property
	def bb(self):
		"""bb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bb'):
			from .Gvector_.Bb import Bb
			self._bb = Bb(self._core, self._base)
		return self._bb

	@property
	def bc(self):
		"""bc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bc'):
			from .Gvector_.Bc import Bc
			self._bc = Bc(self._core, self._base)
		return self._bc

	@property
	def bd(self):
		"""bd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bd'):
			from .Gvector_.Bd import Bd
			self._bd = Bd(self._core, self._base)
		return self._bd

	@property
	def be(self):
		"""be commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_be'):
			from .Gvector_.Be import Be
			self._be = Be(self._core, self._base)
		return self._be

	@property
	def bf(self):
		"""bf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bf'):
			from .Gvector_.Bf import Bf
			self._bf = Bf(self._core, self._base)
		return self._bf

	@property
	def bg(self):
		"""bg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bg'):
			from .Gvector_.Bg import Bg
			self._bg = Bg(self._core, self._base)
		return self._bg

	@property
	def bh(self):
		"""bh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bh'):
			from .Gvector_.Bh import Bh
			self._bh = Bh(self._core, self._base)
		return self._bh

	@property
	def ca(self):
		"""ca commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ca'):
			from .Gvector_.Ca import Ca
			self._ca = Ca(self._core, self._base)
		return self._ca

	@property
	def cb(self):
		"""cb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cb'):
			from .Gvector_.Cb import Cb
			self._cb = Cb(self._core, self._base)
		return self._cb

	@property
	def cc(self):
		"""cc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Gvector_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def cd(self):
		"""cd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cd'):
			from .Gvector_.Cd import Cd
			self._cd = Cd(self._core, self._base)
		return self._cd

	@property
	def ce(self):
		"""ce commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ce'):
			from .Gvector_.Ce import Ce
			self._ce = Ce(self._core, self._base)
		return self._ce

	@property
	def cf(self):
		"""cf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cf'):
			from .Gvector_.Cf import Cf
			self._cf = Cf(self._core, self._base)
		return self._cf

	@property
	def cg(self):
		"""cg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cg'):
			from .Gvector_.Cg import Cg
			self._cg = Cg(self._core, self._base)
		return self._cg

	@property
	def ch(self):
		"""ch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ch'):
			from .Gvector_.Ch import Ch
			self._ch = Ch(self._core, self._base)
		return self._ch

	@property
	def da(self):
		"""da commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_da'):
			from .Gvector_.Da import Da
			self._da = Da(self._core, self._base)
		return self._da

	@property
	def db(self):
		"""db commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_db'):
			from .Gvector_.Db import Db
			self._db = Db(self._core, self._base)
		return self._db

	@property
	def dc(self):
		"""dc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dc'):
			from .Gvector_.Dc import Dc
			self._dc = Dc(self._core, self._base)
		return self._dc

	@property
	def dd(self):
		"""dd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dd'):
			from .Gvector_.Dd import Dd
			self._dd = Dd(self._core, self._base)
		return self._dd

	@property
	def de(self):
		"""de commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_de'):
			from .Gvector_.De import De
			self._de = De(self._core, self._base)
		return self._de

	@property
	def df(self):
		"""df commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_df'):
			from .Gvector_.Df import Df
			self._df = Df(self._core, self._base)
		return self._df

	@property
	def dg(self):
		"""dg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dg'):
			from .Gvector_.Dg import Dg
			self._dg = Dg(self._core, self._base)
		return self._dg

	@property
	def dh(self):
		"""dh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dh'):
			from .Gvector_.Dh import Dh
			self._dh = Dh(self._core, self._base)
		return self._dh

	@property
	def ea(self):
		"""ea commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ea'):
			from .Gvector_.Ea import Ea
			self._ea = Ea(self._core, self._base)
		return self._ea

	@property
	def eb(self):
		"""eb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eb'):
			from .Gvector_.Eb import Eb
			self._eb = Eb(self._core, self._base)
		return self._eb

	@property
	def ec(self):
		"""ec commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ec'):
			from .Gvector_.Ec import Ec
			self._ec = Ec(self._core, self._base)
		return self._ec

	@property
	def ed(self):
		"""ed commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ed'):
			from .Gvector_.Ed import Ed
			self._ed = Ed(self._core, self._base)
		return self._ed

	@property
	def ee(self):
		"""ee commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ee'):
			from .Gvector_.Ee import Ee
			self._ee = Ee(self._core, self._base)
		return self._ee

	@property
	def ef(self):
		"""ef commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ef'):
			from .Gvector_.Ef import Ef
			self._ef = Ef(self._core, self._base)
		return self._ef

	@property
	def eg(self):
		"""eg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eg'):
			from .Gvector_.Eg import Eg
			self._eg = Eg(self._core, self._base)
		return self._eg

	@property
	def eh(self):
		"""eh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_eh'):
			from .Gvector_.Eh import Eh
			self._eh = Eh(self._core, self._base)
		return self._eh

	@property
	def fa(self):
		"""fa commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fa'):
			from .Gvector_.Fa import Fa
			self._fa = Fa(self._core, self._base)
		return self._fa

	@property
	def fb(self):
		"""fb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fb'):
			from .Gvector_.Fb import Fb
			self._fb = Fb(self._core, self._base)
		return self._fb

	@property
	def fc(self):
		"""fc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fc'):
			from .Gvector_.Fc import Fc
			self._fc = Fc(self._core, self._base)
		return self._fc

	@property
	def fd(self):
		"""fd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fd'):
			from .Gvector_.Fd import Fd
			self._fd = Fd(self._core, self._base)
		return self._fd

	@property
	def fe(self):
		"""fe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fe'):
			from .Gvector_.Fe import Fe
			self._fe = Fe(self._core, self._base)
		return self._fe

	@property
	def ff(self):
		"""ff commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ff'):
			from .Gvector_.Ff import Ff
			self._ff = Ff(self._core, self._base)
		return self._ff

	@property
	def fg(self):
		"""fg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fg'):
			from .Gvector_.Fg import Fg
			self._fg = Fg(self._core, self._base)
		return self._fg

	@property
	def fh(self):
		"""fh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_fh'):
			from .Gvector_.Fh import Fh
			self._fh = Fh(self._core, self._base)
		return self._fh

	@property
	def ga(self):
		"""ga commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ga'):
			from .Gvector_.Ga import Ga
			self._ga = Ga(self._core, self._base)
		return self._ga

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gain'):
			from .Gvector_.Gain import Gain
			self._gain = Gain(self._core, self._base)
		return self._gain

	@property
	def gb(self):
		"""gb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gb'):
			from .Gvector_.Gb import Gb
			self._gb = Gb(self._core, self._base)
		return self._gb

	@property
	def gc(self):
		"""gc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gc'):
			from .Gvector_.Gc import Gc
			self._gc = Gc(self._core, self._base)
		return self._gc

	@property
	def gd(self):
		"""gd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gd'):
			from .Gvector_.Gd import Gd
			self._gd = Gd(self._core, self._base)
		return self._gd

	@property
	def ge(self):
		"""ge commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ge'):
			from .Gvector_.Ge import Ge
			self._ge = Ge(self._core, self._base)
		return self._ge

	@property
	def gf(self):
		"""gf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gf'):
			from .Gvector_.Gf import Gf
			self._gf = Gf(self._core, self._base)
		return self._gf

	@property
	def gg(self):
		"""gg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gg'):
			from .Gvector_.Gg import Gg
			self._gg = Gg(self._core, self._base)
		return self._gg

	@property
	def gh(self):
		"""gh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gh'):
			from .Gvector_.Gh import Gh
			self._gh = Gh(self._core, self._base)
		return self._gh

	@property
	def ha(self):
		"""ha commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ha'):
			from .Gvector_.Ha import Ha
			self._ha = Ha(self._core, self._base)
		return self._ha

	@property
	def hb(self):
		"""hb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hb'):
			from .Gvector_.Hb import Hb
			self._hb = Hb(self._core, self._base)
		return self._hb

	@property
	def hc(self):
		"""hc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hc'):
			from .Gvector_.Hc import Hc
			self._hc = Hc(self._core, self._base)
		return self._hc

	@property
	def hd(self):
		"""hd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hd'):
			from .Gvector_.Hd import Hd
			self._hd = Hd(self._core, self._base)
		return self._hd

	@property
	def he(self):
		"""he commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_he'):
			from .Gvector_.He import He
			self._he = He(self._core, self._base)
		return self._he

	@property
	def hf(self):
		"""hf commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hf'):
			from .Gvector_.Hf import Hf
			self._hf = Hf(self._core, self._base)
		return self._hf

	@property
	def hg(self):
		"""hg commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hg'):
			from .Gvector_.Hg import Hg
			self._hg = Hg(self._core, self._base)
		return self._hg

	@property
	def hh(self):
		"""hh commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hh'):
			from .Gvector_.Hh import Hh
			self._hh = Hh(self._core, self._base)
		return self._hh

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Gvector_.Phase import Phase
			self._phase = Phase(self._core, self._base)
		return self._phase

	def preset(self, mimoTap=repcap.MimoTap.Default) -> None:
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:GVECtor:PRESet \n
		Snippet: driver.source.fsimulator.mimo.tap.gvector.preset(mimoTap = repcap.MimoTap.Default) \n
		The command presets the vector matrix to an unitary matrix. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')"""
		mimoTap_cmd_val = self._base.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		self._core.io.write(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:GVECtor:PRESet')

	def preset_with_opc(self, mimoTap=repcap.MimoTap.Default) -> None:
		mimoTap_cmd_val = self._base.get_repcap_cmd_value(mimoTap, repcap.MimoTap)
		"""SCPI: [SOURce<HW>]:FSIMulator:MIMO:TAP<CH>:GVECtor:PRESet \n
		Snippet: driver.source.fsimulator.mimo.tap.gvector.preset_with_opc(mimoTap = repcap.MimoTap.Default) \n
		The command presets the vector matrix to an unitary matrix. \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsSmw.utilities.opc_timeout_set() to set the timeout value. \n
			:param mimoTap: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tap')"""
		self._core.io.write_with_opc(f'SOURce<HwInstance>:FSIMulator:MIMO:TAP{mimoTap_cmd_val}:GVECtor:PRESet')

	def clone(self) -> 'Gvector':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gvector(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
