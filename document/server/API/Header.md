# API - Header

## Description

Header can be read on Action, which will be received as part of the client request.

## Example use case

* **Content Negotiation**: The "Accept" header allows the client to specify the media types it can understand, enabling the
  server to send an appropriate response format. For instance, a client can request JSON or XML data based on its
  capabilities.
* **User-Agent Information**: The "User-Agent" header provides information about the client's software, enabling the server
  to tailor the response according to the capabilities or constraints of the client.
* **Tracking and Analytics**: Clients can send headers containing tracking information or analytics data, helping the server
  collect insights about how its resources are being used.

## How to use

1. Open the **Header** tab.
2. For each Action and Method, Headers can be added, edited or deleted.
3. The following fields are available:
    * **Type**: HTTP Header to read from (example: `Content-Type`)
    * **Value**: Default value of the header if the client request doesn't provide one (example: `application/json`)
      ![Header view](Header-view.png)
