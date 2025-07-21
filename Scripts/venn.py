import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
from matplotlib_set_diagrams import VennDiagram

set1 = set(['DATA SCIENCE', 'MATHEMATICS', 'MACHINE LEARNING', 'STATISTICAL RESEARCH'])
set2 = set(['DATA SCIENCE', 'STATISTICAL RESEARCH', 'DOMAIN EXPERTISE','DATA PROCESSING'])
set3 = set(['DATA SCIENCE', 'MACHINE LEARNING', 'COMPUTER SCIENCE','DATA PROCESSING'])
# print(str(set1))
v = venn3((set1, set2, set3), ('','',''))
# labels = {0:}
# VennDiagram.from_sets(
#     [
#         set1,
#         set2,
#         set3
#     ],
#     subset_labels=lambda x: print(x))

for label in v.subset_labels:
    if label:
        label.set_fontsize(8)

v.get_label_by_id('100').set_text('Mathematics')

v.get_label_by_id('010').set_text('Computer\nScience')
v.get_label_by_id('001').set_text('Domain\nExpertise')
v.get_label_by_id('110').set_text('Machine\nLearning')
v.get_label_by_id('101').set_text('Statistics')
v.get_label_by_id('011').set_text('Data\nAnalysis')
v.get_label_by_id('111').set_text('DATA\nSCIENCE')

label = v.get_label_by_id('111')
if label:
    label.set_fontsize(13)
    label.set_color('white')
    label.set_fontweight('bold')
# VennDiagram.as_wordcloud((set1, set2, set3))
plt.savefig(fname='DataScience.png', dpi=600)