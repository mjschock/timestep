from timestep.app import func, main_loop


def test_answer():
    assert func(3) == 4

def test_main_loop():
    assert main_loop() == 1
