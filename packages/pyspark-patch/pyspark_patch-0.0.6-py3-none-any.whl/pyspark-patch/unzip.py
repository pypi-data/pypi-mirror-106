import os
import argparse
import pyzipper


def unzip(file, dest, password):
    password = password.encode()
    if not os.path.exists(dest):
        os.makedirs(dest, exist_ok=True)
    with pyzipper.AESZipFile(file) as zf:
        zf.setpassword(password)
        for finfo in zf.infolist():
            filename = finfo.filename
            path = os.path.join(dest, filename)
            with open(path, 'wb') as f:
                f.write(zf.read(filename))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-F', help='zipped file')
    parser.add_argument('--dest', '-D', help='path to extraction')
    parser.add_argument('--password', '-P', help='password')
    args = parser.parse_args()

    unzip(file=args.file, dest=args.dest, password=args.password)
