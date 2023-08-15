# Mail.send

## Description

Sends an email through the SMTP server.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| type | The type or protocol to use (e.g. "smtp"). | Text | - | - | Yes |
| smtpHost | The SMTP server host URL to be used. | Text | - | - | Yes |
| smtpPort | The SMTP port number to be used. | Text | - | - | Yes |
| smtpUsername | The username for the email account. | Text | - | - | Yes | 
| smtpPassword | The password for the email account. | Text | - | - | Yes | 
| smtpUseStartTLS | To enable or disable startTSL. | Boolean | true | true, false | No | 
| smtpUseSSL | To enable or disable secure SSL connection. | Boolean | true | true, false | No | 
| fromEmail | The sender's email address. | Text | - | - | Yes | 
| fromName | The sender's display name. | Text | - | - | No | 
| to | The recipients' email addresses. | Object / List | - | - | Yes | 
| cc | The email addresses to carbon copy. | Object / List | - | - | No | 
| bcc | The email addresses to blind carbon copy. | Object / List | - | - | No | 
| subject | The title of the email. | Text | - | - | Yes | 
| body | The content of the email. | Text | - | - | Yes | 
| attachment | The file path of the attachments. | Object / List | - | - | No | 
| extra | The stored value that is passed to all the callbacks. | Any | - | - | No | 

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the fucntion was executed successfully. | Text |
| message | The message to print. | Text |
| data | Any additional message or data to print. | Text |

## Callback

### successCallback

| Description | Output Type |
| ------ | ------ |
| Returns a message to indicate that email has been processed for sending. | Text |

### failureCallback

| Description | Output Type |
| ------ | ------ |
| Returns a message to indicate that email has not been processed for sending. | Text |

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

Coming Soon.

<!-- Share a scenario, like a user requirements. -->

### Steps

Coming Soon.

<!-- Show the steps and share some screenshots.

1. .....

Format: ![]({image-path}?raw=true) -->

### Result

Coming Soon.

<!-- Explain the output.

Format: ![]({image-path}?raw=true) -->

## Links