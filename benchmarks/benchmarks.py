import pip

class TimeSuite:
    def setup(self):
        pip.main(['install', 'git+https://github.com/pybind/pybind11_benchmark'])

    def time_collatz(self):
        from pybind11_benchmark import collatz
        for i in range(1, 10000):
            k = i
            while k != 1:
                k = collatz(k)
