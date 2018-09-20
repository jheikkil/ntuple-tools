import ROOT

version = 'v42'


class Sample():
    def __init__(cls, name, label, version=None):
        cls.name = name
        cls.label = label
        if version:
            version = '_'+version
        else:
            version = ''
        cls.histo_filename = '../plots1/histos_{}{}.root'.format(cls.name, version)
        cls.histo_file = ROOT.TFile(cls.histo_filename)


sample_names = ['ele_flat2to100_PU0',
                'ele_flat2to100_PU200',
                'photonPt35_PU0',
                'photonPt35_PU200']

sample_ele_flat2to100_PU0 = Sample('ele_flat2to100_PU0', 'PU0', version)
sample_ele_flat2to100_PU200 = Sample('ele_flat2to100_PU200', 'PU200', version)

sample_gPt35_PU0 = Sample('photonPt35_PU0', 'Pt35 PU0', version)
sample_gPt35_PU200 = Sample('photonPt35_PU200', 'Pt35 PU200', version)

sample_hadronGun_PU0 = Sample('hadronGun_PU0', 'PU0', version)
sample_hadronGun_PU200 = Sample('hadronGun_PU200', 'PU200', version)

samples_ele = [sample_ele_flat2to100_PU0, sample_ele_flat2to100_PU200]

samples_photon = [sample_gPt35_PU0, sample_gPt35_PU200]
samples_hadrons = [sample_hadronGun_PU0, sample_hadronGun_PU200]

sample_nugunrate = Sample('nugun_alleta_pu200', 'PU200', version)
samples_nugunrates = [sample_nugunrate]


tpset_labels = {'DEF': 'NNDR',
                'DEF_em': 'NNDR + EGID',
                'DEF_pt10': 'NNDR, p_{T}^{L1}>10GeV',
                'DEF_pt10_em': 'NNDR + EGID, p_{T}^{L1}>10GeV',
                'DEF_pt20': 'NNDR, p_{T}^{L1}>20GeV',
                'DEF_pt20_em': 'NNDR + EGID, p_{T}^{L1}>20GeV',
                'DEF_pt25': 'NNDR, p_{T}^{L1}>25GeV',
                'DEF_pt25_em': 'NNDR + EGID, p_{T}^{L1}>25GeV',
                'DEF_pt30': 'NNDR, p_{T}^{L1}>30GeV',
                'DEF_pt30_em': 'NNDR + EGID, p_{T}^{L1}>30GeV'}


particle_labels = {'ele': 'all #eta',
                   'elePt20': 'p_{T}^{GEN}>20GeV',
                   'elePt30': 'p_{T}^{GEN}>30GeV',
                   'elePt40': 'p_{T}^{GEN}>40GeV',
                   'eleA': '|#eta^{GEN}| <= 1.52',
                   'eleB': '1.52 < |#eta^{GEN}| <= 1.7',
                   'eleC': '1.7 < |#eta^{GEN}| <= 2.4',
                   'eleD': '2.4 < |#eta^{GEN}| <= 2.8',
                   'eleE': '|#eta^{GEN}| > 2.8',
                   'eleAB': '|#eta^{GEN}| <= 1.7',
                   'eleABC': '|#eta^{GEN}| <= 2.4',
                   'eleBC': '1.52 < |#eta^{GEN}| <= 2.4',
                   'eleBCD': '1.52 < |#eta^{GEN}| <= 2.8',
                   'eleBCDE': '|#eta^{GEN}| > 1.52',
                   'eleAAA': '|#eta^{GEN}| <= 1.52',
                   'eleAA': '|#eta^{GEN}| <= 1.6',
                   'eleBB': '1.6 < |#eta^{GEN}| <= 2.4',
                   'eleCC': '2.4 < |#eta^{GEN}| <= 2.8',
                   'eleDD': '|#eta^{GEN}| > 2.8',
                   'all': 'all #eta^{L1}',
                   'etaA': '|#eta^{L1}| <= 1.52',
                   'etaB': '1.52 < |#eta^{L1}| <= 1.7)',
                   'etaC': '1.7 < |#eta^{L1}| <= 2.4)',
                   'etaD': '2.4 < |#eta^{L1}| <= 2.8)',
                   'etaE': '|#eta^{L1}| > 2.8',
                   'etaAB': '|#eta^{L1}| <= 1.7',
                   'etaABC': '|#eta^{L1}| <= 2.4',
                   'etaBC': '1.52 < |#eta^{L1}| <= 2.4',
                   'etaBCD': '1.52 < |#eta^{L1}| <= 2.8',
                   'etaBCDE': '|#eta^{L1}| > 1.52'}

samples = []
# particles = ''