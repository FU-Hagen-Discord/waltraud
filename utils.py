import re

import discord


async def send_dm(user, message, embed=None):
    """ Send DM to a user/member """

    if type(user) is discord.User or type(user) is discord.Member:
        if user.dm_channel is None:
            await user.create_dm()

        await user.dm_channel.send(message, embed=embed)


def is_valid_time(time):
    return re.match(r"^\d+[mhd]?$", time)


def to_minutes(time):
    if time[-1:] == "m":
        return int(time[:-1])
    elif time[-1:] == "h":
        h = int(time[:-1])
        return h * 60
    elif time[-1:] == "d":
        d = int(time[:-1])
        h = d * 24
        return h * 60

    return int(time)
