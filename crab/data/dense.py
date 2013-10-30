#-*- coding: utf-8 -*-
import numpy as np

from array import DenseArray 
from categorical import OrderedSet, map_indices
from labels import LabeledVectorMixin, LabeledMatrixMixin

EPSILON = 1e-30


class DenseVector(DenseArray, LabeledVectorMixin):
    __array_priority__ = 2.0    
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
        if self.labels is None:
            return np.ndarray.__str__(self)
        else:
            items = ['%s => %s' % (self.label(i), self[i]) for i in xrange(min(len(self), 10))]
            if len(self) > 10: 
                items.append('...')
                items.append('%s => %s' % (self.label(len(self)-1), self[len(self)-1]))

            return '[' + ','.join(items) + ']'


    def __str__(self):
        return unicode(self).encode('utf-8')

    def normalize(self):
        return self / (np.linalg.norm(self) + EPSILON)

    hat = normalize


class DenseMatrix(DenseArray, LabeledMatrixMixin):
    def __new__(cls, input_array=None, row_labels=None, col_labels=None):
        #add cases for compatibility
        if input_array is None:
            if row_labels is None or col_labels is None:
                raise ValueError('input_array=None only makes sense when there are row and column labels')
            input_array = np.zeros((len(row_labels), len(col_labels)))

        ndarray = np.asarray(input_array)
        if ndarray.ndim !=2:
            raise ValueError('Input is not a 2-D matrix')

        obj = ndarray.view(cls)
        if row_labels is None:
            obj.row_labels = None
        elif isinstance(row_labels, OrderedSet):
            obj.row_labels = OrderedSet(row_labels)
        else:
            #print 'converting rows to OrderedSet'
            obj.row_labels = OrderedSet(row_labels)

        if obj.row_labels is not None:
            assert len(obj.row_labels) == obj.shape[0]
 
        if col_labels is None:
            obj.col_labels = None
        elif isinstance(col_labels, OrderedSet):
            obj.col_labels = col_labels
        else:
            #print 'converting cols to OrderedSet'
            obj.col_labels = OrderedSet(col_labels)

        if obj.col_labels is not None:
            assert len(obj.col_labels) == obj.shape[1]

        return obj

    def __array_finalize__(self, obj):
        if obj is None: return
        self.row_labels = getattr(obj, 'row_labels', None)
        self.col_labels = getattr(obj, 'col_labels', None)

    def __repr__(self):
        return '<DenseMatrix (%d by %d)' % (self.shape[0], self.shape[1])
    
    def get_row(self, row_idx):
        return DenseVector(np.ndarray.__getitem__(self, row_idx), self.col_labels)

    def get_col(self, col_idx):
        return DenseVector(np.ndarray.__getitem__(self, (slice(None), col_idx)), self.row_labels)

    def row_named(self, label):
        '''
        Get the row with a given label as a vector.
        '''
        return self.get_row(self.row_index(label))

    def col_named(self, label):
        '''
        Get the column with a given label as vector
        '''
        return self.get_col(self.col_index(label))

    def entry_named(self, row_label, col_label):
        '''
        Get the entry with a given rown and a given label
        '''
        return np.ndarray.__getitem__(self, (self.row_index(row_label), self.col_index(col_label)))



    


    
        
