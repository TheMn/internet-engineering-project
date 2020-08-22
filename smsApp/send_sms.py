from kavenegar import *


class SendSms:
    api_key = '42704C79676D635968475662366172412B2B5347796C536642677266753662462F6F6534776D57655252413D'

    @staticmethod
    def send_bulk(text, phone_numbers):
        try:
            api = KavenegarAPI(apikey=SendSms.api_key)
            params = {
                'sender': '',
                'receptor': phone_numbers,
                'message': text,
            }
            response = api.sms_send(params)
        except APIException as e:
            print(e)

        except HTTPException as e:
            print(e)
