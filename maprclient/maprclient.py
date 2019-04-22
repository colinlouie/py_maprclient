# Standard libraries.
import ctypes

# Third-party libraries.
# None

# Internal libraries.
# None

dll = ctypes.CDLL('/opt/mapr/lib/libMapRClient.so')

# typedef struct hb_cell_type {
class hb_cell_t(ctypes.Structure):
    _fields_ = [
        # row key
        ('row', ctypes.c_char_p),           # byte_t *row;
        ('row_len', ctypes.c_size_t),       # size_t  row_len;

        # column family
        ('family', ctypes.c_char_p),        # byte_t *family;
        ('family_len', ctypes.c_size_t),    # size_t  family_len;

        # column qualifier
        ('qualifier', ctypes.c_char_p),     # byte_t *qualifier;
        ('qualifier_len', ctypes.c_size_t), # size_t  qualifier_len;

        # column value
        ('value', ctypes.c_char_p),         # byte_t *value;
        ('value_len', ctypes.c_size_t),     # size_t  value_len;

        # timestamp
        ('ts', ctypes.c_longlong),          # int64_t ts;

        # For internal use, applications should not set or alter this variable.
        ('flags_', ctypes.c_longlong),      # int64_t  flags_;
        ('private_', ctypes.c_void_p),      # void    *private_;
    ]
# } hb_cell_t;

# hb_cell_t *p_hb_cell_t;
p_hb_cell_t = ctypes.POINTER(hb_cell_t)

# hb_cell_t **pp_hb_cell_t;
pp_hb_cell_t = ctypes.POINTER(p_hb_cell_t)

def hb_client_create(connection, client_ptr):
    """
    HBASE_API int32_t
    hb_client_create(
        hb_connection_t connection,
        hb_client_t *client_ptr
    )
    """
    _hb_client_create = dll.hb_client_create
    _hb_client_create.restype = ctypes.c_int
    _hb_client_create.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
    return _hb_client_create(connection, ctypes.byref(client_ptr))

def hb_client_destroy(client, callback, extra):
    """
    HBASE_API int32_t
    hb_client_destroy(
        hb_client_t client,
        hb_client_disconnection_cb cb,
        void *extra
    )
    """
    _hb_client_destroy = dll.hb_client_destroy
    _hb_client_destroy.restype = ctypes.c_int
    _hb_client_destroy.argtypes = [ctypes.c_void_p,
                                   ctypes.c_void_p,
                                   ctypes.c_void_p]
    return _hb_client_destroy(client, callback, extra)

def hb_connection_create(zk_quorum, zk_root, connection_ptr):
    """
    HBASE_API int32_t
    hb_connection_create(
        const char *zk_quorum,
        const char *zk_root,
        hb_connection_t *connection_ptr
    )
    """
    _hb_connection_create = dll.hb_connection_create
    _hb_connection_create.restype = ctypes.c_int
    _hb_connection_create.argtypes = [ctypes.c_void_p,
                                      ctypes.c_void_p,
                                      ctypes.c_void_p]
    return _hb_connection_create(zk_quorum,
                                 zk_root,
                                 ctypes.byref(connection_ptr))

def hb_connection_destroy(connection):
    """
    HBASE_API int32_t
    hb_connection_destroy(hb_connection_t connection)
    """
    _hb_connection_destroy = dll.hb_connection_destroy
    _hb_connection_destroy.restype = ctypes.c_int
    _hb_connection_destroy.argtypes = [ctypes.c_void_p]
    return _hb_connection_destroy(connection)

def hb_result_get_cell_count(result, cell_count_ptr):
    """
    HBASE_API int32_t
    hb_result_get_cell_count(
        const hb_result_t result,
        size_t *cell_count_ptr
    )
    """
    _hb_result_get_cell_count = dll.hb_result_get_cell_count
    _hb_result_get_cell_count.restype = ctypes.c_int
    _hb_result_get_cell_count.argtypes = [ctypes.c_void_p,
                                          ctypes.c_void_p]
    return _hb_result_get_cell_count(result, ctypes.byref(cell_count_ptr))

def hb_result_get_cells(result, cells_ptr, num_cells_ptr):
    """
    HBASE_API int32_t
    hb_result_get_cells(
        const hb_result_t result,
        const hb_cell_t ***cells_ptr,
        size_t *num_cells_ptr
    )
    """
    _hb_result_get_cells = dll.hb_result_get_cells
    _hb_result_get_cells.restype = ctypes.c_int
    _hb_result_get_cells.argtypes = [ctypes.c_void_p,
                                     ctypes.c_void_p,
                                     ctypes.c_void_p]
    return _hb_result_get_cells(result,
                                ctypes.byref(cells_ptr),
                                ctypes.byref(num_cells_ptr))

