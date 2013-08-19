#-*- coding: utf-8 -*-

from numpy.testing import assert_equal
from nose.tools import assert_not_equal, assert_raises
from ..categorical import OrderedSet


def test_eq():
    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    ct_cpy = OrderedSet(['a', 'b', 'c', 'd', 'e'])
    assert_equal(ct, ct_cpy)
    
    ct_ne = OrderedSet(['a', 'b', 'c', 'e'])
    assert_not_equal(ct, ct_ne)

    ct_clone = OrderedSet(['e', 'd', 'c' , 'b', 'a'])
    assert_not_equal(ct, ct_clone)

    ct_empty  = OrderedSet([])
    ct_empty2 = OrderedSet([])
    assert_equal(ct_empty, ct_empty2)

    assert(ct == ct_cpy)
    assert(ct != ct_empty)

def test_contains():
    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])

    assert_equal('a' in ct, True)
    assert_equal(4 in ct, False)

def test_len(): 
    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    assert_equal(len(ct), 5)
     
    ct_empty  = OrderedSet([])
    assert_equal(len(ct_empty), 0)

def test_lookup_methods(): 
    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    assert_equal(ct.index('a'), 0)
    assert_equal(ct.index('b'), 1)
    assert_equal(ct.index('c'), 2)
    assert_equal(ct.index('d'), 3) 
    assert_equal(ct.index('e'), 4)
    
    assert_equal(ct.index_for('d'), 3)

def test_getsetitem():
    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    assert_equal(ct[2], 'c')
    assert_equal(ct[0:3], OrderedSet(['a', 'b', 'c']))
    assert_raises(TypeError, ct.__getitem__, None)
    assert_raises(TypeError, ct.__getitem__, '0')

    ct[2] = 'f'
    assert_equal(ct, OrderedSet(['a', 'b', 'f', 'd', 'e']))
    assert_equal(ct[2],'f')
    assert_raises(IndexError, ct.__setitem__, 7, 'casa')


'''

def test_copy():

def test_repr():

def test_getset_state():

def test_reversed():

def test_pop():

def test_add():

def test_extend():

def test_merge():

def test_discard():

def test_del():

def test_iter():
'''
