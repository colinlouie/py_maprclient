# Standard libraries.
import ctypes
import threading

# Third-party libraries.
# None

# Internal libraries.
from maprclient.maprclient import * # All functions are prefixed with "hb_".


# For table scans.
scan_mutex = threading.Lock()
scan_cv = threading.Condition(scan_mutex)
is_scan_done = False


@ctypes.CFUNCTYPE(None,             # void (return)
                  ctypes.c_int,     # int32_t err
                  ctypes.c_void_p,  # hb_client_t client
                  ctypes.c_void_p)  # void *extra
def client_disconnection_callback(err, client, extra):
    """
    static void
    client_disconnection_callback(
        int32_t err,
        hb_client_t client,
        void *extra
    )
    """
    pass

@ctypes.CFUNCTYPE(None,             # void (return)
                  ctypes.c_int,     # int32_t err
                  ctypes.c_void_p,  # hb_scanner_t scanner
                  ctypes.c_void_p,  # hb_result_t results[]
                  ctypes.c_size_t,  # size_t num_results
                  ctypes.c_void_p)  # void *extra
def scan_callback(err, scanner, results, num_results, extra):
    """
    void scan_callback(
        int32_t err,
        hb_scanner_t scanner,
        hb_result_t results[],
        size_t num_results,
        void *extra
    )
    """
    global is_scan_done
    global scan_cv
    global scan_mutex

    if num_results <= 0:
        hb_scanner_destroy(scanner, None, None)
        scan_mutex.acquire()
        is_scan_done = True
        scan_cv.notify()
        scan_mutex.release()
        return

    result_array = ctypes.cast(results, ctypes.POINTER(ctypes.c_void_p))
    for i in range(0, num_results):
        print_row(result_array[i])
        hb_result_destroy(result_array[i])

    hb_scanner_next(scanner, scan_callback, None)

def print_row(result):
    rowkey_buf = ctypes.c_char_p()
    rowkey_len = ctypes.c_size_t()
    hb_result_get_key(result, rowkey_buf, rowkey_len)

    rowkey = rowkey_buf.value[:rowkey_len.value]
    key = rowkey.split(b':', 1)[0]

    cell_count = ctypes.c_size_t()
    hb_result_get_cell_count(result, cell_count)

    cells = pp_hb_cell_t()

    hb_result_get_cells(result, cells, cell_count)

    for i in range(0, cell_count.value):
        family = cells[i][0].family[:cells[i][0].family_len].decode()
        qualifier = cells[i][0].qualifier[:cells[i][0].qualifier_len].decode()
        value = cells[i][0].value[:cells[i][0].value_len].decode()[0]
        ts = cells[i][0].ts

        print(f'{family}:{qualifier} ts:{ts} {value}')

def wait_for_scan():
    global scan_mutex
    global scan_cv

    scan_mutex.acquire()
    while not is_scan_done:
        scan_cv.wait()
    scan_mutex.release()

def main():
    # Reference: https://mapr.com/docs/61/MapR-DB/Sample-C-app-scanTable.html

    table_name = b'/<path.to>/<tablename>'
    num_versions = 1
    num_max_rows = 10000

    hb_connection_t = ctypes.c_void_p   # typedef void *hb_connection_t;
    hb_client_t = ctypes.c_void_p       # typedef void *hb_client_t;
    hb_scanner_t = ctypes.c_void_p      # typedef void *hb_scanner_t;

    connection = hb_connection_t(0)     # hb_connection_t connection = NULL;
    client = hb_client_t(0)             # hb_client_t client = NULL;
    scanner = hb_scanner_t(0)           # hb_scanner_t scanner = NULL;

    hb_connection_create(None, None, connection)
    hb_client_create(connection, client)
    hb_scanner_create(client, scanner)

    hb_scanner_set_table(scanner, table_name, len(table_name))
    hb_scanner_set_num_versions(scanner, num_versions)
    hb_scanner_set_num_max_rows(scanner, num_max_rows)

    hb_scanner_next(scanner, scan_callback, None)
    wait_for_scan()

    hb_client_destroy(client, client_disconnection_callback, None)
    hb_connection_destroy(connection)

if __name__ == '__main__':
    main()

# EOF
