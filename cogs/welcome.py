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
        msg = f"Herzlich willkommen auf dem Lernserversystem Psychologie für Studierende der FUH, {member.mention} 😊\n\n" \
              f"**Aufgrund des grossen Andrangs auf den Server kann es bei Neuaufnahmen zu Verzögerungen kommen, dafür bitten wir um Entschuldigung.**\n\n" \
              f"Bitte beachte, dass du erst nach 10 Minuten Mitgliedschaft hier posten kannst. Das gibt dir genug Zeit, die Infos vorher durchzulesen. Damit dürften sich schon viele Fragen von selbst klären.\n\n" \
              f"Deinen Namen kannst du ändern, indem du mit der rechten Maustaste darauf klickst und dann den Nicknamen änderst. So können nur wir hier deinen Server-Namen sehen und auf Discord bist du weiterhin vollständig anonym.\n\n" \
              f"**Da wir hier viele Dokumente teilen und gemeinsam erarbeiten, muss man sich bei Eintritt in den Server verifizieren. Dafür hast du drei Möglichkeiten:**\n\n" \
              f"**1.** Schicke einen Screenshot von deinem aktuellen Belegbogen an \n" \
              f"                                             Verifizierung-Psychologie-Lernserver@protonmail.com\n\n" \
              f"O D E R\n\n" \
              f"**2.** Schicke während des Semesters jeweils ab 1.4. oder ab 1.10. eine E-Mail __aus deinem Fernuni-Account__\n" \
              f"      an Verifizierung-Psychologie-Lernserver@protonmail.com und gib deine belegten Module an, damit wir\n" \
              f"      Dich in Moodle finden können. **Wer die E-Mail aus dem Fernuni Account während des Semesters schickt,\n" \
              f"      braucht keinen Belegbogen mitschicken!**\n\n\n" \
              f"‼ WICHTIG! Wenn du E-Mails schickst, vergiss nicht, deinen Discord-Namen anzugeben, sonst können wir\n" \
              f"                                   dich hier nicht finden!\n" \
              f"O D E R\n" \
              f"**3.** Schicke den Belegbogen hier privat an <@!{self.verifier}>\n" \
              f" Logos etc. der Fernuni müssen auch sichtbar sein. Folge dafür bitte dem untenstehenden Link und schick ein Foto der __ganzen__  Seite. Ausschnitte werden nicht akzeptiert.\n" \
              f"Sobald du ein ✅  unter deiner Nachricht mit dem Belegbogen hast, kannst du ihn sofort wieder löschen.\n\n" \
              f"Hier geht's zum Belegbogen:\n" \
              f"https://vu.fernuni-hagen.de/lvuweb/lvuauth/app/ActualAssignment?function=Belegbogen"
        await channel.send(msg)
