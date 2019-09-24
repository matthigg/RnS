def send_email(request_POST):

  print('========== request_POST', request_POST)

  import boto3
  from botocore.exceptions import ClientError
  import os

  # Unpack and/or assign variables
  name, email, phone, message = request_POST['name'], request_POST['email'], request_POST['phone'], request_POST['message']
  number_of_stories, type_of_exterior = request_POST['number_of_stories'], request_POST['type_of_exterior']
  fence_cleaning, surface_cleaning, soft_wash, outdoor_stain_removal, deck_cleaning = 'no', 'no', 'no', 'no', 'no'
  if 'fence_cleaning' in request_POST:
    fence_cleaning = 'yes'
  if 'surface_cleaning' in request_POST:
    surface_cleaning = 'yes'
  if 'soft_wash' in request_POST:
    soft_wash = 'yes'
  if 'outdoor_stain_removal' in request_POST:
    outdoor_stain_removal = 'yes'
  if 'deck_cleaning' in request_POST:
    deck_cleaning = 'yes'

  # Replace sender@example.com with your "From" address. This address must be 
  # verified with Amazon SES.
  SENDER = "<{}>".format(os.environ['RNS_EMAIL_SENDER'])

  # Replace recipient@example.com with a "To" address. If your account is still 
  # in the sandbox, this address must be verified.
  RECIPIENT = "{}".format(email)


  # If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
  AWS_REGION = "us-east-1"

  # The subject line for the email.
  SUBJECT = "Thank You For Contacting R & S Pressure Washing!"

  # The email body for recipients with non-HTML email clients.
  BODY_TEXT = ("R & S Pressure Washing\r\n"
              "Thank You for contacting R & S Pressure Washing! "
              "A member of our team will contact you as soon as possible. "
              "If you need to contact us immediately, don't hesitate to "
              "call us at (123) 456-7890."
              "Original Message: "
              "Name: {} "
              "Email: {} "
              "Phone: {} "
              "Message: {} "
              "Number of stories: {}"
              "Type of exterior: {}" 
              "Fence cleaning: {}"
              "Surface cleaning: {}"
              "Soft wash: {}"
              "Outdoor stain removal: {}"
              "Deck cleaning: {}".format(name, email, phone, message, number_of_stories, type_of_exterior, fence_cleaning, surface_cleaning, soft_wash, outdoor_stain_removal, deck_cleaning)
              )
              
  # The HTML body of the email.
  BODY_HTML = """<html>
  <head></head>
  <body>
    <h1>Thank You For Contacting R & S Pressure Washing!</h1>
    <p>
      A member of our team will contact you as soon as possible.<br>
      If you need to contact us immediately, don't hesitate to
      call us at (123) 456-7890.
    </p>
    <hr>
    <p>
      <i>Original Message:</i><br>
      Name: {}<br>
      Email: {}<br>
      Phone: {}<br>
      Address: {}<br>
      Number of stories: {}<br>
      Type of exterior: {}<br> 
      Fence cleaning: {}<br>
      Surface cleaning: {}<br>
      Soft wash: {}<br>
      Outdoor stain removal: {}<br>
      Deck cleaning: {}<br>
    </p>
  </body>
  </html>
              """.format(name, email, phone, message, number_of_stories, type_of_exterior, fence_cleaning, surface_cleaning, soft_wash, outdoor_stain_removal, deck_cleaning)

  # The character encoding for the email.
  CHARSET = "UTF-8"

  # Create a new SES resource and specify a region.
  client = boto3.client('ses',region_name=AWS_REGION)

  # Try to send a response email to the person who submitted the contact form.
  # Note - this won't work unless the Amazon SES account is out of the sandbox,
  # or the recipient address has been verified.
  # try:
  #   response = client.send_email(
  #     Destination={
  #       'ToAddresses': [
  #         RECIPIENT,
  #       ],
  #     },
  #     Message={
  #       'Body': {
  #           'Html': { 'Charset': CHARSET, 'Data': BODY_HTML, },
  #           'Text': { 'Charset': CHARSET, 'Data': BODY_TEXT, },
  #         },
  #         'Subject': { 'Charset': CHARSET, 'Data': SUBJECT, },
  #       },
  #       Source=SENDER,
  #     )
  # except ClientError as e:
  #   print("=== ERROR: ", e.response['Error']['Message'])
  # else:
  #   print("Email sent! Message ID:"),
  #   print(response['MessageId'])

  # Try to send the email to the website owner.
  try:
    response = client.send_email(
      Destination={
        'ToAddresses': [
          os.environ['RNS_EMAIL_SENDER'],
        ],
      },
      Message={
        'Body': {
            'Html': { 'Charset': CHARSET, 'Data': BODY_HTML, },
            'Text': { 'Charset': CHARSET, 'Data': BODY_TEXT, },
          },
          'Subject': { 'Charset': CHARSET, 'Data': SUBJECT, },
        },
        Source=SENDER,
      )
  except ClientError as e:
    print("=== ERROR: ", e.response['Error']['Message'])
  else:
    print("Email sent! Message ID:"),
    print(response['MessageId'])