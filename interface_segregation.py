'''
Interface Segregation Principle:
    A client should not depend on functions it does not use


    Interface segregation principle is about making reasonable choices about how code will be
    interfaced with.

    Add feature for S3Client:
        S3 and FTP share similarities. S3 is not a type of FTP so inheriting from FTP is not appropriate
        Instead since they are both file transfer protocols they can be tied to an abstract base class.


'''

from abc import ABC
class FileTransferClient(ABC):
    def upload(self, file):
        pass

    def download(self, target):
        pass


class BulkFileTransferClient(ABC):
    def upload_bulk(self, files):
        pass

    def download_bulk(self, targets):
        pass



class FTPClient(FileTransferClient,BulkFileTransferClient):
    def __init__(self, host, port):
        self._client = ftp(host, port)

    def upload(self, file):
        self._client.upload(file)

    def upload_bulk(self, files):
        for file in files:
            self.upload(file)

    def download(self, target):
        return self._client.download(target)

    def download_bulk(self, targets):
        files = []
        for target in targets:
            files.append(self.download(target))

        return files


class FTPSClient(FTPClient):
    def __init__(self, host, port, username, password):
        super().__init__(host, port, username,password)
        self._client = ftps(host, port, user=username, password=password)


class SFTPClient(FileTransferClient,BulkFileTransferClient):
    def __init__(self, host, user, password):
        self._client = sftp(host, user=user, password=password)

    def upload(self, file):
        with self._client.Connection() as sftp:
            sftp.put(file)

    def upload_bulk(self, files):
        for file in files:
            self.upload(file)

    def download(self, target):
        with self._client.Connection() as sftp:
            return sftp.get(target)

    def download_bulk(self, targets):
        files = []
        for target in targets:
            files.append(self.download(target))

        return files


class S3Client(FileTransferClient):
    def __init__(self, host, port):
        self._client = s3(host, port)

    def upload(self, file):
        self._client.upload(file)

    def download(self, target):
        return self._client.download(target)

