import expyriment

expyriment.control.set_develop_mode(True)  # fenêtre normale, pas plein écran
exp = expyriment.design.Experiment("Test")
expyriment.control.initialize(exp)
expyriment.stimuli.TextLine("Ça marche !").present()
exp.clock.wait(2000)
expyriment.control.end()