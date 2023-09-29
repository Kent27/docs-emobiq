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

### to (Object | List)

Will contain a single object, or a list of one (1) or more objects which consist of:

| Key | Description | Input Type | Required |
| ------ | ------ | ------ | ------ |
| email | Recipient's email address. | Text | Yes |
| name | Recipient’s display name. | Text | No |

### cc (Object | List)

Will contain a single object, or a list of zero (0) or more objects which consist of:

| Key | Description | Input Type | Required |
| ------ | ------ | ------ | ------ |
| email | CC'ed email address. | Text | Yes |
| name | CC'ed display name. | Text | No |

### bcc (Object | List)

Will contain a single object, or a list of zero (0) or more objects which consist of:

| Key | Description | Input Type | Required |
| ------ | ------ | ------ | ------ |
| email | BCC'ed email address. | Text | Yes |
| name | BCC'ed display name. | Text | No |

### attachment (Object | List)

Will contain a single object, or a list of zero (0) or more objects which consist of:

| Key | Description | Input Type | Required |
| ------ | ------ | ------ | ------ |
| name | Optional name. If not specified, file name will be used. | Text | No |
| value | Contains the direct file path of the attachments. | Text | Yes |

## Output

| Description | Output Type |
| ------ | ------ |
| Returns the formatted information. | Object |

### Object

| Key | Description | Output Type |
| ------ | ------ | ------ |
| success | Boolean value to denote whether the function was executed successfully. | Text |
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

## Example

Coming Soon.

### Steps

Coming Soon.

### Result

Coming Soon.

## Links