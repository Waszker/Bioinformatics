class SimpleEvaluator:
    """
    SimpleEvaluator is a simple class for evaluating (assigning scores to) benchmarked methods.
    """

    def __init__(self):
        pass

    def get_score(self, proper_answer, answer, completion_time):
        """
        Evaluates answer given by the tested method.
        In SimpleEvaluator's implementation this method is binary in regards to the given answer. If the method gave
        wrong answer, the final score will always be zero. Otherwise the score relies on the time it took to compute
        the answer.
        :param proper_answer: proper result which should be returned by tested method
        :param answer: result of the tested method
        :param completion_time: float value of tested method completion time (in seconds)
        :return: float score of the method (bigger value means better performance)
        """
        completion_time = completion_time if completion_time > 0 else 1e-10
        time_score = 10. ** 6 / completion_time
        return time_score * (1 if answer == proper_answer else 0)
