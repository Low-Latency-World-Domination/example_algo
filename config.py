import yaml
from dataclasses import dataclass

@dataclass
class Config:
    symbol:str
    spreadbps:int
    stoppct:int



def load_config(yaml_file_path:str)->dict[str,Config]:
    with open(yaml_file_path, 'r') as file:
        data_raw = yaml.safe_load(file)
    data = {}
    for key, value in data_raw.items():
        data[key] = Config(**value)
    return data



