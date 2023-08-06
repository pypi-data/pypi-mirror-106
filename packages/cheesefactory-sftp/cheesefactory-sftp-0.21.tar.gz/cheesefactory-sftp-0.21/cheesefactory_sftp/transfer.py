# cheesefactory-sftp/transfer.py

import glob
import logging
import os
import re
from pathlib import Path
from typing import List

from .exceptions import BadListValueError, EmptyListError
from .utilities import CfSftpUtilities

logger = logging.getLogger(__name__)


class CfSftpTransfer(CfSftpUtilities):
    """File transfer and logging attributes and methods shared by CfSftpGet() and CfSftpPut().

    Notes:
            CfSftp --> CfSftpGet ----> CfSftpTransfer --> CfSftpUtilities --> CfSftpConnection
                   |-> CfSftpPut ->|
    """
    def __init__(self):
        super().__init__()

        self.log = {}  # Metrics from last file transfer.
        self.logs = []  # Metrics from all file transfers performed during class instantiation.
        
        # Counters used for status messages and logging.
        self._new_file_count = 0
        self._new_dir_count = 0
        self._existing_file_count = 0
        self._existing_dir_count = 0
        self._regex_skip_count = 0

    #
    # PROTECTED METHODS
    #

    def _transfer(self, action: str = None, append_local: str = None, append_remote: str = None,
                  local_path: str = None, preserve_mtime: bool = True, remote_path: str = None,
                  remove_source: bool = False):
        """Download a single, remote file from the SFTP server to the local host.

        Args:
            action: GET or PUT
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            local_path: Local/destination path and filename.
            preserve_mtime: Keep modification time of source file.
            remote_path: Remote/source path and filename.
            remove_source: Remove the remote source file.

        Notes:
            Paramiko's get() already does a size match check between local and remote file.
        """
        if action not in ('GET', 'PUT'):
            raise ValueError("action != 'GET' or 'PUT'")
        if append_local is not None and not isinstance(append_local, str):
            raise ValueError('append_local != str type')
        if append_remote is not None and not isinstance(append_remote, str):
            raise ValueError('append_remote != str type')
        if not isinstance(local_path, str):
            raise ValueError('local_path != str type')
        if not isinstance(preserve_mtime, bool):
            raise ValueError('preserve_mtime != str type')
        if not isinstance(remote_path, str):
            raise ValueError('remote_path != str type')
        if not isinstance(remove_source, bool):
            raise ValueError('remove_source != bool type')

        self.log = {
            'action': action,
            'action_ok': False,
            'append_local': append_local,
            'append_remote': append_remote,
            'client': 'CfSftp',
            'local_path': local_path,
            'notes': None,
            'preserve_mtime': preserve_mtime,
            'preserve_mtime_ok': None,
            'remote_host': self.host,
            'remote_path': remote_path,
            'remove_source': remove_source,
            'remove_source_ok': None,
            'renamed_local_path': None,
            'renamed_remote_path': None,
            'size': None,
            'size_match': True,
            'size_match_ok': False,
            'status': None
        }

        try:
            self.log['notes'] = 'Stat source file.'
            if action == 'GET':
                source_file_stats = self.sftp.stat(remote_path)
            else:  # action == 'PUT'
                source_file_stats = os.stat(local_path)
            self.log['size'] = source_file_stats.st_size

            self.log['notes'] = 'Ensuring destination dir exists.'
            if action == 'GET':
                destination_dir = Path(local_path).parent
                destination_dir.mkdir(exist_ok=True, parents=True)
            else:  # action == 'PUT'
                destination_dir = str(Path(remote_path).parent)
                try:
                    self.sftp.stat(destination_dir)
                except IOError:  # If remote directory does not exist...
                    try:
                        self.sftp.mkdir(destination_dir)
                    except IOError as e:
                        raise IOError(f'Unable to create remote directory: {destination_dir} ({e})')

            new_local_path = ''
            if append_local is not None:
                self.log['notes'] = 'Building new local_path.'
                # Replace % with local_path file extension.
                append_local = append_local.replace('%', str(Path(local_path).suffix))
                new_local_path = local_path.replace(str(Path(local_path).suffix), append_local)
                self.log['renamed_local_path'] = new_local_path

            new_remote_path = ''
            if append_remote is not None:
                self.log['notes'] = 'Building new remote_path.'
                # Replace % with remote_path file extension.
                append_remote = append_remote.replace('%', str(Path(remote_path).suffix))
                new_remote_path = remote_path.replace(str(Path(remote_path).suffix), append_remote)
                self.log['renamed_remote_path'] = new_remote_path

            if action == 'GET':
                self.log['notes'] = 'Downloading file.'

                if append_local is not None:
                    local_path = new_local_path

                self.sftp.get(remotepath=remote_path, localpath=local_path)

                if append_remote is not None:
                    self.log['notes'] = 'Renaming remote path.'
                    self.rename(old_path=remote_path, new_path=new_remote_path)
                    remote_path = new_remote_path

            else:  # action == 'PUT'
                self.log['notes'] = 'Uploading file.'

                if append_remote is not None:
                    remote_path = new_remote_path

                self.sftp.put(remotepath=remote_path, localpath=local_path, confirm=True)  # confirm does filesize stat

                if append_local is not None:
                    self.log['notes'] = 'Renaming local path.'
                    Path(local_path).rename(new_local_path)
                    local_path = new_local_path

            self.log['action_ok'] = True
            self.log['size_match_ok'] = True  # TODO: Make sure parmioko does size match for both PUT and GET.

            if preserve_mtime is True:
                self.log['notes'] = 'Preserving mtime.'
                self.log['preserve_mtime_ok'] = False
                # Restamp the local file with the appropriate modification time.
                if action == 'GET':
                    os.utime(local_path, (source_file_stats.st_atime, source_file_stats.st_mtime))
                else:  # action == 'PUT'
                    local_path_times = (source_file_stats.st_atime, source_file_stats.st_mtime)
                    self.sftp.utime(remote_path, local_path_times)
                self.log['preserve_mtime_ok'] = True
                # TODO: Add preserve_mtime for PUT

            if remove_source is True:
                self.log['notes'] = 'Removing source.'
                self.log['remove_source_ok'] = False
                if action == 'GET':
                    self.remove_file(remote_path)
                else:  # action == 'PUT'
                    Path(local_path).unlink()
                self.log['remove_source_ok'] = True

        except (FileNotFoundError, IOError) as e:
            self.log['notes'] = f"{self.log['notes']}; {str(e)}"
            self.log['status'] = 'ERROR'
            raise
        except BadListValueError as e:
            logger.error(str(e))
            raise
        else:
            if preserve_mtime is True:
                self.log['notes'] = 'preserve_mtime not yet implemented for PUT'
            else:
                self.log['notes'] = ''
            self.log['status'] = 'OK'
        finally:
            self.logs.append(self.log)

    def _transfer_by_glob(self, action: str = None, append_local: str = None, append_remote: str = None,
                          flat_dir: bool = False, glob_filter: str = '*', base_dir: str = '.',
                          preserve_mtime: bool = True, recursive_search: bool = False,
                          source_dir: str = '.', remove_source: bool = False, ) -> List[str]:
        """Create a list of remote files to download based on glob, then download.

        Creates a recursive list of files and directories in remote_dir and filters by glob_filter.

        Args:
            action:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            base_dir: Local base directory for downloaded files. See flat_dir.
            flat_dir: Do not recreate directory structure in local_base_dir.
            glob_filter:
            preserve_mtime: Keep modification time of source file.
            recursive_search:
            remove_source: Remove the remote source file.
            source_dir:
        """
        if action == 'GET':
            file_list = self.find_files_by_glob(glob_filter=glob_filter, recursive_search=recursive_search,
                                                remote_dir=source_dir)
        else:  # action == 'PUT'
            file_list = glob.glob(glob_filter)

        if len(file_list) > 0:
            logger.debug(f'file_list after filter ({glob_filter}): {str(file_list)}')
            # Get the files
            transfer_list = self._transfer_by_list(
                action=action, append_local=append_local, append_remote=append_remote, flat_dir=flat_dir,
                base_dir=base_dir, preserve_mtime=preserve_mtime, file_list=file_list,
                remove_source=remove_source)
        else:
            raise EmptyListError(function_name='get_by_glob', variable_name='file_list')

        return transfer_list

    def _transfer_by_list(self, action: str = None, append_local: str = None, append_remote: str = None,
                          base_dir: str = '.', file_list: List[str] = None, flat_dir: bool = False,
                          preserve_mtime: bool = True, remove_source: bool = False) -> List[str]:
        """Download a list of files from the SFTP server to the local host.

        Args:
            action:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            base_dir: Destination base directory for transferred files. See flat_dir.
            file_list: Remote/source path and filename.
            flat_dir: Do not recreate directory structure in the destination's base_dir.
            preserve_mtime: Keep modification time of source file.
            file_list: Source path and filename.
            remove_source: Remove the source file.
        """
        if not isinstance(file_list, list):
            raise ValueError('remote_files != List[str] type')
        if not isinstance(base_dir, str):
            raise ValueError('local_base_dir != str type')
        if not isinstance(flat_dir, bool):
            raise ValueError('flat_dir != bool type')

        for file in file_list:
            if action == 'GET':
                remote_path = file
                if flat_dir is True:
                    local_path = str(Path(f'{base_dir}/{Path(file).name}'))
                else:
                    local_path = str(Path(f'{base_dir}/{file}'))
            else:  # action == 'PUT':
                local_path = file
                if flat_dir is True:
                    remote_path = str(Path(f'{base_dir}/{Path(file).name}'))
                else:
                    remote_path = str(Path(f'{base_dir}/{file}'))

            try:
                self._transfer(action=action, append_local=append_local, append_remote=append_remote,
                               remote_path=remote_path, local_path=local_path,
                               preserve_mtime=preserve_mtime, remove_source=remove_source)
            except FileExistsError as e:
                logger.warning(str(e))

        return file_list

    def _transfer_by_regex(self, action: str = None, append_local: str = None, append_remote: str = None,
                           flat_dir: bool = False, base_dir: str = '.', preserve_mtime: bool = True,
                           regex_filter: str = r'^', source_dir: str = '.', remove_source: bool = False) -> List[str]:
        """Create a list of remote files to download based on a regex, then download.

        Creates a recursive list of files and directories in remote_dir and filters using re.search().

        Args:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            flat_dir:
            base_dir:
            preserve_mtime: Keep modification time of source file.
            regex_filter:
            source_dir: Remote/source path and filename.
            remove_source:
        """
        if action == 'GET':
            file_list = self.find_files_by_regex(regex_filter=regex_filter, remote_dir=source_dir)

        else:  # action == 'PUT'
            try:
                regex_object = re.compile(regex_filter)
            except re.error as e:
                logger.debug(f'Bad regex ({regex_filter}): {str(e)}')
                raise ValueError(f'Bad regex pattern ({regex_filter}): {str(e)}')

            file_list = glob.glob(f'{source_dir}/*')

            # Identify items that do not match the regex
            hit_list = []  # Files to remove from list
            for file in file_list:
                result = regex_object.search(file)
                if result is None:
                    hit_list.append(file)

            # Remove the unmatched files from the file list
            for hit in hit_list:
                file_list.remove(hit)

        if len(file_list) > 0:
            logger.debug(f'remote_files after filter ({regex_filter}): {str(file_list)}')
            # Get the files
            transfer_list = self._transfer_by_list(
                action=action, append_local=append_local, append_remote=append_remote, flat_dir=flat_dir,
                base_dir=base_dir, preserve_mtime=preserve_mtime, file_list=file_list,
                remove_source=remove_source)
        else:
            raise EmptyListError(function_name='transfer_by_regex', variable_name='remote_files')

        return transfer_list
