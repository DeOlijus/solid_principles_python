'''
    Base Example: Changes will be made using the code below as a base to demonstrate each principle
'''

class FTPClient:
  def __init__(self, **kwargs):
    self._ftp_client = ftp(kwargs['host'], kwargs['port'])
    self._sftp_client = sftp(kwargs['sftp_host'], kwargs['user'], kwargs['pw'])

  def upload(self, file, **kwargs):
    is_sftp = kwargs['sftp']
    if is_sftp:
      with self._sftp_client.Connection() as sftp:
        sftp.put(file)
    else:
      self._ftp_client.upload(file)

  def download(self, target, **kwargs):
    is_sftp = kwargs['sftp']
    if is_sftp:
      with self._sftp_client.Connection() as sftp:
        return sftp.get(target)
    else:
      return self._ftp_client.download(target)