#-*- coding: utf-8 -*-

class LabeledVectorMixin(object):
    """Mixin class for all labeled vectors in crab."""

    def label(self, idx):
        """Get the label of the entry at a given numerical index """
        if self.labels is None: 
            return idx
        else:
            return self.labels[idx]
    def index(self, label):
        """Get the numeric index for the entry with a given label """
        return self.labels.index(label)

    def entry_named(self, label):
        """Get the value with a given label."""
        return self[self.index(label)]

    def all_labels(self):
        """
        Returns an one-element list containing `self.labels`.

        This is useful when mapping lists of indices one-to-one
        with lists of labels.
        """
        return [self.labels]
    
    def same_label_as(self, other):
        """
        Check if this vector has the same coordinate labels as another vector.
        """

        return (self.shape[0] == other.shape[0] and 
                    self.labels == other.labels)

    def unlabeled(self):
        """
        Get a copy of this vector with no labels
        """
        return self.__class__(self, None)


class LabeledMatrixMixin(object):
    """Mixin class for all labeled matrices in crab."""

    def row_label(self, idx):
        """
        Get the label of the row at a given numeric index.
        """
        if self.row_labels is None: 
            return idx
        
        return self.row_labels[idx]

    def col_label(self, idx):
        """
        Get the label of the column at a given numeric index.
        """
        if self.col_labels is None:
            return idx
        
        return self.col_labels[idx]
    
    def row_index(self, label):
        """
        Get the numeric index for the row with a given label.
        """
        if self.row_labels is None: 
            return label
        
        return self.row_labels.index(label)

    def col_index(self, label):
        """
        Get the numeric index for the column with a given label.
        """
        if self.col_labels is None:
            return label
        
        return self.col_labels.index(label)

    def row_named(self, label):
        """
        Get the row with a given label as a vector.
        """
        return self[self.row_index(label)]

    def col_named(self, label):
        """
        Get the column with a given label as a vector.
        """
        return self[:, self.col_index(label)]
    
    def entry_named(self, row_label, col_label):
        """
        Get the entry with a given row and column label.
        """
        return self[self.row_index(row_label), self.col_index(col_label)]

    def set_entry_named(self, row_label, col_label, value):
        """
        Set a new value in the entry with a given rown and column label.
        """
        self[self.row_index(row_label), self.col_index(col_label)] = value

    set = set_entry_named

    def same_row_labels_as(self, other):
        return (self.shape[0] == other.shape[0] and self.row_labels == getattr(other, 'row_labels', None))

    def same_col_labels_as(self, other):
        return (self.shape[1] == other.shape[1] and self.col_labels == getattr(other, 'col_labels', None))

    def same_labels_as(self, other):
        """
        Does this matrix have the same coordinate labels as another matrix ?
        """
        return self.same_row_labels_as(other) and self.same_col_labels_as(other)

    def all_labels(self):
        """
        Returns the two-element list of `[self.row_labels, self.col_labels]`.

        This is useful when mapping lists of indices one-to-one with lists of
        labels.
        """
        return [self.row_labels, self.col_labels]

    def unlabeled(self):
        """
        Get a copy of this matrix with no labels.
        """
        return self.__class__(self, None, None)

