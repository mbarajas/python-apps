import gzip
import shutil

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt.gz'
    compress_file(input_file, output_file)
