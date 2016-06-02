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


cProfile:

    $ pip install pip install pyprof2calltree
    $ python web/cprof.py # it will save a file at `profile` dir
    $ pyprof2calltree -i profile/GET.root.004233ms.1464841262.prof -o profile/callgrind.GET.root.prof
    $ qcachegrind profile/callgrind.GET.root.prof
