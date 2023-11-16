# HNSPullNotification

## Notification Description
The HNSPullNotification facilitates pull-based notifications using the specified connector and configuration.

## Name
- **Description**: The name of the HNSPullNotification instance.
- **Type**: Text (string)
- **Example**: "HNSPullNotificationInstance"

## Connector
- **Description**: The connector used to retrieve notifications.
- **Type**: Text (string)
- **Example**: "HNSConnector"

## Listkey
- **Description**: The key used to identify the notification list.
- **Type**: Text (string)
- **Example**: "notifications"

## Limit
- **Description**: The maximum number of notifications to retrieve per request.
- **Type**: Integer
- **Example**: 10

## Autoload
- **Description**: A flag indicating whether notifications should be automatically loaded on initialization.
- **Type**: Boolean (true/false)
- **Example**: true
