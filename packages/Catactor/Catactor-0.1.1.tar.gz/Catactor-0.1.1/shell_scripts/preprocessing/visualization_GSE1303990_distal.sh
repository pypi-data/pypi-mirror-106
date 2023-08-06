#!/usr/bin/bash
set -euxo pipefail

GSE=GSE1303990
sf_marker='GABAergic_markers_fc.txt,Glutamatergic_markers_fc.txt,Non.Neuronal_markers_fc.txt'
ta_marker='tasic2016_gaba.csv,tasic2016_glu.csv,tasic2016_gli.csv'
cu_marker='cusanovich2018_inh.txt,cusanovich2018_ext.txt,cusanovich2018_gli.txt'
tn_marker='tasic2018_gaba.txt,tasic2018_glu.txt,tasic2018_gli.txt'

OPTIONS=" --na_filtering --norm --cfilter genome_flag --verbose --skip 2 --top-genes 10000 " 
DR_OPTIONS=" --pca 50 --norm --tsne-params nn=30,perplexity=100,learning_rate=100 "
if [ -z "$1" ]; then
	METHOD="preprocess"
else
        METHOD=$1
fi
if [ -z "$2" ]; then
        MDIR="../marker_genes/"
else
        MDIR=$2
fi
if [ -z "$3" ]; then
        DDIR="../mat_data/${GSE}"
else
        DDIR=$3
fi

COLUMN_DATA=${GSE}_bin_ng_Actx_with_bins_annot.csv
ROW_DATA=${GSE}_cell_ng_Actx_meta.csv 
MAT_DATA=${GSE}_sparse_mat_Actx.mtx
CLUSTERS=cluster,cluster_leiden,cluster_louvain,Ident,celltype
REFERENCE=

for dist in gene distal proximal
do
	if [ $dist == "distal" ]; then
		clabel="id_order_distal"
	elif [ $dist == "proximal" ]; then
		clabel="id_proximal"
	else
		clabel="id_order_gene"
	fi
	
for marker in stefan tasic cusanovich ntasic
do
	if [ $marker == "stefan" ]; then
		marker_file=$sf_marker
		mdir="${MDIR}/SF_markers/"
	elif [ $marker == "tasic" ]; then
                marker_file=$ta_marker
                mdir="${MDIR}/TA_markers/"
        elif [ $marker == "cusanovich" ]; then
                marker_file=$cu_marker
                mdir="${MDIR}/CU_markers/"
        else
                marker_file=$tn_marker
                mdir="${MDIR}/TN_markers/"
        fi
if [ "$METHOD" == "average" ]; then
Catactor --update $OPTIONS $DR_OPTIONS --gene-name '' --clabel global_index_5000  --cindex global_index_5000 --rindex local_index --rlabel ''  \
	--dir $DDIR --adir $DDIR --row $ROW_DATA --column $COLUMN_DATA \
	--mdir $mdir --markers $marker_file --cluster $CLUSTERS \
	--output ${GSE}_${dist} preprocess $MAT_DATA
break
elif [ "$METHOD" == "preprocess" ]; then
Catactor $OPTIONS $DR_OPTIONS --gene-name '' --clabel $clabel --cindex global_index_5000 --rindex local_index --rlabel '' \
	--dir $DDIR --adir $DDIR --row $ROW_DATA --column $COLUMN_DATA \
	--mdir $mdir --markers $marker_file --cluster $CLUSTERS \
	--output ${GSE}_${dist} preprocess $MAT_DATA
break
elif [ "$METHOD" == "test" ]; then
Catactor $OPTIONS --update --test-vis --clabel $clabel --cindex global_index --rindex local_index --rlabel '' \
	--dir $DDIR --adir $DDIR --row $ROW_DATA --column $COLUMN_DATA \
	--mdir $mdir --markers $marker_file --cluster $CLUSTERS \
	--output ${GSE}_${dist} visualization $MAT_DATA
break
elif [ "${METHOD}"  == "rank" ]; then
Catactor $OPTIONS $DR_OPTIONS --gene-name '' --clabel $clabel --cindex global_index --rindex local_index --rlabel '' \
	--dir $DDIR --adir $DDIR --row $ROW_DATA --column $COLUMN_DATA \
	--mdir $mdir --markers $marker_file --cluster $CLUSTERS \
	--output ${GSE}_${dist} visualization $MAT_DATA
fi
done
done



