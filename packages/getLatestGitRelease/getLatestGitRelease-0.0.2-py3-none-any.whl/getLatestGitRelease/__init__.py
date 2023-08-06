
from    ConfigFileHelper    import Config
from    urllib.request      import urlopen
from    zipfile             import ZipFile
from    github              import Github
from    io                  import BytesIO
from    pathlib             import Path
from    datetime            import datetime
from    datasize            import DataSize
from    collections         import namedtuple

#
# do a (semi) intelligent import of icecream in case it's not installed in a particular environment
#
try:
    from icecream import ic
    def ic_set (debug):
        if debug:
            ic.enable()
        else:
            ic.disable()
except ImportError:  # Graceful fallback if IceCream isn't installed.
    doDebug : bool  = False
    def ic (thing): # just print to STDOUT
        if doDebug:
            print  (thing)
    def ic_set (debug):
        global doDebug
        doDebug =   debug
        ic ("* icecream module not imported successfully, using STDOUT")


__all__                 :   list    = ['getLatestRelease']

dateTruple = namedtuple('dateTruple', ['created','modified','accessed'])

class gitRepo (object):
    def __init__(self):
        self.id             =   None
        self.owner          =   None
        self.name           =   None
        self.fullName       =   None
        self.url            =   None
        self.private        =   None

    def __repr__(self):
        return str(dict(self))

    def __iter__(self):
        yield 'id', self.id
        yield 'owner', self.owner
        yield 'name', self.name
        yield 'fullName', self.fullName
        yield 'url', self.url
        yield 'private', self.private

# '2021-03-12T01:57:22Z'
DTMask = "%Y-%m-%dT%H:%M:%S%z"

thisPlatform    :   str =   None

def getPlatform():
    import platform
    global thisPlatform
    thisPlatform = platform.system()

getPlatform()

def isWindows() -> bool:
    if not thisPlatform:
        getPlatform()
    return thisPlatform == 'Windows'

def gitConnect  (key        :   str
                ):
    return Github(key)


def getRepo     (g
                ,repoOwner  :   str =   None
                ,repoName   :   str =   None
                ,id         :   int =   None
                ,fullName   :   str =   None
                ):
    if      id:
        name_or_id  =   id
    elif    fullName:
        name_or_id  =   fullName
    elif    (repoOwner and repoName):
        name_or_id  =   f"{repoOwner}/{repoName}"
    else:
        raise AttributeError ("invalid parameters")
    return g.get_repo (name_or_id)

def setFileDateTimes    (filePath
                        ,datetimes : dateTruple
                        ):
    try :

        if isWindows():
            import time, win32file, win32con, pywintypes

            def convertDT (dt_in):
                # handle datetime.datetime parameters
                dt_out  =   dt_in if not isinstance(dt_in, datetime) else time.mktime(dt_in.timetuple())
                # adjust for day light savings
                now = time.localtime()
                dt_out += 3600 * (now.tm_isdst - time.localtime(dt_out).tm_isdst)

                return pywintypes.Time(int(dt_out))

            theseDateTimes  = dateTruple    (created    =   convertDT (datetimes.created)
                                            ,modified   =   convertDT (datetimes.modified)
                                            ,accessed   =   convertDT (datetimes.accessed)
                                            )
            # change time stamps
            winfile = win32file.CreateFile  (str(filePath)
                                            ,win32con.GENERIC_WRITE
                                            ,win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE
                                            ,None
                                            ,win32con.OPEN_EXISTING
                                            ,win32con.FILE_ATTRIBUTE_NORMAL
                                            ,None
                                            )
            win32file.SetFileTime   (winfile
                                    ,theseDateTimes.created
                                    ,theseDateTimes.accessed
                                    ,theseDateTimes.modified
                                    )
            winfile.close()
        else:
            """MUST FIGURE OUT..."""
            raise Warning(f'setFileDateTimes not implemented for {thisPlatform}')
    except Exception as e:
        """ setFileDateTimes failed """
        ic (str(e))

