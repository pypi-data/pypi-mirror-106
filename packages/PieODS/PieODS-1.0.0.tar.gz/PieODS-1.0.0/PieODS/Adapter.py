"""Adapter Service of the ODS
==========================

The adapter service fetches data from external data sources and provides
them via a HTTP API in JSON format. The data coming from the external
sources can be fetched over various protocols and can have various
formats.

Concepts
--------

-  **Datasource**: Description of a datasource. This description can be
   transformed into an *adapter* to import data from a data source and
   forward it to downstream services.
-  **Adapter**: Configuration to import data from a datasource; can be
   derived from a *datasource* config, or is provided by a user to
   generate a *preview*.
-  **Preview**: Stateless preview that allows executing a datasource
   config once and synchronously returning the result of the import and
   interpretation; does not send the result to downstream services
   (difference to creating and triggering a datasource).
-  **Data import**: One execution of the import of a *datasource*. The
   result and metadata get stored in the database and can be accessed
   for each *datasource*.

Current Features
----------------

-  Currently the adapter service is only a prototype and can handle
   JSON, XML and CSV files that can be fetched over HTTP. ## Planned
   Features The handling of new protocols and formats is going to be
   implemented.

Planned protocols: \* ftp

Planned formats:

Getting Started
---------------

-  Build with ``./gradlew build``
-  Run unit tests with ``./gradlew test``
-  Run integration test with ``./gradlew integrationTest`` (note that a
   instance of the adapterService needs to be up).
-  Start with ``./gradlew bootRun`` - not recommended
-  Use Docker-Compose:
   ``docker-compose -f ../docker-compose.yml --env-file ../.env up adapter``
   builds Docker images and starts them up. Note that you need to delete
   existing docker images from your local docker daemon to have recent
   changes integrated.
-  For integration testing run
   ``docker-compose -f ../docker-compose.yml -f ../docker-compose.it.yml --env-file ../.env up adapter-it``
-  To analyze the logs of the service under test we recommend using
   lazydocker. Alternatively, you can attach manually to the adapter
   container using the docker cli.
-  After running integration tests dependant services (e.g. rabbit-mq)
   keep running. In order to stop all services and return to a clean,
   initial state run
   ``docker-compose -f ../docker-compose.yml -f ../docker-compose.it.yml down``.

Architecture
------------

Each adapter consists of a importer that is responsible for the handling
of the data source protocol and a interpreter that reformats the given
data to json format. The implemented importers and interpreters are
stored in a map in the AdapterManager. For each request to the
AdapterEndpoint, the AdapterManager chooses a appropriate Interpreter
and Importer and creates an Adapter to handle the request. Information
about data format, protocal and location of the external data source to
include are stored in a AdapterConfig file which is included in the
request. The basic architecture of the ODS is depicted below. Support
for new protocols or data formats can easily be achieved by adding
classes implementing the importer/interpreter interface and registering
those classes in the AdapterManager. |basic architecture of the adapter
service|

API Docs
--------

Adapter API (data import)
-------------------------

+---------------------------+----------+------------------+---------------------------------------------------------------------------+
| Endpoint                  | Method   | Request Body     | Response Body                                                             |
+===========================+==========+==================+===========================================================================+
| *base\_url*/version       | GET      | -                | String containing the application version                                 |
+---------------------------+----------+------------------+---------------------------------------------------------------------------+
| *base\_url*/formats       | GET      | -                | JsonArray of data formats available for parsing and possible parameters   |
+---------------------------+----------+------------------+---------------------------------------------------------------------------+
| *base\_url*/protocols     | GET      | -                | JsonArray of protocols available for importing and possible parameters    |
+---------------------------+----------+------------------+---------------------------------------------------------------------------+
| *base\_url*/preview       | POST     | AdapterConfig    | PreviewResponse                                                           |
+---------------------------+----------+------------------+---------------------------------------------------------------------------+
| *base\_url*/preview/raw   | POST     | ProtocolConfig   | PreviewResponse                                                           |
+---------------------------+----------+------------------+---------------------------------------------------------------------------+

When started via docker-compose *base\_url* is
``http://localhost:9000/api/adapter``

Adapter Config
~~~~~~~~~~~~~~

::

    {
      "protocol": ProtocolConfig, 
      "format": {
        "type": "JSON" | "XML" | "CSV",
        "parameters": { } | CSVParameters
      }
    }

Protocol Config
~~~~~~~~~~~~~~~

::

    {
      "type": "HTTP",
      "parameters": {
       "location": String,
       "encoding": String
      }
    }

CSV Parameters
~~~~~~~~~~~~~~

::

    {
      "columnSeparator": char,
      "lineSeparator": char,
      "skipFirstDataRow": boolean,
      "firstRowAsHeader": boolean
    }

PreviewResponse
~~~~~~~~~~~~~~~

::

    {
        "data": <<Stringified JSON or RAW representation of payload>>
    }

Datasource API (configs)
------------------------

+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| Endpoint                                               | Method   | Request Body        | Response Body                                                        |
+========================================================+==========+=====================+======================================================================+
| *base\_url*/datasources                                | GET      | -                   | All DatasourceConfigs                                                |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}                           | GET      | -                   | DatasourceConfig wih {id}                                            |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources                                | POST     | Datasource Config   | Created datasource, id generated by server                           |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}                           | PUT      | Datasource Config   | Updated datasource with {id}                                         |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources                                | DELETE   | -                   | Delete all datasources                                               |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}                           | DELETE   | -                   | Delete datasource with {id}                                          |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}/trigger                   | POST     | Parameters          | DataImport                                                           |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}/imports                   | GET      | -                   | All DataImports for datasource with {id}                             |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}/imports/{importId}        | GET      | -                   | DataImports with {importId} for datasource with {id}                 |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}/imports/latest            | GET      | -                   | Latest DataImport for datasource with {id}                           |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}/imports/{importId}/data   | GET      | -                   | Actual data of DataImport with {importId} for datasource with {id}   |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+
| *base\_url*/datasources/{id}/imports/latest/data       | GET      | -                   | Actual data for latest DataImport for datasource with {id}           |
+--------------------------------------------------------+----------+---------------------+----------------------------------------------------------------------+

When started via docker-compose *base\_url* is
``http://localhost:9000/api/adapter``

Datasource Config
~~~~~~~~~~~~~~~~~

::

    {
      "id": Number,
      "protocol": ProtocolConfig,
      "format": FormatConfig,
      "trigger": TriggerConfig,
      "metadata": Metadata
    }

Protocol Config
~~~~~~~~~~~~~~~

::

    {
        "type": "HTTP",
        "parameters": {
          "location": String,
          "encoding": String
        }
    }

Format Config
~~~~~~~~~~~~~

::

    {
      "format": {
        "type": "JSON" | "XML" | "CSV",
        "parameters": { } | CSVParameters
      }
    }

CSV Parameters
~~~~~~~~~~~~~~

::

    {
      "columnSeparator": char,
      "lineSeparator": char,
      "skipFirstDataRow": boolean,
      "firstRowAsHeader": boolean
    }

TriggerConfig
~~~~~~~~~~~~~

::

    {
      "firstExecution": Date (format: yyyy-MM-dd'T'HH:mm:ss.SSSXXX),
      "interval": Number,
      "periodic:" Boolean
    }

Metadata
~~~~~~~~

::

    {
      "author": String,
      "displayName": String,
      "license": String,
      "description": String,
      "creationTimestamp: Date (format: yyyy-MM-dd'T'HH:mm:ss.SSSXXX),
    }

Datasource Config Event (AMQP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    {
      "datasource": DatasourceConfig
    }

Parameters
~~~~~~~~~~

::

    {
      "parameters": <<Map of type <String, String> for open parameter to replace with the value>>
    }

DataImport
~~~~~~~~~~

::

    {
      "id": Number,
      "timestamp": Date (format: yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
      "location": String (relative URI)
    }

"""
import requests
from .helpers import _url, Config, KVpairs, Metadata, Unsupported_by_ODS #this works
from typing import Union

