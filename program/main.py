from time import sleep
from benchmarking.benchmark import Benchmark
from benchmarking.evaluator import SimpleEvaluator


def _benchmark_test():
    # TODO: Remove this function before finishing project. This method is for testing/example purposes only!
    def method1(arg):
        sleep(1)
        return arg

    def method2(arg):
        sleep(3)
        return arg

    def method3(arg):
        return arg + 1

    test_cases = set([(i, i) for i in xrange(10)])
    benchmark = Benchmark(test_cases, SimpleEvaluator())
    print "Method1 scored %.2f" % benchmark.evaluate_method(method=method1)
    print "Method2 scored %.2f" % benchmark.evaluate_method(method=method2)
    print "Method3 scored %.2f" % benchmark.evaluate_method(method=method3)


if __name__ == "__main__":
    print "Bioinformatics 2017 project"

    _benchmark_test()
