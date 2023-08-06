import pytest
from mmdesigner.gui import Gui


def test_gui_initialized_tk(mocker):
    mocked = mocker.patch("mmdesigner.gui.tk.Tk.title")
    gui = Gui("testing", "100x100")
    mocked.assert_called_once()

def test_gui_init_withdraw(mocker):
    mocked = mocker.patch('mmdesigner.gui.tk.Tk.withdraw')
    gui = Gui("testing","100x100")
    mocked.assert_called_once()

#def test_quit_destroys_window(mocker):
    mocked = mocker.patch('mmdesigner.gui.tk.Tk.destroy')
    gui = Gui("testing","100x100")
    gui.quit()
    mocked.assert_called_once()

def test_get_main_window_sets_icon(mocker):
    mocker = mocker.patch('mmdesigner.gui.tk.Tk.iconphoto')
    gui = Gui("testing","100x100")
    gui.get_main_window()
    mocker.assert_called_once()