#### Data Structs ########
###########################################
# Adapter&Datsource Service Data Structs ##
###########################################

class ProtocolConfigParameters(Config):
  def __init__(self, location:str=None, encoding:str="UTF-8", default_params:KVpairs = None) -> None:
      self.location = location
      self.encoding = encoding
      self.default_parameters= default_params

  def get_dict(self):#create dict of non-empty only
    to_be_returned= {
      "location": self.location,
      "encoding": self.encoding,
      "defaultParameters": self.default_parameters.get_dict() if isinstance(self.default_parameters, KVpairs) else None
      }
    return {k: v for k, v in to_be_returned.items() if v is not None}


class ProtocolConfig(Config):
  def __init__(self,protocolConfigParams:ProtocolConfigParameters,  type:str="HTTP") -> None:
      self.type = type
      self.parameters = protocolConfigParams

  @property
  def type(self):
    return self._type
  @type.setter
  def type(self, new_type):
    if type(new_type)==str:
      if new_type == "HTTP": #should be extended to fetch (AdapterAPI.get_supported_protocols()) the supported protocols and loop over them
        self._type = new_type
      else:
        raise Unsupported_by_ODS("The protocol '{}' is not yet supported!".format(new_type))
    else:
      raise TypeError("Invalid value for protocol type!\nType must be passed as string!")

  @property
  def parameters(self):
    return self._parameters
  @parameters.setter
  def parameters(self, new_parameters):
    if type(new_parameters)==ProtocolConfigParameters:
      self._parameters = new_parameters
    else:
      raise TypeError("Invalid type for protocol parameters!\nParameters must be passed as ProtocolConfigParameters!")
  
  def get_dict(self):
    return {"type":self.type, "parameters":self.parameters.get_dict()}


