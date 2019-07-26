class Range:
    """A class that mimics the built-in range class """

    def __init__(self, start, stop=None, step=1):
        """ Initialize a Range instance
            Semantics is similar to built-in range class
        """

        if step == 0:
            raise ValueError("step can not be zero")
        if stop is None:      # special case of range
            start, stop = 0, start  # should be treated as if range(0, n)

        # calculate the effective length at once
        self._length = max(0, (stop - start + step -1)//step)

        # need knowledge of start and step (but no stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """ Return number of entries in the range."""
        return self._length

    def __getitem__(self, item):
        """Return entry at index k (using standard interpretation of negative)"""
        if item < 0:
            item += len(self)             # attempt to convert negative index

        if not 0 <= item < self._length:
            raise IndexError('index out of range')

        return self._start + item*self._step


