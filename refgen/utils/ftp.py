from ftplib import FTP
import json
import math

def download(host, filename, proc_tag = None):
    """download a file on ftp server to the local in binary

    input:
        host        : (str) server host
        filename    : (str) path of target file on server"""

    ftp             = FTP(host)
    ftp.encoding    = 'utf-8'
    ftp.login()

    if proc_tag is not None:
        # callback function fot retr
        def updated_process(block, args):
            args['content']     += block
            args['curr_size']   += len(block)

            # update json file for each 10%
            perc = args['curr_size'] / args['total_size']
            if perc >= args['curr_thres']:
                args['curr_thres'] = math.ceil(perc * 10) / 10
                process = json.load(open(args['proc_tag'], 'r'))
                process['curr_size'] = args['curr_size']
                process['curr_perc'] = perc
                json.dump(process, open(args['proc_tag'], 'w'))

        callback_args   = {
            'content'       : b'',
            'total_size'    : ftp.size(filename),
            'curr_size'     : 0,
            'curr_thres'    : 0.1,
            'proc_tag'      : proc_tag}
        ftp.retrbinary(
            cmd         = 'RETR ' + filename,
            callback    = lambda block: updated_process(block, callback_args),
            blocksize   = 8192)
        content = callback_args['content']
    else:
        content = []
        ftp.retrbinary(
            cmd         = 'RETR ' + filename,
            callback    = content.append,
            blocksize   = 8192)
        content = b''.join(content)
    return content