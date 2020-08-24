'''
Dependency Inversion Principle:
    High level modules should not depend on Low level modules.
    High level modules should depend on abstractions.
    Abstractions should not depend on details.
    Details should depend on Abstractions.


    Code should be at a point where it is independent from the details. Example: The file transfer protocol
    implementation used is now independent from any business logic.

    High level modules do not depend on the low level FTPClient SFTPClient or S3Client but now depend on the
    abstract form of FileTransferClient. (dependent on moving file not on the details of how they are moved)

    Abstraction (FileTransferClient) does not depend on protocol specific details.
    Protocol specific details depend on how the abstraction will use them (uploaded or downloaded)


'''


def exchange(client, to_upload, to_download):
    client.upload(to_upload)
    return client.download(to_download)

if __name__ == '__main__':
    ftp = FTPClient('ftp.host.com')
    sftp = FTPSClient('sftp.host.com', 22)
    ftps = SFTPClient('ftps.host.com', 990, 'ftps_user', 'password123!')
    s3 = S3Client('ftp.host.com')

    for client in [ftp, sftp, ftps, s3, scp]:
        exchange(client, b'Hello', 'hello_world.txt')