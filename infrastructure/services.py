from application.services import EmailService


class AwsEmailService(EmailService):
    def send_email(self, target_email: str, content: str):
        print(f'이메일 발송 완료: {target_email}')
