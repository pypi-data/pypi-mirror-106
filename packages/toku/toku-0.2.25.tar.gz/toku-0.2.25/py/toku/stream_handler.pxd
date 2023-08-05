from libc.stdint cimport uint32_t, uint8_t, uint16_t
cimport toku_c

cdef class TokuStreamHandler:
  cdef uint32_t seq
  cdef toku_c.toku_decode_buffer_t decode_buffer
  cdef toku_c.toku_buffer_t write_buffer
  cdef size_t write_buffer_position

  cdef inline uint32_t next_seq(self)
  cpdef uint32_t current_seq(self)

  cpdef uint32_t send_ping(self, uint8_t flags) except 0
  cpdef uint32_t send_pong(self, uint8_t flags, uint32_t seq) except 0
  cpdef uint32_t send_request(self, uint8_t flags, bytes data) except 0
  cpdef uint32_t send_push(self, uint8_t flags, bytes data) except 0
  cpdef uint32_t send_response(self, uint8_t flags, uint32_t seq, bytes data) except 0
  cpdef uint32_t send_hello(self, uint8_t flags, list supported_encodings, list supported_compressors) except 0
  cpdef uint32_t send_hello_ack(self, uint8_t flags, uint32_t ping_interval, bytes selected_encoding, bytes selected_compressor) except 0
  cpdef uint32_t send_error(self, uint8_t flags, uint16_t code, uint32_t seq, bytes data) except 0
  cpdef uint32_t send_goaway(self, uint8_t flags, uint16_t code, bytes reason) except 0

  cpdef size_t write_buffer_len(self)
  cpdef bytes write_buffer_get_bytes(self, size_t length, bint consume=?)
  cpdef size_t write_buffer_consume_bytes(self, size_t length)
  cpdef list on_bytes_received(self, bytes data)

  cdef object _consume_decode_buffer(self)
  cdef inline _reset_decode_buf(self)
  cdef _reset_or_compact_write_buf(self)
