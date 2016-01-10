# encoding: utf-8
# module posix
# from (built-in)
# by generator 1.135
"""
This module provides access to operating system functionality that is
standardized by the C Standard and the POSIX standard (a thinly
disguised Unix interface).  Refer to the library manual and
corresponding Unix manual entries for more information on calls.
"""
# no imports

# Variables with simple values

CLD_CONTINUED = 6
CLD_DUMPED = 3
CLD_EXITED = 1
CLD_TRAPPED = 4

EX_CANTCREAT = 73
EX_CONFIG = 78
EX_DATAERR = 65
EX_IOERR = 74
EX_NOHOST = 68
EX_NOINPUT = 66
EX_NOPERM = 77
EX_NOUSER = 67
EX_OK = 0
EX_OSERR = 71
EX_OSFILE = 72
EX_PROTOCOL = 76
EX_SOFTWARE = 70
EX_TEMPFAIL = 75
EX_UNAVAILABLE = 69
EX_USAGE = 64

F_LOCK = 1
F_OK = 0
F_TEST = 3
F_TLOCK = 2
F_ULOCK = 0

NGROUPS_MAX = 65536

O_ACCMODE = 3
O_APPEND = 1024
O_ASYNC = 8192
O_CLOEXEC = 524288
O_CREAT = 64
O_DIRECT = 16384
O_DIRECTORY = 65536
O_DSYNC = 4096
O_EXCL = 128
O_LARGEFILE = 0
O_NDELAY = 2048
O_NOATIME = 262144
O_NOCTTY = 256
O_NOFOLLOW = 131072
O_NONBLOCK = 2048
O_PATH = 2097152
O_RDONLY = 0
O_RDWR = 2
O_RSYNC = 1052672
O_SYNC = 1052672
O_TMPFILE = 4259840
O_TRUNC = 512
O_WRONLY = 1

POSIX_FADV_DONTNEED = 4
POSIX_FADV_NOREUSE = 5
POSIX_FADV_NORMAL = 0
POSIX_FADV_RANDOM = 1
POSIX_FADV_SEQUENTIAL = 2
POSIX_FADV_WILLNEED = 3

PRIO_PGRP = 1
PRIO_PROCESS = 0
PRIO_USER = 2

P_ALL = 0
P_PGID = 2
P_PID = 1

RTLD_DEEPBIND = 8
RTLD_GLOBAL = 256
RTLD_LAZY = 1
RTLD_LOCAL = 0
RTLD_NODELETE = 4096
RTLD_NOLOAD = 4
RTLD_NOW = 2

R_OK = 4

SCHED_BATCH = 3
SCHED_FIFO = 1
SCHED_IDLE = 5
SCHED_OTHER = 0

SCHED_RESET_ON_FORK = 1073741824

SCHED_RR = 2

SEEK_DATA = 3
SEEK_HOLE = 4

ST_APPEND = 256
ST_MANDLOCK = 64
ST_NOATIME = 1024
ST_NODEV = 4
ST_NODIRATIME = 2048
ST_NOEXEC = 8
ST_NOSUID = 2
ST_RDONLY = 1
ST_RELATIME = 4096
ST_SYNCHRONOUS = 16
ST_WRITE = 128

TMP_MAX = 238328

WCONTINUED = 8

WEXITED = 4

WNOHANG = 1
WNOWAIT = 16777216

WSTOPPED = 2

WUNTRACED = 2

W_OK = 2

XATTR_CREATE = 1
XATTR_REPLACE = 2

XATTR_SIZE_MAX = 65536

X_OK = 1

# functions

def abort(): # real signature unknown; restored from __doc__
    """
    abort() -> does not return!
    
    Abort the interpreter immediately.  This 'dumps core' or otherwise fails
    in the hardest way possible on the hosting operating system.
    """
    pass

def access(*args, **kwargs): # real signature unknown
    """
    Use the real uid/gid to test for access to a path.
    
      path
        Path to be tested; can be string, bytes, or open-file-descriptor int.
      mode
        Operating-system mode bitfield.  Can be F_OK to test existence,
        or the inclusive-OR of R_OK, W_OK, and X_OK.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be relative; path will then be relative to that
        directory.
      effective_ids
        If True, access will use the effective uid/gid instead of
        the real uid/gid.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        access will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd, effective_ids, and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    Note that most operations will use the effective uid/gid, therefore this
      routine can be used in a suid/sgid environment to test if the invoking user
      has the specified access to the path.
    """
    pass

