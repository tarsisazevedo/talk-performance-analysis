Performance Analysis 101
========================

Exemplos de aplicações python com diversos profilers

line_profile:

    $ pip install line_profiler
    $ kernprof -l wrk_vaurien/app.py


memory_profiler:
    
    $ pip install psutil memory_profiler
    $ python -m memory_profiler wrk_vaurien/app.py
