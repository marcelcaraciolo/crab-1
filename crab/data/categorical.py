# -*- coding: utf-8 -*-

from collections import MutableSet

SLICE_ALL =  slice(None)

class OrderedSet(MutableSet):
    """
    Container that store items like a list. 
    But each item appears in the list only once.
    You can look up an entry's index in the list in constant time.
   """

    def __init__(self, iterable=None):
        self.indices = {}
        self.items = []
        if iterable is not None:
            self |= iterable

        self.setup_lookup_methods()

    def __contains__(self, key):
        return key in self.indices

    def __len__(self):
        return len(self.items)

    def setup_lookup_methods(self):
        self.index = self.indices.__getitem__
        self.index_for = self.index

    def __getitem__(self, index):
        """
        Get the item at a given index.

        If `index` is a slice, you will get back that slice of items. If it's
        the slice [:], exactly the same object is returned. (If you want an
        independent copy of an OrderedSet, use `OrderedSet.copy()`.)

        If `index` is an iterable, you'll get the OrderedSet of items
        corresponding to those indices. This is similar to NumPy's
        "fancy indexing".
        """
        if index is None:
            raise TypeError("Can't index an OrderedSet with None")
        elif index == SLICE_ALL:
            return self
        elif hasattr(index, '__index__') or isinstance(index, slice):
            result = self.items[index]
            if isinstance(result, list):
                return OrderedSet(result)
            else:
                return result
        elif isinstance(index,basestring):
            raise TypeError("Can't use a string as an OrderedSet index.")
        else:
           return OrderedSet([ self.items[i] for i in index]) 

    def __setitem__(self, n, newkey):
        assert hasattr(n , '__index__')
        oldkey = self.items[n]
        del self.indices[oldkey]
        self.items[n] = newkey
        self.indices[newkey] = n

    def copy(self):
        return OrderedSet(self)

    def __repr__(self):
        if not self:
            return u'%s()' % (self.__class__.__name__,)
        elif len(self) < 10:
            return u'%s(%r)' % (self.__class__.__name__, list(self))
        else:
            return u'%s(%r...%r)' % (self.__class__.__name__, self[0], self[len(self)])

    def __getstate__(self):
        return list(self)       

    def __setstate__(self, state):
        self.__init__(state)
        
    def __reversed__(self):
        return reversed(self.items)

    def add(self, key):
        """
        Add `key` as an item to this OrderedSet, then return its index.

        If `key` is already in the OrderedSet, return the index it already
        had.
        """
        if key not in self.indices:
            self.indices[key] = len(self.items)
            self.items.append(key)
        return self.indices[key]
    
    append = add

    def extend(self, iterable):
        """ Add a collection of items to the set. """
        for item in iterable: self.add(item)
    
    __iadd__ = extend

    merge = set.union
    
    def discard(self, key):
        """Discard an item from the Categorical Set."""
        raise NotImplementedError(
            "Cannot remove items from an existing OrderedSet"
        )


    def __iter__(self):
        return iter(self.items)

    def __eq__(self, other):
        """ The OrderedSets are equal if their items are equal.
       
        >>> from crab.data.categorical import OrderedSet
        >>> a = OrderedSet(['a', 'b'])
        >>> b = OrderedSet(['a'])
        >>> b.add('b')
        1
        >>> a == b
        True
        """
        if isinstance(other, OrderedSet):
            return len(self) == len(other) and list(self) == list(other)    
        return set(self) == set(other)

    def __ne__(self, other):
        return not self == other

