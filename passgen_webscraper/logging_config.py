import logging
import sys
from colorama import init, Fore, Style

# Initialize colorama for cross-platform support
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    COLORS = {
        'DEBUG': Fore.CYAN,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, '')
        reset = Style.RESET_ALL
        log_message = super().format(record)
        return f"{log_color}{log_message}{reset}"

# Create a logger
logger = logging.getLogger("passgen_app")
logger.setLevel(logging.DEBUG)

# Create a console handler with the custom formatter
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Set the formatter with color
formatter = ColorFormatter("%(asctime)s - [%(levelname)s] - %(message)s")
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)