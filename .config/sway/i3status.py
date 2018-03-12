from i3pystatus import Status

status = Status(logfile='$HOME/i3statuspy.log')

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
        format="%a, %d %b %H:%M",)

# Shows your CPU temperature, if you have a Intel CPU
status.register("temp",
    format=" {temp:.0f}°C",)

# This would look like this:
# Discharging 6h:51m
status.register("battery",
    format="{status} {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "",
        "CHR": "",
        "FULL": "",
    },)

# Shows disk usage of /
status.register("disk",
    path="/",
    format="/: {percentage_used:.1f}%",)

# Shows disk usage of /home
status.register("disk",
    path="/home",
    format="~: {percentage_used:.1f}%",)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
status.register("pulseaudio",
    format=" {volume}",)


# Shows mpd status
# Format:
# Cloud connected▶Reroute to Remain
status.register("mpd",
    format="{artist} - {title} {song_elapsed} / {song_length}",)

status.run()
