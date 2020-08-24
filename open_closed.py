'''
Open-Closed Principle:
    Software Entities (classes, functions, modules) should be open for extension
    but closed for modification.

    Adding bulk_download feature:
        We want to avoid making changes that require a change to underlying definitions.
        So, Rather than creating a new class BulkFTPClient, BulkSFTPClient for bulk requests
        instead we create functions that extend functionality. Defining new classes would
        require a change to the underlying definition of download/upload to return a
        different datatype than the FTPClient's and SFTPClient's upload/download functions.

'''

class FTPClient:
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


class SFTPClient:
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