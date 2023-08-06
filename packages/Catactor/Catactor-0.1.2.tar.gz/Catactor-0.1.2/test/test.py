import pickle
import scanpy as sc
import sys
sys.path.insert(1, '/home/rkawaguc/ipython/Catactor/')
#import Catactor
from Catactor import mini_catactor


# with open("/home/rkawaguc/ipython/BICCN/script/Catactor/analysis/191219_meta/output/scobj/BICCN2_gene_id_order_gene__all_scanpy_obj.pyn", "rb") as f:
#     a = pickle.load(f)
# out = mini_catactor.run_mini_catactor(a, plot_gene=True, dimension='tsne_')


from Catactor import pseudo_bulk
reference = "/home/rkawaguc/ipython/BICCN/script/Catactor/analysis/191219_meta/output/scobj/BICCN2_gene_id_order_gene__all_scanpy_obj.pyn"
with open(reference, "rb") as f:
    ref = pickle.load(f)
    
peak = "/home/rkawaguc/ipython/BICCN/script/Catactor/analysis/191219_meta/output/scobj/BICCN2_gene_global_index__all_scanpy_obj.pyn"

with open(peak, "rb") as f:
    pdata = pickle.load(f)
pnew = pseudo_bulk.convert_row_and_column(pdata, 'global_index_5000', 'global_index', 'global_index', 'global_index', 'cluster')
print(pnew)
# pseudo_bulk.run_average_profiling(pdata, reference=reference)

# print(pseudo_bulk.genome_binning(pdata.var))