class CSVparameters(Config):

  def __init__(self, col_separtor: str=";" , line_separator: str="\n", skip_first_data_row: bool=False, first_row_as_header: bool=True) -> None:
      self.column_separator = col_separtor
      self.line_separator = line_separator
      self.skip_first_data_row = skip_first_data_row
      self.first_row_as_header = first_row_as_header
  def get_dict(self):
    return  {
      "columnSeparator": self.column_separator,
      "lineSeparator": self.line_separator,
      "skipFirstDataRow": self.skip_first_data_row,
      "firstRowAsHeader": self.first_row_as_header
    }


class FormatConfig(Config):

  def __init__(self, type:str=None, parameters:Union[dict , CSVparameters] =None) -> None:
      self.format_type = type
      self.format_parameters = parameters

  @property
  def format_type(self):
    return self._format_type
  @format_type.setter
  def format_type(self, new_format_type:str):
    if type(new_format_type)==str:
      new_format_type= new_format_type.upper()
      if new_format_type=="JSON" or new_format_type=="XML" or new_format_type=="CSV":
        self._format_type = new_format_type
      else:
        raise Unsupported_by_ODS("This format type is not supported!")
    else:
      raise TypeError("Invalid value for format type!\nFormat type must be passed as string!")

  @property
  def format_parameters(self):
    return self._format_parameters
  @format_parameters.setter
  def format_parameters(self, new_parameters:Union[dict , CSVparameters]):
    if new_parameters=={} or new_parameters==None:
      self._format_parameters = {}
    elif type(new_parameters)==CSVparameters:
      self._format_parameters = new_parameters.get_dict()
    else:
      raise TypeError("Invalid type for format config parameters!\nParameters must be either an empty dict or a CSVparameters object!") 
  
  def get_dict(self):
    return {
              "type":self.format_type,
              "parameters":self.format_parameters
            }

class DatasourceTriggerConfig(Config):

  def __init__(self, first_ex:str=None, interval:int=None, periodic:bool = None) -> None:
      self.first_execution = first_ex #Date (format: yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
      self.interval = int(interval)
      self.periodic = periodic
  def get_dict(self):
    return {
            "firstExecution":self.first_execution,
            "interval":self.interval,
            "periodic":self.periodic,
          }

# class Metadata(Config):
#   def __init__(self, author=None, display_name=None, license=None, description=None, timestamp=None) -> None:
#     self.author = author
#     self.display_name = display_name
#     self.license = license
#     self.description = description
#     self.creation_timestamp = timestamp #Date (format: yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
#   def get_dict(self):#create dict of non-empty only
#     to_be_returned= {
#       "author": self.author,
#       "displayName": self.display_name,
#       "license": self.license,
#       "description": self.description,
#       "creationTimestamp": self.creation_timestamp
#       }
#     return {k: v for k, v in to_be_returned.items() if v is not None}

