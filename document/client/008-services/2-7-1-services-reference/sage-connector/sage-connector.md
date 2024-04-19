# SAGE Connector

The SAGE Connector enables integration with SAGE accounting software, facilitating seamless communication with the SAGE platform.

## Name
- **Description**: The name of the SAGE connector instance.
- **Type**: Text (string)
- **Example**: "SAGEConnectorInstance"

## Url
- **Description**: The base URL of the SAGE service or API.
- **Type**: Text (string)
- **Example**: "https://sage.example.com"

## Basepath
- **Description**: The base path within the SAGE API for accessing resources.
- **Type**: Text (string)
- **Example**: "/api/v1"

## Apiversion
- **Description**: The version of the SAGE API being utilized.
- **Type**: Text (string)
- **Example**: "v1"

## Tenant
- **Description**: The name or identifier of the tenant within the SAGE system.
- **Type**: Text (string)
- **Example**: "TenantABC"

## Company
- **Description**: The name or identifier of the company within the SAGE tenant.
- **Type**: Text (string)
- **Example**: "CompanyXYZ"

## User
- **Description**: The username or user ID used to authenticate the connector with the SAGE system.
- **Type**: Text (string)
- **Example**: "sageuser"

## Password
- **Description**: The password associated with the user account for authentication.
- **Type**: Text (string)
- **Example**: "sagesecretpassword"

## Timeout
- **Description**: The maximum time allowed for the connector to wait for a response from SAGE before timing out.
- **Type**: Integer (milliseconds)
- **Example**: 15000 (15 seconds)
