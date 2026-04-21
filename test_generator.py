#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from generator import significant_change_generator, parallel_significant_change_generator

def test_significant_change_generator_numbers():
    def double(x):
        return x * 2
    
    data = [1, 2, 10, 100]
    gen = significant_change_generator(data, double, 1, threshold=0.5)
    result = list(gen)
    assert result == [2, 4, 20, 200]

def test_significant_change_generator_strings():
    def add_exclamation(s):
        return s + "!"
    
    data = ["a", "hello", "longstring"]
    gen = significant_change_generator(data, add_exclamation, 3, threshold=0.3)
    result = list(gen)
    assert "a!!!" in result

def test_significant_change_generator_empty():
    data = []
    gen = significant_change_generator(data, lambda x: x, 5)
    result = list(gen)
    assert result == []

def test_parallel_generator():
    def square(x):
        return x ** 2
    
    data = [1, 2, 3, 4, 5]
    gen = parallel_significant_change_generator(data, square, 2, threshold=0.5)
    result = list(gen)
    assert 16 in result
    assert 81 in result
    assert 256 in result
    assert 625 in result