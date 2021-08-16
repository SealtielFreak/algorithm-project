from colorama import init, Fore, Style
from lib.priting import pritting
import argparse


class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(Style.BRIGHT)
        super().error(message)
        print(Style.RESET_ALL)