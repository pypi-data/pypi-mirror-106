"""
# Open Data Service - Notification-Service

## Build

`npm install`

`npm run transpile`

## Run

`npm start`

## Running unit tests

Use `npm test` to run the unit tests.

## Running end-to-end tests

* For integration testing run 
  
  ```docker-compose -f ../docker-compose.yml -f ../docker-compose.it.yml --env-file ../.env up notification-it```

* To analyze the logs of the service under test we recommend using lazydocker. Alternatively, you can attach manually to the notification container using the docker cli. 

* After running integration tests dependant services (e.g. rabbit-mq) keep running. In order to stop all services and return to a clean, initial state run 
  
  ```docker-compose -f ../docker-compose.yml -f ../docker-compose.it.yml down```. 


## API
| Endpoint  | Method  | Request Body  | Response Body | Description |
|---|---|---|---|---|
| *base_url*/ | GET | - | text | Get health status |
| *base_url*/version | GET | - | text | Get service version |
| *base_url*/configs | POST | NotificationWriteModel | - | Create a notification config |
| *base_url*/configs?pipelineId={pipelineId} | GET | - | NotificationReadModel[] | Get all notifications, filter by pipelineId if provided |
| *base_url*/configs/{id} | GET | - | NotificationReadModel | Get notification by id |
| *base_url*/configs/{id} | PUT | NotificationWriteModel | - | Update notification |
| *base_url*/configs/{id} | DELETE | - | - | Delete notification |
| *base_url*/trigger | POST | TriggerConfig | - | Trigger all notifications related to pipeline |


### NotificationWriteModel
Base model:
```
{
  "pipelineId": number,
  "condition": string,
  "type": "WEBHOOK" | "SLACK" | "FCM",
  "parameter": {
    ... see below
  }
}
```

Parameter for a webhook notification: 
```
"parameter": {
    "url": string
}
```


Parameter for a slack notification: 
```
"parameter": {
    "workspaceId": string
    "channelId": string
    "secret": string
}
```


Parameter for a firebase notification: 
```
"parameter": {
    "projectId": string
    "clientEmail": string
    "privateKey": string
    "topic": string
}
```

### NotificationReadModel
Equal to `NotificationWriteModel`, but has an additional `id: number` field.

### TriggerConfig
```
{
  "pipelineId": number,
  "pipelineName": string,
  "data": object
}
```


### Slack notification walkthrough
* Create a slack app for your slack channel and enable activations as discribed [here](https://api.slack.com/messaging/webhooks).
* Determine your apps' incoming webhook url at the slack [dashboard](https://api.slack.com/apps).
* POST a slackRequest under the endpoint ```/configs```. The workspaceId, channelId and secret fields can be taken from the parts of the incoming webhook url (separated by '/', in the given order).
* Go to your configured channel and be stunned by the magic. 

"""

import requests
from .helpers import _url, Config, KVpairs
from typing import Union, Literal

#################################################
###### Notification Service Data Structs ########
#################################################

class WebhookNotificationParameter(Config):
    def __init__(self, url:str) -> None:
        self.url = url
    def get_dict(self):
        return {
                "url":self.url
              }

class SlackNotificationParameter(Config):
    def __init__(self, workspaceId:str, channelId:str, secret:str) -> None:
        self.workspace_ID = workspaceId
        self.channel_ID = channelId
        self.secret = secret
    def get_dict(self):
        return {
                "workspaceId":self.workspace_ID,
                "channelId":self.channel_ID,
                "secret":self.secret
              }

class FirebaseNotificationParameter(Config):
    def __init__(self, projectId:str, clientEmail:str, privateKey:str, topic:str) -> None:
        self.project_ID = projectId
        self.client_email = clientEmail
        self.private_key = privateKey
        self.topic = topic
    def get_dict(self):
        return {
                "projectId":self.project_ID,
                "clientEmail":self.client_email,
                "privateKey":self.private_key,
                "topic":self.topic
              }

class NotificationWriteModel(Config):
    def __init__(self, pipelineId:int, condition:bool,
                type:Literal["WEBHOOK", "SLACK" , "FCM"],
                parameter:Union[SlackNotificationParameter, FirebaseNotificationParameter, WebhookNotificationParameter] ) -> None:
        self.pipeline_ID = int(pipelineId)
        self.condition = condition
        self.type = type
        self.parameter = parameter
    def get_dict(self):
        return {
            "pipelineId": self.pipeline_ID,
            "condition": self.condition,
            "type": self.type,
            "parameter": self.parameter.get_dict()
            }

class NotificationTriggerConfig(Config):
    def __init__(self, pipelineId:int, pipelineName:str, data:KVpairs):
        self.pipeline_ID = int(pipelineId)
        self.pipeline_name = pipelineName
        self.data = data
    def get_dict(self):
        return {
            "pipelineId": self.pipeline_ID,
            "pipelineName": self.pipeline_name,
            "data": self.data.get_dict()
            }


