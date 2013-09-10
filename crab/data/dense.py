#-*- coding: utf-8 -*-
import numpy as np

from array import DenseArray 
from categorical import OrderedSet, map_indices
from labels import LabeledMixin

class DenseVector(DenseArray, LabeledMixin):
    
    def __new__(cls, input_array, labels=None):
        if input_array is None:
            if labels is None:
                raise ValueError('input array with None values only makes sense when there are labels')
            input_array = np.zeros((len(labels),))
        elif np.isscalar(input_array):
            input_array = np.zeros((input_array,))

        ndarray = np.asarray(input_array)
        if ndarray.ndim != 1:
            raise ValueError('input is not a 1-D vector')
        
        obj = ndarray.view(cls)
        if labels is None:
            obj.labels = None
        elif isinstance(labels, OrderedSet):
            obj.labels = labels
        else:
            obj.labels = OrderedSet(labels)

        if labels is not None:
            assert len(labels) == len(ndarray), '%r != %r' % (len(labels), len(ndarray))
        return obj

    def __getitem__(self, indices):
        labels = map_indices(indices, self.all_labels())
        data = np.ndarray.__getitem__(self, indices)
        if len(labels) == 1:
            return DenseVector(data, labels[0])
        else:
            return data

    def __repr__(self):
        return 'DenseVector(length %d, %s)' % (self.shape[0], self)

    def __array_finalize__(self, obj):
        if obj is None: return
        self.labels = getattr(obj, 'labels', None)

    def __unicode__(self):
        return np.ndarray.__str__(self)

    def __str__(self):
        return unicode(self).encode('utf-8')