class DataImport(Config):
  def __init__(self, id:int, timestamp, location) -> None:
      self.id = int(id)
      self.timestamp = timestamp #Date (format: yyyy-MM-dd'T'HH:mm:ss.SSSXXX)
      self.location = location #String (relative URI)
  def get_dict(self):
    return {
      "id": self.id,
      "timestamp": self.timestamp,
      "location": self.location
    }

class AdapterConfig(Config):
  def __init__(self, protocol_config:ProtocolConfig, format_config:FormatConfig) -> None:
      self.protocol_config = protocol_config
      self.format_config = format_config
  def get_dict(self):
    return {
      "protocol": self.protocol_config.get_dict(), 
      "format": self.format_config.get_dict()
    }

class DatasourceConfig(Config):
  def __init__(self, id:int=None,
                protocol_config:ProtocolConfig=None,
                format_config:FormatConfig=None,
                trigger_config:DatasourceTriggerConfig=None,
                meta:Metadata=None):
    self.id = int(id) if id!=None else None
    self.protocol_config = protocol_config
    self.format_config = format_config
    self.trigger_config = trigger_config
    self.meta_data = meta
  def get_dict(self):
    to_be_returned= {
      "id": self.id,
      "protocol": self.protocol_config.get_dict() if isinstance(self.protocol_config, ProtocolConfig) else None,
      "format": self.format_config.get_dict() if isinstance(self.format_config, FormatConfig) else None,
      "trigger": self.trigger_config.get_dict() if isinstance(self.trigger_config, DatasourceTriggerConfig) else None,
      "metadata": self.meta_data.get_dict() if isinstance(self.meta_data, Metadata) else None
    }
    return {k: v for k, v in to_be_returned.items() if v is not None}

class DataImportParameters(KVpairs):
  """
  {
  "parameters": <<Map of type <String, String> for open parameter to replace with the value>>
  }

  Example:
  +++++++++

  ::

      {
      "parameters": {
          "station": "BONN"
          }
      }
  """
    #   def __init__(self, *pairs) -> None:
    #     self.kv_pairs = {}
    #     for p in pairs:
    #       for k in p:
    #         self.kv_pairs[k] = p[k]
  def get_dict(self):
      return {
      "parameters":self.kv_pairs
      }


class AdapterAPI():
    def __init__(self) -> None:
        self.BASE_URL = "http://localhost:9000/api/adapter"

        self.relative_paths = {
            "version":"version",
            "formats":"formats",
            "protocols":"protocols",
            "preview":"preview",
            }
        
    def get_application_version(self):
        return requests.get(_url(self.BASE_URL, self.relative_paths["version"]))

    def get_supported_data_formats(self):
        return requests.get(_url(self.BASE_URL, self.relative_paths["formats"]))

    def get_supported_protocols(self):
        """Get all supported protocols

        :return: [description]
        :rtype: [type]
        """    
        return requests.get(_url(self.BASE_URL, self.relative_paths["protocols"]))

    def execute_configured_preview(self, AdapterConfig:AdapterConfig):
        #Note: AdapterConfig consists of both the protcol of data transfer and the format that it should be delivered in.
        #while the raw_preview needs only the protocol of data transfer
        #headers = {'Content-Type': 'application/json'}#, "User-Agent": "vscode-restclient"}
        # headers = {"User-Agent": "vscode-restclient",
        # "Content-Type": "application/json",
        # "accept-encoding": "gzip, deflate",
        # "content-length": "279"}
        #print(len(AdapterConfig.get_json().encode(encoding='UTF-8')))
        #return requests.post(_url(self.BASE_URL, self.relative_paths["preview"]), headers=headers, data=AdapterConfig.get_json().encode(encoding='UTF-8'))
        return requests.post(_url(self.BASE_URL, self.relative_paths["preview"]), json=AdapterConfig.get_dict())

    def execute_raw_preview(self, ProtocolConfig:ProtocolConfig):
      #j ={'type': 'HTTP', 'parameters': {'location': 'https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/PolizeilicheKriminalstatistik/2018/BKATabellen/FaelleLaenderKreiseStaedte/BKA-LKS-F-03-T01-Kreise_csv.csv?__blob=publicationFile&v=3','encoding': 'UTF-8'}}

      # http = urllib3.PoolManager()
      # r = http.request(
      #     'POST',
      #     _url(self.BASE_URL, self.relative_paths["preview"]),
      #     body=str(j).encode('utf-8'),
      #     headers={'Content-Type': 'application/json; charset=UTF-8'})
      # ur = _url(self.BASE_URL, self.relative_paths["preview"])
      #json = ProtocolConfig.get_dict()#.encode("UTF-8")
      # headers = {'Content-Type': 'application/json'}
      # sess = requests.Session()
      # req = requests.Request('POST', ur, 
      #                       headers=headers,
      #                       data=j)
      # preq = req.prepare()
      # preq.headers = {key: value for key, value in preq.headers.items()
      #                 if key in {'Content-Type', 'Cookie'}}
      # r = sess.send(preq)
      #return r
      url = _url(self.BASE_URL, self.relative_paths["preview"], "raw")
      headers = {'Content-Type': 'application/json'}
      #j =b'{"type": "HTTP","parameters": {"location": "https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/PolizeilicheKriminalstatistik/2018/BKATabellen/FaelleLaenderKreiseStaedte/BKA-LKS-F-03-T01-Kreise_csv.csv?__blob=publicationFile&v=3","encoding": "UTF-8"}}'
      # with open('1.json','rb') as payload:
      #   #j = json.load(payload)
      #    return requests.post(url, headers=headers, data=payload.read())
      return requests.post(url=url, headers=headers,json=ProtocolConfig.get_dict())#, headers={"Content-Type": "application/json"})#.replace('\\"',"\""))

