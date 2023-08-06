"""
main entry point to the program
"""
import os

import pylogconf.core
import tqdm
from pytconf import register_main, config_arg_parse_and_launch, register_endpoint
from pycookie.static import VERSION_STR

@register_main(
    main_description="pycookie will help you remove duplicate files",
    app_name="pycookie",
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
