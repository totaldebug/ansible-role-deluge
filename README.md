# ansible-role-deluge

This role installs deluge 2 and configures.

## Install

```
ansible-galaxy install totaldebug.deluge
```

## Features

* TBC

## Role Variables

The following variable defaults are defined in `defaults/main.yml`.

### Deluge

- `deluge_service_user` default: `deluge` - username for the service account
- `deluge_service_group` default: `deluge` - group for the service account
- `deluged_port` default: `58846` - Deluge port
- `deluge_home` default: `/ver/log/deluge/` - sets the default home for the deluge service account, config will be stored here
- `deluge_download_location` default: `/home`
- `deluge_move_completed_path` default: `'{{ deluge_download_location }}'`
- `deluge_torrentfiles_location` default: `'{{ deluge_download_location }}'`
- `deluge_autoadd_location` default: `'{{ deluge_download_location }}'`
- `deluge_user_service_dir` default: `/etc/systemd/system/deluged.service.d/`
- `deluge_core_conf_template` default: `core.conf.j2`

### Deluge Web

- `deluge_web` default: `true` - Installs the deluge-web component
- `deluge_web_port` default: `8112` - Change the web port for the portal
- `deluge_web_user_service_dir` default: `/etc/systemd/system/deluge-web.service.d/` - sets the directory for the user service config
- `deluge_web_conf_template` default: `web.conf.j2` allows the use of a custom config file see custom templates below

#### Custom Templates

The deluge core.conf and web.conf templates packaged with this role are meant to
be very generic. Allowing to set every possible option in there from the
role would be overlly complicated for maintenance.

If the default template does not suit your needs, you can replace it with yours.
What you need to do:
* create a `templates` directory at the same level as your playbook
* create a `templates\mycore.conf.j2` file (just choose a different name from the default template)
* in your playbook set the var `default_web_conf_template: mycore.conf.j2`

### Logging

- `enable_logging` default: false - Enables logging
- `log_rotation` default: false - Enables log rotation
- `deluge_log_dir` default: `/var/log/deluge/` - Log location
- `deluge_log_level` default: warning - Level of logging

## Contributing

Pull requests are welcome.

### Versioning

This project follows semantic versioning.

In the context of semantic versioning, consider the role contract to be defined by the role variables.

* Breaking Changes or changes that require user intervention will increase the major version. This includes changing the default value of a role variable.
* Changes that do not require user intervention, but add new features, will increase the minor version.
* Bug fixes will increase the patch version.