#Datasource API
#As it has the same self.BASE_URL, I put it in the  same file.
class DatasourceAPI():
  def __init__(self) -> None:
      self.BASE_URL = "http://localhost:9000/api/adapter"


      self.relative_paths = { 
          "datasources":"datasources",
          # "trigger":"datasources/{}/trigger", #datasource id goes in here
          # "imports":"datasources/{}/imports", #datasource id goes in here
          # "latest_DataImport":"datasources/{}/imports/latest", #datasource id goes in here
          # "lataest_DataImport":"datasources/{}/imports/{}/data", #datasource id then Dataimport id
          # "lataest_DataImport":"datasources/{}/imports/latest", #datasource id goes in here
          
          }
  def get_all_DatasourceConfigs(self):
    """Gets all DatasourceConfigs.
    Example of a DatasourceConfig is:
      {
      "id": Number,
      "protocol": ProtocolConfig,
      "format": FormatConfig,
      "trigger": TriggerConfig,
      "metadata": Metadata
      }

    :return: DatasourceConfigs
    :rtype: json
    """
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"]))
       
  def get_DatasourceConfig(self, DatasourceID):
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID))

  def create_Datasource(self, DatasourceConfig:DatasourceConfig):
    return requests.post(_url(self.BASE_URL, self.relative_paths["datasources"]), json=DatasourceConfig.get_dict())

  def update_Datasource(self, DatasourceID, DatasourceConfig:DatasourceConfig):
    return requests.put(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID), json=DatasourceConfig.get_dict())

  def delete_all_Datasources(self):
    return requests.delete(_url(self.BASE_URL, self.relative_paths["datasources"], "")) #the trailing slash is added to the url for the DELETE method.
  
  def delete_Datasource(self, DatasourceID:int):
    return requests.delete(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID))

  def trigger_DataImport_without_params(self, DatasourceID):
    return requests.post(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "trigger"))

  def trigger_DataImport_with_params(self, DatasourceID, Parameters:DataImportParameters):
    return requests.post(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "trigger"), json=Parameters.get_dict())

  def get_All_Dataimports_of_Datasource(self, DatasourceID):
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "imports"))

  def get_Dataimport_of_Datasource(self, DatasourceID, importId):
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "imports", importId))

  def get_latest_Dataimport_of_Datasource(self, DatasourceID):
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "imports", "latest"))

  def get_Data_of_Dataimport_of_Datasource(self, DatasourceID, importId):
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "imports", importId, "data"))

  def get_Data_of_latest_Dataimport_of_Datasource(self, DatasourceID):
    return requests.get(_url(self.BASE_URL, self.relative_paths["datasources"], DatasourceID, "imports", "latest", "data"))


