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
            return u'%s([%r...%r])' % (self.__class__.__name__, self[0], self[len(self)-1])

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

    def merge(self, other):
        """
        Returns a new OrderedSet that merges this with another. 
        The indices from this OrderedSet will remain the same, and this
        method will return a mapping of the news indices for the other
        OrderedSet.

        Returns a tuple of `merged`, which is the combined OrderedSet, and
        `indices`, a list the length of `other` giving the new index for each
        of its entries.

        >>> from crab.data.categorical import OrderedSet
        >>> set1 = OrderedSet(['red', 'orange', 'yellow', 'green', 'blue'])
        >>> set2 = OrderedSet(['cyan', 'magenta', 'yellow'])
        >>> merged, indices = set1.merge(set2)
        >>> for item in merged:
        ...     print item,
        red orange yellow green blue cyan magenta
        >>> print indices
        [5, 6, 2]
        """
        merged = self.copy()
        indices = [merged.add(item) for item in other]
        return merged, indices

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


def map_indices(indices, indexables):
    #Check if it is an integer
    if isinstance(indices, int): return indexables[1:]




    # Check a few common cases first
    if isinstance(indices, int): return indexables[1:]
    # TODO: check more.
    
    # Make indices into a list
    if isinstance(indices, tuple):
        indices = list(indices)
    else:
        indices = [indices]
    indexables = list(indexables)

    num_axes_in_data = len(indexables)
    num_axes_known = len(indices)
    for index in indices:
        # .count doesn't work over things that might be NumPy arrays
        if index is None or index is Ellipsis:
            num_axes_known -= 1

    if num_axes_known > num_axes_in_data:
        raise IndexError("Too many indices")

    # Expand ellipses... from right to left, it turns out.
    for i in reversed(xrange(len(indices))):
        if indices[i] is Ellipsis:
            indices[i:i+1] = [ALL] * (num_axes_in_data - num_axes_known)
            num_axes_known = num_axes_in_data

    while num_axes_known < num_axes_in_data:
        indices.append(ALL)
        num_axes_known += 1

    results = []
    which_indexable = 0
    # Now step through the axes and get stuff
    for index in indices:
        if index is newaxis:
            results.append(None)
        else:
            indexable = indexables[which_indexable]
            if hasattr(index, '__index__') and not hasattr(index, 'shape'):
                # simple index: drop this result
                pass
            elif indexable is None:
                results.append(None)
            else:
                results.append(indexable[index])
            which_indexable += 1
    return results



