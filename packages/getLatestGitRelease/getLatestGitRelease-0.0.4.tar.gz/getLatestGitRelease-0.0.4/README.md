# getLatestGitRelease

will grab the latest github release and pull it down locally, unzipping it into the specified folder

### Usage

    getLatestRelease    (github_config_file         =   '.\getLatest.example.yaml'
                        ,github_config_file_type    =   'YAML'
                        )

#### the config file (can be YAML, JSON, XML, INI)

    APP:
        ALLOW_PRERELEASE: true
        OUTPUT_FOLDER: d:\my\local\path
        DEBUG: false
        KEEP_ARCHIVE: false
    GITHUB:
        REPO_NAME: theRepoName
        REPO_OWNER: theRepoOwner
        REPO_ID: None # You can use the REPO_ID _INSTEAD_ if you want
        KEY: ghp_000000000000000000000000000000000000
