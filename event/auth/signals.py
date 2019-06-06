from blinker import Namespace
from ..tasks import send_email

signals = Namespace()

user_registered = signals.signal('user-registered')
requested_for_password_reset = signals.signal('user-forgot-password')

@user_registered.connect
def on_user_registration(user):
	# - TODO (yashpokar) :: Change the algorythm of email token & reset password token
		# issue :: token with same algo can be used at both the side if it is not expired
	send_email.delay(
		'Email verification',
		f'Your registration has been completed successful. verify your email with token {user.generate_email_verification_token()}',
		recipients=[user.email]
	)

@requested_for_password_reset.connect
def user_forgot_password(user):
	# TODO (yashpokar) :: replace this by beautify html template
	body = f'Click this link to reset your password {user.generate_password_reset_token()}'

	send_email.delay('Reset Password', body, recipients=[user.email])
