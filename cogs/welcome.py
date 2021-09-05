import os

from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channel_id = int(os.getenv("DISCORD_WELCOME_CHANNEL"))
        self.verifier = int(os.getenv("DISCORD_VERIFIER"))
        self.work_on = int(os.getenv("DISCORD_WORK_ON"))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await self.bot.fetch_channel(self.channel_id)
        msg = f"Herzlich willkommen auf dem Lernserversystem Psychologie für Studierende der FUH, {member.mention} :blush:\n\n" \
              f"**Der große Andrang auf den Server  verursacht u.U. bis zu 2 -3 Tagen Wartezeit bei der Aufnahme. Wer die Mail aus Moodle geschickt hat (und die belegten Module, sowie seinen Discord-Namen da reingeschrieben hat) bzw. hier seinen Belegbogen privat an <@!{self.verifier}> geschickt hat, wird automatisch aufgenommen. Ihr bekommt eine private Nachricht, wenn es soweit ist.**\n\n" \
              f"Bitte beachte, dass du erst nach 10 Minuten Mitgliedschaft hier posten kannst. Das gibt dir genug Zeit, die Infos vorher durchzulesen. Damit dürften sich schon viele Fragen von selbst klären.\n\n" \
              f"**Wenn du aus deinem Fernuni-Email-Account (hier findest du den: https://studium.fernuni-hagen.de/ ) eine Email mit deinem Nicknamen hier und den belegten Modulen an**\n\n" \
              f":round_pushpin: Verifizierung-Psychologie-Lernserver@protonmail.com :round_pushpin:\n\n" \
              f"**schickst, können wir dir auch die geschlossenen Bereiche freigeben.**\n" \
              f"(Wenn du den Belegbogen lieber in einem Anruf mit Screensharing vorzeigen möchtest, geht das auch. Vereinbare dann bitte einen Termin mit <@!{self.verifier}> )\n" \
              f"Du kannst den Belegbogen auch wie bisher direkt an <@!{self.verifier}> in einer privaten Nachricht schicken, sorge dann bitte selbst dafür, diesen sofort wieder zu löschen, sobald du dein grünes Häkchen erhalten hast. (Diese Lösung ist aus Datenschutzgründen nicht so gut, obwohl wir bisher nie damit Probleme hatten.)\n\n" \
              f"Hier geht's zum Belegbogen:\n" \
              f"https://vu.fernuni-hagen.de/lvuweb/lvuauth/app/ActualAssignment?function=Belegbogen\n\n" \
              f"Bitte trag doch nach der Freigabe noch bei <#{self.work_on}> Deine Module für dieses und nächstes Semester ein und sag evtl. Hallo in deiner lokalen Lerngruppe :blush:"
        await channel.send(msg)
