import logging
import click
from mmdesigner.gui import Gui

from .__version__ import __version__


def run_gui():
    gui = Gui("mmdesigner", "800x600")
    main_window = gui.get_main_window()
    main_window.withdraw()
    # setup widgets
    main_window.deiconify()
    try:
        main_window.mainloop()
    finally:
        # save settings
        pass


# command line interface
@click.version_option(__version__, '-v', '--version')

@click.command()
@click.option("--debug", "-d", is_flag=True, help="Run in debug mode")
@click.option("--gui", "-g", is_flag=True, help="Run in gui mode")
def main(debug, gui):
    print("mmdesigner")
    if debug:
        print("debug mode")
    if gui:
        run_gui()

# python -m math_magik
if __name__ == '__main__':
    main()
