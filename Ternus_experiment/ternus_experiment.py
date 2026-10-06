import expyriment as xpy
import config

def run_trial(experiment, frame_a, frame_b, instructions, response_sreen, repetitions = 3):
    instructions.present()
    exp.keyboard.wait(keys=[xpy.misc.constants.K_SPACE])

    for _ in range(repetitions):
        frame_a.present()
        experiment.clock.wait(config.FRAME_DURATION)
        frame_b.present()
        experiment.clock.wait(config.FRAME_DURATION)

    response_screen.present()
    key, rt = exp.keyboard.wait(keys=[xpy.misc.constants.K_LEFT, xpy.misc.constants.K_RIGHT])

    if key == xpy.misc.constants.K_LEFT:
        response = config.LEFT_KEY
    else:
        response = config.RIGHT_KEY
    return response, key, rt


xpy.control.set_develop_mode(True)  # fenêtre normale, pas plein écran
exp = xpy.design.Experiment(name=config.EXPERIMENT_NAME, background_colour=config.BACKGROUND_COLOR, foreground_colour=config.FOREGROUND_COLOR)
xpy.control.defaults.window_size = config.WINDOW_SIZE

frame_duration = config.FRAME_DURATION

exp.data_variable_names = ["run_type", "transition", "frame_duration", "response", "key_pressed", "reaction_time", "rt_ms"]

xpy.control.initialize(exp)

frame_a=xpy.stimuli.Canvas(size=config.CANVAS_SIZE, colour=config.BACKGROUND_COLOR)
for x in config.FRAME_A_POSITIONS:
    xpy.stimuli.Circle(radius=config.DOT_RADIUS, position=(x, 0), colour=config.FOREGROUND_COLOR).plot(frame_a)

frame_b=xpy.stimuli.Canvas(size=config.CANVAS_SIZE, colour=config.BACKGROUND_COLOR)
for x in config.FRAME_B_POSITIONS:
    xpy.stimuli.Circle(radius=config.DOT_RADIUS, position=(x, 0), colour=config.FOREGROUND_COLOR).plot(frame_b)   


instructions = xpy.stimuli.TextScreen( heading = "Ternus demonstration", text = "Press space to start the experiment.", text_colour = (250,250,250), heading_bold = True)

response_screen = xpy.stimuli.TextScreen( heading = "What did you see ?", text = "Press left key for element motion or press right key for group motion", text_colour = (250,250,250), heading_bold = True)

for stimulus in (frame_a, frame_b, instructions, response_screen):
    stimulus.preload()

xpy.control.start(skip_ready_screen=True)

response, key, rt = run_trial(exp, frame_a, frame_b, instructions, response_screen)

exp.data.add(["self_test", "direct", config.FRAME_DURATION, response, key, rt])
 
xpy.control.end()