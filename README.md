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

- `deluge_service_user`: deluge
- `deluge_service_group`: deluge
- `enable_logging`: true
- `deluged_port`: 58846
- `deluge_web_port`: 8112
- `deluge_log_dir`: '/var/log/deluge'
- `deluge_home`: ''

# Contributing

Pull requests are welcome.

## Versioning

This project follows semantic versioning.

In the context of semantic versioning, consider the role contract to be defined by the role variables.

* Breaking Changes or changes that require user intervention will increase the major version. This includes changing the default value of a role variable.
* Changes that do not require user intervention, but add new features, will increase the minor version.
* Bug fixes will increase the patch version.

