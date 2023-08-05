from ssl import get_server_certificate
from OpenSSL import crypto
from threading import Thread
from queue import Queue
from datetime import datetime
from socket import setdefaulttimeout
from argparse import ArgumentParser, FileType
from codecs import decode

__version__ = '1.0'


def worker(queue, callback):
    while True:
        domain = queue.get()
        if domain is None:
            break
        try:
            cert = get_server_certificate((domain, 443))
        except Exception as exc:
            result = exc
        else:
            x509 = crypto.load_certificate(crypto.FILETYPE_PEM, cert)
            result = datetime.strptime(x509.get_notAfter().decode('ascii'), '%Y%m%d%H%M%SZ')
        callback(domain, result)


def formatter(separator, date_format):

    def inner(domain, data):
        if isinstance(data, datetime):
            notafter = data.isoformat() if date_format == 'iso' else data.strftime(date_format)
            extra = ''
        else:
            notafter = ''
            extra = str(data)
        return separator.join((domain, notafter, extra))

    return inner


def unescape(value):
    return decode(str(value), 'unicode_escape')


def main():
    parser = ArgumentParser(description='Get ssl certificates expiration dates.'
                            ' Outputs a CSV formatted list of domains with dates.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-w', '--workers', default=8, type=int, help='Workers (default 8)')
    parser.add_argument('-t', '--timeout', default=1.0, type=float, help='Timeout (default 1.0)')
    parser.add_argument('-s', '--separator', default=';', type=unescape, help='Field separator (default ;)')
    parser.add_argument('-f', '--format', default='iso', type=str, help='Datetime format (default iso)')
    parser.add_argument('inputfile', type=FileType('rt'), help='Input file or - for stdin')
    args = parser.parse_args()
    setdefaulttimeout(args.timeout)
    formatr = formatter(args.separator, args.format)
    queue = Queue()
    for i in range(args.workers):
        Thread(target=worker, args=(queue, lambda *a: print(formatr(*a)))).start()
    try:
        for line in args.inputfile:
            domain = line.strip()
            if not domain or domain.startswith('#'):
                continue
            queue.put(domain)
    except KeyboardInterrupt:
        pass
    for i in range(args.workers):
        queue.put(None)


if __name__ == '__main__':
    main()
