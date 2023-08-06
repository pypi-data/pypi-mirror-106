# cheesefactory-sftp/put.py

import logging
from typing import List
from .transfer import CfSftpTransfer

logger = logging.getLogger(__name__)


class CfSftpPut(CfSftpTransfer):
    """GET-related attributes and methods.

    Notes:
        CfSftp --> CfSftpGet ----> CfSftpTransfer --> CfSftpUtilities --> CfSftpConnection
               |-> CfSftpPut ->|
    """
    def __init__(self):
        super().__init__()

    #
    # PUBLIC METHODS
    #

    def put(self, append_local: str = None, append_remote: str = None, remote_path: str = None,
            local_path: str = None, preserve_mtime: bool = True,
            remove_source: bool = False):
        """Upload a single, remote file from the local host to the SFTP server.

        Args:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            remote_path: Remote/source path and filename.
            local_path: Local/destination path and filename.
            preserve_mtime: Keep modification time of source file.
            remove_source: Remove the remote source file.
        """
        self._transfer(
            action='PUT', remote_path=remote_path, local_path=local_path, preserve_mtime=preserve_mtime,
            remove_source=remove_source
        )

    def put_by_glob(self, append_local: str = None, append_remote: str = None, glob_filter: str = '*', recursive_search: bool = False, remote_dir: str = '.',
                    local_base_dir: str = '.', preserve_mtime: bool = True, remove_source: bool = False,
                    flat_dir: bool = False) -> List[str]:
        """Create a list of remote files to upload based on glob, then upload.

        Creates a recursive list of files and directories in remote_dir and filters by glob_filter.

        Args:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            glob_filter:
            recursive_search:
            remote_dir:
            local_base_dir: Local base directory for downloaded files. See flat_dir.
            preserve_mtime: Keep modification time of source file.
            remove_source: Remove the remote source file.
            flat_dir: Do not recreate directory structure in local_base_dir.
        """
        files = self._transfer_by_glob(
            action='PUT', glob_filter=glob_filter, recursive_search=recursive_search, remote_dir=remote_dir,
            local_base_dir=local_base_dir, preserve_mtime=preserve_mtime, remove_source=remove_source,
            flat_dir=flat_dir
        )
        return files

    def put_by_list(self, append_local: str = None, append_remote: str = None, remote_files: List[str] = None, local_base_dir: str = '.',
                    preserve_mtime: bool = True, remove_source: bool = False, flat_dir: bool = False) -> List[str]:
        """Upload a list of files from the local host to the SFTP server.

        Args:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            remote_files: Remote/source path and filename.
            local_base_dir: Local base directory for downloaded files. See flat_dir.
            preserve_mtime: Keep modification time of source file.
            remove_source: Remove the remote source file.
            flat_dir: Do not recreate directory structure in local_base_dir.
        """
        files = self._transfer_by_list(
            action='PUT', remote_files=remote_files, local_base_dir=local_base_dir, preserve_mtime=preserve_mtime,
            remove_source=remove_source, flat_dir=flat_dir
        )
        return files

    def put_files_by_regex(self, append_local: str = None, append_remote: str = None, regex_filter: str = r'^',
                           remote_dir: str = '.', local_base_dir: str = '.',
                           preserve_mtime: bool = True, remove_source: bool = False,
                           flat_dir: bool = False) -> List[str]:
        """Create a list of remote files to upload based on a regex, then upload.

        Creates a recursive list of files and directories in remote_dir and filters using re.search().

        Args:
            append_local: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If no
                          extension exists, then string is appended to end of filename.
            append_remote: String to replace extension (Path.suffix) with. Use '%' to represent original extension. If
                           no extension exists, then string is appended to end of filename.
            regex_filter:
            remote_dir: Remote/source path and filename.
            local_base_dir:
            preserve_mtime: Keep modification time of source file.
            remove_source:
            flat_dir:
        """
        files = self._transfer_by_regex(
            action='PUT', regex_filter=regex_filter, remote_dir=remote_dir,
            local_base_dir=local_base_dir, preserve_mtime=preserve_mtime, remove_source=remove_source, flat_dir=flat_dir
        )
        return files
