from PyCalculotron.components.calculation.bernouilli import experience, print_bernouilli_result_array


def test_experience():
    assert experience(20)


def test_print_bernouilli_result_array():
    assert print_bernouilli_result_array(30, 10)
