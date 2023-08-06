from stdinutils import on_line, get_cmd, execute_per_line_seg_with_delim

if __name__ == '__main__':
    on_line(execute_per_line_seg_with_delim, get_cmd())