def hb_result_get_key(result, key_ptr, key_length_ptr):
    """
    HBASE_API int32_t
    hb_result_get_key(
        const hb_result_t result,
        const byte_t **key_ptr,
        size_t *key_length_ptr
    )
    """
    _hb_result_get_key = dll.hb_result_get_key
    _hb_result_get_key.restype = ctypes.c_int
    _hb_result_get_key.argtypes = [ctypes.c_void_p,
                                   ctypes.c_void_p,
                                   ctypes.c_void_p]
    return _hb_result_get_key(result,
                              ctypes.byref(key_ptr),
                              ctypes.byref(key_length_ptr))

def hb_result_destroy(result):
    """
    HBASE_API int32_t
    hb_result_destroy(hb_result_t result)
    """
    _hb_result_destroy = dll.hb_result_destroy
    _hb_result_destroy.restype = ctypes.c_int
    _hb_result_destroy.argtypes = [ctypes.c_void_p]
    return _hb_result_destroy(result)

def hb_scanner_create(client, scanner_ptr):
    """
    HBASE_API int32_t
    hb_scanner_create(
        hb_client_t client,
        hb_scanner_t *scanner_ptr
    )
    """
    _hb_scanner_create = dll.hb_scanner_create
    _hb_scanner_create.restype = ctypes.c_int
    _hb_scanner_create.argtypes = [ctypes.c_void_p,
                                   ctypes.c_void_p]
    return _hb_scanner_create(client, ctypes.byref(scanner_ptr))

def hb_scanner_destroy(scanner, callback, extra):
    """
    HBASE_API int32_t
    hb_scanner_destroy(
        hb_scanner_t scanner,
        hb_scanner_destroy_cb cb,
        void *extra
    )
    """
    _hb_scanner_destroy = dll.hb_scanner_destroy
    _hb_scanner_destroy.restype = ctypes.c_int
    _hb_scanner_destroy.argtypes = [ctypes.c_void_p,
                                    ctypes.c_void_p,
                                    ctypes.c_void_p]
    return _hb_scanner_destroy(scanner, callback, extra)

def hb_scanner_next(scanner, callback, extra):
    """
    HBASE_API int32_t
    hb_scanner_next(
        hb_scanner_t scanner,
        hb_scanner_cb cb,
        void *extra
    )
    """
    _hb_scanner_next = dll.hb_scanner_next
    _hb_scanner_next.restype = ctypes.c_int
    _hb_scanner_next.argtypes = [ctypes.c_void_p,
                                 ctypes.c_void_p,
                                 ctypes.c_void_p]
    return _hb_scanner_next(scanner, callback, extra)

def hb_scanner_set_num_max_rows(scanner, cache_size):
    """
    HBASE_API int32_t
    hb_scanner_set_num_max_rows(
        hb_scanner_t scanner,
        const size_t cache_size
    )
    """
    _hb_scanner_set_num_max_rows = dll.hb_scanner_set_num_max_rows
    _hb_scanner_set_num_max_rows.restype = ctypes.c_int
    _hb_scanner_set_num_max_rows.argtypes = [ctypes.c_void_p,
                                             ctypes.c_size_t]
    return _hb_scanner_set_num_max_rows(scanner, cache_size)

def hb_scanner_set_num_versions(scanner, num_versions):
    """
    HBASE_API int32_t
    hb_scanner_set_num_versions(
        hb_scanner_t scanner,
        const int8_t num_versions
    )
    """
    _hb_scanner_set_num_versions = dll.hb_scanner_set_num_versions
    _hb_scanner_set_num_versions.restype = ctypes.c_int
    _hb_scanner_set_num_versions.argtypes = [ctypes.c_void_p,
                                             ctypes.c_int8]
    return _hb_scanner_set_num_versions(scanner, num_versions)

def hb_scanner_set_table(scanner, table, table_length):
    """
    HBASE_API int32_t
    hb_scanner_set_table(
        hb_scanner_t scanner,
        const char *table,
        const size_t table_length
    )
    """
    _hb_scanner_set_table = dll.hb_scanner_set_table
    _hb_scanner_set_table.restype = ctypes.c_int
    _hb_scanner_set_table.argtypes = [ctypes.c_void_p,
                                      ctypes.c_char_p,
                                      ctypes.c_size_t]
    return _hb_scanner_set_table(scanner, table, table_length)

# EOF
