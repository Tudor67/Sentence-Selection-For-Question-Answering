import pandas as pd


def load_data(filename):
    data_frame = pd.read_json(filename)
    data = data_frame.to_dict(orient='list')
    
    return data


def write_results(results):
    print('Method: {}'.format(results['Method']))
    print('AvgPrec@1: {} (std = {})'.format(results['AvgPrec@1'], 
                                    results['StdPrec@1']))
    print('MAP: {} (std = {})'.format(results['MAP'], results['StdAP']))
    print('\n')
