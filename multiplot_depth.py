genes = [
    'ABCC8', 'ABCC9', 'ACTC1', 'ACTN2', 'AKAP9', 'ANK2', 'ANKRD1', 'BAG3', 'CACNA1C', 'CACNA2D1', 'CACNB2',
    'CALM1', 'CALR3', 'CAMK2A', 'CASQ2', 'CAV3', 'CSRP3', 'DES', 'DLG1', 'DPP6', 'DSC2', 'DSG2', 'DTNA',
    'FGF12', 'GJA5', 'GJD4', 'GLA', 'GPD1L', 'HCN4', 'HEY2', 'JUP', 'KCNA5', 'KCND3', 'KCNE1', 'KCNE1L',
    'KCNE2', 'KCNE3', 'KCNH2', 'KCNJ2', 'KCNJ5', 'KCNJ8', 'KCNQ1', 'LAMP2', 'LDB3', 'LMNA', 'MYBPC3', 'MYH6',
    'MYH7', 'MYL2', 'MYL3', 'MYLK2', 'MYOZ2', 'MYPN', 'NEXN', 'NOS1AP', 'PKP2', 'PLN', 'PRKAG2', 'RANGRF',
    'RYR2', 'SCN10A', 'SCN1B', 'SCN2B', 'SCN3B', 'SCN4B', 'SCN5A', 'SLMAP', 'SNTA1', 'TAZ', 'TCAP', 'TGFB3',
    'TMEM43', 'TNNC1', 'TNNI3', 'TNNT2', 'TPM1', 'TRDN', 'TRPM4', 'TTN', 'TTR', 'VCL',
    ]