class NotificationAPI():
    def __init__(self) -> None:
        self.BASE_URL = "http://localhost:9000/api/notification"
        self.relative_paths = {
            "version":"version",
            "trigger":"trigger",
            "configs":"configs",
        }

    def get_health_status(self):
        return requests.get(_url(self.BASE_URL))

    def get_service_version(self):
        return requests.get(_url(self.BASE_URL, self.relative_paths["version"]))

    def create_notificationConfig(self, NotificationWriteModel:NotificationWriteModel):
        return requests.post(_url(self.BASE_URL, self.relative_paths["configs"]), json=NotificationWriteModel.get_dict())

    def get_all_notificationConfigs(self):
        return requests.get(_url(self.BASE_URL, self.relative_paths["configs"]))

    def get_pipeline_notificationConfigs(self, PipelineID):
        return requests.get(_url(self.BASE_URL, "{}?pipelineId={}".format(self.relative_paths["configs"], PipelineID)))
    
    def get_notificationConfig(self, NotificationConfigID:int):
        return requests.get(_url(self.BASE_URL, self.relative_paths["configs"], NotificationConfigID))

    def update_notificationConfig(self, NotificationConfigID:int, NotificationWriteModel:NotificationWriteModel):
        return requests.put(_url(self.BASE_URL, self.relative_paths["configs"], NotificationConfigID), json=NotificationWriteModel.get_dict())

    def delete_notificationConfig(self, NotificationConfigID:int):
        return requests.delete(_url(self.BASE_URL, self.relative_paths["configs"], NotificationConfigID))

    def trigger_all_notifications(self, TriggerConfig:NotificationTriggerConfig):
        return requests.post(_url(self.BASE_URL, self.relative_paths["trigger"]), json=TriggerConfig.get_dict())


#########################################
####### Example Requests ################
#########################################

# ## creating fresh datasources and pipelines to get ids from
# import Adapter
# import Pipeline
# import json

# #creating a datasource
# dsa = Adapter.DatasourceAPI()
# protocol_config_params_json = ProtocolConfigParameters(location="https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json",
#                                                                     encoding= "UTF-8")
# protocol_config_json = ProtocolConfig("HTTP", protocol_config_params_json)
# format_config_json = FormatConfig(type="JSON",
#                                               parameters={})
# ds_trigger_config = DatasourceTriggerConfig(first_ex="2018-10-07T01:32:00.123Z",
#                                                           interval=60000,
#                                                           periodic=True)
# ds_metadata = Metadata(author="icke",
#                                     display_name="pegelOnline",
#                                     license="none")
# ds_config = DatasourceConfig(None, protocol_config_json, format_config_json, ds_trigger_config, ds_metadata) 
# create_datasource = dsa.create_Datasource(ds_config)
# ds_id = json.loads(create_datasource.content)["id"]

# #creating a pipeline
# pl = Pipeline.PipelineAPI()
# pl_config_DTO = PipeLineConfigDTO(ds_id,
#                                               Transformation("data.test = 'abc'; return data;"),
#                                               Metadata(author="icke",
#                                                                     license= "none",
#                                                                     display_name= "exampleRequest",
#                                                                     description="none"
#                                                                     )
#                                               )
# created_pipeline = pl.create_pipeline_config(pl_config_DTO)
# pl_id = json.loads(created_pipeline.content)["id"]



# nt = NotificationAPI()
# ### Get version
# version_request = nt.get_service_version()

# ### Get all notification configs
# all_notification_configs = nt.get_all_notificationConfigs()

# ### Get all notification configs for pipeline
# notification_configs_by_pipelineID  = nt.get_pipeline_notificationConfigs(pl_id)

# ### Save notification webhook config
# web_hook_nt=nt.create_notificationConfig(NotificationWriteModel(
#                                             pl_id,
#                                             True,
#                                             "WEBHOOK",
#                                             WebhookNotificationParameter("http://www.mocky.io/v2/5dc94f7a2f0000680073eb96")
#                                             )
#                                         )
# nt_config_id = json.loads(web_hook_nt.content)["id"]

# ### Save notification firebase config
# ### needs to have the below entries at hand
# # firebase_nt=nt.create_notificationConfig(NotificationWriteModel(pl_id,
# #                                                                             True,
# #                                                                             "FCM",
# #                                                                             FirebaseNotificationParameter(
# #                                                                                 projectId= None,
# #                                                                                 clientEmail=None,
# #                                                                                 privateKey=None,
# #                                                                                 topic=None
# #                                                                                 )
# #                                                                             )
# #                                         )

# ### Save notification slack config
# slack_nt = nt.create_notificationConfig(NotificationWriteModel(pl_id,
#                                                                             True,
#                                                                             "SLACK",
#                                                                             SlackNotificationParameter(
#                                                                                 "T01U3SL56Q7",
#                                                                                 "B020AN6JCBU",
#                                                                                 "IY7hbRJ8idzfnsSdcpIhX1Px"
#                                                                                 )
#                                                                             )
#                                         )

# ### Get notification config
# retreived_nt = nt.get_notificationConfig(nt_config_id)

# ### Edit notification config
# updated_nt = nt.update_notificationConfig(nt_config_id, NotificationWriteModel(
#                                             pl_id, #should be different, but I am tired at the moment
#                                             True,
#                                             "WEBHOOK",
#                                             WebhookNotificationParameter("http://www.mocky.io/v2/5dc94f7a2f0000680073eb96")
#                                             )
#                                         )

# ### Trigger all notifications of pipeline
# triggered_all_notifications = nt.trigger_all_notifications(NotificationTriggerConfig(pl_id,
#                                                                                                 "Integration-Test Pipeline 2 (not triggering)",
#                                                                                                 KVpairs({"value1":1})
#                                                                                                 )
#                                                             )


# ### Delete notification config
# delted_nt = nt.delete_notificationConfig(nt_config_id)
# # # import json
# # # nt = NotificationAPI()
# # # ### Get all notification configs
# # # all_notification_configs = nt.get_all_notificationConfigs()
# # # for ntcfg in json.loads(all_notification_configs.content):
# # #     nt.delete_notificationConfig(ntcfg["id"])