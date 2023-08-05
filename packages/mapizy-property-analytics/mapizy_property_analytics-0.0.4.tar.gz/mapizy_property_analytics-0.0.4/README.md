# REST API

The REST API has 2 modes, you can register a request using PERFORM mode and then after a while you can get the result using GET_STATUS mode. If you have enough credit and enough pricing mode the process starts, otherwise REST API returns the corresponding error message. The API expires after 2 months and you have to generate a new API key.

## PERFORM

In this mode, you should provide the following parameters:

- ADDRESS: the postal address of the property that you want to analyse

- MODE: you should use "GET_STATUS" for this parameter

- FIRST_DATE and LAST_DATE: Its needed in analyse type "change". It should be in the ISO mode. 

- FREQUENCY: is the frequency of searching for the images. It has four options:

  - 2-yearly
  - yearly
  - half-yearly
  - quarterly

  If you are using long time ranges (for example 20 years), you can use 2-yearly for lowering the cost of request.

- ANALYSE_TYPE: It can be "change" or "latest".

An example for using REST API in this mode:

### CURL method

```
curl -X POST https://7bofdt5cy2.execute-api.ap-southeast-2.amazonaws.com/dev/api -H "Content-Type: application/json" -d '{"API_KEY":"xhtDgF5W9GuBkWY8WxmRBMuyS0aE_7YkRXJvRjXlIYZpnwsgNAdlU2-B9FbJ8EWlT-lcqG80smGc19-1GBR3ow", "MODE" : "PERFORM", "ADDRESS" : "5 Pele Ave Salisbury East Salisbury SA 5109", "FIRST_DATE" : "2018-01-01", "LAST_DATE" : "2020-01-01", "FREQUENCY" : "half-yearly", "ANALYSE_TYPE" : "change"}'
```

## GET_STATUS

In this mode, you should provide the following parameters:

- MODE: you should use "GET_STATUS" for this parameter
- TIME_CREATED: this parameter can be found in the response of API in the PERFORM mode and is used to retrieve analyse result.

An example for using REST API in this mode:

### CURL method

```
curl -X POST https://7bofdt5cy2.execute-api.ap-southeast-2.amazonaws.com/dev/api -H "Content-Type: application/json" -d '{"API_KEY":"xhtDgF5W9GuBkWY8WxmRBMuyS0aE_7YkRXJvRjXlIYZpnwsgNAdlU2-B9FbJ8EWlT-lcqG80smGc19-1GBR3ow",  "MODE": "GET_STATUS", "TIME_CREATED" : "2021-05-14 18:50:35.636573"}'
```

