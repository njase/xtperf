import sys
import perf

runner = perf.Runner()
runner.bench_command('python_startup', [sys.executable, '-c', 'pass'])
