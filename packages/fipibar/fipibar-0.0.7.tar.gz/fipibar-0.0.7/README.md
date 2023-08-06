# Fipibar

Fip radio plugin for Polybar with Spotify (TODO) and Last FM integration.

## Screenshots/Usage:

TODO!

## Installation:

`python3 -m pip install fipibar`

Installation needs the following config in your polybar config:

```
[module/fipibar-station-name]
type = custom/script
exec = fipibar --print-current-station-name
exec-if = [ $(fipibar --is-currently-playing) = "True" ]
click-left = fipibar --next-station
click-right = fipibar --previous-station
scroll-up = fipibar --next-station
scroll-down = fipibar --previous-station
format-underline = #aa7722
format-padding = 2

[module/fipibar-toggle-playback]
type = custom/script
exec = echo " "
click-left = fipibar --toggle-playback
click-right = fipibar --config-popup
format-underline = #aa7722
format-padding = 2

[module/fipibar-song-details]
type = custom/script
exec = fipibar --get-currently-playing
exec-if = [ $(fipibar --is-currently-playing) = "True" ]
format-underline = #aa7722
format-padding = 2
```

Place the following in `~/.fibibar_config.json` for Last.fm integration:

```
{
  "should_notify": true,
  "lastfm_should_scrobble": true,
  "lastfm_api_key": "XXXX",
  "lastfm_api_secret": "XXXX",
  "lastfm_username": "XXXX",
  "lastfm_password_hash": "XXXX"
}
```
