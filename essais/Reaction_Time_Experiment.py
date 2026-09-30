import expyriment as xpy

xpy.control.set_develop_mode(True)  # fenêtre normale, pas plein écran
exp =xpy.design.Experiment("Reaction Time Experiment")
xpy.control.defaults.window_size = (800, 600)

white=(255, 255, 255)

xpy.control.initialize(exp)

circle = xpy.stimuli.Circle(250, colour=white, line_width=5, position=(0, 0))
delay = xpy.design.randomise.rand_int(1000, 5000)
circle.preload()

xpy.control.start()

exp.clock.wait(delay)
circle.present()
exp.keyboard.wait()

xpy.control.end()

