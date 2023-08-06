# -*- coding: utf-8 -*-

from __future__ import absolute_import

import numpy as np
import pandas as pd


### Pre-process RNAseq datasets
def drop_empty_genes(rnaseq_data):
    data = rnaseq_data.copy()
    data = data.dropna(how='all')
    data = data.fillna(0)  # Put zeros to all missing values
    data = data.loc[data.sum(axis=1) != 0]  # Drop rows will 0 among all cell/tissues
    return data


def log10_transformation(rnaseq_data, addition = 1e-6):
    ### Apply this only after applying "drop_empty_genes" function
    data = rnaseq_data.copy()
    data = data.apply(lambda x: np.log10(x + addition))
    data = data.replace([np.inf, -np.inf], np.nan)
    return data


def scale_expression_by_sum(rnaseq_data, axis=0,sum_value=1e6):
    '''
    This function scale all samples to sum up the same value.
    '''
    data = rnaseq_data.values
    data = sum_value * np.divide(data, np.nansum(data, axis=axis))
    scaled_data = pd.DataFrame(data, index=rnaseq_data.index, columns=rnaseq_data.columns)
    return scaled_data


def divide_expression_by_max(rnaseq_data, axis=1):
    '''
    This function divides each gene value given the max value. Axis = 0 is the max of each sample, while axis = 1
    indicates that each gene is divided by its max value across samples.
    '''
    new_data = rnaseq_data.div(rnaseq_data.max(axis=axis), axis=int(not axis))
    new_data = new_data.fillna(0.0).replace(np.inf, 0.0)
    return new_data


def divide_expression_by_mean(rnaseq_data, axis=1):
    '''
    This function divides each gene value given the mean value. Axis = 0 is the max of each sample, while axis = 1
    indicates that each gene is divided by its median value across samples.
    '''
    new_data = rnaseq_data.div(rnaseq_data.mean(axis=axis), axis=int(not axis))
    new_data = new_data.fillna(0.0).replace(np.inf, 0.0)
    return new_data


def add_complexes_to_expression(rnaseq_data, complexes):
    tmp_rna = rnaseq_data.copy()
    for k, v in complexes.items():
        if all(g in tmp_rna.index for g in v):
            df = tmp_rna.loc[v, :]
            tmp_rna.loc[k] = df.min().values.tolist()
        else:
            tmp_rna.loc[k] = [0] * tmp_rna.shape[1]
    return tmp_rna


def aggregate_single_cells(rnaseq_data, metadata, barcode_col='barcodes', celltype_col='cell_types', method='average',
                           transposed=True):
    '''
    rnaseq_data is an expression matrix with genes as rows and single cells as columns. Transposed has to be set True when
    rows are single cells and columns are genes.
    '''
    assert metadata is not None, "Please provide metadata containing the barcodes and cell-type annotation."
    assert method in ['average', 'nn_cell_fraction'], "{} is not a valid option for method".format(method)

    meta = metadata.reset_index()
    meta = meta[[barcode_col, celltype_col]].set_index(barcode_col)
    mapper = meta[celltype_col].to_dict()

    if transposed:
        df = rnaseq_data
    else:
        df = rnaseq_data.T
    df.index = [mapper[c] for c in df.index]
    df.index.name = 'celltype'
    df.reset_index(inplace=True)

    agg_df = pd.DataFrame(index=df.columns).drop('celltype')

    for celltype, ct_df in df.groupby('celltype'):
        ct_df = ct_df.drop('celltype', axis=1)
        if method == 'average':
            agg = ct_df.mean()
        elif method == 'nn_cell_fraction':
            agg = ((ct_df > 0).sum() / ct_df.shape[0])
        agg_df[celltype] = agg
    return agg_df

