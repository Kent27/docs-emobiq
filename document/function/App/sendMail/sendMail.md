#  sendMail

## Description

Sends an email through the app.

## Input / Parameter

| Name | Description | Input Type | Default | Options | Required |
| ------ | ------ | ------ | ------ | ------ | ------ |
| config | The configuration of the email to be sent. | Object | - | - | Yes |
| from | The name of the sender. | Object | - | - | Yes |
| to | The name of the recipient. | Array/List | - | - | Yes |
| cc | The carbon copy. | Array/List | - | - | No |
| bcc | The blind carbon copy. | Array/List | - | - | No |
| data | The contents of the email. | Object | - | - | Yes |
| attachment | The file(s) to be attached. | Array/List | - | - | No |

## Output

N/A

## Callback?

### callback

The function to be executed when the email is sent successfully.

### errCallback

The function to be executed when the email is not sent successfully.

## Video

Coming Soon.

<!-- Format: [![Video]({image-path}?raw=true)]({url-link}) -->

## Example

The user want to send an email via the app.

### Step

1. Call the sendMail function, add toObject function in "config" parameter as below:

    ![](../../../../document/function/App/sendMail/sendMail-step-1.png?raw=true)

2. For "from" paremeter, add toObject with "email" & "name".

    ![](../../../../document/function/App/sendMail/sendMail-step-2.png?raw=true)

3. For "to" paremeter, add toArray function then toObject funtion.

    ![](../../../../document/function/App/sendMail/sendMail-step-3.png?raw=true)

    Add fields "email" & "name".

    ![](../../../../document/function/App/sendMail/sendMail-step-5.png?raw=true)

4. For "cc" paremeter, add toArray function then toObject funtion.
   
    ![](../../../../document/function/App/sendMail/sendMail-step-4.png?raw=true)

    Add fields "email" & "name".

    ![](../../../../document/function/App/sendMail/sendMail-step-6.png?raw=true)

5. For "data" paremeter, add toObject function then add fields "subject" "body". 

    ![](../../../../document/function/App/sendMail/sendMail-step-7.png?raw=true)
    
### Result

Email Received:
![](../../../../document/function/App/sendMail/sendMail-result-1.png?raw=true)

## Links