depth_files = [
    # 'depth_ion/S01.tsv',
    # 'depth_ion/S02.tsv',
    # 'depth_ion/S03.tsv',
    # 'depth_ion/S04.tsv',
    # 'depth_ion/S05.tsv',
    # 'depth_ion/S06.tsv',
    # 'depth_ion/S07.tsv',
    # 'depth_ion/S08.tsv',
    # 'depth_ion/S09.tsv',
    # 'depth_ion/S10.tsv',
    # 'depth_ion/S11.tsv',
    # 'depth_ion/S12.tsv',
    # 'depth_ion/S13.tsv',
    # 'depth_ion/S14.tsv',
    # 'depth_ion/S15.tsv',
    # 'depth_ion/S16.tsv',
    # 'depth_ion/S17.tsv',
    # 'depth_ion/S18.tsv',
    # 'depth_ion/S19.tsv',
    # 'depth_ion/S20.tsv',
    # 'depth_ion/S21.tsv',
    # 'depth_ion/S22.tsv',
    # 'depth_ion/S23.tsv',
    # 'depth_ion/S24.tsv',
    # 'depth_ion/S25.tsv',
    # 'depth_ion/S26.tsv',
    # 'depth_ion/S27.tsv',
    # 'depth_ion/S28.tsv',
    # 'depth_ion/S29.tsv',
    # 'depth_ion/S30.tsv',
    # 'depth_ion/S31.tsv',
    # 'depth_ion/S32.tsv',
    # 'depth_ion/S33.tsv',
    # 'depth_ion/S34.tsv',
    # 'depth_ion/S35.tsv',
    # 'depth_ion/S36.tsv',
    # 'depth_ion/S37.tsv',
    # 'depth_ion/S38.tsv',
    # 'depth_ion/S39.tsv',
    # 'depth_ion/S40.tsv',
    # 'depth_ion/S41.tsv',
    # 'depth_ion/S42.tsv',
    # 'depth_ion/S43.tsv',
    # 'depth_ion/S44.tsv',
    # 'depth_ion/S45.tsv',
    # 'depth_ion/S46.tsv',
    # 'depth_ion/S47.tsv',

    # 'depth_miseq/S00.tsv',
    # 'depth_miseq/S01.tsv',
    # 'depth_miseq/S02.tsv',
    # 'depth_miseq/S03.tsv',
    # 'depth_miseq/S04.tsv',
    # 'depth_miseq/S05.tsv',
    # 'depth_miseq/S06.tsv',
    # 'depth_miseq/S07.tsv',
    # 'depth_miseq/S08.tsv',
    # 'depth_miseq/S09.tsv',
    # 'depth_miseq/S10.tsv',
    # 'depth_miseq/S11.tsv',
    # 'depth_miseq/S12.tsv',
    # 'depth_miseq/S13.tsv',
    # 'depth_miseq/S14.tsv',
    # 'depth_miseq/S15.tsv',
    # 'depth_miseq/S16.tsv',
    # 'depth_miseq/S17.tsv',
    # 'depth_miseq/S18.tsv',
    # 'depth_miseq/S19.tsv',
    # 'depth_miseq/S20.tsv',
    # 'depth_miseq/S21.tsv',
    # 'depth_miseq/S22.tsv',
    # 'depth_miseq/S23.tsv',
    # 'depth_miseq/S24.tsv',
    # 'depth_miseq/S25.tsv',
    # 'depth_miseq/S26.tsv',
    # 'depth_miseq/S27.tsv',
    # 'depth_miseq/S28.tsv',
    # 'depth_miseq/S29.tsv',
    # 'depth_miseq/S30.tsv',
    # 'depth_miseq/S31.tsv',
    # 'depth_miseq/S32.tsv',
    # 'depth_miseq/S33.tsv',
    # 'depth_miseq/S34.tsv',
    # 'depth_miseq/S35.tsv',
    # 'depth_miseq/S36.tsv',
    # 'depth_miseq/S37.tsv',
    # 'depth_miseq/S38.tsv',
    # 'depth_miseq/S39.tsv',
    # 'depth_miseq/S40.tsv',
    # 'depth_miseq/S41.tsv',
    # 'depth_miseq/S42.tsv',
    # 'depth_miseq/S43.tsv',
    # 'depth_miseq/S44.tsv',
    # 'depth_miseq/S45.tsv',
    # 'depth_miseq/S46.tsv',
    # 'depth_miseq/S47.tsv',
    # 'depth_miseq/S48.tsv',

    # 'depth_basespace/10.tsv',
    # 'depth_basespace/11.tsv',
    # 'depth_basespace/12.tsv',
    # 'depth_basespace/13.tsv',
    # 'depth_basespace/14.tsv',
    # 'depth_basespace/15.tsv',
    # 'depth_basespace/16.tsv',
    # 'depth_basespace/17.tsv',
    # 'depth_basespace/18.tsv',
    # 'depth_basespace/19.tsv',
    # 'depth_basespace/01.tsv',
    # 'depth_basespace/20.tsv',
    # 'depth_basespace/21.tsv',
    # 'depth_basespace/22.tsv',
    # 'depth_basespace/23.tsv',
    # 'depth_basespace/24.tsv',
    # 'depth_basespace/25.tsv',
    # 'depth_basespace/26.tsv',
    # 'depth_basespace/27.tsv',
    # 'depth_basespace/28.tsv',
    # 'depth_basespace/29.tsv',
    # 'depth_basespace/02.tsv',
    # 'depth_basespace/30.tsv',
    # 'depth_basespace/31.tsv',
    # 'depth_basespace/32.tsv',
    # 'depth_basespace/33.tsv',
    # 'depth_basespace/34.tsv',
    # 'depth_basespace/35.tsv',
    # 'depth_basespace/36.tsv',
    # 'depth_basespace/37.tsv',
    # 'depth_basespace/38.tsv',
    # 'depth_basespace/39.tsv',
    # 'depth_basespace/03.tsv',
    # 'depth_basespace/40.tsv',
    # 'depth_basespace/41.tsv',
    # 'depth_basespace/42.tsv',
    # 'depth_basespace/43.tsv',
    # 'depth_basespace/44.tsv',
    # 'depth_basespace/45.tsv',
    # 'depth_basespace/46.tsv',
    # 'depth_basespace/47.tsv',
    # 'depth_basespace/48.tsv',
    # 'depth_basespace/04.tsv',
    # 'depth_basespace/05.tsv',
    # 'depth_basespace/06.tsv',
    # 'depth_basespace/07.tsv',
    # 'depth_basespace/08.tsv',
    # 'depth_basespace/09.tsv',

    'depth_miseq_hg19/S10.tsv',
    'depth_miseq_hg19/S11.tsv',
    'depth_miseq_hg19/S12.tsv',
    'depth_miseq_hg19/S13.tsv',
    'depth_miseq_hg19/S14.tsv',
    'depth_miseq_hg19/S15.tsv',
    'depth_miseq_hg19/S16.tsv',
    'depth_miseq_hg19/S17.tsv',
    'depth_miseq_hg19/S18.tsv',
    'depth_miseq_hg19/S19.tsv',
    'depth_miseq_hg19/S01.tsv',
    'depth_miseq_hg19/S20.tsv',
    'depth_miseq_hg19/S21.tsv',
    'depth_miseq_hg19/S22.tsv',
    'depth_miseq_hg19/S23.tsv',
    'depth_miseq_hg19/S24.tsv',
    'depth_miseq_hg19/S25.tsv',
    'depth_miseq_hg19/S26.tsv',
    'depth_miseq_hg19/S27.tsv',
    'depth_miseq_hg19/S28.tsv',
    'depth_miseq_hg19/S29.tsv',
    'depth_miseq_hg19/S02.tsv',
    'depth_miseq_hg19/S30.tsv',
    'depth_miseq_hg19/S31.tsv',
    'depth_miseq_hg19/S32.tsv',
    'depth_miseq_hg19/S33.tsv',
    'depth_miseq_hg19/S34.tsv',
    'depth_miseq_hg19/S35.tsv',
    'depth_miseq_hg19/S36.tsv',
    'depth_miseq_hg19/S37.tsv',
    'depth_miseq_hg19/S38.tsv',
    'depth_miseq_hg19/S39.tsv',
    'depth_miseq_hg19/S03.tsv',
    'depth_miseq_hg19/S40.tsv',
    'depth_miseq_hg19/S41.tsv',
    'depth_miseq_hg19/S42.tsv',
    'depth_miseq_hg19/S43.tsv',
    'depth_miseq_hg19/S44.tsv',
    'depth_miseq_hg19/S45.tsv',
    'depth_miseq_hg19/S46.tsv',
    'depth_miseq_hg19/S47.tsv',
    'depth_miseq_hg19/S48.tsv',
    'depth_miseq_hg19/S04.tsv',
    'depth_miseq_hg19/S05.tsv',
    'depth_miseq_hg19/S06.tsv',
    'depth_miseq_hg19/S07.tsv',
    'depth_miseq_hg19/S08.tsv',
    'depth_miseq_hg19/S09.tsv',
    
]

depths = {}
for gene in genes:
    depths[gene] = {}
    
bins = []
for path in depth_files:
    with open(path, 'r') as f:
        for l in f.readlines():
            (gene, depth) = l.split()
            if path in depths[gene]:
                depths[gene][path].append(depth)
            else:
                depths[gene][path] = [depth,]

                
import matplotlib
matplotlib.use('agg')
import pylab as pl
import matplotlib.pyplot as plt

for gene in genes:
    plt.cla()
    for sample in depths[gene]:
        plt.plot(range(0,len(depths[gene][sample])),depths[gene][sample], '-')
    plt.savefig("%s.png" % gene)

