'''
  Single Responsibility Principle:
      Do not write complex functions and classes that do a lot of things.

      Increase cohesion and decrease coupling. There should only be one reason
      to change.

      The Base File has many responsibilities:
          1. manage connections for FTP and SFTP
          2. Each method has to determine which protocol to work with

      Single Responsibility would encourage separate classes to handle each responsibility
'''


class FTPClient:
  def __init__(self, host, port):
    self._client = ftp(host, port)

  def upload(self, file):
      self._client.upload(file)

  def download(self, target):
      return self._client.download(target)


class SFTPClient:
  def __init__(self, host, user, password):
    self._client = sftp(host, user=user, password=password)

  def upload(self, file):
      with self._client.Connection() as sftp:
          sftp.put(file)

  def download(self, target):
      with self._client.Connection() as sftp:
          return sftp.get(target)