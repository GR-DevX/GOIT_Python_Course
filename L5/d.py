from shutil import make_archive, unpack_archive
make_archive('arch1','gztar',root_dir='.')
unpack_archive('arch1',extract_dir='1')