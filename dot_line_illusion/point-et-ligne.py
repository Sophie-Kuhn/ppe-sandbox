import expyriment as xpy

xpy.control.set_develop_mode(True)  # fenêtre normale, pas plein écran
exp = xpy.design.Experiment("Illusory-Line motion")
xpy.control.defaults.window_size = (800, 600)
xpy.io.Keyboard.set_quit_key(xpy.misc.constants.K_ESCAPE)

start = (-250, 0)
end=(250, 0)
size=20
white=(255, 255, 255)
cue_duration_ms=250

xpy.control.initialize(exp)

line = xpy.stimuli.Line(start, end, size, colour=white)
cue = xpy.stimuli.Rectangle(size=(size, size), position=start, colour=white)
line.preload()
cue.preload()

xpy.control.start()

cue.present()
exp.clock.wait(cue_duration_ms)
line.present()
exp.keyboard.wait()
xpy.control.end()

