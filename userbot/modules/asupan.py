 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import register
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo
from telethon.tl.types import InputMessagesFilterVoice


@register(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Gabutnyazaen", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"**Berhasil menemukan Video**.")
        
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")

        

CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim video asupan secara random.\
    "
    }
)
