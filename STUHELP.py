from time import sleep
import os
import numpy

Welcome = ("""
░█▀▀▀█ ▀▀█▀▀ ░█─░█ ░█─░█ ░█▀▀▀ ░█─── ░█▀▀█ 
─▀▀▀▄▄ ─░█── ░█─░█ ░█▀▀█ ░█▀▀▀ ░█─── ░█▄▄█ 
░█▄▄▄█ ─░█── ─▀▄▄▀ ░█─░█ ░█▄▄▄ ░█▄▄█ ░█───""")


def sort(Array_process_s):
    print(Welcome)
    print("sorting...")
    sleep(3)
    os.system('cls')
    Array_process_s.sort()
    print(Array_process_s)


def mean(Array_process):
    print(Welcome)
    print("Finding mean...")
    sleep(3)
    os.system('cls')
    Array_process_m_1 = numpy.array(Array_process)
    Array_process_m_2 = numpy.mean(Array_process_m_1)
    print(Array_process_m_2)


def average(Array_process):
    print(Welcome)
    print("Finding average...")
    sleep(3)
    os.system('cls')
    Array_process_a_1 = numpy.array(Array_process)
    Array_process_a_2 = numpy.average(Array_process_a_1)
    print(Array_process_a_2)


def median(Array_process,):
    print(Welcome)
    print("Finding median...")
    sleep(3)
    os.system('cls')
    Array_process_md_1 = numpy.array(Array_process)
    Array_process_md_2 = numpy.median(Array_process_md_1)
    print(Array_process_md_2)


def mode(Array_process,):
    print(Welcome)
    print("Finding mode...")
    sleep(3)
    os.system('cls')
    most = max(list(map(Array_process.count, Array_process)))
    return list(set(filter(lambda x: Array_process.count(x) == most, Array_process)))
