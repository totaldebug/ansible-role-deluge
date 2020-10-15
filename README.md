# ansible-role-deluge

This role installs deluge 2 and configures.

# Install

```
ansible-galaxy install totaldebug.deluge
```

# Features

* TBC

# Role Variables

The following variable defaults are defined in `defaults/main.yml`.

- `deluge_repo` URL to the Deluge Git Repo
  - Defaults: `git://deluge-torrent.org/deluge.git`
- `deluge_version` Version of deluge to install (2.0 upwards)
  - Defaults: `2.0.3`
- `deluge_config_dir` Directory for deluge config
- `deluge_users` Creates a list of Deluge users for Auth
- `deluge_web_port` Port on which Deluge's Web UI is listening.
- `deluge_web_log_level` Log level for the UI. See available options with deluge-web --help.
- `deluge_web_args` Arguments passed to the deluge-web binary that's running as a service. See available options with deluge-web --help.
- `deluge_web_password` Password to be used for the Web UI.
- `deluge_web_password_salt` Password salt used when generating the Web UI password.
- `deluge_allow_remote`
- `deluge_autoadd_location`
- `deluge_download_location`
- `deluge_move_completed_path`
- `deluge_prioritize_first_last_pieces`
- `deluge_queue_new_to_top`
- `deluge_torrentfiles_location`

# Contributing

Pull requests are welcome.

## Versioning

This project follows semantic versioning.

In the context of semantic versioning, consider the role contract to be defined by the role variables.

* Breaking Changes or changes that require user intervention will increase the major version. This includes changing the default value of a role variable.
* Changes that do not require user intervention, but add new features, will increase the minor version.
* Bug fixes will increase the patch version.

