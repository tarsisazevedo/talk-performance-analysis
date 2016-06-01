Performance Analysis 101
========================

python profiling examples.

line_profiler:

    $ pip install line_profiler
    $ kernprof -l web/app.py
    $ python -m line_profiler web/app.py.lprof


memory_profiler:
    
    $ pip install psutil memory_profiler
    $ python -m memory_profiler web/mem.py
