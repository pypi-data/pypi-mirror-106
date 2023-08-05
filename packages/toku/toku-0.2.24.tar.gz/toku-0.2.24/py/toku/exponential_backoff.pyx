import random

cdef class Backoff:
  def __init__(self, min_delay=0.5, max_delay=None, jitter=True):
    self._min = min_delay
    if max_delay is None:
      max_delay = min_delay * 10
    
    self._max = max_delay
    self._jitter = jitter

    self._current = self._min
    self._fails = 0
  
  cdef int fails(self):
    return self._fails
  
  cdef float current(self):
    return self._current

  cdef void succeed(self):
    self._fails = 0
    self._current = self._min
  
  cdef float fail(self):
    self._fails += 1
    delay = self._current * 2
    if self._jitter:
      delay *= random.random()
    
    self._current += delay

    if self._max:
      self._current = min(self._current, self._max)

    self._current = round(self._current, 2)
    return self._current
