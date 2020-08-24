'''
Liskov Substitution Principle:
    If an entity S is a subtype of Entity T, then objects of type T should be replaceable
    by entities of type S without breaking functionality.


    Adding support for FTPS:
        What should we do?
           1. We can add an upload_secure/download_secure function to our FTP Client
           2. We can add a secure flag as a parameter
           3. We can create a new FTPSClient that extends FTPClient

        We should create a new class. This way we maintain open-closed principle and
        we can also continue to substitute FTP SFTP or FTPS interchangeably based on
        our use case
'''

class FTPClient:
  def __init__(self, host, port):
    self._client = ftp(host, port)

  def upload(self, file):
      self._client.upload(file)

  def download(self, target):
      return self._client.download(target)



class FTPSClient(FTPClient):
    def __init__(self, host, port, username, password):
        self._client = ftps(host, port, user=username, password=password)