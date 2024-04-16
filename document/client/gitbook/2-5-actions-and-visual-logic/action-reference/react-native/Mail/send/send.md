# send

## Description

Sends an e-mail through SMTP server.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| type | Type or protocol to use. | Text | - | SMTP | required |
| smtpHost | SMTP server host URL to be used. | Text | - | - | required |
| smtpPort | SMTP port number to be used. | Number | - | - | required |
| smtpUsername | Username for the email account. | Text | - | - | required |
| smtpPassword | Password for the email account. | Text | - | - | required |
| smtpUseSSL | Enable/disable secure SSL connection. | Boolean | True | - | - |
| fromName | Sender’s display name. | Text | - | - | - |
| to | Contain a single object, or a list of one (1) or more objects which consist of: email (Text) Recipient’s email address & name (Text) – Recipient’s display name. | Object / Array | - | - | required |
| bcc | Contain a single object, or a list of one (1) or more objects which consist of: email (Text) BCC’ed email address & name (Text) – BCC’ed display name. | Object / Array | - | - | - |
| subject | The email’s title a.k.a. subject. | Text | - | - | required |
| body | The email’s content a.k.a. body. | Text | - | - | required |
| attachment | Contain a single object, or a list of one (1) or more objects which consist of: name (Text) File name that will be used.  & value (Text) – direct file path of the attachments. | Object / Array | - | - | - |
| extra | Additional data to be used in the callbacks. | Any | - | - | No | 

## Output

Formatted Result

## Callback

### callback

The function to be executed when the email successfully sent.

### errorCallback

The function to be executed when the email unsuccessfully sent.

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user wants to send an email.

<!-- Share a scenario, like a user requirements. -->

### Steps

| No. | Description |  |
| ------ | ------ | ------ |
| 1. | ![](./send-step-1.png) | Drag a button component to a page in the mobile designer and open up the `Action` tab. |
| 2. | ![](./send-step-2.png) | Select the event `click` and drag the `Mail.send` function to the event flow. |
| 3. | ![](./send-step-3.png) | Fill in the parameters of the function. |

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}) -->

### Result

The email recipients should received an email from user

<!-- Explain the output.

Format: ![]({image-path}) -->

## Links
