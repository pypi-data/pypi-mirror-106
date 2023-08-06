
import  yaml
import  json
import  configparser
import  xmltodict
from    pathlib         import Path, PurePath
from    os              import path
from    collections     import OrderedDict

__all__                 :   list    =   ["Config"
                                        ,"FILE_TYPES"
                                        ,"FALLBACK_FILE_TYPE"
                                        ,"FILE_TYPE_ALIAS"
                                        ,"BOOLEAN_STATES"
                                        ,"FILE_TYPE_YAML"
                                        ,"FILE_TYPE_JSON"
                                        ,"FILE_TYPE_INI"
                                        ,"FILE_TYPE_XML"
                                        ]

FILE_TYPE_YAML          :   str     =   'yaml'
FILE_TYPE_JSON          :   str     =   'json'
FILE_TYPE_INI           :   str     =   'ini'
FILE_TYPE_XML           :   str     =   'xml'

FILE_TYPE_MAX_DEPTH     :   dict    =   {'ini'  : 2}
FILE_TYPES              :   tuple   =   (FILE_TYPE_INI
                                        ,FILE_TYPE_JSON
                                        ,FILE_TYPE_XML
                                        ,FILE_TYPE_YAML
                                        )

XML_FALLBACK_ROOT_NODE  :   str     =   'ROOT'

FALLBACK_FILE_TYPE      :   str     =   FILE_TYPE_JSON

FILE_TYPE_ALIAS         :   dict    =   {'yml'      :   FILE_TYPE_YAML
                                        ,'param'    :   FILE_TYPE_JSON
                                        ,'params'   :   FILE_TYPE_JSON
                                        ,'config'   :   FILE_TYPE_JSON
                                        ,'cfg'      :   FILE_TYPE_INI
                                        ,'ora'      :   FILE_TYPE_INI
                                        ,'txt'      :   FILE_TYPE_INI
                                        }

BOOLEAN_STATES          :   dict    =   {'1'      :   True  ,   '0'     :   False
                                        ,1        :   True  ,   0       :   False
                                        ,'yes'    :   True  ,   'no'    :   False
                                        ,'true'   :   True  ,   'false' :   False
                                        ,'on'     :   True  ,   'off'   :   False
                                        ,'y'      :   True  ,   'n'     :   False
                                        ,'+'      :   True  ,   '-'     :   False
                                                            ,   ''      :   False
                                                            ,   None    :   False
                                                            ,   'none'  :   False
                                                            ,   'null'  :   False
                                        }

def _appendMimeTypeAliases():
    # add application and text ones
    for pre in ('application','text'):
        for k in [k for k in FILE_TYPES if not '/' in k]:
            newKey = f"{pre}/{k}"
            if newKey not in FILE_TYPE_ALIAS:
                FILE_TYPE_ALIAS[newKey] = k

    from mimetypes import MimeTypes
    mt  =   MimeTypes()
    # Get from registered MIME types
    for tk in range(0,len(mt.types_map_inv)):
        for k in mt.types_map_inv[tk]:
            if k not in FILE_TYPE_ALIAS:
                for l in mt.types_map_inv[tk][k]:
                    extn = l.lstrip('.')
                    if extn in FILE_TYPES:
                        FILE_TYPE_ALIAS [k] = extn
    mt = None

_appendMimeTypeAliases()

def _ensureNotFolder(file_path):
    if file_path and path.isdir(file_path):
        raise ValueError(f'\'{file_path}\' is a folder, not a file')


def _to_bool(value):
    """
    Converts 'something' to boolean. Raises exception if it gets a string it doesn't handle.
    Case is ignored for strings. These string values are handled:
    True: 'True', "1", "TRue", "yes", "y", "t"
    False: "", "0", "faLse", "no", "n", "f"
    Non-string values are passed to bool.
    """
    if type(value) == str:
        value   =   value.lower()

    if isinstance(value,bool):
        retval  = value
    elif isinstance(value,(dict,list)):
        retval  = Exception(f'Invalid value type for boolean conversion: \'{type(value)}\'')
    elif value in BOOLEAN_STATES:
        retval = BOOLEAN_STATES[value]
    else:
        raise ValueError(f'Value is not a boolean: \'{value}\'')
    return retval

