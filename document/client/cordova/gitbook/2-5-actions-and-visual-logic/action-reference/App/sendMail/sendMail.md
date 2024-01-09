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

<!-- Format: [![Video]({image-path})]({url-link}) -->

## Example

The user want to send an email via the app.

### Step

1. Call the sendMail function, add toObject function in "config" parameter as below:

    ![](./sendMail-step-1.png)

2. For "from" paremeter, add toObject with "email" & "name".

    ![](./sendMail-step-2.png)

3. For "to" paremeter, add toArray function then toObject funtion.

    ![](./sendMail-step-3.png)

    Add fields "email" & "name".

    ![](./sendMail-step-5.png)

4. For "cc" paremeter, add toArray function then toObject funtion.
   
    ![](./sendMail-step-4.png)

    Add fields "email" & "name".

    ![](./sendMail-step-6.png)

5. For "data" paremeter, add toObject function then add fields "subject" "body". 

    ![](./sendMail-step-7.png)
    
### Result

Email Received:
![](./sendMail-result-1.png)

## Links