def chdir(path): # real signature unknown; restored from __doc__
    """
    chdir(path)
    
    Change the current working directory to the specified path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def chmod(path, mode, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
    
    Change the access permissions of a file.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chmod will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def chown(path, uid, gid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
    
    Change the owner and group id of path to the numeric uid and gid.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, chown will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    dir_fd and follow_symlinks may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def chroot(path): # real signature unknown; restored from __doc__
    """
    chroot(path)
    
    Change root directory to path.
    """
    pass

def close(fd): # real signature unknown; restored from __doc__
    """
    close(fd)
    
    Close a file descriptor (for low level IO).
    """
    pass

def closerange(fd_low, fd_high): # real signature unknown; restored from __doc__
    """
    closerange(fd_low, fd_high)
    
    Closes all file descriptors in [fd_low, fd_high), ignoring errors.
    """
    pass

def confstr(name): # real signature unknown; restored from __doc__
    """
    confstr(name) -> string
    
    Return a string-valued system configuration variable.
    """
    return ""

def cpu_count(): # real signature unknown; restored from __doc__
    """
    cpu_count() -> integer
    
    Return the number of CPUs in the system, or None if this value cannot be
    established.
    """
    return 0

def ctermid(): # real signature unknown; restored from __doc__
    """
    ctermid() -> string
    
    Return the name of the controlling terminal for this process.
    """
    return ""

def device_encoding(fd): # real signature unknown; restored from __doc__
    """
    device_encoding(fd) -> str
    
    Return a string describing the encoding of the device
    if the output is a terminal; else return None.
    """
    return ""

def dup(fd): # real signature unknown; restored from __doc__
    """
    dup(fd) -> fd2
    
    Return a duplicate of a file descriptor.
    """
    pass

def dup2(old_fd, new_fd): # real signature unknown; restored from __doc__
    """
    dup2(old_fd, new_fd)
    
    Duplicate file descriptor.
    """
    pass

def execv(path, args): # real signature unknown; restored from __doc__
    """
    execv(path, args)
    
    Execute an executable path with arguments, replacing current process.
    
        path: path of executable file
        args: tuple or list of strings
    """
    pass

def execve(path, args, env): # real signature unknown; restored from __doc__
    """
    execve(path, args, env)
    
    Execute a path with arguments and environment, replacing current process.
    
        path: path of executable file
        args: tuple or list of arguments
        env: dictionary of strings mapping to strings
    
    On some platforms, you may specify an open file descriptor for path;
      execve will execute the program the file descriptor is open to.
      If this functionality is unavailable, using it raises NotImplementedError.
    """
    pass

def fchdir(fd): # real signature unknown; restored from __doc__
    """
    fchdir(fd)
    
    Change to the directory of the given file descriptor.  fd must be
    opened on a directory, not a file.  Equivalent to os.chdir(fd).
    """
    pass

def fchmod(fd, mode): # real signature unknown; restored from __doc__
    """
    fchmod(fd, mode)
    
    Change the access permissions of the file given by file
    descriptor fd.  Equivalent to os.chmod(fd, mode).
    """
    pass

def fchown(fd, uid, gid): # real signature unknown; restored from __doc__
    """
    fchown(fd, uid, gid)
    
    Change the owner and group id of the file given by file descriptor
    fd to the numeric uid and gid.  Equivalent to os.chown(fd, uid, gid).
    """
    pass

def fdatasync(fildes): # real signature unknown; restored from __doc__
    """
    fdatasync(fildes)
    
    force write of file with filedescriptor to disk.
     does not force update of metadata.
    """
    pass

def fork(): # real signature unknown; restored from __doc__
    """
    fork() -> pid
    
    Fork a child process.
    Return 0 to child process and PID of child to parent process.
    """
    pass

def forkpty(): # real signature unknown; restored from __doc__
    """
    forkpty() -> (pid, master_fd)
    
    Fork a new process with a new pseudo-terminal as controlling tty.
    
    Like fork(), return 0 as pid to child process, and PID of child to parent.
    To both, return fd of newly opened pseudo-terminal.
    """
    pass

def fpathconf(fd, name): # real signature unknown; restored from __doc__
    """
    fpathconf(fd, name) -> integer
    
    Return the configuration limit name for the file descriptor fd.
    If there is no limit, return -1.
    """
    return 0

def fstat(fd): # real signature unknown; restored from __doc__
    """
    fstat(fd) -> stat result
    
    Like stat(), but for an open file descriptor.
    Equivalent to stat(fd=fd).
    """
    pass

def fstatvfs(fd): # real signature unknown; restored from __doc__
    """
    fstatvfs(fd) -> statvfs result
    
    Perform an fstatvfs system call on the given fd.
    Equivalent to statvfs(fd).
    """
    pass

def fsync(fildes): # real signature unknown; restored from __doc__
    """
    fsync(fildes)
    
    force write of file with filedescriptor to disk.
    """
    pass

def ftruncate(fd, length): # real signature unknown; restored from __doc__
    """
    ftruncate(fd, length)
    
    Truncate a file to a specified length.
    """
    pass

def getcwd(): # real signature unknown; restored from __doc__
    """
    getcwd() -> path
    
    Return a unicode string representing the current working directory.
    """
    pass

def getcwdb(): # real signature unknown; restored from __doc__
    """
    getcwdb() -> path
    
    Return a bytes string representing the current working directory.
    """
    pass

def getegid(): # real signature unknown; restored from __doc__
    """
    getegid() -> egid
    
    Return the current process's effective group id.
    """
    pass

def geteuid(): # real signature unknown; restored from __doc__
    """
    geteuid() -> euid
    
    Return the current process's effective user id.
    """
    pass

def getgid(): # real signature unknown; restored from __doc__
    """
    getgid() -> gid
    
    Return the current process's group id.
    """
    pass

def getgrouplist(user, group): # real signature unknown; restored from __doc__
    """
    getgrouplist(user, group) -> list of groups to which a user belongs
    
    Returns a list of groups to which a user belongs.
    
        user: username to lookup
        group: base group id of the user
    """
    return []

def getgroups(): # real signature unknown; restored from __doc__
    """
    getgroups() -> list of group IDs
    
    Return list of supplemental group IDs for the process.
    """
    return []

def getloadavg(): # real signature unknown; restored from __doc__
    """
    getloadavg() -> (float, float, float)
    
    Return the number of processes in the system run queue averaged over
    the last 1, 5, and 15 minutes or raises OSError if the load average
    was unobtainable
    """
    pass

def getlogin(): # real signature unknown; restored from __doc__
    """
    getlogin() -> string
    
    Return the actual login name.
    """
    return ""

def getpgid(pid): # real signature unknown; restored from __doc__
    """
    getpgid(pid) -> pgid
    
    Call the system call getpgid().
    """
    pass

def getpgrp(): # real signature unknown; restored from __doc__
    """
    getpgrp() -> pgrp
    
    Return the current process group id.
    """
    pass

def getpid(): # real signature unknown; restored from __doc__
    """
    getpid() -> pid
    
    Return the current process id
    """
    pass

def getppid(): # real signature unknown; restored from __doc__
    """
    getppid() -> ppid
    
    Return the parent's process id.  If the parent process has already exited,
    Windows machines will still return its id; others systems will return the id
    of the 'init' process (1).
    """
    pass

def getpriority(which, who): # real signature unknown; restored from __doc__
    """
    getpriority(which, who) -> current_priority
    
    Get program scheduling priority.
    """
    pass

def getresgid(): # real signature unknown; restored from __doc__
    """
    getresgid() -> (rgid, egid, sgid)
    
    Get tuple of the current process's real, effective, and saved group ids.
    """
    pass

def getresuid(): # real signature unknown; restored from __doc__
    """
    getresuid() -> (ruid, euid, suid)
    
    Get tuple of the current process's real, effective, and saved user ids.
    """
    pass

def getsid(pid): # real signature unknown; restored from __doc__
    """
    getsid(pid) -> sid
    
    Call the system call getsid().
    """
    pass

def getuid(): # real signature unknown; restored from __doc__
    """
    getuid() -> uid
    
    Return the current process's user id.
    """
    pass

def getxattr(path, attribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    getxattr(path, attribute, *, follow_symlinks=True) -> value
    
    Return the value of extended attribute attribute on path.
    
    path may be either a string or an open file descriptor.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, getxattr will examine the symbolic link itself instead of the file
      the link points to.
    """
    pass

def get_inheritable(fd): # real signature unknown; restored from __doc__
    """
    get_inheritable(fd) -> bool
    
    Get the close-on-exe flag of the specified file descriptor.
    """
    return False

