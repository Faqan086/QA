import json

with open('Json\config1.json', 'r') as f:
    config_data = json.load(f)

config_data['author'] = 'Fagan_Aliyev'
config_data['server']['port'] = '2024'
config_data['server']['port2'] = '2025'
config_data['openInBrowser'] = True
config_data['dist']['fonts'] = 'Arial'

with open('Json\my_config.json', 'w') as f:
    json.dump(config_data, f, indent=4)
