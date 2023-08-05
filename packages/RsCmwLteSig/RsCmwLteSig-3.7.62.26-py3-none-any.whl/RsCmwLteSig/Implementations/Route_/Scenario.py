from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.StructBase import StructBase
from ...Internal.ArgStruct import ArgStruct
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scenario:
	"""Scenario commands group definition. 112 total commands, 105 Sub-groups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._base = CommandsGroup("scenario", core, parent)

	@property
	def scell(self):
		"""scell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scell'):
			from .Scenario_.Scell import Scell
			self._scell = Scell(self._core, self._base)
		return self._scell

	@property
	def tro(self):
		"""tro commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tro'):
			from .Scenario_.Tro import Tro
			self._tro = Tro(self._core, self._base)
		return self._tro

	@property
	def ad(self):
		"""ad commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ad'):
			from .Scenario_.Ad import Ad
			self._ad = Ad(self._core, self._base)
		return self._ad

	@property
	def scFading(self):
		"""scFading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scFading'):
			from .Scenario_.ScFading import ScFading
			self._scFading = ScFading(self._core, self._base)
		return self._scFading

	@property
	def troFading(self):
		"""troFading commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_troFading'):
			from .Scenario_.TroFading import TroFading
			self._troFading = TroFading(self._core, self._base)
		return self._troFading

	@property
	def adf(self):
		"""adf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adf'):
			from .Scenario_.Adf import Adf
			self._adf = Adf(self._core, self._base)
		return self._adf

	@property
	def catRfOut(self):
		"""catRfOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catRfOut'):
			from .Scenario_.CatRfOut import CatRfOut
			self._catRfOut = CatRfOut(self._core, self._base)
		return self._catRfOut

	@property
	def cafrfOut(self):
		"""cafrfOut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cafrfOut'):
			from .Scenario_.CafrfOut import CafrfOut
			self._cafrfOut = CafrfOut(self._core, self._base)
		return self._cafrfOut

	@property
	def bf(self):
		"""bf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bf'):
			from .Scenario_.Bf import Bf
			self._bf = Bf(self._core, self._base)
		return self._bf

	@property
	def bfsm(self):
		"""bfsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bfsm'):
			from .Scenario_.Bfsm import Bfsm
			self._bfsm = Bfsm(self._core, self._base)
		return self._bfsm

	@property
	def bh(self):
		"""bh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bh'):
			from .Scenario_.Bh import Bh
			self._bh = Bh(self._core, self._base)
		return self._bh

	@property
	def catf(self):
		"""catf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_catf'):
			from .Scenario_.Catf import Catf
			self._catf = Catf(self._core, self._base)
		return self._catf

	@property
	def caff(self):
		"""caff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caff'):
			from .Scenario_.Caff import Caff
			self._caff = Caff(self._core, self._base)
		return self._caff

	@property
	def bff(self):
		"""bff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bff'):
			from .Scenario_.Bff import Bff
			self._bff = Bff(self._core, self._base)
		return self._bff

	@property
	def bhf(self):
		"""bhf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bhf'):
			from .Scenario_.Bhf import Bhf
			self._bhf = Bhf(self._core, self._base)
		return self._bhf

	@property
	def cc(self):
		"""cc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cc'):
			from .Scenario_.Cc import Cc
			self._cc = Cc(self._core, self._base)
		return self._cc

	@property
	def ccmp(self):
		"""ccmp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccmp'):
			from .Scenario_.Ccmp import Ccmp
			self._ccmp = Ccmp(self._core, self._base)
		return self._ccmp

	@property
	def ccms(self):
		"""ccms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccms'):
			from .Scenario_.Ccms import Ccms
			self._ccms = Ccms(self._core, self._base)
		return self._ccms

	@property
	def cf(self):
		"""cf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cf'):
			from .Scenario_.Cf import Cf
			self._cf = Cf(self._core, self._base)
		return self._cf

	@property
	def ch(self):
		"""ch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ch'):
			from .Scenario_.Ch import Ch
			self._ch = Ch(self._core, self._base)
		return self._ch

	@property
	def chsm(self):
		"""chsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chsm'):
			from .Scenario_.Chsm import Chsm
			self._chsm = Chsm(self._core, self._base)
		return self._chsm

	@property
	def cj(self):
		"""cj commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cj'):
			from .Scenario_.Cj import Cj
			self._cj = Cj(self._core, self._base)
		return self._cj

	@property
	def cjsm(self):
		"""cjsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cjsm'):
			from .Scenario_.Cjsm import Cjsm
			self._cjsm = Cjsm(self._core, self._base)
		return self._cjsm

	@property
	def cl(self):
		"""cl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cl'):
			from .Scenario_.Cl import Cl
			self._cl = Cl(self._core, self._base)
		return self._cl

	@property
	def cff(self):
		"""cff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cff'):
			from .Scenario_.Cff import Cff
			self._cff = Cff(self._core, self._base)
		return self._cff

	@property
	def chf(self):
		"""chf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_chf'):
			from .Scenario_.Chf import Chf
			self._chf = Chf(self._core, self._base)
		return self._chf

	@property
	def cjf(self):
		"""cjf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cjf'):
			from .Scenario_.Cjf import Cjf
			self._cjf = Cjf(self._core, self._base)
		return self._cjf

	@property
	def cjfs(self):
		"""cjfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_cjfs'):
			from .Scenario_.Cjfs import Cjfs
			self._cjfs = Cjfs(self._core, self._base)
		return self._cjfs

	@property
	def dd(self):
		"""dd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dd'):
			from .Scenario_.Dd import Dd
			self._dd = Dd(self._core, self._base)
		return self._dd

	@property
	def dh(self):
		"""dh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dh'):
			from .Scenario_.Dh import Dh
			self._dh = Dh(self._core, self._base)
		return self._dh

	@property
	def dj(self):
		"""dj commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dj'):
			from .Scenario_.Dj import Dj
			self._dj = Dj(self._core, self._base)
		return self._dj

	@property
	def djsm(self):
		"""djsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_djsm'):
			from .Scenario_.Djsm import Djsm
			self._djsm = Djsm(self._core, self._base)
		return self._djsm

	@property
	def downlink(self):
		"""downlink commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_downlink'):
			from .Scenario_.Downlink import Downlink
			self._downlink = Downlink(self._core, self._base)
		return self._downlink

	@property
	def dlsm(self):
		"""dlsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dlsm'):
			from .Scenario_.Dlsm import Dlsm
			self._dlsm = Dlsm(self._core, self._base)
		return self._dlsm

	@property
	def dn(self):
		"""dn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dn'):
			from .Scenario_.Dn import Dn
			self._dn = Dn(self._core, self._base)
		return self._dn

	@property
	def dnsm(self):
		"""dnsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dnsm'):
			from .Scenario_.Dnsm import Dnsm
			self._dnsm = Dnsm(self._core, self._base)
		return self._dnsm

	@property
	def dp(self):
		"""dp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dp'):
			from .Scenario_.Dp import Dp
			self._dp = Dp(self._core, self._base)
		return self._dp

	@property
	def dhf(self):
		"""dhf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dhf'):
			from .Scenario_.Dhf import Dhf
			self._dhf = Dhf(self._core, self._base)
		return self._dhf

	@property
	def dpf(self):
		"""dpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dpf'):
			from .Scenario_.Dpf import Dpf
			self._dpf = Dpf(self._core, self._base)
		return self._dpf

	@property
	def ee(self):
		"""ee commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ee'):
			from .Scenario_.Ee import Ee
			self._ee = Ee(self._core, self._base)
		return self._ee

	@property
	def ej(self):
		"""ej commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ej'):
			from .Scenario_.Ej import Ej
			self._ej = Ej(self._core, self._base)
		return self._ej

	@property
	def ejf(self):
		"""ejf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ejf'):
			from .Scenario_.Ejf import Ejf
			self._ejf = Ejf(self._core, self._base)
		return self._ejf

	@property
	def el(self):
		"""el commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_el'):
			from .Scenario_.El import El
			self._el = El(self._core, self._base)
		return self._el

	@property
	def elsm(self):
		"""elsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_elsm'):
			from .Scenario_.Elsm import Elsm
			self._elsm = Elsm(self._core, self._base)
		return self._elsm

	@property
	def en(self):
		"""en commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_en'):
			from .Scenario_.En import En
			self._en = En(self._core, self._base)
		return self._en

	@property
	def ensm(self):
		"""ensm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ensm'):
			from .Scenario_.Ensm import Ensm
			self._ensm = Ensm(self._core, self._base)
		return self._ensm

	@property
	def ep(self):
		"""ep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ep'):
			from .Scenario_.Ep import Ep
			self._ep = Ep(self._core, self._base)
		return self._ep

	@property
	def epsm(self):
		"""epsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_epsm'):
			from .Scenario_.Epsm import Epsm
			self._epsm = Epsm(self._core, self._base)
		return self._epsm

	@property
	def epf(self):
		"""epf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_epf'):
			from .Scenario_.Epf import Epf
			self._epf = Epf(self._core, self._base)
		return self._epf

	@property
	def epfs(self):
		"""epfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_epfs'):
			from .Scenario_.Epfs import Epfs
			self._epfs = Epfs(self._core, self._base)
		return self._epfs

	@property
	def er(self):
		"""er commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_er'):
			from .Scenario_.Er import Er
			self._er = Er(self._core, self._base)
		return self._er

	@property
	def ersm(self):
		"""ersm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ersm'):
			from .Scenario_.Ersm import Ersm
			self._ersm = Ersm(self._core, self._base)
		return self._ersm

	@property
	def et(self):
		"""et commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_et'):
			from .Scenario_.Et import Et
			self._et = Et(self._core, self._base)
		return self._et

	@property
	def frsm(self):
		"""frsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frsm'):
			from .Scenario_.Frsm import Frsm
			self._frsm = Frsm(self._core, self._base)
		return self._frsm

	@property
	def fr(self):
		"""fr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fr'):
			from .Scenario_.Fr import Fr
			self._fr = Fr(self._core, self._base)
		return self._fr

	@property
	def fnsm(self):
		"""fnsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fnsm'):
			from .Scenario_.Fnsm import Fnsm
			self._fnsm = Fnsm(self._core, self._base)
		return self._fnsm

	@property
	def fn(self):
		"""fn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fn'):
			from .Scenario_.Fn import Fn
			self._fn = Fn(self._core, self._base)
		return self._fn

	@property
	def ftsm(self):
		"""ftsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftsm'):
			from .Scenario_.Ftsm import Ftsm
			self._ftsm = Ftsm(self._core, self._base)
		return self._ftsm

	@property
	def ft(self):
		"""ft commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ft'):
			from .Scenario_.Ft import Ft
			self._ft = Ft(self._core, self._base)
		return self._ft

	@property
	def fp(self):
		"""fp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fp'):
			from .Scenario_.Fp import Fp
			self._fp = Fp(self._core, self._base)
		return self._fp

	@property
	def fpsm(self):
		"""fpsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpsm'):
			from .Scenario_.Fpsm import Fpsm
			self._fpsm = Fpsm(self._core, self._base)
		return self._fpsm

	@property
	def fv(self):
		"""fv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fv'):
			from .Scenario_.Fv import Fv
			self._fv = Fv(self._core, self._base)
		return self._fv

	@property
	def fvsm(self):
		"""fvsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fvsm'):
			from .Scenario_.Fvsm import Fvsm
			self._fvsm = Fvsm(self._core, self._base)
		return self._fvsm

	@property
	def fx(self):
		"""fx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fx'):
			from .Scenario_.Fx import Fx
			self._fx = Fx(self._core, self._base)
		return self._fx

	@property
	def ff(self):
		"""ff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ff'):
			from .Scenario_.Ff import Ff
			self._ff = Ff(self._core, self._base)
		return self._ff

	@property
	def fl(self):
		"""fl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fl'):
			from .Scenario_.Fl import Fl
			self._fl = Fl(self._core, self._base)
		return self._fl

	@property
	def flf(self):
		"""flf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_flf'):
			from .Scenario_.Flf import Flf
			self._flf = Flf(self._core, self._base)
		return self._flf

	@property
	def fpf(self):
		"""fpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpf'):
			from .Scenario_.Fpf import Fpf
			self._fpf = Fpf(self._core, self._base)
		return self._fpf

	@property
	def fpfs(self):
		"""fpfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpfs'):
			from .Scenario_.Fpfs import Fpfs
			self._fpfs = Fpfs(self._core, self._base)
		return self._fpfs

	@property
	def grsm(self):
		"""grsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_grsm'):
			from .Scenario_.Grsm import Grsm
			self._grsm = Grsm(self._core, self._base)
		return self._grsm

	@property
	def gr(self):
		"""gr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gr'):
			from .Scenario_.Gr import Gr
			self._gr = Gr(self._core, self._base)
		return self._gr

	@property
	def gtsm(self):
		"""gtsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gtsm'):
			from .Scenario_.Gtsm import Gtsm
			self._gtsm = Gtsm(self._core, self._base)
		return self._gtsm

	@property
	def gt(self):
		"""gt commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gt'):
			from .Scenario_.Gt import Gt
			self._gt = Gt(self._core, self._base)
		return self._gt

	@property
	def gg(self):
		"""gg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gg'):
			from .Scenario_.Gg import Gg
			self._gg = Gg(self._core, self._base)
		return self._gg

	@property
	def gn(self):
		"""gn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gn'):
			from .Scenario_.Gn import Gn
			self._gn = Gn(self._core, self._base)
		return self._gn

	@property
	def gnf(self):
		"""gnf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gnf'):
			from .Scenario_.Gnf import Gnf
			self._gnf = Gnf(self._core, self._base)
		return self._gnf

	@property
	def gpsm(self):
		"""gpsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gpsm'):
			from .Scenario_.Gpsm import Gpsm
			self._gpsm = Gpsm(self._core, self._base)
		return self._gpsm

	@property
	def gpfs(self):
		"""gpfs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpfs'):
			from .Scenario_.Gpfs import Gpfs
			self._gpfs = Gpfs(self._core, self._base)
		return self._gpfs

	@property
	def gp(self):
		"""gp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gp'):
			from .Scenario_.Gp import Gp
			self._gp = Gp(self._core, self._base)
		return self._gp

	@property
	def gpf(self):
		"""gpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gpf'):
			from .Scenario_.Gpf import Gpf
			self._gpf = Gpf(self._core, self._base)
		return self._gpf

	@property
	def gv(self):
		"""gv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gv'):
			from .Scenario_.Gv import Gv
			self._gv = Gv(self._core, self._base)
		return self._gv

	@property
	def gvsm(self):
		"""gvsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gvsm'):
			from .Scenario_.Gvsm import Gvsm
			self._gvsm = Gvsm(self._core, self._base)
		return self._gvsm

	@property
	def gx(self):
		"""gx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gx'):
			from .Scenario_.Gx import Gx
			self._gx = Gx(self._core, self._base)
		return self._gx

	@property
	def gxsm(self):
		"""gxsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gxsm'):
			from .Scenario_.Gxsm import Gxsm
			self._gxsm = Gxsm(self._core, self._base)
		return self._gxsm

	@property
	def gya(self):
		"""gya commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gya'):
			from .Scenario_.Gya import Gya
			self._gya = Gya(self._core, self._base)
		return self._gya

	@property
	def gyas(self):
		"""gyas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gyas'):
			from .Scenario_.Gyas import Gyas
			self._gyas = Gyas(self._core, self._base)
		return self._gyas

	@property
	def gyc(self):
		"""gyc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gyc'):
			from .Scenario_.Gyc import Gyc
			self._gyc = Gyc(self._core, self._base)
		return self._gyc

	@property
	def htsm(self):
		"""htsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_htsm'):
			from .Scenario_.Htsm import Htsm
			self._htsm = Htsm(self._core, self._base)
		return self._htsm

	@property
	def ht(self):
		"""ht commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ht'):
			from .Scenario_.Ht import Ht
			self._ht = Ht(self._core, self._base)
		return self._ht

	@property
	def hh(self):
		"""hh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hh'):
			from .Scenario_.Hh import Hh
			self._hh = Hh(self._core, self._base)
		return self._hh

	@property
	def hp(self):
		"""hp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hp'):
			from .Scenario_.Hp import Hp
			self._hp = Hp(self._core, self._base)
		return self._hp

	@property
	def hr(self):
		"""hr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hr'):
			from .Scenario_.Hr import Hr
			self._hr = Hr(self._core, self._base)
		return self._hr

	@property
	def hrsm(self):
		"""hrsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hrsm'):
			from .Scenario_.Hrsm import Hrsm
			self._hrsm = Hrsm(self._core, self._base)
		return self._hrsm

	@property
	def hv(self):
		"""hv commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hv'):
			from .Scenario_.Hv import Hv
			self._hv = Hv(self._core, self._base)
		return self._hv

	@property
	def hvsm(self):
		"""hvsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hvsm'):
			from .Scenario_.Hvsm import Hvsm
			self._hvsm = Hvsm(self._core, self._base)
		return self._hvsm

	@property
	def hx(self):
		"""hx commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hx'):
			from .Scenario_.Hx import Hx
			self._hx = Hx(self._core, self._base)
		return self._hx

	@property
	def hxsm(self):
		"""hxsm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hxsm'):
			from .Scenario_.Hxsm import Hxsm
			self._hxsm = Hxsm(self._core, self._base)
		return self._hxsm

	@property
	def hya(self):
		"""hya commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hya'):
			from .Scenario_.Hya import Hya
			self._hya = Hya(self._core, self._base)
		return self._hya

	@property
	def hyas(self):
		"""hyas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyas'):
			from .Scenario_.Hyas import Hyas
			self._hyas = Hyas(self._core, self._base)
		return self._hyas

	@property
	def hyc(self):
		"""hyc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyc'):
			from .Scenario_.Hyc import Hyc
			self._hyc = Hyc(self._core, self._base)
		return self._hyc

	@property
	def hycs(self):
		"""hycs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hycs'):
			from .Scenario_.Hycs import Hycs
			self._hycs = Hycs(self._core, self._base)
		return self._hycs

	@property
	def hye(self):
		"""hye commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hye'):
			from .Scenario_.Hye import Hye
			self._hye = Hye(self._core, self._base)
		return self._hye

	@property
	def hyes(self):
		"""hyes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyes'):
			from .Scenario_.Hyes import Hyes
			self._hyes = Hyes(self._core, self._base)
		return self._hyes

	@property
	def hyg(self):
		"""hyg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hyg'):
			from .Scenario_.Hyg import Hyg
			self._hyg = Hyg(self._core, self._base)
		return self._hyg

	@property
	def hpf(self):
		"""hpf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpf'):
			from .Scenario_.Hpf import Hpf
			self._hpf = Hpf(self._core, self._base)
		return self._hpf

	# noinspection PyTypeChecker
	class ValueStruct(StructBase):
		"""Structure for reading output parameters. Fields: \n
			- Scenario: enums.Scenario: NAV | SCEL | TRO | AD | SCF | TROF | ADF | CATR | CAFR | BF | BFSM4 | BH | CATF | CAFF | BFF | BHF | CC | CCMP | CCMS1 | CF | CH | CHSM4 | CJ | CJSM4 | CL | CFF | CHF | CJF | CJFS4 | DD | DH | DJ | DJSM4 | DL | DLSM4 | DN | DNSM4 | DP | DHF | DPF | EE | EJ | EL | ELSM4 | EN | ENSM4 | EP | EPSM4 | ER | ERSM4 | ET | EJF | EPF | EPFS4 | FF | FL | FN | FNSM4 | FP | FPSM4 | FR | FRSM4 | FT | FTSM4 | FV | FVSM4 | FX | FPF | FPFS4 | GG | GN | GP | GPSM4 | GR | GRSM4 | GT | GTSM4 | GV | GVSM4 | GX | GXSM4 | GPF | GPFS4 | HH | HP | HT | HTSM4 | HPF For mapping of the values to scenario names, see Table 'Mapping of Scenario to scenario names'.
			- Fader: enums.SourceInt: EXTernal | INTernal Only returned for fading scenarios Indicates whether internal or external fading is active."""
		__meta_args_list = [
			ArgStruct.scalar_enum('Scenario', enums.Scenario),
			ArgStruct.scalar_enum('Fader', enums.SourceInt)]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Scenario: enums.Scenario = None
			self.Fader: enums.SourceInt = None

	# noinspection PyTypeChecker
	def get_value(self) -> ValueStruct:
		"""SCPI: ROUTe:LTE:SIGNaling<instance>:SCENario \n
		Snippet: value: ValueStruct = driver.route.scenario.get_value() \n
		Returns the active scenario. \n
			:return: structure: for return value, see the help for ValueStruct structure arguments.
		"""
		return self._core.io.query_struct('ROUTe:LTE:SIGNaling<Instance>:SCENario?', self.__class__.ValueStruct())

	def clone(self) -> 'Scenario':
		"""Clones the group by creating new object from it and its whole existing sub-groups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scenario(self._core, self._base.parent)
		self._base.synchronize_repcaps(new_group)
		return new_group