# ada = AdapterAPI()
# print(ada.get_supported_protocols().text)
# print(ada.get_supported_data_formats().text)
# protocol_config_params_raw = ProtocolConfigParameters(location='https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/PolizeilicheKriminalstatistik/2018/BKATabellen/FaelleLaenderKreiseStaedte/BKA-LKS-F-03-T01-Kreise_csv.csv?__blob=publicationFile&v=3',
#                                                                   encoding= 'UTF-8')
# protocol_config_raw = ProtocolConfig(r'HTTP', protocol_config_params_raw)
# print(protocol_config_raw.get_json())

#########################################
########## Example Requests #############
#########################################
"""
############# AdapterAPI ################
ada = AdapterAPI()

### Get application version
application_version = ada.get_application_version()
#print(application_version.text)

### Get all supported protocols
supported_protocols = ada.get_supported_protocols()
#print(supported_protocols.text)

### Get all supported data formats
supported_data_formats = ada.get_supported_data_formats()
#print(supported_data_formats.text)

### Perform Data Import RAW                                     https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/PolizeilicheKriminalstatistik/2020/Bund/Faelle/BU-F-01-T01-Faelle_csv.csv?__blob=publicationFile&v=4
protocol_config_params_raw = ProtocolConfigParameters(location='https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/PolizeilicheKriminalstatistik/2018/BKATabellen/FaelleLaenderKreiseStaedte/BKA-LKS-F-03-T01-Kreise_csv.csv?__blob=publicationFile&v=3',
                                                                  encoding= 'UTF-8')
protocol_config_raw = ProtocolConfig(r'HTTP', protocol_config_params_raw)
print(protocol_config_raw.get_json())
raw_preview = ada.execute_raw_preview(protocol_config_raw)
print(raw_preview.status_code)
print(raw_preview.request.body)


### Perform Data Import JSON
protocol_config_params_json = ProtocolConfigParameters(location="https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations.json",
                                                                    encoding= "UTF-8")
protocol_config_json = ProtocolConfig("HTTP", protocol_config_params_json)
format_config_json = FormatConfig(type="JSON",
                                              parameters={})
json_configured_preview = ada.execute_configured_preview(AdapterConfig(protocol_config_json, format_config_json))
print(json_configured_preview.status_code)
print(json_configured_preview.request.body)

### Perform Data Import CSV
protocol_config_params_csv = ProtocolConfigParameters(location="https://www.bka.de/SharedDocs/Downloads/DE/Publikationen/PolizeilicheKriminalstatistik/2018/BKATabellen/FaelleLaenderKreiseStaedte/BKA-LKS-F-03-T01-Kreise_csv.csv?__blob=publicationFile&v=3",
                                                                  encoding= "ISO-8859-1")
protocol_config_csv = ProtocolConfig("HTTP", protocol_config_params_csv)
csv_params = CSVparameters(";", "\n", False, True)
format_config_csv = FormatConfig(type="CSV",
                                              parameters=csv_params)
csv_configured_preview = ada.execute_configured_preview(AdapterConfig(protocol_config_csv, format_config_csv))
print(csv_configured_preview.text)


############ DataSourceAPI ####################
dsa = DatasourceAPI()

### Get all datasources
all_datasources_configs = dsa.get_all_DatasourceConfigs()
print(all_datasources_configs.text)

### Create a datasource
ds_trigger_config = DatasourceTriggerConfig(first_ex="2018-10-07T01:32:00.123Z",
                                                          interval=60000,
                                                          periodic=True)
ds_metadata = Metadata(author="icke",
                                    display_name="pegelOnline",
                                    license="none")
ds_config = DatasourceConfig(None, protocol_config_json, format_config_json, ds_trigger_config, ds_metadata) 
create_datasource = dsa.create_Datasource(ds_config)
print(create_datasource.text)

### Delete all datasources
#delete_all_ds = dsa.delete_all_Datasources()
#print(delete_all_ds.text)

#hypothetical_ds_ID = 1
hypothetical_ds_ID = json.loads(create_datasource.content)["id"]

# ### Delete datasource x
# delete_ds_by_ID = dsa.delete_Datasource(hypothetical_ds_ID)
# print(delete_ds_by_ID.text)

### Update datasource x
update_ds_trigger_config = DatasourceTriggerConfig(first_ex="2018-10-07T01:32:00.123Z",
                                                          interval=1000,
                                                          periodic=True)
update_ds_metadata = Metadata(author="newauthor", license="AGPL3")
update_ds_config =  DatasourceConfig(None, protocol_config_json, format_config_json, update_ds_trigger_config, update_ds_metadata) 
update_ds_by_ID = dsa.update_Datasource(hypothetical_ds_ID, update_ds_config)
print(update_ds_by_ID.text)

### Perform manual data import without runtime parameters
dataimport_without_params = dsa.trigger_DataImport_without_params(hypothetical_ds_ID)
print(dataimport_without_params.text)

### Create datasource with dynamic parameters
protocol_config_params_dynamic_ds = ProtocolConfigParameters(location="https://www.pegelonline.wsv.de/webservices/rest-api/v2/stations/{station}/W/measurements.json?start=P1D",
                                                                      encoding= "UTF-8",
                                                                      default_params=KVpairs({"station": "BAMBERG"}))
protocol_config_dynamic_ds = ProtocolConfig("HTTP", protocol_config_params_dynamic_ds )
 
ds_with_dynamic_params_trigger_config = DatasourceTriggerConfig(first_ex="2018-10-07T01:32:00.123Z",
                                                          interval=60000,
                                                          periodic=False)
ds_with_dynamic_params_dsconfig = DatasourceConfig(None, protocol_config_dynamic_ds,
                                                                format_config_json,
                                                                ds_with_dynamic_params_trigger_config, 
                                                                ds_metadata)
create_ds_with_dynamic_params = dsa.create_Datasource(ds_with_dynamic_params_dsconfig)
print(create_ds_with_dynamic_params.text)

### Perform manual data import with runtime parameters
dataimport_params = DataImportParameters({"station": "BONN"})
manual_dataimport_with_params = dsa.trigger_DataImport_with_params(hypothetical_ds_ID, dataimport_params)
print(manual_dataimport_with_params.text)

### List imports of a certain datasource
ds_imports = dsa.get_All_Dataimports_of_Datasource(hypothetical_ds_ID)
print(ds_imports.text)

### Find latest import of a certain datasource
ds_latest_import = dsa.get_latest_Dataimport_of_Datasource(hypothetical_ds_ID)
print(ds_latest_import.text)

### Fetch latest import data
ds_data_of_latest_import = dsa.get_Data_of_latest_Dataimport_of_Datasource(hypothetical_ds_ID)
print(ds_data_of_latest_import.text)

### Look at data import metadata
# should use the id from the trigger response
hypothetical_dataImportId = json.loads(ds_latest_import.content)["id"]
fetched_dataimport = dsa.get_Dataimport_of_Datasource(hypothetical_ds_ID, hypothetical_dataImportId)
print(fetched_dataimport.text)

### Fetch imported data
data_of_fetched_dataimport = dsa.get_Data_of_Dataimport_of_Datasource(hypothetical_ds_ID, hypothetical_dataImportId)
print(data_of_fetched_dataimport.text)

######## cleaning up, or at least trying! #########

### Delete datasource x
delete_ds_by_ID = dsa.delete_Datasource(hypothetical_ds_ID)
print(delete_ds_by_ID.text)

## Delete all datasources
delete_all_ds = dsa.delete_all_Datasources()
print(delete_all_ds.text)
"""

# dsa = DatasourceAPI()
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

# ### Get all datasources
# all_datasources_configs = dsa.get_all_DatasourceConfigs()
# for ds in json.loads(all_datasources_configs.content):
#   #dsa.delete_Datasource(ds["id"])
#   try:
#     print(ds["id"])
#     #dsa.delete_Datasource(ds["id"])
#   except:
#     print("Not there")
  
# delete_all_ds = dsa.delete_all_Datasources()

# all_datasources_configs = dsa.get_all_DatasourceConfigs()
# for ds in json.loads(all_datasources_configs.content):
  
#   try:
#     print(ds["id"])
#   except:
#     print("Not there")

# print("done")