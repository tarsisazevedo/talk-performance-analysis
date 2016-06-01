Performance Analysis 101
========================

python profiling examples.

line_profiler:

    $ pip install line_profiler
    $ kernprof -l wrk_vaurien/app.py
    $ python -m line_profiler wrk_vaurien/app.py.lprof


memory_profiler:
    
    $ pip install psutil memory_profiler
    $ python -m memory_profiler wrk_vaurien/app.py
