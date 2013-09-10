#-*- coding: utf-8 -*-

class LabeledMixin(object):
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

