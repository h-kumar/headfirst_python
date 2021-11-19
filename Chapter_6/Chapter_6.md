# Python Data Storage and Manipulation
## Processing data from Text File
- Python supports `open()`, `process()` and `close()` operations on a file.
- Open a file - `open('filename.txt','a')`
    - Open () - method to open a file
    - Arguments - (filename, a) where a = append mode.
- To append data to file.
    - `print('Sample Text',file=filename)`
- To close a file, use the close() method. Always remember to close the file after an operation.
    - `filename.close()`
- To print contents of a file.
    - ```python
        variable = open(filename)
        for lines in variable:
            print(lines)
        variable.close()
        ```