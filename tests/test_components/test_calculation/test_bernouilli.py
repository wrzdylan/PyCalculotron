from PyCalculotron.components.calculation.bernouilli import experience, bernouilli_result_array


def test_experience():
    assert 20 >= experience(20) > 0


def test_bernouilli_result_array():
    assert isinstance(bernouilli_result_array(30, 10), list) and len(bernouilli_result_array(30, 10)) == 30