def get_terminal_size(*args, **kwargs): # real signature unknown
    """
    Return the size of the terminal window as (columns, lines).
    
    The optional argument fd (default standard output) specifies
    which file descriptor should be queried.
    
    If the file descriptor is not connected to a terminal, an OSError
    is thrown.
    
    This function will only be defined if an implementation is
    available for this system.
    
    shutil.get_terminal_size is the high-level function which should 
    normally be used, os.get_terminal_size is the low-level implementation.
    """
    pass

def initgroups(username, gid): # real signature unknown; restored from __doc__
    """
    initgroups(username, gid) -> None
    
    Call the system initgroups() to initialize the group access list with all of
    the groups of which the specified username is a member, plus the specified
    group id.
    """
    pass

def isatty(fd): # real signature unknown; restored from __doc__
    """
    isatty(fd) -> bool
    
    Return True if the file descriptor 'fd' is an open file descriptor
    connected to the slave end of a terminal.
    """
    return False

def kill(pid, sig): # real signature unknown; restored from __doc__
    """
    kill(pid, sig)
    
    Kill a process with a signal.
    """
    pass

def killpg(pgid, sig): # real signature unknown; restored from __doc__
    """
    killpg(pgid, sig)
    
    Kill a process group with a signal.
    """
    pass

def lchown(path, uid, gid): # real signature unknown; restored from __doc__
    """
    lchown(path, uid, gid)
    
    Change the owner and group id of path to the numeric uid and gid.
    This function will not follow symbolic links.
    Equivalent to os.chown(path, uid, gid, follow_symlinks=False).
    """
    pass

