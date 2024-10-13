# rwall

Randomly set your Linux wallpaper using wal.

Run `rwall -h` to see all the available modules.

rwall depends on the RWALL_WALLPAPERS environment variable. This variable specifies the directory that rwall will use to look for wallpapers.
You can set this variable when running rwall like so:
```bash
RWALL_WALLPAPERS="/path/to/wallpapers" rwall
```
or you can set it in `.zshrc`/`.bashrc`:
```bash
export RWALL_WALLPAPERS="/path/to/wallpapers"
```

## Cron

rwall is best used with Cron. First, you'll need to setup Cron for your system. As cronjobs run in a minimal environment, you need to specify some environment variables before running the script.

1. Get the values for the required variables:
```bash
echo $DISPLAY
echo $DBUS_SESSION_BUS_ADDRESS
```

2. Add the cronjob. An example could look like:
```bash
*/15 * * * * DISPLAY=<display> DBUS_SESSION_BUS_ADDRESS="<dbus>" PATH="/usr/bin:/path/to/rwall" RWALL_WALLPAPERS="/path/to/wallpapers" rwall
```

## Notes

Your configuration needs to be set up properly in order for certain modules to work.

#### Polybar

The `-p` flag will output your wal colours to an ini file: `~/.config/polybar/colors`. You can then load these into your polybar config:
```
[ini]
include-file = ~/.config/polybar/colors
```

#### BSPWM

If you're using BSPWM, you can use the `-b` flag to reload the BSPWM config. This only affects the border colours for the windows.

#### Zed

After running rwall with the `-z` flag you need to install the wal theme:
1. Open Zed
2. Press `ctrl + shift + p` to enter the command palette
3. Search for extensions an choose `zed: extensions`
4. Click "Install Dev Extension", navigate to `/path/to/rwall/scripts/zed-theme-wal` and select it (replace `/path/to/rwall` with the path to where you cloned rwall)
5. Press `ctrl + k` then `ctrl + t`, and select the wal theme

rwall forces a refresh of Zed by copying the generated Zed theme to `~/.config/zed/themes`, so it should pickup your wal changes every time you run rwall.

#### Dunst

The `-d` flag relies on the existence of the dunst config file: `~/.config/dunst/dunstrc`. It then looks for any references to `background` and `foreground` and replaces them with the new wal colours.
```
[urgency_low]
...
background = "#101010"
foreground = "#dcc8db"

[urgency_normal]
...
background = "#101010"
foreground = "#dcc8db"

[urgency_critical]
...
background = "#101010"
foreground = "#dcc8db"
```
