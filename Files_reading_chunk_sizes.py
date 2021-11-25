# chunk sixes


with open('tropical-palm-tree.jpg', 'rb') as rf:
    with open('tropical-palm-tree_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            # to keep this from being an infinite loop
            rf_chunk = rf.read(chunk_size)
            