def link(src, dst, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    link(src, dst, *, src_dir_fd=None, dst_dir_fd=None, follow_symlinks=True)
    
    Create a hard link to a file.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    If follow_symlinks is False, and the last element of src is a symbolic
      link, link will create a link to the symbolic link itself instead of the
      file the link points to.
    src_dir_fd, dst_dir_fd, and follow_symlinks may not be implemented on your
      platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    """
    pass

def listdir(path='.'): # real signature unknown; restored from __doc__
    """
    listdir(path='.') -> list_of_filenames
    
    Return a list containing the names of the files in the directory.
    The list is in arbitrary order.  It does not include the special
    entries '.' and '..' even if they are present in the directory.
    
    path can be specified as either str or bytes.  If path is bytes,
      the filenames returned will also be bytes; in all other circumstances
      the filenames returned will be str.
    On some platforms, path may also be specified as an open file descriptor;
      the file descriptor must refer to a directory.
      If this functionality is unavailable, using it raises NotImplementedError.
    """
    pass

def listxattr(path='.', *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    listxattr(path='.', *, follow_symlinks=True)
    
    Return a list of extended attributes on path.
    
    path may be either None, a string, or an open file descriptor.
    if path is None, listxattr will examine the current directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, listxattr will examine the symbolic link itself instead of the file
      the link points to.
    """
    pass

def lockf(fd, cmd, len): # real signature unknown; restored from __doc__
    """
    lockf(fd, cmd, len)
    
    Apply, test or remove a POSIX lock on an open file descriptor.
    
    fd is an open file descriptor.
    cmd specifies the command to use - one of F_LOCK, F_TLOCK, F_ULOCK or
    F_TEST.
    len specifies the section of the file to lock.
    """
    pass

def lseek(fd, pos, how): # real signature unknown; restored from __doc__
    """
    lseek(fd, pos, how) -> newpos
    
    Set the current position of a file descriptor.
    Return the new cursor position in bytes, starting from the beginning.
    """
    pass

def lstat(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    lstat(path, *, dir_fd=None) -> stat result
    
    Like stat(), but do not follow symbolic links.
    Equivalent to stat(path, follow_symlinks=False).
    """
    pass

def major(device): # real signature unknown; restored from __doc__
    """
    major(device) -> major number
    Extracts a device major number from a raw device number.
    """
    pass

def makedev(major, minor): # real signature unknown; restored from __doc__
    """
    makedev(major, minor) -> device number
    Composes a raw device number from the major and minor device numbers.
    """
    pass

def minor(device): # real signature unknown; restored from __doc__
    """
    minor(device) -> minor number
    Extracts a device minor number from a raw device number.
    """
    pass

def mkdir(path, mode=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    mkdir(path, mode=0o777, *, dir_fd=None)
    
    Create a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    
    The mode argument is ignored on Windows.
    """
    pass

def mkfifo(path, mode=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    mkfifo(path, mode=0o666, *, dir_fd=None)
    
    Create a FIFO (a POSIX named pipe).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def mknod(path, mode=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    mknod(path, mode=0o600, device=0, *, dir_fd=None)
    
    Create a filesystem node (file, device special file or named pipe)
    named path. mode specifies both the permissions to use and the
    type of node to be created, being combined (bitwise OR) with one of
    S_IFREG, S_IFCHR, S_IFBLK, and S_IFIFO. For S_IFCHR and S_IFBLK,
    device defines the newly created device special file (probably using
    os.makedev()), otherwise it is ignored.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def nice(inc): # real signature unknown; restored from __doc__
    """
    nice(inc) -> new_priority
    
    Decrease the priority of process by inc and return the new priority.
    """
    pass

def open(path, flags, mode=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    open(path, flags, mode=0o777, *, dir_fd=None)
    
    Open a file for low level IO.  Returns a file handle (integer).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def openpty(): # real signature unknown; restored from __doc__
    """
    openpty() -> (master_fd, slave_fd)
    
    Open a pseudo-terminal, returning open fd's for both master and slave end.
    """
    pass

def pathconf(path, name): # real signature unknown; restored from __doc__
    """
    pathconf(path, name) -> integer
    
    Return the configuration limit name for the file or directory path.
    If there is no limit, return -1.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    return 0

def pipe(): # real signature unknown; restored from __doc__
    """
    pipe() -> (read_end, write_end)
    
    Create a pipe.
    """
    pass

def pipe2(flags): # real signature unknown; restored from __doc__
    """
    pipe2(flags) -> (read_end, write_end)
    
    Create a pipe with flags set atomically.
    flags can be constructed by ORing together one or more of these values:
    O_NONBLOCK, O_CLOEXEC.
    """
    pass

def posix_fadvise(fd, offset, len, advice): # real signature unknown; restored from __doc__
    """
    posix_fadvise(fd, offset, len, advice)
    
    Announces an intention to access data in a specific pattern thus allowing
    the kernel to make optimizations.
    The advice applies to the region of the file specified by fd starting at
    offset and continuing for len bytes.
    advice is one of POSIX_FADV_NORMAL, POSIX_FADV_SEQUENTIAL,
    POSIX_FADV_RANDOM, POSIX_FADV_NOREUSE, POSIX_FADV_WILLNEED or
    POSIX_FADV_DONTNEED.
    """
    pass

def posix_fallocate(fd, offset, len): # real signature unknown; restored from __doc__
    """
    posix_fallocate(fd, offset, len)
    
    Ensures that enough disk space is allocated for the file specified by fd
    starting from offset and continuing for len bytes.
    """
    pass

def pread(fd, buffersize, offset): # real signature unknown; restored from __doc__
    """
    pread(fd, buffersize, offset) -> string
    
    Read from a file descriptor, fd, at a position of offset. It will read up
    to buffersize number of bytes. The file offset remains unchanged.
    """
    return ""

def putenv(key, value): # real signature unknown; restored from __doc__
    """
    putenv(key, value)
    
    Change or add an environment variable.
    """
    pass

def pwrite(fd, string, offset): # real signature unknown; restored from __doc__
    """
    pwrite(fd, string, offset) -> byteswritten
    
    Write string to a file descriptor, fd, from offset, leaving the file
    offset unchanged.
    """
    pass

def read(fd, buffersize): # real signature unknown; restored from __doc__
    """
    read(fd, buffersize) -> bytes
    
    Read a file descriptor.
    """
    return b""

def readlink(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    readlink(path, *, dir_fd=None) -> path
    
    Return a string representing the path to which the symbolic link points.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def readv(fd, buffers): # real signature unknown; restored from __doc__
    """
    readv(fd, buffers) -> bytesread
    
    Read from a file descriptor fd into a number of mutable, bytes-like
    objects ("buffers").  readv will transfer data into each buffer
    until it is full and then move on to the next buffer in the sequence
    to hold the rest of the data.
    
    readv returns the total number of bytes read (which may be less than
    the total capacity of all the buffers.
    """
    pass

def remove(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    remove(path, *, dir_fd=None)
    
    Remove a file (same as unlink()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def removexattr(path, attribute, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    removexattr(path, attribute, *, follow_symlinks=True)
    
    Remove extended attribute attribute on path.
    path may be either a string or an open file descriptor.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, removexattr will modify the symbolic link itself instead of the file
      the link points to.
    """
    pass

def rename(src, dst, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    
    Rename a file or directory.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def replace(src, dst, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
    
    Rename a file or directory, overwriting the destination.
    
    If either src_dir_fd or dst_dir_fd is not None, it should be a file
      descriptor open to a directory, and the respective path string (src or dst)
      should be relative; the path will then be relative to that directory.
    src_dir_fd and dst_dir_fd, may not be implemented on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def rmdir(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    rmdir(path, *, dir_fd=None)
    
    Remove a directory.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def sched_getaffinity(pid, ncpus): # real signature unknown; restored from __doc__
    """
    sched_getaffinity(pid, ncpus) -> cpu_set
    
    Return the affinity of the process with PID *pid*.
    The returned cpu_set will be of size *ncpus*.
    """
    pass

def sched_getparam(pid): # real signature unknown; restored from __doc__
    """
    sched_getparam(pid) -> sched_param
    
    Returns scheduling parameters for the process with *pid* as an instance of the
    sched_param class. A PID of 0 means the calling process.
    """
    return sched_param

def sched_getscheduler(pid): # real signature unknown; restored from __doc__
    """
    sched_getscheduler(pid)
    
    Get the scheduling policy for the process with a PID of *pid*.
    Passing a PID of 0 returns the scheduling policy for the calling process.
    """
    pass

def sched_get_priority_max(policy): # real signature unknown; restored from __doc__
    """
    sched_get_priority_max(policy)
    
    Get the maximum scheduling priority for *policy*.
    """
    pass

def sched_get_priority_min(policy): # real signature unknown; restored from __doc__
    """
    sched_get_priority_min(policy)
    
    Get the minimum scheduling priority for *policy*.
    """
    pass

def sched_rr_get_interval(pid): # real signature unknown; restored from __doc__
    """
    sched_rr_get_interval(pid) -> float
    
    Return the round-robin quantum for the process with PID *pid* in seconds.
    """
    return 0.0

def sched_setaffinity(pid, cpu_set): # real signature unknown; restored from __doc__
    """
    sched_setaffinity(pid, cpu_set)
    
    Set the affinity of the process with PID *pid* to *cpu_set*.
    """
    pass

def sched_setparam(pid, param): # real signature unknown; restored from __doc__
    """
    sched_setparam(pid, param)
    
    Set scheduling parameters for a process with PID *pid*.
    A PID of 0 means the calling process.
    """
    pass

def sched_setscheduler(pid, policy, param): # real signature unknown; restored from __doc__
    """
    sched_setscheduler(pid, policy, param)
    
    Set the scheduling policy, *policy*, for *pid*.
    If *pid* is 0, the calling process is changed.
    *param* is an instance of sched_param.
    """
    pass

def sched_yield(): # real signature unknown; restored from __doc__
    """
    sched_yield()
    
    Voluntarily relinquish the CPU.
    """
    pass

def sendfile(out, in, offset, count): # real signature unknown; restored from __doc__
    """
    sendfile(out, in, offset, count) -> byteswritten
    sendfile(out, in, offset, count[, headers][, trailers], flags=0)
                -> byteswritten
    Copy count bytes from file descriptor in to file descriptor out.
    """
    pass

def setegid(gid): # real signature unknown; restored from __doc__
    """
    setegid(gid)
    
    Set the current process's effective group id.
    """
    pass

def seteuid(uid): # real signature unknown; restored from __doc__
    """
    seteuid(uid)
    
    Set the current process's effective user id.
    """
    pass

def setgid(gid): # real signature unknown; restored from __doc__
    """
    setgid(gid)
    
    Set the current process's group id.
    """
    pass

def setgroups(p_list): # real signature unknown; restored from __doc__
    """
    setgroups(list)
    
    Set the groups of the current process to list.
    """
    pass

def setpgid(pid, pgrp): # real signature unknown; restored from __doc__
    """
    setpgid(pid, pgrp)
    
    Call the system call setpgid().
    """
    pass

def setpgrp(): # real signature unknown; restored from __doc__
    """
    setpgrp()
    
    Make this process the process group leader.
    """
    pass

def setpriority(which, who, prio): # real signature unknown; restored from __doc__
    """
    setpriority(which, who, prio) -> None
    
    Set program scheduling priority.
    """
    pass

def setregid(rgid, egid): # real signature unknown; restored from __doc__
    """
    setregid(rgid, egid)
    
    Set the current process's real and effective group ids.
    """
    pass

def setresgid(rgid, egid, sgid): # real signature unknown; restored from __doc__
    """
    setresgid(rgid, egid, sgid)
    
    Set the current process's real, effective, and saved group ids.
    """
    pass

def setresuid(ruid, euid, suid): # real signature unknown; restored from __doc__
    """
    setresuid(ruid, euid, suid)
    
    Set the current process's real, effective, and saved user ids.
    """
    pass

def setreuid(ruid, euid): # real signature unknown; restored from __doc__
    """
    setreuid(ruid, euid)
    
    Set the current process's real and effective user ids.
    """
    pass

def setsid(): # real signature unknown; restored from __doc__
    """
    setsid()
    
    Call the system call setsid().
    """
    pass

def setuid(uid): # real signature unknown; restored from __doc__
    """
    setuid(uid)
    
    Set the current process's user id.
    """
    pass

def setxattr(path, attribute, value, flags=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    setxattr(path, attribute, value, flags=0, *, follow_symlinks=True)
    
    Set extended attribute attribute on path to value.
    path may be either a string or an open file descriptor.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, setxattr will modify the symbolic link itself instead of the file
      the link points to.
    """
    pass

def set_inheritable(fd, inheritable): # real signature unknown; restored from __doc__
    """
    set_inheritable(fd, inheritable)
    
    Set the inheritable flag of the specified file descriptor.
    """
    pass

def stat(*args, **kwargs): # real signature unknown
    """
    Perform a stat system call on the given path.
    
      path
        Path to be examined; can be string, bytes, or open-file-descriptor int.
      dir_fd
        If not None, it should be a file descriptor open to a directory,
        and path should be a relative string; path will then be relative to
        that directory.
      follow_symlinks
        If False, and the last element of the path is a symbolic link,
        stat will examine the symbolic link itself instead of the file
        the link points to.
    
    dir_fd and follow_symlinks may not be implemented
      on your platform.  If they are unavailable, using them will raise a
      NotImplementedError.
    
    It's an error to use dir_fd or follow_symlinks when specifying path as
      an open file descriptor.
    """
    pass

def statvfs(path): # real signature unknown; restored from __doc__
    """
    statvfs(path)
    
    Perform a statvfs system call on the given path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def stat_float_times(newval=None): # real signature unknown; restored from __doc__
    """
    stat_float_times([newval]) -> oldval
    
    Determine whether os.[lf]stat represents time stamps as float objects.
    If newval is True, future calls to stat() return floats, if it is False,
    future calls return ints. 
    If newval is omitted, return the current setting.
    """
    pass

def strerror(code): # real signature unknown; restored from __doc__
    """
    strerror(code) -> string
    
    Translate an error code to a message string.
    """
    return ""

def symlink(src, dst, target_is_directory=False, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    symlink(src, dst, target_is_directory=False, *, dir_fd=None)
    
    Create a symbolic link pointing to src named dst.
    
    target_is_directory is required on Windows if the target is to be
      interpreted as a directory.  (On Windows, symlink requires
      Windows 6.0 or greater, and raises a NotImplementedError otherwise.)
      target_is_directory is ignored on non-Windows platforms.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def sync(): # real signature unknown; restored from __doc__
    """
    sync()
    
    Force write of everything to disk.
    """
    pass

def sysconf(name): # real signature unknown; restored from __doc__
    """
    sysconf(name) -> integer
    
    Return an integer-valued system configuration variable.
    """
    return 0

def system(command): # real signature unknown; restored from __doc__
    """
    system(command) -> exit_status
    
    Execute the command (a string) in a subshell.
    """
    pass

def tcgetpgrp(fd): # real signature unknown; restored from __doc__
    """
    tcgetpgrp(fd) -> pgid
    
    Return the process group associated with the terminal given by a fd.
    """
    pass

def tcsetpgrp(fd, pgid): # real signature unknown; restored from __doc__
    """
    tcsetpgrp(fd, pgid)
    
    Set the process group associated with the terminal given by a fd.
    """
    pass

def times(): # real signature unknown; restored from __doc__
    """
    times() -> times_result
    
    Return an object containing floating point numbers indicating process
    times.  The object behaves like a named tuple with these fields:
      (utime, stime, cutime, cstime, elapsed_time)
    """
    return times_result

def truncate(path, length): # real signature unknown; restored from __doc__
    """
    truncate(path, length)
    
    Truncate the file given by path to length bytes.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    """
    pass

def ttyname(*args, **kwargs): # real signature unknown
    """
    Return the name of the terminal device connected to 'fd'.
    
      fd
        Integer file descriptor handle.
    """
    pass

def umask(new_mask): # real signature unknown; restored from __doc__
    """
    umask(new_mask) -> old_mask
    
    Set the current numeric umask and return the previous umask.
    """
    pass

def uname(): # real signature unknown; restored from __doc__
    """
    uname() -> uname_result
    
    Return an object identifying the current operating system.
    The object behaves like a named tuple with the following fields:
      (sysname, nodename, release, version, machine)
    """
    return uname_result

def unlink(path, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    unlink(path, *, dir_fd=None)
    
    Remove a file (same as remove()).
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
      If it is unavailable, using it will raise a NotImplementedError.
    """
    pass

def unsetenv(key): # real signature unknown; restored from __doc__
    """
    unsetenv(key)
    
    Delete an environment variable.
    """
    pass

def urandom(n): # real signature unknown; restored from __doc__
    """
    urandom(n) -> str
    
    Return n random bytes suitable for cryptographic use.
    """
    return ""

def utime(path, times=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    utime(path, times=None, *[, ns], dir_fd=None, follow_symlinks=True)
    Set the access and modified time of path.
    
    path may always be specified as a string.
    On some platforms, path may also be specified as an open file descriptor.
      If this functionality is unavailable, using it raises an exception.
    
    If times is not None, it must be a tuple (atime, mtime);
        atime and mtime should be expressed as float seconds since the epoch.
    If ns is specified, it must be a tuple (atime_ns, mtime_ns);
        atime_ns and mtime_ns should be expressed as integer nanoseconds
        since the epoch.
    If times is None and ns is unspecified, utime uses the current time.
    Specifying tuples for both times and ns is an error.
    
    If dir_fd is not None, it should be a file descriptor open to a directory,
      and path should be relative; path will then be relative to that directory.
    If follow_symlinks is False, and the last element of the path is a symbolic
      link, utime will modify the symbolic link itself instead of the file the
      link points to.
    It is an error to use dir_fd or follow_symlinks when specifying path
      as an open file descriptor.
    dir_fd and follow_symlinks may not be available on your platform.
      If they are unavailable, using them will raise a NotImplementedError.
    """
    pass

def wait(): # real signature unknown; restored from __doc__
    """
    wait() -> (pid, status)
    
    Wait for completion of a child process.
    """
    pass

def wait3(options): # real signature unknown; restored from __doc__
    """
    wait3(options) -> (pid, status, rusage)
    
    Wait for completion of a child process.
    """
    pass

def wait4(pid, options): # real signature unknown; restored from __doc__
    """
    wait4(pid, options) -> (pid, status, rusage)
    
    Wait for completion of a given child process.
    """
    pass

def waitid(idtype, id, options): # real signature unknown; restored from __doc__
    """
    waitid(idtype, id, options) -> waitid_result
    
    Wait for the completion of one or more child processes.
    
    idtype can be P_PID, P_PGID or P_ALL.
    id specifies the pid to wait on.
    options is constructed from the ORing of one or more of WEXITED, WSTOPPED
    or WCONTINUED and additionally may be ORed with WNOHANG or WNOWAIT.
    Returns either waitid_result or None if WNOHANG is specified and there are
    no children in a waitable state.
    """
    return waitid_result

def waitpid(pid, options): # real signature unknown; restored from __doc__
    """
    waitpid(pid, options) -> (pid, status)
    
    Wait for completion of a given child process.
    """
    pass

def WCOREDUMP(status): # real signature unknown; restored from __doc__
    """
    WCOREDUMP(status) -> bool
    
    Return True if the process returning 'status' was dumped to a core file.
    """
    return False

def WEXITSTATUS(status): # real signature unknown; restored from __doc__
    """
    WEXITSTATUS(status) -> integer
    
    Return the process return code from 'status'.
    """
    return 0

def WIFCONTINUED(status): # real signature unknown; restored from __doc__
    """
    WIFCONTINUED(status) -> bool
    
    Return True if the process returning 'status' was continued from a
    job control stop.
    """
    return False

def WIFEXITED(status): # real signature unknown; restored from __doc__
    """
    WIFEXITED(status) -> bool
    
    Return true if the process returning 'status' exited using the exit()
    system call.
    """
    return False

def WIFSIGNALED(status): # real signature unknown; restored from __doc__
    """
    WIFSIGNALED(status) -> bool
    
    Return True if the process returning 'status' was terminated by a signal.
    """
    return False

def WIFSTOPPED(status): # real signature unknown; restored from __doc__
    """
    WIFSTOPPED(status) -> bool
    
    Return True if the process returning 'status' was stopped.
    """
    return False

def write(fd, data): # real signature unknown; restored from __doc__
    """
    write(fd, data) -> byteswritten
    
    Write bytes to a file descriptor.
    """
    pass

def writev(fd, buffers): # real signature unknown; restored from __doc__
    """
    writev(fd, buffers) -> byteswritten
    
    Write the contents of *buffers* to file descriptor *fd*. *buffers*
    must be a sequence of bytes-like objects.
    
    writev writes the contents of each object to the file descriptor
    and returns the total number of bytes written.
    """
    pass

def WSTOPSIG(status): # real signature unknown; restored from __doc__
    """
    WSTOPSIG(status) -> integer
    
    Return the signal that stopped the process that provided
    the 'status' value.
    """
    return 0

def WTERMSIG(status): # real signature unknown; restored from __doc__
    """
    WTERMSIG(status) -> integer
    
    Return the signal that terminated the process that provided the 'status'
    value.
    """
    return 0

def _exit(status): # real signature unknown; restored from __doc__
    """
    _exit(status)
    
    Exit to the system with specified status, without normal exit processing.
    """
    pass

# classes

from .Exception import Exception

class error(Exception):
    """ Base class for I/O related errors. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    characters_written = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """POSIX exception code"""

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception filename"""

    filename2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """second exception filename"""

    strerror = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """exception strerror"""



from .tuple import tuple

class sched_param(tuple):
    """
    sched_param(sched_priority): A scheduling parameter.
    
    Current has only one field: sched_priority
    """
    def __init__(self, sched_priority): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    sched_priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the scheduling priority"""


    n_fields = 1
    n_sequence_fields = 1
    n_unnamed_fields = 0


from .tuple import tuple

class statvfs_result(tuple):
    """
    statvfs_result: Result from statvfs or fstatvfs.
    
    This object may be accessed either as a tuple of
      (bsize, frsize, blocks, bfree, bavail, files, ffree, favail, flag, namemax),
    or via the attributes f_bsize, f_frsize, f_blocks, f_bfree, and so on.
    
    See os.statvfs for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    f_bavail = property(lambda self: 0)
    """:type: int"""

    f_bfree = property(lambda self: 0)
    """:type: int"""

    f_blocks = property(lambda self: 0)
    """:type: int"""

    f_bsize = property(lambda self: 0)
    """:type: int"""

    f_favail = property(lambda self: 0)
    """:type: int"""

    f_ffree = property(lambda self: 0)
    """:type: int"""

    f_files = property(lambda self: 0)
    """:type: int"""

    f_flag = property(lambda self: 0)
    """:type: int"""

    f_frsize = property(lambda self: 0)
    """:type: int"""

    f_namemax = property(lambda self: 0)
    """:type: int"""


    n_fields = 10
    n_sequence_fields = 10
    n_unnamed_fields = 0


from .tuple import tuple

class stat_result(tuple):
    """
    stat_result: Result from stat, fstat, or lstat.
    
    This object may be accessed either as a tuple of
      (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    or via the attributes st_mode, st_ino, st_dev, st_nlink, st_uid, and so on.
    
    Posix/windows: If your platform supports st_blksize, st_blocks, st_rdev,
    or st_flags, they are available as attributes only.
    
    See os.stat for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    st_atime = property(lambda self: 0)
    """time of last access

    :type: int
    """

    st_atime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last access in nanoseconds"""

    st_blksize = property(lambda self: 0)
    """blocksize for filesystem I/O

    :type: int
    """

    st_blocks = property(lambda self: 0)
    """number of blocks allocated

    :type: int
    """

    st_ctime = property(lambda self: 0)
    """time of last change

    :type: int
    """

    st_ctime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last change in nanoseconds"""

    st_dev = property(lambda self: 0)
    """device

    :type: int
    """

    st_gid = property(lambda self: 0)
    """group ID of owner

    :type: int
    """

    st_ino = property(lambda self: 0)
    """inode

    :type: int
    """

    st_mode = property(lambda self: 0)
    """protection bits

    :type: int
    """

    st_mtime = property(lambda self: 0)
    """time of last modification

    :type: int
    """

    st_mtime_ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """time of last modification in nanoseconds"""

    st_nlink = property(lambda self: 0)
    """number of hard links

    :type: int
    """

    st_rdev = property(lambda self: 0)
    """device type (if inode device)

    :type: int
    """

    st_size = property(lambda self: 0)
    """total size, in bytes

    :type: int
    """

    st_uid = property(lambda self: 0)
    """user ID of owner

    :type: int
    """


    n_fields = 19
    n_sequence_fields = 10
    n_unnamed_fields = 3


from .tuple import tuple

class terminal_size(tuple):
    """ A tuple of (columns, lines) for holding terminal window size """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width of the terminal window in characters"""

    lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height of the terminal window in characters"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0


from .tuple import tuple

class times_result(tuple):
    """
    times_result: Result from os.times().
    
    This object may be accessed either as a tuple of
      (user, system, children_user, children_system, elapsed),
    or via the attributes user, system, children_user, children_system,
    and elapsed.
    
    See os.times for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    children_system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time of children"""

    children_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time of children"""

    elapsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """elapsed time since an arbitrary point in the past"""

    system = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """system time"""

    user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """user time"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


from .tuple import tuple

class uname_result(tuple):
    """
    uname_result: Result from os.uname().
    
    This object may be accessed either as a tuple of
      (sysname, nodename, release, version, machine),
    or via the attributes sysname, nodename, release, version, and machine.
    
    See os.uname for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    machine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """hardware identifier"""

    nodename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of machine on network (implementation-defined)"""

    release = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system release"""

    sysname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system name"""

    version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """operating system version"""


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


from .tuple import tuple

class waitid_result(tuple):
    """
    waitid_result: Result from waitid.
    
    This object may be accessed either as a tuple of
      (si_pid, si_uid, si_signo, si_status, si_code),
    or via the attributes si_pid, si_uid, and so on.
    
    See os.waitid for more information.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    si_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_signo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    si_uid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    n_fields = 5
    n_sequence_fields = 5
    n_unnamed_fields = 0


from .object import object

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """ Load a built-in module. """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is ''


# variables with complex values

confstr_names = {
    'CS_GNU_LIBC_VERSION': 2,
    'CS_GNU_LIBPTHREAD_VERSION': 3,
    'CS_LFS64_CFLAGS': 1004,
    'CS_LFS64_LDFLAGS': 1005,
    'CS_LFS64_LIBS': 1006,
    'CS_LFS64_LINTFLAGS': 1007,
    'CS_LFS_CFLAGS': 1000,
    'CS_LFS_LDFLAGS': 1001,
    'CS_LFS_LIBS': 1002,
    'CS_LFS_LINTFLAGS': 1003,
    'CS_PATH': 0,
    'CS_XBS5_ILP32_OFF32_CFLAGS': 1100,
    'CS_XBS5_ILP32_OFF32_LDFLAGS': 1101,
    'CS_XBS5_ILP32_OFF32_LIBS': 1102,
    'CS_XBS5_ILP32_OFF32_LINTFLAGS': 1103,
    'CS_XBS5_ILP32_OFFBIG_CFLAGS': 1104,
    'CS_XBS5_ILP32_OFFBIG_LDFLAGS': 1105,
    'CS_XBS5_ILP32_OFFBIG_LIBS': 1106,
    'CS_XBS5_ILP32_OFFBIG_LINTFLAGS': 1107,
    'CS_XBS5_LP64_OFF64_CFLAGS': 1108,
    'CS_XBS5_LP64_OFF64_LDFLAGS': 1109,
    'CS_XBS5_LP64_OFF64_LIBS': 1110,
    'CS_XBS5_LP64_OFF64_LINTFLAGS': 1111,
    'CS_XBS5_LPBIG_OFFBIG_CFLAGS': 1112,
    'CS_XBS5_LPBIG_OFFBIG_LDFLAGS': 1113,
    'CS_XBS5_LPBIG_OFFBIG_LIBS': 1114,
    'CS_XBS5_LPBIG_OFFBIG_LINTFLAGS': 1115,
}

environ = {} # real value of type <class 'dict'> skipped

pathconf_names = {
    'PC_ALLOC_SIZE_MIN': 18,
    'PC_ASYNC_IO': 10,
    'PC_CHOWN_RESTRICTED': 6,
    'PC_FILESIZEBITS': 13,
    'PC_LINK_MAX': 0,
    'PC_MAX_CANON': 1,
    'PC_MAX_INPUT': 2,
    'PC_NAME_MAX': 3,
    'PC_NO_TRUNC': 7,
    'PC_PATH_MAX': 4,
    'PC_PIPE_BUF': 5,
    'PC_PRIO_IO': 11,
    'PC_REC_INCR_XFER_SIZE': 14,
    'PC_REC_MAX_XFER_SIZE': 15,
    'PC_REC_MIN_XFER_SIZE': 16,
    'PC_REC_XFER_ALIGN': 17,
    'PC_SOCK_MAXBUF': 12,
    'PC_SYMLINK_MAX': 19,
    'PC_SYNC_IO': 9,
    'PC_VDISABLE': 8,
}

sysconf_names = {
    'SC_2_CHAR_TERM': 95,
    'SC_2_C_BIND': 47,
    'SC_2_C_DEV': 48,
    'SC_2_C_VERSION': 96,
    'SC_2_FORT_DEV': 49,
    'SC_2_FORT_RUN': 50,
    'SC_2_LOCALEDEF': 52,
    'SC_2_SW_DEV': 51,
    'SC_2_UPE': 97,
    'SC_2_VERSION': 46,
    'SC_AIO_LISTIO_MAX': 23,
    'SC_AIO_MAX': 24,
    'SC_AIO_PRIO_DELTA_MAX': 25,
    'SC_ARG_MAX': 0,
    'SC_ASYNCHRONOUS_IO': 12,
    'SC_ATEXIT_MAX': 87,
    'SC_AVPHYS_PAGES': 86,
    'SC_BC_BASE_MAX': 36,
    'SC_BC_DIM_MAX': 37,
    'SC_BC_SCALE_MAX': 38,
    'SC_BC_STRING_MAX': 39,
    'SC_CHARCLASS_NAME_MAX': 45,
    'SC_CHAR_BIT': 101,
    'SC_CHAR_MAX': 102,
    'SC_CHAR_MIN': 103,
    'SC_CHILD_MAX': 1,
    'SC_CLK_TCK': 2,
    'SC_COLL_WEIGHTS_MAX': 40,
    'SC_DELAYTIMER_MAX': 26,
    'SC_EQUIV_CLASS_MAX': 41,
    'SC_EXPR_NEST_MAX': 42,
    'SC_FSYNC': 15,
    'SC_GETGR_R_SIZE_MAX': 69,
    'SC_GETPW_R_SIZE_MAX': 70,
    'SC_INT_MAX': 104,
    'SC_INT_MIN': 105,
    'SC_IOV_MAX': 60,
    'SC_JOB_CONTROL': 7,
    'SC_LINE_MAX': 43,
    'SC_LOGIN_NAME_MAX': 71,
    'SC_LONG_BIT': 106,
    'SC_MAPPED_FILES': 16,
    'SC_MB_LEN_MAX': 108,
    'SC_MEMLOCK': 17,
    'SC_MEMLOCK_RANGE': 18,
    'SC_MEMORY_PROTECTION': 19,
    'SC_MESSAGE_PASSING': 20,
    'SC_MQ_OPEN_MAX': 27,
    'SC_MQ_PRIO_MAX': 28,
    'SC_NGROUPS_MAX': 3,
    'SC_NL_ARGMAX': 119,
    'SC_NL_LANGMAX': 120,
    'SC_NL_MSGMAX': 121,
    'SC_NL_NMAX': 122,
    'SC_NL_SETMAX': 123,
    'SC_NL_TEXTMAX': 124,
    'SC_NPROCESSORS_CONF': 83,
    'SC_NPROCESSORS_ONLN': 84,
    'SC_NZERO': 109,
    'SC_OPEN_MAX': 4,
    'SC_PAGESIZE': 30,
    'SC_PAGE_SIZE': 30,
    'SC_PASS_MAX': 88,
    'SC_PHYS_PAGES': 85,
    'SC_PII': 53,
    'SC_PII_INTERNET': 56,
    'SC_PII_INTERNET_DGRAM': 62,
    'SC_PII_INTERNET_STREAM': 61,
    'SC_PII_OSI': 57,
    'SC_PII_OSI_CLTS': 64,
    'SC_PII_OSI_COTS': 63,
    'SC_PII_OSI_M': 65,
    'SC_PII_SOCKET': 55,
    'SC_PII_XTI': 54,
    'SC_POLL': 58,
    'SC_PRIORITIZED_IO': 13,
    'SC_PRIORITY_SCHEDULING': 10,
    'SC_REALTIME_SIGNALS': 9,
    'SC_RE_DUP_MAX': 44,
    'SC_RTSIG_MAX': 31,
    'SC_SAVED_IDS': 8,
    'SC_SCHAR_MAX': 111,
    'SC_SCHAR_MIN': 112,
    'SC_SELECT': 59,
    'SC_SEMAPHORES': 21,
    'SC_SEM_NSEMS_MAX': 32,
    'SC_SEM_VALUE_MAX': 33,
    'SC_SHARED_MEMORY_OBJECTS': 22,
    'SC_SHRT_MAX': 113,
    'SC_SHRT_MIN': 114,
    'SC_SIGQUEUE_MAX': 34,
    'SC_SSIZE_MAX': 110,
    'SC_STREAM_MAX': 5,
    'SC_SYNCHRONIZED_IO': 14,
    'SC_THREADS': 67,
    'SC_THREAD_ATTR_STACKADDR': 77,
    'SC_THREAD_ATTR_STACKSIZE': 78,
    'SC_THREAD_DESTRUCTOR_ITERATIONS': 73,
    'SC_THREAD_KEYS_MAX': 74,
    'SC_THREAD_PRIORITY_SCHEDULING': 79,
    'SC_THREAD_PRIO_INHERIT': 80,
    'SC_THREAD_PRIO_PROTECT': 81,
    'SC_THREAD_PROCESS_SHARED': 82,
    'SC_THREAD_SAFE_FUNCTIONS': 68,
    'SC_THREAD_STACK_MIN': 75,
    'SC_THREAD_THREADS_MAX': 76,
    'SC_TIMERS': 11,
    'SC_TIMER_MAX': 35,
    'SC_TTY_NAME_MAX': 72,
    'SC_TZNAME_MAX': 6,
    'SC_T_IOV_MAX': 66,
    'SC_UCHAR_MAX': 115,
    'SC_UINT_MAX': 116,
    'SC_UIO_MAXIOV': 60,
    'SC_ULONG_MAX': 117,
    'SC_USHRT_MAX': 118,
    'SC_VERSION': 29,
    'SC_WORD_BIT': 107,
    'SC_XBS5_ILP32_OFF32': 125,
    'SC_XBS5_ILP32_OFFBIG': 126,
    'SC_XBS5_LP64_OFF64': 127,
    'SC_XBS5_LPBIG_OFFBIG': 128,
    'SC_XOPEN_CRYPT': 92,
    'SC_XOPEN_ENH_I18N': 93,
    'SC_XOPEN_LEGACY': 129,
    'SC_XOPEN_REALTIME': 130,
    'SC_XOPEN_REALTIME_THREADS': 131,
    'SC_XOPEN_SHM': 94,
    'SC_XOPEN_UNIX': 91,
    'SC_XOPEN_VERSION': 89,
    'SC_XOPEN_XCU_VERSION': 90,
    'SC_XOPEN_XPG2': 98,
    'SC_XOPEN_XPG3': 99,
    'SC_XOPEN_XPG4': 100,
}

_have_functions = [
    'HAVE_FACCESSAT',
    'HAVE_FCHDIR',
    'HAVE_FCHMOD',
    'HAVE_FCHMODAT',
    'HAVE_FCHOWN',
    'HAVE_FCHOWNAT',
    'HAVE_FEXECVE',
    'HAVE_FDOPENDIR',
    'HAVE_FPATHCONF',
    'HAVE_FSTATAT',
    'HAVE_FSTATVFS',
    'HAVE_FTRUNCATE',
    'HAVE_FUTIMENS',
    'HAVE_FUTIMES',
    'HAVE_FUTIMESAT',
    'HAVE_LINKAT',
    'HAVE_LCHOWN',
    'HAVE_LSTAT',
    'HAVE_LUTIMES',
    'HAVE_MKDIRAT',
    'HAVE_MKFIFOAT',
    'HAVE_MKNODAT',
    'HAVE_OPENAT',
    'HAVE_READLINKAT',
    'HAVE_RENAMEAT',
    'HAVE_SYMLINKAT',
    'HAVE_UNLINKAT',
    'HAVE_UTIMENSAT',
]

__spec__ = None # (!) real value is ''

