from ..common import WhatsappContentType
from ..proto import notification_hub_pb2 as pb


class ChatbotWhatsapp:
    def __init__(
            self,
            content_type: WhatsappContentType = WhatsappContentType.HSM,
            message_id: str ="",
            extra_param: str = "",
            button_url_param: str = ""
    ):
        """
        Parameters:
            content_type (WhatsappContentType): default to WhatsappContentType.HSM
            message_id (str, optional): this works a session id
            extra_params (str, optional): additional information to send
        """
        self._chatbot_whatsapp = pb.ChatbotWhatsapp()
        self._chatbot_whatsapp.contentType = content_type
        self._chatbot_whatsapp.messageID = message_id
        self._chatbot_whatsapp.extraParam = extra_param
        self._chatbot_whatsapp.buttonUrlParam = button_url_param

    @property
    def proto(self) -> pb.ChatbotWhatsapp:
        return self._chatbot_whatsapp