def releasesToDictList (releases):
    return [releaseToDict(r) for r in releases]

def releaseToDict (release):
    outDict = {}

    outDict['id']               =   release.id
    outDict['title']            =   release.title
    outDict['tag_name']         =   release.tag_name
    outDict['prerelease']       =   release.prerelease
    outDict['created_at']       =   (release.created_at).strftime(DTMask)
    outDict['published_at']     =   (release.published_at).strftime(DTMask)
    outDict['zip_url']          =   release.zipball_url

    return outDict

def getLatestRelease    (github_config_file         :   str
                        ,github_config_file_type    :   str =   None
                        ):

    gitConfig  =   Config   (file_path  =   github_config_file
                            ,file_type  =   github_config_file_type
                            )

    ic_set (gitConfig.get_bool('APP/DEBUG'))

    ic ("debug ON (\'APP/DEBUG\')")
    ic (f'Configuration File      : {Path(github_config_file).resolve()}')
    if github_config_file_type:
        ic (f'Configuration File Type : {github_config_file_type}')


    repo        =   gitRepo ()
    repo.id     =   gitConfig.get   (keys       =   'GITHUB/REPO_ID'
                                    ,raiseNDF   =   False
                                    )
    repo.owner  =   gitConfig.get   (keys       =   'GITHUB/REPO_OWNER'
                                    ,raiseNDF   =   False
                                    )
    repo.name   =   gitConfig.get   (keys       =   'GITHUB/REPO_NAME'
                                    ,raiseNDF   =   False
                                    )
    assert  (   (repo.owner is None     and repo.name is None       and repo.id is not None and isinstance(repo.id,int))
                or
                (repo.owner is not None and repo.name is not None   and repo.id is None     and isinstance(repo.owner,str) and isinstance(repo.name,str))
            ), f"((REPO_OWNER \"{repo.owner}\" AND REPO_NAME \"{repo.name}\") XOR (REPO_ID \"{repo.id}\")) must be supplied as parameters in \'{github_config_file}\'"


    git                 =   gitConnect      (key    =   gitConfig.get('GITHUB/KEY'))

    if repo.id:
        thisRepo        =   getRepo     (g          =   git
                                        ,id         =   repo.id
                                        )
        repo.owner     =   thisRepo.owner.login
        repo.name      =   thisRepo.name
    else:
        thisRepo        =   getRepo     (g          =   git
                                        ,repoOwner  =   repo.owner
                                        ,repoName   =   repo.name
                                        )
        repo.id         =   thisRepo.id

    repo.fullName       =   thisRepo.full_name
    repo.url            =   thisRepo.html_url
    repo.private        =   thisRepo.private

    ic (repo)

    releases            =   [r for r in thisRepo.get_releases()]
    allowPrelease       =   gitConfig.get_bool (['APP','ALLOW_PRERELEASE'])
    keepArchive         =   gitConfig.get_bool (['APP','KEEP_ARCHIVE'])
    filteredReleases    =   releases if allowPrelease else [r for r in releases if r.prerelease == False]

    basePath            =   gitConfig.get   (keys       =   ['APP','OUTPUT_FOLDER']
                                            ,raiseNDF   =   False
                                            )
    if not basePath:
        basePath        =   '.'
        gitConfig.set   (keys       =   ['APP','OUTPUT_FOLDER']
                        ,value      =   basePath
                        )
    gitConfig.save()

    basePath            =   Path(basePath).resolve()
    ic (f"Output Path : {basePath}")

    Path(basePath).mkdir    (parents    =   True
                            ,exist_ok   =   True
                            )

    try:
        ic (f"Release count          = {len(releases)}")
        if not len(releases) == len(filteredReleases):
            ic (f"Filtered Release count = {len(filteredReleases)}")

        if len(filteredReleases) == 0:
            release = {"message" : f"No releases found{'' if allowPrelease else ' (PreReleases are not permitted)'}"}
            raise   Warning(release["message"])
        else:
            # ic (f"{len(releases)} release{', using this one' if len(releases) == 1 else 's, using newest'}")

            release                     =   releaseToDict(filteredReleases[0])
            release["message"]          =   f"Release with tag \'{filteredReleases[0].tag_name}\' retrieved"
            if filteredReleases[0].prerelease:
                release["message"]     +=   " (this is a PreRelease)"
            release["downloaded_at"]    =   datetime.utcnow().strftime(DTMask)

            with urlopen(release['zip_url']) as zipresp:

                theBytes                     =   zipresp.read()

                if keepArchive:
                    releaseFolder   =   basePath.joinpath('releases',repo.owner,repo.name)
                    Path(releaseFolder).mkdir       (parents    =   True
                                                    ,exist_ok   =   True
                                                    )
                    release["zip_file_name"]     =   str(releaseFolder.joinpath(f"{release['tag_name']}.zip"))
                    with open (release["zip_file_name"],'wb') as f:
                        f.write(theBytes)

                    def getDT (dateStr : str) -> datetime:
                        try:
                            retval = datetime.strptime(dateStr, DTMask)
                        except ValueError:
                            retval = datetime.strptime(dateStr, DTMask[:-2])
                        try:
                            retval  =   retval.astimezone(tz=None)
                        except:
                            ...
                        return retval

                    setFileDateTimes    (filePath   =   release["zip_file_name"]
                                        ,datetimes  =   dateTruple  (created    =   getDT(release['created_at'])
                                                                    ,modified   =   getDT(release['published_at'])
                                                                    ,accessed   =   datetime.now()
                                                                    )
                                        )

                else:
                    release["zip_file_name"]     =   None

            release["zip_file_size"]     =   DataSize(f"{len(theBytes)}B").__format__('m')
            release["zip_file_bytes"]    =   len(theBytes)

            with ZipFile(BytesIO(theBytes)) as zfile:
                release['files']    =   []
                for f in zfile.filelist:
                    thisPath    =   basePath
                    origPath    =   Path(f.filename)

                    for p in list(origPath.parts[1:]):
                        thisPath    =   thisPath.joinpath(p)

                    if origPath.parts[-1] == '.gitignore':
                        # Ignore these files
                        ...
                    elif f.is_dir ():
                        # Creating folder
                        Path(thisPath).mkdir    (parents    =   True
                                                ,exist_ok   =   True
                                                )
                    else:
                        fileTime = datetime(*f.date_time)
                        d = dict()
                        d["name"]   =   str(thisPath)
                        d["size"]   =   DataSize(f"{f.file_size}B").__format__('m')
                        d["bytes"]  =   f.file_size
                        d["date"]   =   fileTime.strftime(DTMask)

                        release['files'].append (d)

                        with open(thisPath, "wb") as thisFile:
                            thisFile.write(zfile.read (f))
                        setFileDateTimes    (filePath   =   thisPath
                                            ,datetimes  =   dateTruple  (created    =   fileTime
                                                                        ,modified   =   fileTime
                                                                        ,accessed   =   fileTime
                                                                        )
                                            )
    except Warning as w:
        pass

    finally:
        ic (repo.fullName)
        if "message" in release and release["message"]:
            ic (release["message"])

        # write data out from what we've got here. use the Config object to write it
        yamlDump    =   Config  (file_path          =   basePath.joinpath(f"{repo.owner}.{repo.name}.release.yaml")
                                ,raiseFileNotFound  =   False
                                ,config             =   {"config"           :   gitConfig.get('APP')
                                                        ,"repo"             :   dict(repo)
                                                        ,"release"          :   release
                                                        ,"allReleases"      :   releasesToDictList(releases)
                                                        }
                                )
        yamlDump.set('config/OUTPUT_FOLDER',str(basePath))
        yamlDump.save()
        yamlDump = None

if __name__ == '__main__':
    ...