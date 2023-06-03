import json
import random

with open('Json\config2.json', 'r') as f:
    config_data = json.load(f)

x = random.randint(0, 255)
config_data['vm']['ip'] = '192.168.42.' + str(x)
config_data['vm']['memory'] = '2048'
config_data['vm']['forwarded_ports'].append({
    'guest_port': 35729,
    'host_port': 35729
})
config_data['vdd']['sites']['drupal7']['account_name'] = 'Fagan'
config_data['vdd']['sites']['drupal7']['account_pass'] = 'qwerty'
config_data['vdd']['sites']['drupal7']['account_mail'] = 'fagan@example.com'

with open('Json\my_config.json', 'w') as f:
    json.dump(config_data, f, indent=4)
