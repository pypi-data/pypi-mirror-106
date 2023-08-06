import pandas as pd
import yaml
import json

# from hypertable import append, load, save
DEFAULT_HYPERTABLE_PATH = 'hypertable.yaml'
EXT2NAME = dict(
    yml='yaml',
    yaml='yaml',
    csv='csv',
    js='json',
    json='json'
)


def filepath2formatname(filepath):
    return EXT2NAME.get(filepath.split(',')[-1].lower().strip())


def append(row, filepath=DEFAULT_HYPERTABLE_PATH):
    dfrow = pd.DataFrame(pd.Series(row)).T
    fileformat = filepath2formatname(filepath)
    if fileformat == 'yaml':
        with open(filepath, 'a') as stream:
            yaml.dump(dfrow.iloc[0].to_dict(), stream)
    else:
        df = load(filepath=filepath)
        df = pd.concat([df, dfrow])
        df = df.reset_index()
        save(df, filepath=filepath)
    return df


def load(filepath=DEFAULT_HYPERTABLE_PATH):
    fileformat = filepath2formatname(filepath)
    if fileformat == 'yaml':
        with open(filepath, 'r') as stream:
            listofdicts = yaml.full_load(stream)
        df = pd.DataFrame(listofdicts)
    elif fileformat == 'csv':
        df = pd.read_csv(filepath)
    elif fileformat == 'json':
        df = json.load(filepath)
    return df


def save(df, filepath=DEFAULT_HYPERTABLE_PATH, mode='w'):
    fileformat = filepath2formatname(filepath)
    if fileformat == 'csv':
        df.to_csv(filepath)
    elif fileformat == 'json':
        df.to_json(filepath)
    elif fileformat == 'yaml':
        with open(filepath, mode=mode) as stream:
            yaml.dump(df.to_dict(), stream=stream)
    return filepath
