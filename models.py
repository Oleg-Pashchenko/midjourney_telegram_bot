import dataclasses


@dataclasses.dataclass
class Secrets:
    BOT_TELEGRAM_TOKEN: str
    BOT_DISCORD_TOKEN: str
    DISCORD_WEBHOOK: str


@dataclasses.dataclass
class Request:
    text: str
    tg_chat_id: int
    discord_webhook: str

