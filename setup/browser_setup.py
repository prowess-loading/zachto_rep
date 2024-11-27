import random
from setup.config_loader import load_config
from setup.device_manager import get_device, get_proxy
from setup.browser_init import get_browser_options, initialize_driver
from setup.utils import adjust_dimensions, set_window_size

SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


class BrowserSetup:
    def __init__(self):
        self.devices = load_config("data/devices.json")
        self.proxies = load_config("data/proxies.json")
        self.browser_deltas = load_config("data/browser_deltas.json")

    def setup_browser(self, device_name, browser_name, region="usa"):

        device = get_device(self.devices, device_name)
        proxy = get_proxy(self.proxies, region)

        # Browser Selection
        if browser_name == "random":
            browser_name = random.choice(SUPPORTED_BROWSERS)

        print(f"Browser name: {browser_name}")

        if browser_name not in SUPPORTED_BROWSERS:
            raise ValueError(f"Unsupported browser: {browser_name}")

        # Dimension Adjustment
        adjusted_width, adjusted_height = adjust_dimensions(
            device, self.browser_deltas, browser_name)

        # Initialize Browser
        user_agent = device.get("userAgent")
        options = get_browser_options(browser_name, device, user_agent)
        driver = initialize_driver(
            browser_name, options, proxy, adjusted_width, adjusted_height)

        # Set Window Size
        set_window_size(driver, device, self.browser_deltas, browser_name)

        return driver
