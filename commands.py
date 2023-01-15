import translate


def handle_response_command(message) -> str:
    p_message = message.lower()
    command_end = p_message.find(' ')

    if p_message[:command_end] == "translate":
        return translate.translate_google(p_message[command_end:], "pl", "en")
    if p_message[:command_end] == "tłumacz":
        return translate.translate_google(p_message[command_end:], "en", "pl")
    if p_message == "ping":
        return "Pong!"
