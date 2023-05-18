def test_import_variation_1():
    import timestep.envs.rock_paper_scissors.env

    assert timestep.envs.rock_paper_scissors.env.rock_paper_scissors("openai_api_key") == 1

def test_import_variation_2():
    from timestep.envs.rock_paper_scissors import env

    assert env.rock_paper_scissors("openai_api_key") == 1

def test_import_variation_3():
    from timestep.envs.rock_paper_scissors.env import rock_paper_scissors

    assert rock_paper_scissors("openai_api_key") == 1