class Config (object):

    def __init__    (self
                    ,**kwargs
                    ):

        kwargs.setdefault('file_path',None)
        kwargs.setdefault('file_type',None)
        kwargs.setdefault('raiseFileNotFound',True)
        kwargs.setdefault('config',None)

        file_path           :   str     =   kwargs.get("file_path")
        file_type           :   str     =   kwargs.get("file_type")
        raiseFileNotFound   :   bool    =   _to_bool(kwargs.get("raiseFileNotFound"))
        configDict          :   dict    =   kwargs.get("config")

        Config._check_file_path (file_path)

        saveNeeded          :   bool    =   False
        self.params                     =   None

        if  configDict:
            self.params =   configDict
            saveNeeded  =   True

        if not file_path:
            self.file_path  =   None
            self.file_type  =   None
            saveNeeded      =   False
        else:

            file_type = Config._workOutFileType (file_type  =   file_type
                                                ,file_path  =   file_path
                                                )
            _ensureNotFolder (file_path)

            self.file_path  = file_path
            self.file_type  = file_type

            fexists         =  path.isfile(self.file_path)

            if configDict:
                """
                If the dict for the config has been passed as a parameter, then do not load from file
                """
                ...
            elif not fexists:
                # file does not exist
                if raiseFileNotFound:
                    raise FileNotFoundError(self.file_path)
                else:
                    self.params =   None
                    saveNeeded  =   True
            else:

                with open(self.file_path, "r") as f:
                    if file_type == FILE_TYPE_YAML:
                        self.params = yaml.safe_load(f)
                    elif file_type == FILE_TYPE_XML:
                        self.params = xmltodict.parse(f.read())
                        if  (len(self.params) == 1
                            and XML_FALLBACK_ROOT_NODE in self.params
                            and len(self.params[XML_FALLBACK_ROOT_NODE]) > 1
                            ):
                            allDict =   True
                            for k in self.params[XML_FALLBACK_ROOT_NODE]:
                                if not isinstance(self.params[XML_FALLBACK_ROOT_NODE][k], (dict,OrderedDict)):
                                    allDict =   False
                                    break
                            if allDict:
                                self.params =   self.params[XML_FALLBACK_ROOT_NODE]
                    elif file_type == FILE_TYPE_JSON:
                        self.params = json.loads(f.read())
                    elif file_type == FILE_TYPE_INI:
                        config_INI              =   configparser.ConfigParser(allow_no_value = True)
                        config_INI.optionxform  =   str
                        theData                 =   f.read()
                        try:
                            config_INI.read_string(theData)
                        except configparser.MissingSectionHeaderError:
                            theData =   f"[{configparser.DEFAULTSECT}]\n{theData}"
                            config_INI.read_string(theData)
                            saveNeeded  =   True

                        self.params         =   {}
                        dFaults  = config_INI.defaults()
                        sections = config_INI.sections()
                        if dFaults is not None and isinstance(dFaults,(dict,OrderedDict)) and len(dFaults) > 0:
                            self.params[configparser.DEFAULTSECT] = dFaults
                        for s in sections:
                            self.params[s]         =  config_INI._sections[s]
                        config_INI              =   None
                    else:
                        raise NotImplementedError(f'file_type =  \'{file_type}\'')

                if isinstance(self.params, OrderedDict):
                    self.params =   json.loads(json.dumps(self.params))

        if saveNeeded and self.file_path:
            self.save()

    def __repr__ (self):
        strVal = 'Config('
        try:
            if self.file_path:
                strVal += f'\'{self.file_path}\''
            else:
                strVal += 'None'
            try:
                if self.file_type:
                    strVal += f',\'{self.file_type}\''
            except AttributeError:
                ...
        except AttributeError:
            ...
        strVal += ')'
        return strVal

    def __str__ (self):
        strVal = None
        if self.params:
            try:
                    strVal = str(self.params) if len(self.params) > 0 else None
            except AttributeError:
                ...
        return strVal if strVal else self.__repr__()

    @staticmethod
    def _check_file_path (file_path):
        if file_path and not isinstance (file_path, (str,PurePath)):
            raise TypeError (f'Invalid type for file_path : {type(file_path)}')

    @staticmethod
    def _workOutFileType (**kwargs) -> str:

        kwargs.setdefault ('file_type',None)
        kwargs.setdefault ('file_path',None)
        kwargs.setdefault ('fallback_file_type',None)

        file_type           : str = kwargs.get('file_type')
        file_path           : str = kwargs.get('file_path')

        Config._check_file_path (file_path)

        if not file_type:
            if not file_path:
                raise Exception("file_type OR file_path must be supplied")
            file_type   =   Path(file_path).suffix.lstrip('.')

        file_type   =   file_type.lower()
        if file_type in FILE_TYPE_ALIAS:
            file_type = FILE_TYPE_ALIAS[file_type]
        if file_type not in FILE_TYPES:
            fallback_file_type  : str = kwargs.get('fallback_file_type')
            if fallback_file_type and fallback_file_type in FILE_TYPES:
                # fall back to JSON/whatever if can't work it out
                file_type = fallback_file_type
            else:
                raise NotImplementedError(f'file_type =  \'{file_type}\'')

        if not (file_type and file_type in FILE_TYPES):
            raise NotImplementedError(f'file_type =  \'{file_type}\'')

        return file_type

    def getMaxParamDepth(self) -> int:

        try:
            if self.params is None:
                return 0
            elif type(self.params) == list:
                return 1
        except AttributeError:
            return 0

        def recur (theDict, startDepth :    int):
            deepest =   startDepth

            if startDepth > 10: # Sanity check
                raise RecursionError(f"Bailing at recursion level {startDepth}")

            for k in theDict:

                thisOne = startDepth + 1

                if type(theDict[k]) == dict:
                    thisOne = recur (theDict[k], thisOne)
                elif type(theDict[k]) == list:
                    thisOne += 1

                if thisOne > deepest:
                    deepest =   thisOne

            return deepest

        return recur (self.params,0)

    def save_as (self
                ,file_path          :   str
                ,**kwargs
                ):

        kwargs.setdefault('file_type',None)
        kwargs.setdefault('updateObject',True)

        indent  :   int =   4

        if file_path:
            _ensureNotFolder(file_path)
        else:
            raise ValueError ('No file_path value provided')

        file_type = Config._workOutFileType (file_type          =   kwargs.get('file_type')
                                            ,file_path          =   file_path
                                            ,fallback_file_type =   FALLBACK_FILE_TYPE
                                            )

        if not file_type:
            raise ValueError('No idea what type to save as - file_type not set')

        try:
            theDict =   self.params
            if file_type in FILE_TYPE_MAX_DEPTH and FILE_TYPE_MAX_DEPTH[file_type] > 0:
                dictDepth   =   self.getMaxParamDepth()
                if dictDepth > FILE_TYPE_MAX_DEPTH[file_type]:
                    raise ValueError(f"File type \'{file_type}\' only supports values {FILE_TYPE_MAX_DEPTH[file_type]} deep, not {dictDepth}")
        except AttributeError:
            theDict =   {}

        if file_type == FILE_TYPE_YAML:
            if theDict == {}:
                content =   '# No parameters in object'
            else:
                content = yaml.safe_dump    (theDict
                                            ,sort_keys  =   False
                                            ,indent     =   indent
                                            )
        elif file_type  == FILE_TYPE_JSON:
            content =   json.dumps  (theDict
                                    ,sort_keys  =   False
                                    ,indent     =   indent
                                    )
        elif file_type == FILE_TYPE_XML:
            content =   xmltodict.unparse   (theDict if len(theDict) == 1 else {XML_FALLBACK_ROOT_NODE: theDict}
                                            ,short_empty_elements   =   True
                                            ,pretty                 =   True
                                            # ,full_document          =   False
                                            ,indent                 =   (' '*indent)
                                            )

        elif file_type == FILE_TYPE_INI:
            config  = configparser.ConfigParser(allow_no_value = True)
            config.optionxform=str
            config.read_dict (theDict)
            with open(file_path, 'w') as file:
                config.write    (fp                         =   file
                                ,space_around_delimiters    =   True
                                )
            config  =   None
            content =   None
        else:
            raise NotImplementedError(f'file_type =  \'{file_type}\'')

        if content:
            with open(file_path, 'w') as file:
                file.write  (content)

        if _to_bool(kwargs.get('updateObject')):
            self.file_path  = file_path
            self.file_type  = file_type

    def save (self):
        self.save_as    (file_path      =   self.file_path
                        ,file_type      =   self.file_type
                        )

    def get_bool (self, keys, **kwargs) -> bool:

        kwargs.setdefault ('raiseNDF',False)

        grabbed =   self.get(keys, **kwargs)
        boolVal =   _to_bool(value = grabbed)
        if not str(boolVal) == str(grabbed):
            self.set    (keys   = keys
                        ,value  = boolVal
                        )
        return boolVal

    def set (self, keys, value):
        if type(keys) == str:
            keys    =   keys.split('/')
        if self.params is None:
            self.params =   {}
        val = self.params
        for ix,k in enumerate(keys):
            if k not in val:
                val[k]  =   {}
            if (ix+1) == len(keys):
                val[k]  =   value
            else:
                val     =   val[k]

    def get (self, keys, **kwargs):

        kwargs.setdefault ('raiseNDF',True)
        kwargs.setdefault ('None_to_none',True)

        if type(keys) == str:
            keys    =   keys.split('/')

        try:
            val = self.params
        except AttributeError:
            raise AttributeError ("Config option not initialised properly")

        raiseNDF    :   bool    =   _to_bool(kwargs.get('raiseNDF'))

        if type(val) == dict:
            for ix,k in enumerate(keys):
                try:
                    thisOne =   '/'.join(keys[:(ix+1)])
                    if val:
                        val = val[k]
                    else:
                        raise KeyError
                except KeyError:
                    if raiseNDF:
                        raise   KeyError(f"Key \'{thisOne}\' not defined in config")
                    else:
                        val =   None
                        # print (f'\'{thisOne}\' - writing empty key')
                        self.set (keys, value = val)
        elif raiseNDF: # self.params is none
            raise   KeyError(f"No keys defined in config")

        if  (   type(val)   == str
            and val.lower() in ('none','null','')
            and _to_bool(kwargs.get('None_to_none'))
            ):
            # None_to_none parameter
            # means that a string value of 'None' is returned as None
            val =   None

        return val

if __name__ == '__main__':
    ...
