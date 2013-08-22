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

def test_copy():
    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    ct_cpy = ct.copy()
    assert(ct is not ct_cpy)
    assert(ct == ct_cpy)

def test_repr():
    #repr() of an empty OrderedSet should not fail
    ct_empty  = OrderedSet()
    assert_equal(repr(ct_empty), "OrderedSet()")

    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    assert_equal(repr(ct),"OrderedSet(['a', 'b', 'c', 'd', 'e'])")

    ct = OrderedSet(range(30))
    assert_equal(repr(ct),"OrderedSet([0...29])")

def test_reversed():
    ct_empty  = OrderedSet()
    l = [ i for i in reversed(ct_empty)]
    assert_equal(l, [])

    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    l = [ i for i in reversed(ct)]
    assert_equal(l, ['e', 'd', 'c', 'b', 'a'])

def test_add(): 
    ct_empty  = OrderedSet()
    ct_empty.add('a')
    assert_equal(ct_empty, OrderedSet(['a']))
    
    ct_empty.add('a')
    assert_equal(ct_empty, OrderedSet(['a']))
    
    ct_empty.append('b')
    assert_equal(ct_empty, OrderedSet(['a', 'b']))

def test_extend():
    ct_empty = OrderedSet()
    ct_empty.extend([2,3,4,5])
    assert_equal(ct_empty, OrderedSet([2,3,4,5]))

    ct_empty.extend(OrderedSet([3,4,5,6,2]))
    assert_equal(ct_empty, OrderedSet([2,3,4,5,6]))

def test_merge():
    ct_empty = OrderedSet()
    merged = ct_empty.merge(OrderedSet([1,2,3,4]))
    assert_equal(merged, (OrderedSet([1,2,3,4]), [0,1,2,3]))

def test_discard():
    ct = OrderedSet([2,3,4,5])
    assert_raises(NotImplementedError, ct.discard, 3)

def test_del():
    ct = OrderedSet([2,3,4,5,6])
    assert_equal(hasattr(ct, '__del__'), False)

def test_iter():
    ct_empty  = OrderedSet()
    l = [ i for i in iter(ct_empty)]
    assert_equal(l, [])

    ct = OrderedSet(['a', 'b', 'c', 'a', 'd', 'e'])
    l = [ i for i in iter(ct)]
    assert_equal(l, ['a', 'b', 'c', 'd', 'e'])

def test_pickle():
    ct = OrderedSet(['a','b','c'])
    import cPickle as pickle
    ctp = pickle.loads(pickle.dumps(ct))
    assert_equal(ct, ctp)
    assert_equal(ct[0], 'a')
    assert_equal(ct.index('b'), 1)
