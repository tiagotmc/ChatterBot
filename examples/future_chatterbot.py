from chatterbot import ChatBot


class MyChatBot(ChatBot)

    logic_adapters = (
        'chatterbot.adapters.logic.ClosestMatch',
        'chatterbot.adapters.logic.EvaluateMathematically',
        'chatterbot.adapters.logic.CurrentTime',
    )

    # IO adapters are now pairs where the first is input and the second is output
    # This allows you to mix and match inputs and output types
    io_adapters = (
        ('chatterbot.adapters.io.terminal', 'chatterbot.adapters.io.terminal'),
        ('chatterbot.adapters.io.email', 'chatterbot.adapters.io.email'),
        ('chatterbot.adapters.io.terminal', 'chatterbot.adapters.io.voice'),
    )

    storage_adapters = (
        ('chatterbot.adapters.storage.MongoDB'),
        ('chatterbot.adapters.storage.Twitter'),
    )
