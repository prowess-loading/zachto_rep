from setup.utils import generate_user_agent
from setup.config_loader import load_config
from setup.device_manager import get_device

device_name = "Samsung Galaxy S22 5G"

devices = load_config("data/new_agents.json")

device = get_device(devices, device_name)

agent = generate_user_agent(device, "chrome")

print(agent)
